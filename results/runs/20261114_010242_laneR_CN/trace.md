# Reasoning of lane run 20261114_010242_laneR_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, tree-lined multilane road continues ahead; no intersection or lane ending
                        is clearly visible. My car is in the rightmost of three same-direction motor-vehicle
                        lanes. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved roadside
                        strip carrying a cyclist beyond it and a raised sidewalk farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 3 agree with a lane line on the
                        left and a roadway or motor/non-motor edge line on the right. | roles: The broken
                        white left line fits a same-direction lane divider; the solid white right line fits a
                        right-side edge or motor/non-motor separation line. | markings: No guidance arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        movement arrow or intersection layout is inferred from the distant road; the roadside
                        strip's precise designation is not assumed. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to cross into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        roadside strip, except in an emergency when safe; the supplied edge-line passages
                        provide no applicable crossing permission here. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible movement marking governs this action.
Step 6  turn_left       not_applicable: No visible movement marking governs this action.
Step 6  turn_right      not_applicable: No visible movement marking governs this action.
Step 6  u_turn          not_applicable: No visible movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the solid right edge line and leave clearance for the cyclist beyond it; a
                        left lane change is permitted when safe. No visible arrows establish turn-lane
                        assignments or a stopping position, so reassess the markings and signs as you approach
                        any junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 913, 13.43 s

culane_test__d100_05251207_0380_02130 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, three-lane road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with long painted segments and clear gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with long painted segments and clear gaps separates my lane from
                        another same-direction lane on the right; the roadside fence is beyond that lane, not
                        at my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No features beyond the visible road stretch or
                        obscured by distant traffic are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may remain in the middle lane or cross either broken white boundary when safe
                        after checking surrounding traffic. No turn guidance or stopping line is visible;
                        choose a lane for any later intersection only when its guidance becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 757, 9.86 s

culane_test__d100_05251207_0380_02190 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with no visible intersection or lane
                        ending. My car is in the middle of three lanes in this direction. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane line on each
                        side. | roles: Both white broken boundaries fit crossable same-direction lane lines. |
                        markings: No arrows, words, symbols, waiting areas or transverse markings are visible
                        in my lane. | unseen: No distant intersection layout or movement restriction has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the left. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the right. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
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
Advice                  You may change lanes across either broken white boundary when safe, checking
                        surrounding traffic first. No visible markings assign intersection movements or
                        specify a stopping point; reassess when the junction and its guidance become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 765, 10.01 s

culane_test__d100_05251207_0380_02400 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight urban road with three lanes in this direction and no intersection or lane
                        ending visible ahead. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from the lane
                        occupied by the white van; no curb borders my lane on this side.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from the right-hand
                        lane containing the small cargo vehicle; the roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane line on each
                        side. | roles: Both white broken boundaries fit crossable same-direction lane lines. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are discernible
                        in my lane. | unseen: No movement restriction or marking beyond the visible stretch is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
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
Advice                  You may cross either broken boundary after checking traffic and yielding as needed,
                        particularly to the van on the left and vehicles on the right. No visible marking
                        assigns intersection movements or a stopping position; reassess when approaching a
                        junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 775, 9.69 s

culane_test__d100_05251207_0380_03270 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending clearly visible. My car is in the rightmost of three lanes travelling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip and
                        then a raised sidewalk curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane line on the left
                        and a roadway edge line on the right. | roles: The broken white left line fits a same-
                        direction lane separator; the solid white right line fits a right-hand roadway edge. |
                        markings: No guidance arrows, words, symbols, waiting areas or transverse markings are
                        visible in my lane. | unseen: No movement instructions are inferred from the distant
                        signs or from pavement beyond the readable stretch. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to cross into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted when safe. No visible
                        pavement arrow assigns an intersection movement, so follow upcoming lane guidance and
                        signs rather than assuming this lane permits a particular turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 840, 11.54 s

culane_test__d100_05251222_0385_01140 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight, with an elevated structure and guardrail on
                        the left and a sidewalk on the right. My car is in the leftmost of three lanes
                        travelling in this direction; no intersection or lane ending is visible. (lanes 3,
                        mine 1, full)
Step 2  Left            A continuous pale white line borders my lane on the left, with a narrow roadside
                        strip, raised curb and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car being in lane
                        1 of three. | roles: The broken white right boundary fits a same-direction lane
                        divider. The left line appears white despite being a left edge; its edge role follows
                        from the visible roadside strip and guardrail, not an assumed paint colour. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No hidden markings or intersection movements have been inferred;
                        the distant roadway is too small to establish features beyond the visible stretch. |
                        result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, with an exception only for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a curb and guardrail lie beyond.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
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
                        movement markings is not treated as permission to turn.
Advice                  Remain within the left edge line; a rightward lane change is permitted by the broken
                        divider when traffic conditions are safe. No visible turn guidance or stopping line
                        establishes where to turn or stop.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 953, 15.51 s

culane_test__d100_05251222_0385_01710 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs alongside an elevated structure toward a signalized
                        intersection. My car is in the second of four visible lanes in this direction. (lanes
                        4, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the lane occupied by the dark sedan
                        on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (insufficient): A white longitudinal arrow-like marking is visible
                        immediately behind the silver sedan, but its head is obscured, preventing reliable
                        identification of all indicated directions.; line:crosswalk (partial): White
                        pedestrian-crossing stripes extend across the road ahead; the portion across my lane
                        is partly obscured by the silver sedan.
Step 4  Cross-check     position: The second-of-four position agrees with same-direction lane lines on both
                        sides. | roles: Both white solid boundaries fit no-crossing lane lines on an
                        intersection approach. | markings: The obscured arrow head cannot establish the
                        permitted movements; the crossing does not contradict either boundary. | unseen: No
                        direction has been assigned to the obscured arrow head. A separate stop line cannot be
                        reliably distinguished. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            symbol:other: Guide-arrow heads indicate permitted travel directions, but the obscured
                        head prevents determining those directions here. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers this pedestrian crossing, and
                        it does not determine any of the seven requested actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined (WRONG, label allowed): The lane arrow's head is obscured, so its
                        permitted directions cannot be confirmed.
Step 6  turn_left       not_determined (WRONG, label prohibited): The lane arrow's head is obscured, so its
                        permitted directions cannot be confirmed.
Step 6  turn_right      not_determined (WRONG, label prohibited): The lane arrow's head is obscured, so its
                        permitted directions cannot be confirmed.
Step 6  u_turn          not_determined (WRONG, label prohibited): The lane arrow's head is obscured, so its
                        permitted directions cannot be confirmed.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white boundaries; do not change lanes across them. Confirm
                        the obscured lane arrow and intersection controls before choosing a movement, and keep
                        the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'symbol:other'], missed ['arrow:straight']), actions False, unsafe
                        [], citation None, contradictions []
Tokens                  in 6475, out 1205, 21.4 s

culane_test__d100_05251222_0385_02280 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside an elevated structure, with traffic continuing
                        ahead. My car is in the leftmost lane; vehicles obscure the outer lanes and the
                        distant lane end. (lanes None, mine 1, partial)
Step 2  Left            A solid white line follows a raised curb on the left, with a planted strip and metal
                        guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments and intervening gaps separate my lane from another same-
                        direction traffic lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge places my lane first from the left, and the right lane
                        line confirms an adjacent same-direction lane; the total lane count is obscured. |
                        roles: The broken white right boundary fits a same-direction lane line. The left line
                        is visibly white despite its location at the left roadway edge; its colour has not
                        been inferred from its position. | markings: No pavement arrows, words, symbols, areas
                        or transverse lines are readable in the visible portion of my lane. | unseen: The
                        total lane count and markings at the distant lane end cannot be established; overhead
                        sign arrows have not been treated as pavement markings. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_determined (WRONG, label prohibited): The distant lane end is obscured, so any
                        pavement arrow governing the exit movement cannot be established.
Step 6  turn_left       not_determined (WRONG, label allowed): The distant lane end is obscured, so any
                        pavement arrow governing the exit movement cannot be established.
Step 6  turn_right      not_determined (WRONG, label prohibited): The distant lane end is obscured, so any
                        pavement arrow governing the exit movement cannot be established.
Step 6  u_turn          not_determined (WRONG, label allowed): The distant lane end is obscured, so any
                        pavement arrow governing the exit movement cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked waiting area ahead or two-way left-turn lane directly to
                          the left is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left curb; a rightward lane change is permitted by the dashed line
                        only when the adjacent traffic leaves a safe gap. Check the lane-direction signs and
                        upcoming pavement arrows before selecting an intersection movement; the roadside
                        U-turn sign indicates a facility 100 m ahead, not an immediate turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 7333, out 1002, 17.37 s

culane_test__d100_05251222_0385_02400 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside an elevated structure, with traffic continuing
                        ahead; the next intersection is not clearly visible. My car is in the second lane from
                        the left. (lanes 4, mine 2, partial)
Step 2  Left            A continuous white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the lane occupied by the white sedan on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood, but its stem and any possible branches are obscured.
Step 4  Cross-check     position: Same-direction lanes on both sides agree with my lane being second from the
                        left; the apparent four-lane count is less certain on the vehicle-obscured right side.
                        | roles: Both white solid boundaries fit no-crossing lane lines separating same-
                        direction traffic. | markings: The visible forward arrowhead is compatible with the
                        lane boundaries, but the hood prevents confirming whether it is a straight-only or
                        combined arrow. | unseen: No hidden arrow branches, stop line, or intersection layout
                        are assumed. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead indicates straight travel, but the
                        hidden remainder prevents establishing whether additional movements are indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): The solid white lane boundary prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white lane boundary prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The obscured remainder of the arrow prevents
                        determining whether a left-turn branch exists.
Step 6  turn_right      not_determined (WRONG, label prohibited): The obscured remainder of the arrow prevents
                        determining whether a right-turn branch exists.
Step 6  u_turn          not_determined (WRONG, label prohibited): The obscured remainder of the arrow prevents
                        fully determining its permitted movements.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay within the solid white boundaries and continue straight as indicated by the
                        visible arrowhead. Confirm the complete lane arrow and intersection controls before
                        planning any turn; no stopping position is identifiable here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6475, out 1054, 17.86 s

culane_test__d100_05251222_0385_04920 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection beneath an elevated
                        railway. My car is behind a black sedan in a through lane; one same-direction lane is
                        visible to the left, but the truck and image edge prevent a reliable count of lanes to
                        the right. (lanes None, mine 2, partial)
Step 2  Left            A single solid white line runs along the left of my lane, with another traffic lane
                        beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with another traffic lane
                        beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted immediately ahead of
                        the hood, with its forward-pointing head below the sedan.; line:stop_line (partial): A
                        transverse white stop line is visible ahead, with part of its span obscured by the
                        sedan.; line:crosswalk (partial): White pedestrian-crossing stripes are visible beyond
                        the stop line; the sedan obscures part of the crossing through my lane.
Step 4  Cross-check     position: The lane lines on both sides agree with an interior lane. One same-direction
                        lane is visible to the left; the total lane count remains uncertain on the right. |
                        roles: Both boundaries are solid white lines separating same-direction approach lanes,
                        consistent with their lane-line roles. | markings: The straight arrow agrees with a
                        through approach lane between solid guide lines; the stop line and crossing do not
                        specify additional movements. | unseen: The total lane count and the obscured portions
                        of the transverse markings have not been inferred as fully visible. | result:
                        consistent
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
Step 5  Rule            line:stop_line: The stop line identifies where my car stops when required to yield or
                        wait to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding
                        or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        it does not determine any of the seven requested actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight guide arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight; do not cross either solid boundary to change
                        lanes. Follow the traffic signals, stop before the stop line when required, and keep
                        the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6541, out 1489, 26.62 s

culane_test__d100_05251222_0385_05250 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues ahead beneath an elevated structure, with no
                        intersection or lane ending visible. My car is in the leftmost of three same-direction
                        lanes. (lanes 3, mine 1, full)
Step 2  Left            A continuous solid white line borders my lane on the left, with diagonal white
                        hatching and a guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being the leftmost of three same-direction lanes. | roles: The broken white right
                        boundary fits a same-direction lane line. The left boundary visibly has white paint
                        despite its position at the left roadway edge; its edge role follows from the hatched
                        margin and guardrail beyond it. | markings: No arrows, words, symbols or transverse
                        lines are visible in my lane. The diagonal hatching is outside its left boundary. |
                        unseen: No unseen junction markings or lane-end movements have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the solid left edge and do not enter the hatched margin during normal
                        driving. You may change right across the broken line after checking traffic; no
                        visible junction arrows establish turn permissions.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 933, 14.31 s

culane_test__d100_05251309_0397_03150 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward a distant
                        junction. My car is in the rightmost lane, behind the SUV, beside a raised roadside
                        verge. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right edge of my lane beside a raised curb and
                        grassy verge, with a separate paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is painted
                        behind the SUV; the right-pointing head is clear, while the forward portion is partly
                        obscured by the SUV.
Step 4  Cross-check     position: Three lanes and a rightmost ego position agree with a lane divider on the
                        left and a road edge on the right. | roles: The broken white divider fits a same-
                        direction lane line, and the solid white roadside line fits a right edge line. |
                        markings: The combined straight-and-right arrow is consistent with this rightmost
                        lane; no conflicting word, symbol or waiting area is visible. | unseen: The SUV
                        obscures part of the arrow and the pavement farther ahead; no hidden stop line or
                        additional marking is asserted. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, and the
                        raised curb also forms a physical road edge. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The combined arrow indicates straight or right movements from
                        this lane, excluding left turns and U-turns. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The identifiable combined straight-and-right arrow permits going
                        straight under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-and-right arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-pointing arrow head permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-and-right arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight or turn right at the junction; do not cross the
                        solid right edge or curb. For a left turn or U-turn, change left only when safe and
                        select a lane explicitly marked for that movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7736, out 1053, 15.75 s

culane_test__d100_05251309_0397_03390 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. My car is in
                        the third of four visible approach lanes, with another lane between it and the right-
                        hand traffic island. (lanes 4, mine 3, full)
Step 2  Left            A continuous white line separates my lane from the lane occupied by the white van; no
                        curb lies along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the approach lane to its right; the
                        raised island is beyond that adjacent lane, not on my boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): The forward-pointing head of a white straight arrow is
                        visible immediately above the hood; its lower portion is obscured.; arrow:straight
                        (full): A smaller white straight-ahead arrow is visible farther along my lane near the
                        intersection.; line:stop_line (partial): A transverse white stop line is visible at
                        the end of the approach, although its distant appearance limits detail.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane: two approach lanes lie
                        to the left and one to the right. | roles: White solid boundaries fit same-direction,
                        no-crossing approach lane lines. | markings: The visible straight arrows agree with
                        each other and with a lane bounded by solid approach lines. | unseen: The hood hides
                        the lower part of the nearest arrow; its visible head agrees with the farther straight
                        arrow. Fine detail at the stop line is limited by distance. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible straight arrow indicates straight-ahead travel, with its
                        lower portion hidden. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The complete straight arrow permits straight-ahead travel rather than
                        left turns, right turns or U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The farther straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight and do not cross either solid boundary. Obey the
                        applicable traffic signal and stop before the stop line when required; turning
                        requires a suitably marked lane reached before the solid-line approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6541, out 1564, 29.34 s

culane_test__d100_05251327_0403_00180 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three visible lanes in this direction continues toward a
                        distant overhead structure. My car is in the leftmost lane; no intersection or lane
                        ending is clearly visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane beside a raised curb, with a paved
                        verge and trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from the same-
                        direction lane occupied by the dark sedan; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible directly
                        ahead in my lane; its lower shaft is hidden by the hood.
Step 4  Cross-check     position: The left road edge and right lane divider agree with my car being in lane 1
                        of three same-direction lanes. | roles: The broken white right boundary fits a same-
                        direction lane divider. The left paint visibly appears white despite its position at
                        the left roadway edge; its color is recorded as seen rather than inferred from the
                        usual color convention. | markings: The visible straight arrowhead is consistent with
                        a continuing through lane; no conflicting guidance marking is visible. | unseen: The
                        arrow shaft is partly hidden by the hood, and distant markings cannot be resolved;
                        neither has been reconstructed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The identifiable straight-ahead arrow indicates straight travel rather
                        than a left turn, right turn or U-turn from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a raised curb also forming the road edge.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The visible straight arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn from this
                        lane under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn from this
                        lane under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn from this lane
                        under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the readable arrowhead governs travel direction despite its hidden shaft,
                        the boundaries govern only their respective crossing actions, and no unseen waiting
                        area is assumed.
Advice                  Continue straight in this lane and do not cross the solid left edge or curb. If a
                        different movement is needed, change right across the broken divider only when safe
                        and seek the appropriate signed or marked lane ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7736, out 1067, 16.86 s

culane_test__d100_05251327_0403_00630 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A barrier-lined, divided urban roadway continues ahead with no intersection or lane
                        ending visible. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane, with a narrow paved
                        strip and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car being in lane
                        1 of 2. | roles: The broken white right boundary fits a same-direction lane divider.
                        The solid white left boundary visibly marks the roadway edge beside a barrier,
                        although its white colour differs from the supplied rule prescribing yellow for a left
                        edge. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No unseen intersection, lane-use arrow or
                        continuation beyond the visible stretch has been inferred. | result: Observations are
                        consistent; the observed left-edge paint colour is retained rather than changed to
                        match the prescribed colour.
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, with an emergency exception only when safe. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left edge line normally prohibits crossing under
                        CN-4.2.2-a, and a concrete barrier lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: only boundary-crossing actions are decided by the visible boundaries;
                        absent movement markings do not establish permission for an unseen intersection.
Advice                  Remain within the left edge line; do not move toward the barrier. You may change into
                        the right lane across the broken white line after checking traffic and a safe gap; no
                        visible markings establish turn permissions or a stopping point ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 916, 14.19 s

culane_test__d100_05251327_0403_00930 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three visible lanes in this direction continues toward a
                        distant junction. My car is in the leftmost lane beside a raised landscaped median.
                        (lanes 3, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane, with a narrow paved
                        strip and a raised median curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead.
Step 4  Cross-check     position: Three same-direction lanes and ego position 1 agree with a median-side edge
                        on the left and a lane divider on the right. | roles: The broken white right boundary
                        fits a same-direction lane line. The left boundary is visibly white despite its
                        median-side position; its physical location establishes its edge-line role, although
                        the colour differs from the supplied convention for left edges. | markings: The
                        straight-only arrow agrees with the continuing lane; no conflicting words, arrows or
                        waiting areas are visible in my lane. | unseen: No stop line or additional marking can
                        be resolved in the distant junction area; none is inferred. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal edge line normally prohibits crossing to
                        the left, with only the stated safe-emergency exception. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The single straight arrow designates straight travel from this lane,
                        excluding left turns, right turns and U-turns. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow designates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not designate a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not designate a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not designate a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the solid median-side boundary. If a turn
                        is needed, change right across the broken divider when safe and select a lane whose
                        markings permit that turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7736, out 1000, 15.91 s

culane_test__d100_05251327_0403_01200 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An elevated, barrier-lined urban road continues straight ahead, with no intersection
                        or lane ending visible. My car is in the middle of three lanes travelling in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long painted segments and gaps, separates my lane
                        from another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken white line, with visible segments and gaps, separates my lane from
                        another traffic lane on the right; the concrete barrier is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White pavement text is visible ahead in my lane, but its
                        characters cannot be read confidently at this distance.
Step 4  Cross-check     position: Three lanes with my lane second from the left agrees with a same-direction
                        lane line on each side. | roles: Both white broken boundaries fit their roles as
                        crossable same-direction lane lines. | markings: The partially legible pavement text
                        does not establish a directional restriction or contradict the boundaries; no
                        identifiable directional arrow or waiting area is visible. | unseen: The pavement text
                        has not been guessed, and movements at an unseen intersection have not been inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            text:other: No supplied passage covers this unreadable pavement text, and text does
                        not govern any of the seven movement actions under the supplied definitions.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible directional marking governs this action.
Step 6  turn_left       not_applicable: No visible directional marking governs this action.
Step 6  turn_right      not_applicable: No visible directional marking governs this action.
Step 6  u_turn          not_applicable: No visible directional marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may remain in the middle lane or cross either broken boundary after checking
                        traffic and clearance. No junction movement or stopping requirement can be established
                        from the visible markings; read the pavement text as you approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 1045, 18.86 s

culane_test__d100_05251327_0403_02340 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road curves gently left, with traffic continuing ahead and no visible
                        intersection or lane ending. My car is in the leftmost of two apparent same-direction
                        lanes. (lanes 2, mine 1, partial)
Step 2  Left            A continuous white line follows a raised curb and fenced divider on the left; opposing
                        traffic is beyond the divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with another paved strip
                        between it and the roadside curb; no marking identifying that strip's use is visible.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left edge and divider establish that my lane is leftmost; the apparent
                        second lane could instead be a non-motorized strip, so the total motor-lane count
                        remains uncertain. | roles: The left line functions as an edge line despite its
                        visibly white paint; the right solid white line could be a lane line or motor/non-
                        motor separation line. | markings: No readable arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: The use of the strip to the
                        right and the road beyond the visible curve cannot be established; no unseen guidance
                        markings are inferred. | result: Consistent with a provisional lane count and an
                        unresolved right-boundary role.
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing left,
                        and the raised divider is also a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid longitudinal line normally prohibits crossing right;
                        its uncertain specific role provides no visible exception. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised divider lies beyond.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
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
Step 7  Reflect         Consistent: solid boundaries prohibit normal crossing, while the absence of visible
                        movement markings does not establish permission for intersection movements.
Advice                  Stay between the solid boundaries through the visible curve; do not cross either for a
                        normal lane change. Observe the posted 30 km/h limit and reassess turn guidance when
                        an intersection becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6414, out 989, 19.51 s

culane_test__d100_05251327_0403_03870 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated structure and continues around a bend ahead; no
                        intersection or lane ending is visible. My car is in the left lane of two apparent
                        same-direction lanes, behind a sedan. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line runs beside a raised curb and narrow paved walkway on the
                        left, with a wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears solid along the visible stretch to the right of my lane, with
                        another traffic lane beyond; its continuation is obscured by the sedan and my hood.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being the leftmost of two same-direction lanes. | roles: The solid white right
                        boundary fits a no-crossing lane line. The left line visibly marks the roadway edge,
                        although its white paint differs from the yellow prescribed for a left edge of a
                        directional carriageway. | markings: No guidance arrows, words, symbols, waiting areas
                        or transverse markings are visible in my lane. | unseen: The sedan and hood hide part
                        of the lane surface, and the road beyond the bend cannot be assessed; no hidden
                        markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal edge line normally prohibits crossing to
                        the left; the curb also forms a physical roadway edge. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my lane into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_applicable: No visible marking governs this movement.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary restrictions govern only crossing their respective sides, and the
                        absence of visible movement markings is not treated as permission to turn.
Advice                  Remain within the current lane without crossing either solid boundary, and leave a
                        safe gap behind the sedan. The photo does not establish turn permissions or a stopping
                        point at an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6414, out 958, 18.37 s

culane_test__d100_05251327_0403_03960 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A narrow urban road runs alongside an elevated structure, with two apparent lanes in
                        this direction. My car is in the left lane behind a sedan; the distant road and any
                        junction markings are partly obscured. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line follows a raised curb on the left, with a narrow paved strip
                        and the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous on the visible stretch to the right of the sedan,
                        separating my lane from another paved traffic lane; its continuation ahead is
                        obscured.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my lane
                        being the first of two same-direction lanes. | roles: The white right-hand divider
                        fits a same-direction lane line. The left line is visibly white despite being a left
                        roadway edge; its color has not been inferred from the expected convention. |
                        markings: No arrows, words, symbols, waiting areas, or transverse lines are readable
                        in the visible portions of my lane. | unseen: The sedan and hood conceal portions of
                        the lane surface, and distant markings cannot be assessed. No hidden markings have
                        been assumed. | result: consistent
Step 5  Rule            left_boundary: The visible solid edge line normally prohibits crossing to the left;
                        the raised curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white same-direction lane divider prohibits crossing
                        to the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane divider prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The lane surface ahead is obscured, so any lane-end directional
                        marking cannot be determined.
Step 6  turn_left       not_determined: The lane surface ahead is obscured, so any lane-end directional
                        marking cannot be determined.
Step 6  turn_right      not_determined: The lane surface ahead is obscured, so any lane-end directional
                        marking cannot be determined.
Step 6  u_turn          not_determined: The lane surface ahead is obscured, so any directional or prohibited-
                        movement marking cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the visible boundaries and keep a safe distance behind the sedan; do
                        not cross either solid line. Confirm lane-use markings as the view opens before
                        choosing a movement at the next junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6734, out 969, 18.84 s

culane_test__d100_05251627_0452_02850 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches an underpass, with opposing traffic beyond a median
                        fence on the left. My car is in the leftmost of three visible lanes travelling in this
                        direction; vehicles and darkness obscure the road farther ahead. (lanes 3, mine 1,
                        full)
Step 2  Left            A continuous pale white line follows the left edge of my lane beside a raised median
                        base and metal fence; a yellow strip lies closer to the fence, with opposing traffic
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A faint white line appears continuous between my lane and the adjacent lane occupied
                        by the yellow taxi; wear and vehicles obscure its farther continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and same-direction lane on the right agree with
                        my position as lane 1 of 3. | roles: The white right boundary fits a same-direction
                        lane line. The left paint appears white despite its median-side location; its edge
                        role follows the physical median, not an assumed yellow colour. | markings: No
                        readable arrows, words, symbols, areas or transverse lines are visible in my lane. |
                        unseen: No hidden guidance marking is inferred; traffic and the dark underpass limit
                        inspection farther ahead. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing to the
                        left, and the physical median also prevents a normal lane change. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white lane line prohibits crossing from my lane into
                        the lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 6  change_left     prohibited (correct): The solid left edge line prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
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
Step 7  Reflect         consistent: boundary restrictions govern only crossing their respective sides, and no
                        intersection movement permission is inferred from the absence of visible arrows.
Advice                  Remain in this lane without crossing either visible solid boundary, and leave space
                        behind the vehicle ahead. The photo does not establish turn permissions or a stopping
                        position; check the signals and newly visible markings as you approach the underpass.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6870, out 1079, 20.69 s

culane_test__d100_05251718_0469_00390 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in a through lane; the outer approach lanes are partly outside the
                        image, so the total lane count and exact lane index cannot be established confidently.
                        (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line runs along the left of my lane toward the intersection, with
                        another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane toward the intersection,
                        with another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.; line:stop_line (full): A
                        solid white transverse stop line crosses my lane before the pedestrian crossing.;
                        line:crosswalk (full): Broad white pedestrian-crossing stripes extend across my lane
                        beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from same-direction lanes, confirming an
                        interior lane; the exact number of lanes on either side is not confidently countable.
                        | roles: The white solid boundaries fit same-direction no-crossing lane lines on an
                        intersection approach. | markings: The visible straight arrowhead agrees with a
                        through guide lane; the stop line precedes the crosswalk. | unseen: The arrow shaft is
                        partly hidden by the hood, and no exact lane count or index is asserted. No waiting
                        area is visible. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The identifiable straight-ahead arrow permits straight travel rather
                        than turning out of this lane. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when required to wait
                        or yield. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing; it
                        does not determine any of the seven lane-movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The identifiable forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not indicate a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not indicate a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not indicate a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight; do not cross either solid boundary to reach a
                        turn lane here. Follow the applicable traffic signal, stop before the stop line when
                        required, and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6541, out 1624, 33.31 s

culane_test__d100_05251718_0469_01320 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road passes beneath a pedestrian footbridge, with two lanes travelling in
                        this direction. My car is in the left lane; no intersection or lane ending is visible
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb on the left, with a paved pedestrian area
                        and bridge supports beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from another traffic lane on the right; vehicles
                        obscure part of its farther stretch.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left road edge and the lane divider on the right agree with my car
                        occupying lane 1 of 2. | roles: The broken white divider fits a same-direction lane
                        line. The left edge paint appears white despite the supplied rule prescribing yellow
                        for a left edge; its colour is reported as seen, not inferred from its position. |
                        markings: No guidance arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: The leading vehicle hides some pavement ahead, so no
                        markings underneath it are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb lies beside it.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits crossing under
                        CN-5.2.1-2.
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
Step 7  Reflect         Consistent: boundary rules govern only the corresponding lateral crossing, and no
                        permission for an intersection movement is inferred from the absence of visible
                        arrows.
Advice                  Stay clear of the left curb and solid edge line; a right lane change is permitted by
                        the broken divider only when the adjacent lane is clear. Keep a safe following
                        distance, and check later markings and signs before choosing a turning movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 985, 17.65 s

culane_test__d100_05251718_0469_02040 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb on the left, with a planted median beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of 2. | roles: The broken white right boundary fits a same-direction lane
                        divider. The left line appears white despite bordering the median; its edge role
                        follows from the visible curb, not an assumed yellow colour. | markings: No arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        movement marking or intersection beyond the visible stretch has been inferred;
                        vehicles obscure some distant pavement. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left edge line normally prohibits crossing under
                        CN-4.2.2-a, with a raised curb immediately beyond.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
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
Step 7  Reflect         Consistent: boundary rules govern only their respective crossing actions, and no
                        intersection movement permission is inferred from the absence of arrows.
Advice                  Remain within the left curb and broken white divider; a right lane change is permitted
                        by the marking only when traffic conditions are safe. No visible intersection guidance
                        establishes a turn lane or stopping point.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 894, 13.53 s

culane_test__d100_05251718_0469_02250 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight, with traffic ahead and no
                        intersection or lane ending visible. My car is in the leftmost of two same-direction
                        lanes, beside a raised landscaped median. (lanes 2, mine 1, full)
Step 2  Left            A continuous raised gray curb borders the lane on the left, with grass, trees and
                        hedges beyond; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gap, separates my lane from the same-
                        direction lane occupied by the silver car; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and the lane line on the right agree with being lane 1 of two
                        same-direction lanes. | roles: The curb forms the left roadway edge, and the broken
                        white line separates same-direction lanes. | markings: No guidance markings are
                        visible within my lane, so none contradict the boundaries. | unseen: No unseen arrows
                        or intersection markings are inferred; the hood obscures the nearest pavement and the
                        next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: No supplied passage specifically authorizes crossing a raised curb; the
                        physical roadway edge is not a traversable lane-change boundary.
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The raised median curb is a physical edge, not a traversable
                        lane-change boundary.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
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
Advice                  Stay clear of the raised median curb. You may change right across the broken white
                        line after checking clearance around the silver car; no visible markings establish
                        turning permissions or a stopping point ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6997, out 892, 14.66 s

culane_test__d100_05251718_0469_05070 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues ahead, with two visible lanes in this
                        direction. My car is in the leftmost lane beside the raised landscaped median; no
                        intersection or lane ending is clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A narrow solid white line runs beside a raised curb on the left, with a planted median
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of two same-direction lanes. | roles: The broken white right boundary fits a
                        same-direction lane divider. The left boundary is physically the roadway edge,
                        although its visible white paint differs from the prescribed yellow left-edge colour.
                        | markings: No readable arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No distant lane-use marking or intersection layout has
                        been inferred from the overhead sign or vehicles. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised median curb lies alongside it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the boundaries govern only their respective crossing actions, and no
                        intersection movement is inferred from the overhead sign.
Advice                  Stay clear of the left median curb; a rightward lane change is permitted by the broken
                        line only when safe. Check the overhead lane-direction sign and subsequent pavement
                        markings before choosing a lane for the next intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 932, 14.5 s

culane_test__d100_05251718_0469_05190 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road continues straight ahead with traffic travelling in the same
                        direction. My car is in the middle of three lanes; no intersection or lane ending is
                        clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 2 agree with a lane line on each
                        side. | roles: Both white broken boundaries fit crossable same-direction lane lines. |
                        markings: No visible arrows, words, symbols, transverse lines or waiting areas in my
                        lane create a conflict. | unseen: No distant intersection layout or concealed lane
                        guidance has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
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
Advice                  Stay centred in the middle lane; either broken boundary may be crossed after checking
                        mirrors, blind spots and traffic gaps. No visible markings establish turn permissions
                        or a stopping point, so check the guidance farther ahead before choosing a lane for a
                        turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 809, 10.41 s

culane_test__d100_05251947_0499_00840 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided multilane road continues ahead, with opposing traffic beyond the
                        median on the left and an elevated roadway on the right. My car is in the leftmost
                        lane; the far-right roadway extent is difficult to resolve in the low light. (lanes
                        None, mine 1, partial)
Step 2  Left            A solid white painted line runs beside the raised concrete median on the left, with
                        opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and adjoining gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes that my lane is leftmost, and the
                        right lane line confirms another same-direction lane; the total lane count remains
                        uncertain. | roles: The broken white right boundary fits a same-direction lane line.
                        The left boundary is an edge beside a physical median, although its visibly white
                        paint differs from the prescribed yellow left edge line. | markings: No arrows, words,
                        symbols, transverse markings or waiting areas are discernible in my lane. | unseen:
                        The total lane count and any markings beyond the clearly visible stretch have not been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies alongside it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible movement arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible movement arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible movement arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible movement arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: only boundary-crossing actions are decided by the visible boundaries, and
                        no intersection movement permission is inferred from the absence of arrows.
Advice                  Stay clear of the solid line and raised median on the left; a rightward lane change is
                        permitted by the broken line when traffic conditions are safe. No visible intersection
                        markings establish turn permissions or a stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 957, 14.44 s

culane_test__d100_05251947_0499_04830 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road continues straight ahead, with traffic in the distance and
                        landscaped verges. My car appears to be in the rightmost of three same-direction
                        lanes; the distant intersection approach is difficult to resolve in the low light.
                        (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with visible separated dashes and gaps, lies to my left, with
                        another same-direction lane beyond it and no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faint continuous white line follows the right edge beside a raised curb and planted
                        verge; darkness reduces the clarity of the paint.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes appear to lie to my left, while the curb and verge bound my right,
                        consistent with lane 3 of 3. | roles: The broken white left boundary fits a same-
                        direction lane divider; the white right boundary beside the curb fits a roadway edge.
                        | markings: No guidance marking can be read confidently in my lane; faint distant
                        paint cannot establish a lane-use direction. | unseen: No arrow direction, stop line,
                        or waiting area is inferred from the indistinct distant pavement. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: No supplied passage specifically authorizes crossing a raised curb;
                        the physical roadway edge is not a usable lane-change route.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The raised curb forms a physical edge, not a traversable lane
                        boundary.
Step 6  go_straight     not_determined (WRONG, label prohibited): Distant lane-use markings cannot be
                        resolved, so the movement permitted at the lane end is uncertain.
Step 6  turn_left       not_determined (WRONG, label prohibited): Distant lane-use markings cannot be
                        resolved, so left-turn permission is uncertain.
Step 6  turn_right      not_determined (WRONG, label allowed): Distant lane-use markings cannot be resolved,
                        so right-turn permission is uncertain.
Step 6  u_turn          not_determined (WRONG, label prohibited): Distant lane-use markings cannot be
                        resolved, so U-turn permission is uncertain.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          identifiable in view.
Step 7  Reflect         consistent: the visible broken divider permits changing left, the curb prevents
                        changing right, and unreadable distant markings do not establish intersection
                        movements.
Advice                  Keep clear of the right curb; a leftward lane change is permitted across the broken
                        line only when safe. Read the lane arrows and intersection controls as they become
                        visible before choosing a turning lane; no stopping position can be identified
                        reliably here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:right']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 7736, out 1081, 21.91 s

culane_test__d100_05252026_0512_00450 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, divided urban road at night continues toward distant traffic signals. My car is
                        in the rightmost of three visible same-direction lanes. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip and
                        a raised landscaped edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The rightmost lane position agrees with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white lane separator
                        and solid white right edge line fit their observed roles. | markings: No readable
                        guidance markings appear within my lane in the visible stretch. | unseen: Distant
                        pavement near the signals is too small and partly obscured by vehicles to establish
                        intersection arrows or transverse markings; none are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant lane-end pavement is not readable enough to establish a
                        governing directional marking.
Step 6  turn_left       not_determined: The distant lane-end pavement is not readable enough to establish a
                        governing directional marking.
Step 6  turn_right      not_determined: The distant lane-end pavement is not readable enough to establish a
                        governing directional marking.
Step 6  u_turn          not_determined: The distant lane-end pavement is not readable enough to establish a
                        governing directional marking.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary decisions follow the visible lines, and intersection movements
                        remain undecided because the relevant distant pavement is unreadable.
Advice                  Remain inside the solid right edge line; a safe lane change left is permitted across
                        the broken line. Confirm lane-direction markings and signals closer to the
                        intersection before choosing a turning lane; no stop line is readable here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 944, 14.9 s

culane_test__d100_05252026_0512_01020 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road at night, with traffic continuing ahead and opposing headlights
                        to the left. My lane has another same-direction lane on its left and at least one on
                        its right; darkness prevents a reliable total lane count or identification of the next
                        intersection. (lanes None, mine 2, partial)
Step 2  Left            A white longitudinal marking separates my lane from the lane occupied by the car
                        ahead-left; only a limited illuminated stretch is clear, so its continuity cannot be
                        established reliably, and no curb forms this boundary.
                        white none, curb no, lane_line, evidence partial
Step 2  Right           White broken line segments with intervening dark gaps separate my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane; the visible lane to
                        the left places my lane second from the left, while the far-right lane arrangement is
                        unclear. | roles: Both white boundaries fit separation of same-direction traffic; the
                        left boundary's solid or broken pattern remains unresolved. | markings: No arrows,
                        words, symbols, transverse lines or waiting areas can be identified in my lane. |
                        unseen: The lane total, left-line pattern and distant lane-end markings are not
                        inferred from the darkness. | result: consistent
Step 5  Rule            left_boundary: A broken boundary permits crossing and a solid boundary normally
                        prohibits it, so the unresolved pattern prevents deciding whether my car may cross
                        left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: The visible broken white lane line permits crossing into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     not_determined (WRONG, label allowed): The left lane-line pattern is insufficiently
                        visible to distinguish permission to cross from a solid-line prohibition.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     not_determined: The distant lane end is too dark to establish whether a lane-use arrow
                        governs this movement.
Step 6  turn_left       not_determined: The distant lane end is too dark to establish whether a lane-use arrow
                        governs this movement.
Step 6  turn_right      not_determined: The distant lane end is too dark to establish whether a lane-use arrow
                        governs this movement.
Step 6  u_turn          not_determined: The distant lane end is too dark to establish whether a directional or
                        prohibited-movement marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No identifiable waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Keep your lane until the left boundary and upcoming direction markings are clearer;
                        the broken right boundary permits a lane change only after checking adjacent traffic.
                        No turn-lane assignment or stopping position can be established from this image.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 1118, 23.32 s

culane_test__d100_05252026_0512_01350 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road at night continues ahead, with vehicles in the distance and no
                        clearly visible intersection. My car is in the rightmost lane; darkness and glare make
                        the total number of same-direction lanes uncertain. (lanes None, mine None,
                        insufficient)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow paved margin
                        and a raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to the left, and the
                        right edge line places my car in the rightmost lane; the total lane count and
                        numerical index remain uncertain. | roles: The broken white lane separator and solid
                        white right edge line fit their assigned roles. | markings: No readable arrows, words,
                        symbols, areas or transverse lines are visible in my lane. | unseen: The distant lane
                        surface is obscured by darkness, traffic and windshield glare; no distant markings or
                        lane ending are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The lane end and any movement markings there are hidden by distance,
                        darkness and glare.
Step 6  turn_left       not_determined: The lane end and any movement markings there are hidden by distance,
                        darkness and glare.
Step 6  turn_right      not_determined: The lane end and any movement markings there are hidden by distance,
                        darkness and glare.
Step 6  u_turn          not_determined: The lane end and any movement markings there are hidden by distance,
                        darkness and glare.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted by the visible broken
                        line only when safe. Reassess movement arrows and stopping requirements as the road
                        ahead becomes clearer.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 985, 16.11 s

culane_test__d193_06042058_0527_02610 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, physically divided road continues straight at night, with two lanes in this
                        direction and no visible intersection or lane ending. My car is in the right-hand
                        lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible long dash and gaps, separates my lane from the
                        lane carrying the car ahead to the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow dark paved
                        strip beyond; no raised curb is clearly discernible at the line.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 2 agree with a lane line on the left and a
                        roadway edge line on the right. | roles: The broken white separator fits a same-
                        direction lane line, and the solid white right boundary fits an edge line. | markings:
                        No arrows, words, symbols, waiting areas or transverse markings are discernible in my
                        lane. | unseen: The distant roadway and the physical edge beyond the right line are
                        poorly resolved; no hidden markings or curb have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe; the supplied edge-line passages provide no applicable
                        ordinary-crossing permission. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The clearly visible solid right boundary normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible movement marking governs this action.
Step 6  turn_left       not_applicable: No visible movement marking governs this action.
Step 6  turn_right      not_applicable: No visible movement marking governs this action.
Step 6  u_turn          not_applicable: No visible movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the visible boundary patterns determine crossing actions, while the
                        absence of visible movement markings does not establish permission for intersection
                        movements.
Advice                  Remain within the right edge line; moving into the left lane is permitted by the
                        dashed separator only when safe. No intersection movement guidance or stopping line is
                        visible, so do not infer turn or U-turn permission from this image.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 821, 10.65 s

culane_test__d193_06042058_0527_03240 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit multilane road at night continues ahead with no intersection or lane ending
                        visible. My car is in the right lane of two visible lanes travelling in this
                        direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the white vehicle; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip and
                        roadside posts beyond it; no raised curb is visible at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my car
                        occupying lane 2 of 2. | roles: The broken white separator fits a same-direction lane
                        line, and the solid white right boundary fits a roadway edge line. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are discernible in my lane.
                        | unseen: No markings or intersection layout beyond the visible stretch are inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible marking governs this movement.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain within the right edge line. A left lane change is permitted by the markings,
                        but the white vehicle alongside must be allowed for; no visible markings establish
                        turn permissions or a stopping point ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 758, 10.74 s

culane_test__d193_06051114_0632_02790 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection. My car is behind the
                        red car in a through lane, with another lane to the left and additional roadway to the
                        right; fading paint makes the total same-direction lane count uncertain. (lanes None,
                        mine 2, partial)
Step 2  Left            A worn white line runs along the left of my lane and appears continuous over the
                        visible approach, with another same-direction lane beyond it and no curb on this
                        boundary.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A faded solid white line extends diagonally from the right foreground toward the red
                        car, separating my lane from same-direction roadway on the right; no curb forms this
                        boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A faded white straight-ahead arrow is visible in my lane
                        behind the red car; its forward portion is partly obscured.
Step 4  Cross-check     position: Lane lines on both sides place my car in an interior lane. The lane visible
                        between my left boundary and the median supports position 2, but the outer lanes on
                        the right cannot be counted confidently. | roles: White paint fits same-direction lane
                        separation; the visible continuous stretches fit solid approach lane lines, although
                        the left line is especially worn. | markings: The visible straight arrow agrees with a
                        through lane bounded by approach lane lines. The left-turn arrow farther left belongs
                        to the adjacent lane, not mine. | unseen: No stop line, crosswalk, waiting area, or
                        additional arrow head can be read confidently in my lane. The total lane count and the
                        worn left boundary remain uncertain. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing, but wear prevents a fully
                        confident classification of this boundary. [CN-6.2.1] "The no-crossing lane line
                        separates vehicles travelling in the same direction and prohibits vehicles on the
                        solid-line side from crossing. It has two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the
                        roadway on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 5  Rule            arrow:straight: A straight-only guide arrow permits straight travel and excludes
                        turns, provided its partly obscured head has no additional branch. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     not_determined (WRONG, label prohibited): The worn left boundary appears solid, which
                        CN-6.2.1 prohibits crossing, but its classification is not fully secure.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible straight-ahead arrow indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The arrow's forward portion is partly
                        obscured, preventing confident exclusion of an additional left branch.
Step 6  turn_right      not_determined (WRONG, label prohibited): The arrow's forward portion is partly
                        obscured, preventing confident exclusion of an additional right branch.
Step 6  u_turn          not_determined (WRONG, label prohibited): The arrow is partly obscured, so its
                        complete set of permitted movements cannot be verified.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent: rightward crossing is prohibited, while uncertainty in the worn left
                        boundary and partly obscured arrow is retained rather than converted into definite
                        permissions or prohibitions.
Advice                  Remain in this lane for the visible straight-ahead movement and do not cross the solid
                        right boundary; treat the worn left boundary as no-crossing unless clarified. Check
                        the complete arrow and traffic signals ahead before proceeding; a stopping position
                        cannot be identified confidently from this image.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6475, out 1224, 24.02 s

culane_test__d193_06051114_0632_04320 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues ahead, with opposing traffic behind a median
                        fence and a separated roadside path on the right. My car is in the left lane of two
                        lanes in this direction; no intersection or lane ending is clearly visible. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid white painted line runs beside the median fence and its raised base, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A worn broken white line separates my lane from the adjacent same-direction lane
                        occupied by the black sedan; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.
Step 4  Cross-check     position: The median edge on the left and a same-direction lane line on the right
                        agree with being lane 1 of 2. | roles: The broken white right boundary fits a same-
                        direction lane divider. The left paint appears white despite being at the left roadway
                        edge; its physical location beside the median establishes its edge role without
                        reclassifying its observed color. | markings: The visible straight arrowhead agrees
                        with the continuing lane; no conflicting word, area, or directional head is visible. |
                        unseen: The arrow shaft is partly hidden by the hood, and the distant end of the lane
                        is not readable; no unseen stop line or waiting area is assumed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary, which is also physically bounded by the median fence. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight guide arrow permits straight travel and restricts
                        movements out of this lane to the indicated direction. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed: The visible forward arrowhead indicates straight travel under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not indicate a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not indicate a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not indicate a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the median-side solid line. A
                        rightward lane change is permitted by the broken line, but give way to the black sedan
                        and check the adjacent lane; use later lane guidance to select a lane for any turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 7736, out 1060, 17.75 s

culane_test__d193_06051123_0635_00450 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road approaches a broad intersection with a zebra crossing. My car is
                        in the leftmost of three visible lanes in its direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid yellow line runs along my lane's left side to the stop line, with
                        opposing-direction roadway beyond and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent same-direction lane on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white transverse stop line spans my lane immediately
                        before the zebra crossing.; line:crosswalk (full): White zebra-crossing stripes extend
                        across the road immediately beyond the stop line.
Step 4  Cross-check     position: The center line on the left and two same-direction lanes to the right agree
                        with three lanes and ego lane index 1. | roles: The solid yellow center line separates
                        opposing traffic; the solid white lane line separates same-direction traffic. |
                        markings: The stop line and crossing agree with an intersection approach. No lane-use
                        arrow, prohibited-movement marking, or waiting area is visible. | unseen: The hood
                        obscures the closest pavement; no markings beneath it are inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits crossing my left
                        boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing my right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when yielding or waiting to
                        proceed, without specifying a permitted turning movement. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage covers the zebra crossing; it identifies a
                        pedestrian crossing and does not determine any of the seven actions.
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
                        action; the center line governs only crossing the left boundary.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: both boundary crossings are prohibited, while intersection movements are
                        not assigned permissions absent governing markings.
Advice                  Stay between the solid boundaries; do not change lanes in this visible approach. These
                        markings do not establish which intersection movements this lane serves: check signs
                        and signals, keep the crossing clear, and stop before the stop line when required.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6274, out 1085, 14.4 s

culane_test__d193_06051123_0635_00900 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently ahead, with no visible intersection or lane
                        ending. My car is in the single motor-vehicle lane in its direction, between a yellow
                        centre line and a white edge line. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line runs along the left of my lane, with opposing-
                        direction roadway beyond it and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs along the right of my lane, with a roadside strip
                        beyond it and a raised sidewalk curb farther to the right, not at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane in my direction agrees with a centre line on the left
                        and an edge line on the right. | roles: The solid yellow centre line separates
                        opposing traffic; the solid white edge line marks the right limit of the motor-vehicle
                        lane. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No unseen intersection markings or lane-end movements
                        have been inferred; the roadside curb is distinguished from the actual right boundary.
                        | result: consistent
Step 5  Rule            left_boundary: The single solid yellow centre line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The solid white longitudinal edge line normally prohibits crossing the
                        right boundary, with an exception for a safe emergency crossing. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid yellow centre line prohibits crossing under CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this movement.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this movement.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this movement.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this movement; the centre line
                        governs boundary crossing, not movement at an unseen intersection.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the curve within the yellow centre line and white edge line; do not cross
                        either in normal driving. No intersection movement arrows or stopping point are
                        visible, so assess turning arrangements when they come into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6521, out 837, 12.93 s

culane_test__d193_06051123_0635_00990 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead with no clearly visible intersection or lane
                        ending. My car is in the single motor-vehicle lane in its direction, with a narrow
                        roadside strip to the right. (lanes 1, mine 1, full)
Step 2  Left            A single broken yellow line, with visible long dashes and gaps, separates my lane from
                        opposing traffic; there is no curb at this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A single broken white line, with visible dashes and gaps, separates my lane from a
                        narrow roadside strip; the raised sidewalk curb is beyond that strip rather than at my
                        lane boundary.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and the roadside edge line on the right
                        agree with one motor-vehicle lane in my direction, indexed 1. | roles: The broken
                        yellow line fits a crossable center line; the broken white line fits the boundary of
                        the roadside strip. | markings: No arrows, words, symbols, waiting areas or transverse
                        lines are visible in my lane. | unseen: No movement arrows or distant intersection
                        controls have been inferred; the roadside strip is not assumed to be another motor-
                        vehicle lane. | result: consistent
Step 5  Rule            left_boundary: The broken center line permits crossing to overtake or turn when doing
                        so does not affect safety. [CN-5.1.1] "The crossable centre line separates traffic
                        flows in opposite directions. It means vehicles may cross the line to overtake, turn
                        or make a U-turn when this does"
Step 5  Rule            right_boundary: The broken longitudinal line permits crossing into or out of the
                        roadside strip, without establishing that the strip is a normal driving lane.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): The broken yellow center line permits safe crossing under CN-5.1.1.
Step 6  change_right    allowed (correct): The broken white boundary permits crossing under CN-4.2.2-a.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action; center-
                        line crossing permission does not determine movement at a future intersection.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane between the yellow center line and white roadside boundary.
                        Cross either broken boundary only when safe, checking for opposing traffic on the left
                        and cyclists or other roadside users on the right; no visible lane-use marking assigns
                        turning movements.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6718, out 901, 15.13 s

culane_test__d193_06051123_0635_01980 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches an intersection. There are three lanes in this
                        direction, and my car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; the roadside curb is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Three same-direction lanes and lane index 2 agree with a lane line on each
                        side. | roles: Both white solid boundaries fit same-direction no-crossing lane lines
                        on an intersection approach. | markings: The straight arrow is consistent with a
                        straight-ahead guide lane bounded by solid white lines; the arrows in neighboring
                        lanes do not govern my lane. | unseen: No distant stop line, crosswalk, or additional
                        marking is readable enough to report; none has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The straight-only arrow allows proceeding straight and excludes left
                        turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, subject to intersection signals and signs, without
                        crossing either solid boundary. For a turn, select the appropriate marked lane before
                        the solid-line section; no stopping position is clearly readable here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6475, out 940, 13.01 s

culane_test__d193_06051123_0635_02160 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the rightmost approach lane, which is marked for a right turn;
                        the far-left extent of the approach is cropped. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another approach lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line curves along the right of my lane, with a diagonally hatched paved
                        wedge beyond it and a raised roadside curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has one head pointing right, with no straight-
                        ahead head.; line:stop_line (full): A transverse solid white stop line crosses the end
                        of the approach lane before the pedestrian crossing.; line:crosswalk (full): White
                        zebra-crossing stripes extend across the roadway immediately beyond the stop line.
Step 4  Cross-check     position: The left lane line establishes another same-direction lane to my left, and
                        the right edge line establishes that my lane is rightmost; cropping prevents a
                        reliable total count and therefore a numerical index from the left. | roles: The solid
                        white left boundary fits an intersection approach lane separator; the solid white
                        right boundary fits an edge adjoining a hatched roadside wedge. | markings: The right-
                        only arrow agrees with the rightmost approach position. The stop line and crossing do
                        not add any permitted movement. | unseen: No total lane count is inferred from the
                        cropped left side. The hatched wedge is outside my lane, not an area painted within
                        it. | result: consistent
Step 5  Rule            left_boundary: The solid white same-direction lane separator prohibits my car from
                        crossing left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-only guide arrow permits a right turn and excludes straight,
                        left-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car should stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing; it
                        identifies a pedestrian crossing location and does not govern any of the seven
                        movement decisions.
Step 6  change_left     prohibited (correct): The solid white lane separator prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     prohibited (correct): The right-only arrow excludes straight travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain within the solid boundaries and use this lane for a right turn only; do not
                        move onto the hatched wedge. Obey the applicable signal, stop before the stop line
                        when required, and check for pedestrians before turning.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 7090, out 1371, 22.15 s

culane_test__d193_06051123_0635_03690 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection. My car is in the
                        middle of three visible approach lanes travelling in this direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Two closely spaced solid white lines separate my lane from the adjacent lane on the
                        left; no curb forms this boundary.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another approach lane on the right; no curb
                        forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in the centre of my lane has one head pointing
                        straight ahead.; line:stop_line (full): A transverse solid white stop line spans my
                        lane at the intersection approach.; line:crosswalk (full): White zebra-crossing
                        stripes cross the projected path of my lane immediately beyond the stop line.
Step 4  Cross-check     position: Lane boundaries on both sides agree with my position as lane 2 of 3, with a
                        same-direction lane on either side. | roles: Both boundaries are white longitudinal
                        markings separating same-direction lanes; their solid patterns indicate no crossing. |
                        markings: The straight-only arrow agrees with the solid approach boundaries and the
                        stop line ahead; no waiting area is visible. | unseen: No hidden markings or
                        additional arrowheads have been inferred; the crosswalk is explicitly beyond the stop
                        line. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal lines prohibit ordinary crossing to the left,
                        with only the stated safe-emergency exception. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The single straight arrow designates straight-ahead travel, excluding
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        it does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white longitudinal boundary prohibits ordinary
                        crossing under CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits straight-ahead travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid boundary.
                        Obey the traffic signal, stop before the stop line when required, and keep the
                        pedestrian crossing clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6654, out 1352, 21.28 s

culane_test__d193_06051411_0691_03960 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road curves gently left, with a median fence on the left and shops
                        and parked vehicles on the right. Two same-direction lanes are visible; my car is in
                        the left lane, and no intersection or lane end is clearly visible ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid yellow line follows the base of a raised median fence on the left, with
                        opposing traffic beyond the fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A faded broken white line, with visible segments and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb along this dividing line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side left edge and the lane divider on the right agree with my
                        car being in lane 1 of 2. | roles: The yellow solid line fits the left carriageway
                        edge, and the broken white line fits a same-direction lane divider. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No movement restriction or intersection layout has been inferred from the
                        distant road. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left;
                        the raised median fence also physically prevents that movement. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid yellow left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
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
Advice                  Follow the road's gentle left curve without crossing the median boundary. A right lane
                        change is permitted by the broken line when safe, but watch for parked vehicles and
                        roadside activity; no visible markings establish turn-lane assignments or a stopping
                        point.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 871, 12.78 s

culane_test__d193_06051603_0727_01080 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           My car is on a single-lane right-hand branch separating from a wider urban road, with
                        a painted gore and a divider developing on the left and a concrete barrier on the
                        right. The branch continues ahead; no intersection is visible. (lanes 1, mine 1, full)
Step 2  Left            A worn solid white line borders the diagonal white hatching on the left; farther
                        ahead, a raised divider with posts separates this branch from the adjacent roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A concrete barrier forms the right edge of the lane, with no separate painted boundary
                        line clearly visible along its base.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The ego branch has one lane, bounded by roadway edges rather than lane
                        dividers; the lanes across the gore belong to the adjacent roadway. | roles: The left
                        solid white line visibly borders the gore and serves as an edge, although its white
                        colour does not match the supplied rule prescribing yellow for a left edge line. The
                        right physical barrier forms an unpainted edge. | markings: No arrows, words, symbols
                        or transverse markings are visible inside my lane. The diagonal hatching lies outside
                        its left boundary. | unseen: No lane-use arrow or intersection beyond the visible
                        stretch is inferred. | result: Consistent geometry; the observed white left edge is
                        retained despite the colour-rule mismatch.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised divider also prevents an ordinary lane change farther ahead.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: No supplied passage directly governs crossing a concrete barrier; as a
                        physical roadway edge, it cannot be used for a rightward lane change.
Step 6  change_left     prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised divider continues ahead.
Step 6  change_right    prohibited (correct): The concrete barrier physically closes the right boundary.
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
Step 7  Reflect         Consistent: boundary restrictions govern only lateral crossing, and the absence of
                        movement arrows is not treated as permission for intersection movements.
Advice                  Stay within the single-lane branch; do not cross the solid left boundary or the
                        hatched gore, and keep clear of the right barrier. Follow the branch ahead and check
                        subsequent signs and markings for your intended route.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6414, out 1003, 20.22 s

culane_test__d193_06051603_0727_01620 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane elevated ramp curving left between concrete barriers. No
                        intersection, lane ending, or merge is visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A concrete barrier with a metal rail forms the left edge, beside a narrow pale
                        pavement strip; no distinct painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A continuous concrete barrier forms the right edge, with a narrow strip at its base
                        and no distinct painted boundary line visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The physical edges on both sides and absence of an internal lane divider
                        agree with one lane and ego lane index 1. | roles: Both boundaries are physical
                        roadway edges; neither is identified as a painted lane line or centre line. |
                        markings: No arrows, words, symbols, transverse lines, or marked waiting areas are
                        visible in the lane. | unseen: No paint colour or line pattern is inferred from the
                        pale strips beside the barriers; the road beyond the bend is not assessed. | result:
                        consistent
Step 5  Rule            left_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        as a physical roadway boundary, it is not a traversable lane-change boundary.
Step 5  Rule            right_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        as a physical roadway boundary, it is not a traversable lane-change boundary.
Step 6  change_left     prohibited (correct): The concrete barrier physically closes the left side; crossing
                        it is prohibited.
Step 6  change_right    prohibited (correct): The concrete barrier physically closes the right side; crossing
                        it is prohibited.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the barriers prohibit lateral departures, while the absence of movement
                        markings does not establish permission for turns or a U-turn.
Advice                  Stay within the single ramp lane and follow its leftward curve; neither side permits a
                        lane change. Keep a safe distance from the vehicle ahead and adjust speed for the
                        bend.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6414, out 888, 14.86 s

culane_test__d193_06051734_0757_00000 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, three-lane expressway continues straight ahead, with no intersection, ramp
                        or lane ending visible. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and a middle-lane position agree with a same-direction lane line
                        on each side. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane separators. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No hidden
                        markings or intersection movements have been inferred; the distant continuation is too
                        small to assess in detail. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent left lane
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent right
                        lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): The broken white left lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white right lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along the expressway; either broken white boundary may be crossed after
                        checking mirrors, blind spots and safe gaps. No junction, turning guidance or stopping
                        point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 765, 9.94 s

culane_test__d193_06051734_0757_02430 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided highway with three lanes in this direction continues straight ahead, with no
                        intersection, ramp or lane ending visible. My car is in the middle lane. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps ahead of the hood, separates my lane
                        from another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane across each
                        boundary. | roles: Both boundaries are broken white lines, consistent with crossable
                        same-direction lane lines. | markings: No guidance arrows, words, symbols, waiting
                        areas or transverse traffic markings are visible in my lane; the transverse pavement
                        seam is not a traffic marking. | unseen: No markings or intersection movements have
                        been inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either broken white boundary may be crossed after
                        checking surrounding traffic and blind spots. No turn guidance or stopping point is
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 809, 10.29 s

culane_test__d193_06051734_0757_04050 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A single-lane ramp curves right toward an overpass, with guardrails on both sides. My
                        car is in the only visible travel lane; no intersection or lane ending is visible.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line borders the lane on the left, with a narrow paved
                        shoulder and a raised edge and guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A continuous solid white line borders the lane on the right, with a paved shoulder and
                        a raised edge and guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane with roadway edge lines on both sides agrees with my lane being the
                        only travel lane. | roles: Both lines visibly separate the travel lane from shoulders,
                        supporting edge-line roles. The left line is visibly white despite CN-5.4.3 specifying
                        yellow for a left-side edge line; its observed color is retained. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No features beyond the visible curve are inferred. The raised edges and
                        guardrails are beyond the shoulders, not immediate lane boundaries. | result:
                        consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, with an exception for an emergency when safe; the supplied edge-line passages
                        provide no different crossing permission here. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        right, with an exception for an emergency when safe; the supplied edge-line passages
                        provide no different crossing permission here. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid white left edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white right edge line normally prohibits crossing
                        under CN-4.2.2-a.
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
Step 7  Reflect         Consistent: the solid boundaries prohibit ordinary crossing, and no unobserved
                        movement markings or waiting areas are used to decide actions.
Advice                  Stay between the solid white edge lines and follow the ramp's rightward curve; do not
                        move onto either shoulder in ordinary driving. The roadside chevrons reinforce the
                        curve, and no stop line is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6414, out 934, 14.61 s

culane_test__d193_06060642_0768_00360 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight urban road continues ahead, with opposing traffic to the left and a planted
                        separator along the right. My car is in the rightmost of two lanes in its direction;
                        no intersection or lane ending is clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           White painted segments with intervening gaps run beside a raised curb and planted
                        separator on the right.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 2 agree with a lane line on the left
                        and a roadway edge on the right. | roles: The broken white left line fits a crossable
                        same-direction lane divider; the white right line and curb identify the roadway edge.
                        | markings: No readable arrows, words, symbols, waiting areas or transverse lines are
                        visible in my lane. | unseen: No movement restriction or distant intersection marking
                        has been inferred from the unobstructed but increasingly distant roadway. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: This passage recognizes a curb as a physical roadway outline; although
                        the broken paint itself is crossable, the raised curb is a physical edge rather than
                        an available lane-change route. [CN-5.4.5] "Where a non-motorized lane is needed and
                        there is no separating facility between it and the motor vehicle lanes, a motor/non-
                        motor separation line shall be prov"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The raised curb physically bounds the lane; crossing the broken
                        paint does not provide a route through that physical edge.
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
Step 7  Reflect         consistent: the left change follows the broken lane line, the right change is
                        restricted by the physical curb rather than the broken paint, and no intersection
                        movement permission is inferred.
Advice                  Remain within the curb-bounded roadway; a left lane change is permitted across the
                        broken white divider when safe. No visible lane-use markings establish turn
                        permissions or a stopping point ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6884, out 1146, 22.38 s

culane_test__d193_06060642_0768_00900 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently right, with an overpass visible ahead and no clear
                        intersection or lane ending in view. My car is in the rightmost of two lanes
                        travelling in this direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line follows the right edge of my lane beside a raised curb, with
                        planting and a separate paved roadside area beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 2 agree with a lane line on the
                        left and a roadway edge on the right. | roles: The broken white line fits a same-
                        direction lane separator; the solid white line beside the curb fits the right roadway
                        edge. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No direction arrows or intersection movements are
                        inferred from the distant roadway; the lane's eventual end is outside clear view. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white longitudinal boundary normally prohibits crossing to
                        the right, with only the stated safe-emergency exception. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb lies beyond it.
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
Step 7  Reflect         consistent: the boundary decisions follow the observed lines, and no intersection
                        movement is inferred without a governing marking.
Advice                  Follow the road's gentle right curve and stay inside the solid right edge beside the
                        curb. You may change left across the broken white line when safe; choose a lane for
                        any upcoming turn only after its guidance becomes visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 834, 11.21 s

culane_test__d193_06060642_0768_03060 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs beside an elevated roadway, with three lanes travelling in
                        this direction. My car is in the rightmost lane; the distant junction approach and
                        pavement markings are small in the image. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the green bus; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip
                        beyond it and a raised sidewalk curb farther away.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge line on the right agree with my
                        position as lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white line fits a right roadway edge. | markings: No arrow,
                        word, symbol or transverse line is readable with confidence in my lane; a small
                        distant white pavement marking cannot be resolved sufficiently to identify its
                        directions. | unseen: No direction is inferred from the distant marking or from the
                        overhead sign; the lane's eventual stop line is not discernible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to a safe gap.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant pavement guidance is too small to establish whether
                        straight travel is indicated.
Step 6  turn_left       not_determined: The distant pavement guidance is too small to establish whether a left
                        turn is indicated.
Step 6  turn_right      not_determined: The distant pavement guidance is too small to establish whether a
                        right turn is indicated.
Step 6  u_turn          not_determined: The distant pavement guidance is too small to establish whether a
                        U-turn is indicated.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: boundary-crossing decisions follow the visible lines, while junction
                        movements remain undecided because the distant guidance cannot be read.
Advice                  Stay inside the solid right edge line. Confirm the lane arrows and overhead guidance
                        before selecting a junction movement; if a leftward lane change is needed, cross the
                        broken line only after checking carefully for the bus and other traffic.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7623, out 1102, 22.16 s

culane_test__d193_06060748_0790_02970 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad multilane road with dense traffic continuing ahead; no intersection or lane
                        ending is visible. My car is behind the red hatchback, apparently in the middle of
                        five same-direction lanes. (lanes 5, mine 3, partial)
Step 2  Left            A broken white line separates my lane from the lane containing the white van farther
                        ahead; a dash and the gap ahead are visible, with no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line runs beside the cream minibus, separating my lane from another
                        same-direction lane; visible painted segments have gaps, and there is no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides establish that my lane is an interior lane,
                        consistent with the apparent third-of-five position; vehicles obscure parts of the
                        outer lanes, so the total count is less certain. | roles: White broken boundaries fit
                        crossable separators between same-direction lanes. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        hidden guidance marking is inferred; traffic and the hood obscure portions of the
                        pavement, and the lane's eventual end is not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane separator permits crossing into
                        the lane on the left. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 5  Rule            right_boundary: The broken white same-direction lane separator permits crossing into
                        the lane on the right. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
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
Step 7  Reflect         consistent; boundary permissions apply only to lateral crossings, and no intersection
                        movement permission is inferred from the absence of visible arrows.
Advice                  Either broken boundary may be crossed only when a safe gap exists; nearby vehicles
                        make careful checks essential. No visible marking establishes a turn lane or stopping
                        point, so reassess guidance as the road ahead becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 1441, 32.69 s

culane_test__d193_06060919_0820_00450 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with parked vehicles along the right curb and
                        oncoming traffic to the left. My car is in the single visible through lane in its
                        direction; no intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faded yellow broken line, with a visible dash and gap, runs to the left of my car;
                        opposing traffic lies beyond it.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           No painted boundary is discernible on the right; a raised roadside curb and sidewalk
                        form the edge farther ahead, partly hidden by parked cars and interrupted by an access
                        opening.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and roadside edge on the right agree with one
                        lane in my direction, indexed 1. | roles: The yellow broken line separates opposing
                        traffic; the unpainted curb defines the right roadway edge rather than another traffic
                        lane. | markings: No readable arrows, words, symbols, waiting areas, or transverse
                        markings appear in my lane. | unseen: Parked vehicles conceal portions of the right
                        edge, and the distant end of the lane is not resolved; no hidden markings are assumed.
                        | result: consistent
Step 5  Rule            left_boundary: The broken center line permits crossing the left boundary, subject to
                        safe conditions and opposing traffic. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A curb can define an unpainted roadway edge; it is a physical
                        boundary, not a traversable adjacent lane. [CN-5.4.5] "Where a non-motorized lane is
                        needed and there is no separating facility between it and the motor vehicle lanes, a
                        motor/non-motor separation line shall be prov"
Step 6  change_left     allowed (correct): CN-4.2.2-a permits crossing the visible broken yellow center line.
Step 6  change_right    prohibited (correct): The raised curb forms the right physical edge; the access
                        opening does not establish an adjacent lane.
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
Step 7  Reflect         consistent: boundary decisions concern only crossing their respective sides, and no
                        intersection movement is inferred from the absence of arrows.
Advice                  Stay in the current lane and allow clearance for parked vehicles, pedestrians, and
                        scooters. Crossing the broken yellow line is marking-permitted but enters opposing
                        traffic; do not cross unless safe, and do not drive over the right curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 5706, out 1010, 18.91 s

culane_test__d193_06060925_0822_01260 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beside an elevated roadway, with no intersection
                        or lane ending visible. My car is in the rightmost of three lanes travelling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line runs along the right edge of my lane, with a narrow
                        paved margin and a raised curb topped by fencing beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my lane being lane 3 of
                        3. | roles: The broken white line separates same-direction lanes, and the solid white
                        line follows the right roadway edge. | markings: No arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: No markings at a distant
                        intersection or beyond the visible road have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to cross into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing to the right,
                        with an emergency exception only when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right boundary normally prohibits crossing under
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
Advice                  Stay within the right edge line; a left lane change is permitted by the dashed marking
                        if traffic conditions allow. No visible markings establish turn permissions at a
                        forthcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 849, 12.52 s

culane_test__d193_06060925_0822_02700 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban boulevard continues straight ahead, with four lanes in this direction
                        and no visible intersection or lane ending. My car is in the third lane from the left.
                        (lanes 4, mine 3, full)
Step 2  Left            A broken white line with long dashes and visible gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and position three agree with same-direction lane lines on both
                        sides: two lanes lie to my left and one to my right. | roles: Both white broken
                        boundaries fit crossable same-direction lane lines. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        marking at a distant intersection is inferred; the lane's eventual end is outside the
                        readable view. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may cross either broken lane boundary after checking traffic and ensuring a safe
                        gap. No visible arrows establish the lane to use for a future turn, and no stopping
                        line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6479, out 862, 14.4 s

culane_test__d193_06060925_0822_04140 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward a distant
                        overpass. My car is in the rightmost lane beside the sidewalk; no intersection stop
                        line or lane ending is clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right edge beside a raised curb, with the sidewalk and
                        roadside railing beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow directly ahead has a single forward-pointing head
                        and no visible turning branch.
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a roadway edge on the right. | roles: The broken white left line fits a crossable
                        lane divider; the solid white right line and curb fit the right roadway edge. |
                        markings: The straight arrow is consistent with the continuing lane; no conflicting
                        word, symbol or waiting area is visible. | unseen: No hidden markings or distant
                        intersection details have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        right, and the raised curb also forms a physical edge. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight from this lane and
                        excludes left turns, right turns and U-turns. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits ordinary crossing under
                        CN-4.2.2-a, with a curb beyond.
Step 6  go_straight     allowed (correct): The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line when safe. Do
                        not cross the right edge or curb; for another movement, first locate an appropriately
                        marked lane rather than assuming the adjacent lane permits it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7736, out 1021, 16.55 s

culane_test__d193_06060925_0822_04320 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight beneath a pedestrian bridge, with a bus stop
                        and paved stopping bay on the right. My car is in the rightmost of three through
                        lanes; no intersection or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another through lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Broad broken white segments separate my lane from the paved bus-stop bay on the right;
                        the raised roadside curb lies beyond that bay rather than along my lane boundary.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three through lanes and an ego position of third from the left agree with a
                        lane line on the left and the boundary to a roadside stopping bay on the right. |
                        roles: The broken white left line fits a crossable same-direction lane separator; the
                        broader broken white right line fits access to the roadside bay. | markings: No
                        guidance marking is visible within my lane. The visible arrow to the left belongs to
                        the adjacent lane. | unseen: No arrow, word, stop line, intersection movement
                        restriction or waiting area has been inferred beyond the visible road. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken edge line at the roadside stopping-bay opening permits
                        crossing for access to the bay, subject to other applicable restrictions. [CN-5.4.6]
                        "At roadside openings and on sections where roadside parking is allowed, the edge line
                        is a broken edge line as needed ..."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The broken edge line allows access across the
                        boundary to the roadside bay under CN-5.4.6; this does not establish permission to
                        stop there.
Step 6  go_straight     not_applicable: No marking in my lane governs this movement.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in the through lane rather than drifting into the bus-stop bay, and watch for
                        buses entering or leaving it. A left lane change is permitted by the broken line when
                        safe; no visible marking establishes turn permissions at a forthcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6479, out 1105, 20.65 s

culane_test__d193_06060925_0822_04680 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beside a landscaped separator and a parallel
                        roadway on the right. My car is in the right-hand lane of two lanes travelling in this
                        direction; the next intersection is not clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane, with a narrow paved
                        margin and a raised curb beside the landscaped separator beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A worn but readable white arrow in my lane has one head
                        pointing straight ahead.
Step 4  Cross-check     position: Two same-direction lanes and my position in lane 2 agree with a lane divider
                        on the left and a roadway edge on the right. | roles: The broken white divider fits a
                        crossable same-direction lane line; the solid white line beside the roadside curb fits
                        a right edge line. | markings: The straight-only arrow is consistent with the visible
                        lane boundaries; no conflicting word, symbol or waiting area is visible. | unseen: No
                        distant stop line or intersection layout is inferred; the road farther ahead is partly
                        obscured by vehicles and distance. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        right, with an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): Crossing the solid white right boundary is normally prohibited
                        under CN-4.2.2-a.
Step 6  go_straight     allowed: The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the solid right edge line. A left lane
                        change is permitted when safe, but for any turn use a lane explicitly marked for that
                        movement; the adjacent lane's suitability for turning is not established here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 7736, out 1081, 17.39 s

culane_test__d193_06060925_0822_05310 | lane | Test R | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a planted median on the left and a
                        raised roadside strip on the right. My car is in the rightmost of three lanes
                        travelling in this direction; no intersection or lane ending is clearly visible.
                        (lanes 3, mine 3, full)
Step 2  Left            A faded broken white line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved strip beyond
                        it and a raised curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane line on the left
                        and a roadway edge line on the right. | roles: The broken white left line fits a same-
                        direction lane divider; the solid white right line fits a right-hand roadway edge. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are discernible
                        in my lane. | unseen: No direction marking or intersection layout has been inferred
                        from the distant road; the curb beyond the right edge line is not treated as the
                        immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-direction marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-direction marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-direction marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-direction marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted across the broken
                        line after checking traffic. No visible arrows establish turn permissions or a
                        required turn lane, so reassess the markings when approaching an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7220, out 869, 11.9 s

culane_test__d37_05181608_0235_03090 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection. My car is behind a taxi in
                        a right-side channelized approach lane; the full number of same-direction lanes is not
                        reliably visible. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line borders the lane on the left, with diagonal white channelizing
                        paint and a large yellow traffic barrel beyond it; the taxi obscures its continuation.
                        white solid, curb no, other, evidence partial
Step 2  Right           A solid white line runs along the right side beside a metal separation fence, with a
                        separate roadside space beyond; the fence forms a physical boundary.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse solid white line is visible ahead, with its
                        central portion hidden by the taxi.; line:crosswalk (partial): Broad white pedestrian-
                        crossing stripes extend across the approach beyond the stop line, partly hidden by the
                        taxi and other road users.
Step 4  Cross-check     position: The visible lane is bounded by channelization on the left and a roadside
                        separation fence on the right; the total lane count and numerical lane position cannot
                        be confirmed. | roles: The left white line borders a channelized separation rather
                        than an immediately adjacent traffic lane; the right white line and fence fit a
                        roadway-edge boundary. | markings: The stop line and crossing are compatible with an
                        intersection approach. No lane-use arrow can be read in the exposed portion of my
                        lane. | unseen: The taxi hides pavement that could contain a lane-use arrow; no arrow
                        direction or hidden boundary continuation is inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: This line identifies the roadway edge, and the visible physical fence
                        makes moving across this boundary prohibited. [CN-5.4.1] "The carriageway edge line
                        marks the edge of motor vehicle lanes or non-motorized vehicle lanes, or the boundary
                        between motor vehicle lanes and non-motorized ve"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        it does not determine any of the seven requested actions.
Step 6  change_left     prohibited (correct): The solid white longitudinal boundary normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The right boundary is physically blocked by a separation fence.
Step 6  go_straight     not_determined: The taxi hides pavement that could contain the lane-use arrow
                        determining this movement.
Step 6  turn_left       not_determined: The taxi hides pavement that could contain the lane-use arrow
                        determining this movement.
Step 6  turn_right      not_determined: The taxi hides pavement that could contain the lane-use arrow
                        determining this movement.
Step 6  u_turn          not_determined: The taxi hides pavement that could contain the lane-use arrow
                        determining this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the channelized lane and do not cross the solid left boundary or the
                        right-side fence. Confirm the lane-use markings as the taxi moves, obey the signals,
                        and stop before the stop line when required while keeping the pedestrian crossing
                        clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6480, out 1176, 20.07 s

culane_test__d37_05181608_0235_03720 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight ahead, with opposing traffic behind the
                        median fence on the left. My car is in the leftmost of three apparent same-direction
                        lanes; traffic obscures parts of the lane layout farther ahead. (lanes 3, mine 1,
                        partial)
Step 2  Left            A solid white line runs beside a raised median curb and metal fence, with opposing
                        traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Broken white paint separates my lane from the same-direction lane occupied by the
                        white hatchback; vehicles and the hood obscure much of its nearer extent.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane line on the right
                        agree with my lane being leftmost; the total lane count is less certain because of
                        traffic. | roles: The broken white right boundary fits a same-direction lane divider.
                        The left paint appears white despite its position beside the median; its edge role
                        follows the visible curb and fence, not an assumed yellow colour. | markings: No
                        readable arrows, words, symbols, transverse lines or waiting areas are visible in my
                        lane. | unseen: The nearby right boundary and distant pavement are partly obscured; no
                        hidden guidance markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        where a raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible broken white same-direction lane divider permits crossing
                        into the adjacent lane. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median curb lies beyond it.
Step 6  change_right    allowed (correct): The identifiable broken white lane divider permits crossing under
                        CN-5.2.1-2, although its nearer extent is obscured.
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
Step 7  Reflect         consistent: crossing decisions follow the observed boundaries, while no intersection
                        movement permission is inferred from the absence of visible arrows.
Advice                  Remain clear of the median and do not cross the solid left edge. A rightward lane
                        change is permitted across the broken divider only after checking the white hatchback
                        and other traffic; intersection lane choices and any stopping point are not
                        established by this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7333, out 1059, 19.29 s

culane_test__d37_05181608_0235_05220 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A wide urban road with several same-direction lanes has queued traffic ahead near a
                        signalized intersection. My car is between two white lane boundaries; vehicles obscure
                        the outer lanes and much of the approach. (lanes None, mine None, insufficient)
Step 2  Left            A single continuous white line runs along my left, with another lane of queued
                        vehicles beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line runs along my right, with another lane of vehicles
                        beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines and same-direction vehicles on both sides establish that my lane
                        is an interior lane, but the outer lanes are obscured, preventing an exact count or
                        index. | roles: Both white solid boundaries fit no-crossing lane lines separating
                        same-direction traffic. | markings: No guidance marking within my lane can be read;
                        the car ahead obscures much of the pavement. | unseen: No arrows, stop line, or
                        waiting area are inferred from the obscured approach. | result: consistent
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
Step 6  go_straight     not_determined: Vehicles obscure the pavement ahead where a lane-use arrow could
                        govern this movement.
Step 6  turn_left       not_determined: Vehicles obscure the pavement ahead where a lane-use arrow or
                        prohibited-movement marking could govern this movement.
Step 6  turn_right      not_determined: Vehicles obscure the pavement ahead where a lane-use arrow or
                        prohibited-movement marking could govern this movement.
Step 6  u_turn          not_determined: Vehicles obscure the pavement ahead where a lane-use arrow or
                        prohibited-movement marking could govern this movement.
Step 6  enter_waiting_areanot_determined: Queued vehicles obscure the approach and any marked waiting area
                          ahead or directly to the left.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and maintain space behind the queued car. Confirm
                        your lane's permitted movements and stopping position when the pavement becomes
                        visible, and obey the intersection signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6072, out 846, 13.31 s

culane_test__d37_05181608_0235_05340 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A busy multilane urban road has queues of traffic ahead, with the car between occupied
                        lanes on both sides. Vehicles obscure the outer road edges and the approach ahead, so
                        the total lane count, lane index and next intersection layout cannot be established.
                        (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line runs along the left of this lane, with another lane of
                        queued vehicles beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of this lane, with another lane of
                        vehicles beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane lines and vehicles on both sides establish an interior lane, but do
                        not establish the total number of lanes or its index from the left. | roles: Both
                        white solid boundaries fit no-crossing lines separating traffic travelling in the same
                        direction. | markings: No guidance marking is readable on the exposed pavement in this
                        lane; vehicles conceal much of the lane ahead. | unseen: No arrows, transverse lines
                        or waiting areas have been inferred beneath the queued vehicles; the lane-end markings
                        remain hidden. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing the left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing the right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Queued vehicles hide the lane-end pavement where movement arrows could
                        be marked.
Step 6  turn_left       not_determined: Queued vehicles hide the lane-end pavement where movement arrows or
                        restrictions could be marked.
Step 6  turn_right      not_determined: Queued vehicles hide the lane-end pavement where movement arrows or
                        restrictions could be marked.
Step 6  u_turn          not_determined: Queued vehicles hide the lane-end pavement where movement arrows or
                        restrictions could be marked.
Step 6  enter_waiting_areanot_determined: The approach ahead is obscured, so the presence of a left-turn
                          waiting area cannot be determined.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and maintain a safe gap in the queue. Check the
                        lane arrows, stop line, signs and signals as they become visible before choosing an
                        intersection movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6072, out 837, 12.01 s

culane_test__d37_05181919_0299_02970 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road with three visible motor-vehicle lanes in this direction
                        continues toward a distant intersection. My car is in the rightmost lane, behind a
                        dark sedan; roadside vehicles and two-wheelers are beyond its right boundary. (lanes
                        3, mine 3, full)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, separating it from the
                        roadside strip occupied by vehicles and two-wheelers; no curb forms this immediate
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible immediately ahead of
                        the hood, with its forward-pointing head behind the sedan; the sedan obscures the lane
                        farther ahead.
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and the roadway edge on the right. | roles: The broken white left line fits a
                        crossable lane divider; the solid white right line fits a right-hand carriageway edge.
                        | markings: The straight-ahead arrow is consistent with the lane boundaries; no
                        conflicting marking is visible in my lane. | unseen: The sedan and distance hide later
                        pavement markings and any intersection stop line; none is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits proceeding straight and
                        restricts this lane against left turns, right turns and U-turns. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The visible straight arrow indicates straight-ahead travel under
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
Advice                  Use this lane to continue straight, and do not cross its solid right edge. For a turn
                        or U-turn, move safely across the broken left divider to an appropriately marked lane
                        before any solid approach markings; watch the braking sedan and roadside traffic.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7623, out 1047, 16.64 s

culane_test__d37_05181919_0299_03120 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection. My car is in the
                        middle of three same-direction lanes, with vehicles alongside on both sides. (lanes 3,
                        mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft is hidden by the hood.; arrow:straight (full): A
                        smaller white straight-ahead arrow is visible farther ahead in my lane.
Step 4  Cross-check     position: Three lanes and position 2 agree with same-direction lane boundaries on both
                        sides. | roles: Both boundaries are white solid lines, consistent with no-crossing
                        lane lines on an intersection approach. | markings: The visible forward arrows agree
                        with each other and with a straight-ahead guide lane; no conflicting words or areas
                        are visible. | unseen: The hood hides the nearest arrow's lower portion, and distant
                        traffic limits inspection of the lane's end; no hidden stop line or waiting area is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing the left
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing the right
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible straight-ahead arrow indicates straight travel rather than
                        turning. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 5  Rule            arrow:straight: The farther straight-ahead arrow permits straight travel and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight-ahead arrows indicate this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel; do not cross either solid white boundary to
                        reach a turn lane here. The signal ahead appears red: obey the applicable signal and
                        stop before the intersection's stop line, whose position is not clearly visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6475, out 1082, 15.72 s

culane_test__d37_05190927_0395_02340 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an intersection. My car is beside the raised planted
                        median, behind a truck; vehicles obscure much of the roadway to the right and the lane
                        ahead. (lanes None, mine 1, partial)
Step 2  Left            A solid white painted line follows a raised median curb, with planting and a fence
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from same-direction traffic on the right;
                        the silver car obscures its nearer continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge places my lane leftmost; a lane line on the right agrees
                        with visible same-direction lanes there, although their total count is obscured. |
                        roles: The solid white right boundary fits a no-crossing lane line. The left paint
                        appears white despite being beside the median; its edge role follows the visible curb,
                        not an assumed yellow color. | markings: No guidance marking can be read on the
                        exposed pavement of my lane; the truck hides the farther approach. | unseen: No
                        arrows, stop line, or waiting area are inferred beneath vehicles. The complete lane
                        count and downstream markings remain uncertain. | result: consistent
Step 5  Rule            left_boundary: The visible solid edge line normally prohibits crossing to the left,
                        where a raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white same-direction lane boundary prohibits crossing to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The truck hides the downstream pavement where a governing lane-use
                        marking could appear.
Step 6  turn_left       not_determined: The truck hides the downstream pavement where a governing lane-use
                        marking could appear.
Step 6  turn_right      not_determined: The truck hides the downstream pavement where a governing lane-use
                        marking could appear.
Step 6  u_turn          not_determined: The truck hides the downstream pavement where a governing movement
                        marking could appear.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain between the median and the solid right lane line; do not cross either boundary.
                        Leave room behind the truck and confirm the lane-use markings, signals, and stopping
                        position when they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6734, out 999, 19.02 s

culane_test__d37_05190927_0395_02430 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches an intersection with a pedestrian crossing. My car
                        is in the leftmost lane beside a raised traffic island; three same-direction lanes are
                        visible. (lanes 3, mine 1, full)
Step 2  Left            A raised concrete island with a pole forms the left boundary; no distinct painted
                        boundary line is visible, and opposing traffic is beyond the island.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line runs toward the intersection, with another same-direction lane
                        beyond it.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft and any possible branches are hidden.;
                        line:stop_line (full): A transverse solid white line crosses the lane before the
                        pedestrian crossing.; line:crosswalk (full): Broad white pedestrian-crossing stripes
                        extend across the lane beyond the stop line.
Step 4  Cross-check     position: The island on the left and a same-direction lane on the right agree with my
                        lane being the first of three lanes. | roles: The physical island forms the left
                        roadway edge; the solid white line separates same-direction lanes. | markings: The
                        visible forward arrowhead agrees with an intersection approach, and the stop line
                        precedes the crosswalk; the hidden lower arrow prevents excluding additional
                        directions. | unseen: No painted line is inferred along the island, and no hidden
                        arrow branches are assumed. | result: consistent
Step 5  Rule            left_boundary: No supplied passage specifically governs crossing a raised island curb;
                        as a physical lane edge, it is not a traversable lane-change boundary.
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the
                        obscured remainder does not establish whether another movement is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing; it
                        identifies a pedestrian crossing area rather than governing any of the seven movement
                        actions.
Step 6  change_left     prohibited (correct): The raised island is a physical boundary, not a traversable
                        lane-change route.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (correct): The lower arrow is hidden by the hood, so a left-turn branch
                        cannot be confirmed or excluded.
Step 6  turn_right      not_determined (correct): The lower arrow is hidden by the hood, so a right-turn
                        branch cannot be confirmed or excluded.
Step 6  u_turn          not_determined (correct): The obscured portion of the arrow prevents determining
                        whether a U-turn indication is present.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within this lane for the visibly indicated straight movement; do not cross the
                        island or the solid white line. Confirm the complete arrow before attempting a turn,
                        watch for pedestrians, and stop before the stop line when required.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7203, out 1272, 21.48 s

culane_test__d37_05190927_0395_05220 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A narrow, tree-lined two-way urban street continues ahead, with opposing vehicles on
                        the left and parked vehicles on the right; no intersection is clearly visible. My car
                        is in the single visible through lane in its direction. (lanes 1, mine 1, full)
Step 2  Left            A yellow line appears continuous along the left of my lane, with opposing vehicles
                        beyond; the cyclist and vehicles obscure part of its length, and no curb forms this
                        boundary.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two closely spaced white continuous lines run beside the parked vehicles on the right;
                        the nearby SUV hides part of the boundary and the roadside edge.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with an opposing-traffic center line
                        on the left and a parking-side edge on the right. | roles: The yellow center line and
                        white parking-side boundary fit their observed roles; the visible stretches appear
                        solid. | markings: No readable arrows, words, symbols, waiting areas or transverse
                        markings are visible in my lane. | unseen: The cyclist, parked SUV and other vehicles
                        obscure portions of the boundaries; no hidden markings or curb have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The visible solid yellow center line prohibits my car from crossing
                        into the opposing side. [CN-6.1.4] "A single solid yellow line prohibits vehicles in
                        both directions from crossing. It is generally used on two-lane two-way roads with
                        limited sight distance or wh"
Step 5  Rule            right_boundary: The solid longitudinal white boundary normally prohibits crossing
                        toward the parked vehicles, with an emergency exception only when safe. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
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
                        action; the center line governs crossing the left boundary separately.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible solid boundaries prohibit lateral crossing, while no observed
                        movement markings determine movements at a lane end.
Advice                  Stay within the visible boundaries and slow or stop as necessary for the cyclist
                        immediately ahead-left and the close parked SUV on the right. No visible marking
                        establishes a turning lane or stopping point; do not infer permission to turn or make
                        a U-turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6634, out 920, 16.48 s
```
