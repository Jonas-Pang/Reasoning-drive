# Reasoning of lane run 20261114_004918_laneB_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no clearly visible
                        intersection or lane ending. My car is in the rightmost of three motor-vehicle lanes,
                        beside a separated roadside strip used by a cyclist. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction motor-vehicle lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved roadside strip containing
                        a cyclist; the raised sidewalk curb lies beyond that strip, not on my lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three motor-vehicle lanes and ego position 3 agree with a lane line on the
                        left and a motor/non-motor edge line on the right. | roles: The broken white left line
                        fits a crossable same-direction lane boundary; the solid white right line fits a
                        motor/non-motor separation boundary. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are discernible in my lane. | unseen: No distant
                        intersection layout or movement restriction has been inferred; the lane's eventual
                        endpoint is not readable. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
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
Step 7  Reflect         Consistent: boundary decisions follow the observed lines, and no intersection movement
                        permission is inferred from the absence of arrows.
Advice                  Remain inside the solid right boundary and leave clearance for the cyclist; a left
                        lane change is permitted across the broken line only when safe. No visible markings
                        establish turn-lane assignments or a stopping point ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 916, 13.14 s

culane_test__d100_05251207_0380_02130 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the middle of three lanes travelling in this direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside fence is beyond that lane, not at my
                        lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane across each
                        boundary. | roles: Both boundaries are broken white lines, consistent with crossable
                        same-direction lane lines. | markings: No arrows, text, symbols, transverse lines or
                        marked waiting areas are discernible in my lane. | unseen: No hidden markings or
                        intersection movements have been inferred; the distant lane continuation is too small
                        to assess for additional markings. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the same-direction
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The left broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right broken white lane line is crossable under CN-5.2.1-2.
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
Step 7  Reflect         Consistent: both lane changes are permitted by the observed broken lane lines, while
                        no visible marking governs the other five actions.
Advice                  Continue in the middle lane, or change to either adjacent lane after checking traffic
                        and blind spots. No turn guidance or stopping point is visible; reassess lane arrows,
                        signs and signals when approaching an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 822, 10.79 s

culane_test__d100_05251207_0380_02190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road has three visible lanes in this direction. My car is in the
                        middle lane; the road continues ahead with no visible intersection or lane ending.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and a middle-lane position agree with a same-direction lane line
                        on each side. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane separators. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No unseen
                        markings or intersection movements have been inferred; distant pavement details cannot
                        be resolved. | result: consistent
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
Step 6  go_straight     not_applicable: No visible marking governs this movement at a lane end.
Step 6  turn_left       not_applicable: No visible marking governs this movement at a lane end.
Step 6  turn_right      not_applicable: No visible marking governs this movement at a lane end.
Step 6  u_turn          not_applicable: No visible marking governs this movement at a lane end.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in the middle lane to follow the road; either broken boundary may be crossed
                        after checking traffic and clearance. No intersection movement or stopping position is
                        established by the visible markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 760, 8.79 s

culane_test__d100_05251207_0380_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with three lanes in this direction. My
                        car is in the middle lane; no intersection or lane ending is visible. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the white van; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the lane
                        occupied by the small delivery vehicle; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car being in lane 2 of 3. | roles:
                        Both boundaries are broken white lines separating same-direction lanes, consistent
                        with their lane-line roles. | markings: No visible arrows, words, symbols, transverse
                        lines or marked waiting areas conflict with the boundaries. | unseen: No lane-end
                        markings are inferred beyond the visible road or behind vehicles. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent lane on
                        the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent lane on
                        the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
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
Advice                  You may remain in the middle lane or cross either broken white boundary after checking
                        for a safe gap, particularly around the van, motorcycle and delivery vehicle. No
                        visible markings establish turn permissions or a stopping point at a next
                        intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 829, 10.55 s

culane_test__d100_05251207_0380_03270 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead; no intersection or lane
                        ending is visible nearby. My car is in the rightmost of three same-direction lanes.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved roadside
                        strip and a raised sidewalk curb farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and the rightmost position agree with a same-direction lane line
                        on the left and a roadway edge line on the right. | roles: The broken white left line
                        fits a crossable same-direction lane separator; the solid white right line fits a
                        right roadway edge. | markings: No visible in-lane arrows, words, symbols, transverse
                        lines or marked waiting areas conflict with the boundaries. | unseen: No movement
                        arrows or intersection markings are inferred from the distant road or overhead signs.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; you may change left across the broken line after
                        checking traffic. No pavement arrows yet assign intersection movements, so use
                        upcoming lane guidance and signs to choose the appropriate lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 850, 11.92 s

culane_test__d100_05251222_0385_01140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight, with an elevated structure beside the left
                        side and roadside access beyond the right edge. My car is in the leftmost of three
                        visible lanes in this direction; no intersection or lane ending is visible. (lanes 3,
                        mine 1, full)
Step 2  Left            A continuous pale white painted line follows the left edge beside a raised curb, with
                        a narrow planted strip and metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another lane travelling in the same direction; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge and right lane divider agree with my car being in lane 1 of
                        three same-direction lanes. | roles: The broken white right boundary fits a same-
                        direction lane divider. The left boundary functions visibly as a road edge, although
                        its apparent white paint differs from the prescribed yellow for a left edge; its color
                        is reported as seen. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are visible in my lane. | unseen: No movements at a distant intersection
                        or markings hidden beyond the visible road have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing the left
                        boundary; the raised curb also forms a physical road edge. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left edge line prohibits normal crossing under
                        CN-4.2.2-a.
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
Step 7  Reflect         Consistent: boundary rules decide only lateral crossing, and the absence of movement
                        markings or waiting areas is not treated as permission for intersection movements.
Advice                  Stay within the left edge; a rightward lane change is permitted across the dashed
                        divider after checking traffic and blind spots. No intersection guidance or stopping
                        point is visible, so choose any later turning lane according to the markings and
                        controls encountered ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 915, 12.73 s

culane_test__d100_05251222_0385_01710 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs alongside an elevated structure and approaches a
                        pedestrian crossing and intersection. My car is in the second lane from the left,
                        behind a white sedan. (lanes 4, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another traffic lane on the left; the
                        curb and guardrail are beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the lane occupied by the dark sedan
                        on the right, with another traffic lane farther right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing lane arrow is partly obscured by
                        the white sedan ahead.; line:crosswalk (partial): White pedestrian-crossing stripes
                        extend across the roadway ahead; the portion across my lane is partly obscured by the
                        sedan.
Step 4  Cross-check     position: Four lanes with my lane second from the left agree with another same-
                        direction lane on its left and two on its right. | roles: Both white solid boundaries
                        fit same-direction no-crossing lane lines on an intersection approach. | markings: The
                        visible straight arrow agrees with a through guide lane bounded by solid white lines;
                        no conflicting marking is visible. | unseen: The sedan obscures part of the arrow and
                        crossing, and the precise stopping position ahead cannot be read confidently; no
                        unseen stop line or waiting area is asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight guide arrow designates straight-ahead travel, rather than
                        left, right or U-turn movements. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            line:crosswalk: No supplied passage specifically governs crosswalks, and this
                        transverse marking does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The identifiable straight guide arrow permits straight-ahead travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only guide arrow does not designate a left turn
                        under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only guide arrow does not designate a right turn
                        under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only guide arrow does not designate a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: the identified arrow governs intersection movements, the solid boundaries
                        prohibit lateral crossings, and no permission is inferred from the obscured stopping
                        position.
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid boundary
                        to change lanes. Watch for pedestrians and obey the intersection controls; keep the
                        crossing clear and stop before the stop line if required once its position becomes
                        visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1241, 18.53 s

culane_test__d100_05251222_0385_02280 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road runs beside an elevated structure, with traffic ahead and a
                        possible junction farther on. My car is in the leftmost lane; vehicles obscure the
                        outer lanes and the distant approach, so the total lane count is uncertain. (lanes
                        None, mine 1, partial)
Step 2  Left            A continuous white line follows a raised curb on the left, with a narrow planted strip
                        and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White longitudinal dashes separated by clear gaps divide my lane from another same-
                        direction traffic lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left physical road edge and right lane divider place my car in lane 1;
                        the total number of lanes cannot be counted reliably through the vehicles to the
                        right. | roles: The broken white right boundary fits a same-direction lane divider.
                        The left paint appears white despite its left-edge position; the curb and guardrail
                        establish its edge role without assuming yellow paint. | markings: No guidance marking
                        is readable on the visible pavement within my lane; overhead signs are not pavement
                        arrows. | unseen: The distant lane surface and its endpoint are obscured by traffic,
                        so arrows, transverse lines, or a waiting area there cannot be established. | result:
                        consistent
Step 5  Rule            left_boundary: The visible solid boundary normally prohibits crossing to the left; the
                        raised curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_determined (WRONG, label prohibited): Traffic hides the distant pavement where a
                        lane-use arrow could determine the movement.
Step 6  turn_left       not_determined (WRONG, label allowed): Traffic hides the distant pavement where a
                        lane-use arrow could determine the movement.
Step 6  turn_right      not_determined (WRONG, label prohibited): Traffic hides the distant pavement where a
                        lane-use arrow could determine the movement.
Step 6  u_turn          not_determined (WRONG, label allowed): Traffic hides the distant pavement where an
                        arrow or prohibited-movement marking could determine the movement.
Step 6  enter_waiting_areanot_determined: The distant approach is obscured, so a waiting area ahead cannot be
                          confirmed or excluded.
Step 7  Reflect         consistent
Advice                  Do not cross the solid left edge; a rightward lane change is permitted by the dashed
                        divider only when the adjacent traffic leaves a safe gap. Check the overhead direction
                        signs and upcoming pavement arrows before choosing a junction movement; no stopping
                        position is visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1105, 21.53 s

culane_test__d100_05251222_0385_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs beside and beneath an elevated structure, with several
                        vehicles ahead. My car is in the second of four same-direction lanes; the next
                        intersection and the lane's endpoint are not clearly visible. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from another same-direction lane on the left; no
                        curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the same-direction lane occupied by the
                        white sedan on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is obscured by the hood.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being second from the left, with
                        one lane to the left and two to the right. | roles: Both boundaries are solid white,
                        consistent with no-crossing separators between same-direction lanes. | markings: The
                        visible straight arrow agrees with remaining within the solid lane boundaries; no
                        conflicting marking is visible in my lane. | unseen: The arrow's lower shaft and the
                        distant lane endpoint are not visible clearly; no additional markings or waiting areas
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing the left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing the right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight guide arrow indicates straight travel rather than left,
                        right or U-turn movements. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking governs this action.
Step 7  Reflect         consistent: both crossing prohibitions follow the solid lane lines, and movement
                        decisions follow the identifiable arrowhead rather than its obscured shaft.
Advice                  Remain in this lane for straight travel and do not cross either solid white boundary.
                        For a turn, wait for a permitted lane-change section and select an appropriately
                        marked lane; the stopping point ahead is not visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1059, 16.1 s

culane_test__d100_05251222_0385_04920 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is approaching a broad signal-controlled intersection beneath an elevated
                        railway. Three approach lanes are discernible, with the car in the middle lane behind
                        the black sedan; vehicles obscure parts of the intersection. (lanes 3, mine 2,
                        partial)
Step 2  Left            A single solid white line runs along the left of my lane, with another traffic lane
                        beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with another traffic lane
                        and the truck beyond it; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in my lane, with its
                        forward head visible immediately behind the black sedan.; line:stop_line (partial): A
                        transverse white stop line is visible at the front of the approach, partly obscured by
                        the black sedan.; line:crosswalk (partial): White pedestrian-crossing stripes are
                        visible beyond the stop line, with the portion directly ahead partly obscured by
                        vehicles.
Step 4  Cross-check     position: A lane line on each side agrees with the car occupying an interior lane,
                        apparently lane 2 of 3; the outer approach limits are less clear. | roles: Both solid
                        white boundaries fit same-direction, no-crossing approach lane lines. | markings: The
                        straight arrow agrees with a through guide lane bounded by solid white lines; the stop
                        line and crossing do not conflict with it. | unseen: No hidden additional arrow or
                        waiting area is assumed; vehicles obscure parts of the stop line, crossing and distant
                        pavement. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits crossing to the lane on the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing to the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits going straight and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when yielding or waiting to
                        proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the crosswalk, and it does not
                        determine any of the seven movement permissions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight guide arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only guide arrow excludes a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only guide arrow excludes a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only guide arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid boundary. Obey
                        the traffic signals, stop before the stop line when required, and keep the pedestrian
                        crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1297, 18.97 s

culane_test__d100_05251222_0385_05250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight alongside an elevated structure, with
                        vehicles ahead and no intersection visible. My car is in the leftmost of three lanes
                        in this direction. (lanes 3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a diagonally hatched paved strip
                        and a guardrail farther beyond; no curb directly bounds my lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge and the same-direction lane to the right agree with my car
                        occupying lane 1 of 3. | roles: The broken white right boundary fits a crossable lane
                        line. The left boundary is visibly white despite being at the left edge, unlike the
                        yellow left-edge colour specified by CN-5.4.3; its edge role follows the hatched strip
                        beyond it, not an assumed paint colour. | markings: No arrows, words, symbols or
                        transverse markings are discernible in my lane. The diagonal hatching is outside its
                        left boundary. | unseen: No movement restriction at a future intersection is inferred;
                        no intersection or lane-end markings are visible. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
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
Step 7  Reflect         Consistent: boundary decisions apply only to crossing their respective sides, and no
                        intersection movement permission is inferred from the absence of arrows.
Advice                  Stay to the right of the solid left boundary and out of the hatched strip. A rightward
                        lane change is permitted by the broken line when safe; this view does not establish
                        the lanes to use for turns at a future intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 984, 16.53 s

culane_test__d100_05251309_0397_03150 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction; my car is in the rightmost
                        lane behind an SUV. The road continues ahead, but the next intersection and lane
                        endpoint are not clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from the adjacent
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs beside a raised curb and planted verge on the right, with
                        a separate paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is visible
                        ahead: its right-pointing head is clear, while the forward-pointing portion is partly
                        obscured by the SUV.
Step 4  Cross-check     position: Three same-direction lanes and an ego position of 3 agree with a lane
                        divider on the left and the roadway edge on the right. | roles: The broken white left
                        boundary fits a crossable same-direction lane divider; the solid white right boundary
                        beside the curb fits a roadway edge. | markings: The combined straight-and-right arrow
                        is compatible with the rightmost lane; no conflicting word, symbol or marked area is
                        visible. | unseen: The SUV obscures part of the arrow, and the distant lane endpoint
                        cannot be inspected fully; no stop line or waiting area is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing, and the raised
                        curb is a physical roadway edge rather than an available traffic lane. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The combined straight-and-right guide arrow permits straight or
                        rightward travel from this lane, not left turns or U-turns. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2,
                        subject to safety.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies alongside it.
Step 6  go_straight     allowed (correct): The identifiable straight-and-right arrow permits straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-and-right arrow does not include a left turn under
                        CN-5.13.1.
Step 6  turn_right      allowed (correct): The clearly visible right arrowhead permits a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-and-right arrow does not include a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, confirming the partly obscured
                        arrow as it becomes visible. For a left turn or U-turn, move safely into an
                        appropriately marked lane where permitted; do not cross the right edge or curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1142, 18.39 s

culane_test__d100_05251309_0397_03390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A wide urban road approaches a signal-controlled intersection. My car is in a through
                        lane, with two same-direction lanes to the left and a right-turn lane to the right.
                        (lanes 4, mine 3, full)
Step 2  Left            A single solid white line separates my lane from the lane containing the white van on
                        the left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the lane on the right; the roadside
                        island lies beyond that adjacent lane, not at my boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower part of the arrow is hidden by the hood.; arrow:straight
                        (full): A smaller white straight-ahead arrow is visible farther along my lane near the
                        intersection.; line:stop_line (partial): A transverse white stop line is visible at
                        the intersection approach, although distance limits its detail.
Step 4  Cross-check     position: Lane 3 of 4 has a same-direction lane on each side, consistent with both
                        boundaries being lane lines. | roles: Both boundaries are white solid lines,
                        consistent with no-crossing lane boundaries on an intersection approach. | markings:
                        The visible straight arrows agree with each other and with a through guide lane
                        bounded by solid white lines. | unseen: The hood hides the nearest arrow's lower
                        portion, and the distant stop line has limited detail; neither is treated as
                        completely visible. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight arrow indicates straight-ahead travel rather than a turn.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            arrow:straight: The farther straight arrow confirms that this lane permits only
                        straight-ahead movement at the intersection. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when yielding or waiting to
                        proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The clearly visible farther straight arrow permits straight-ahead
                        travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signals, and stop before
                        the stop line when required. Do not cross either solid boundary to reach a turning
                        lane here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1443, 21.62 s

culane_test__d100_05251327_0403_00180 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road continues straight ahead, with vehicles ahead and an overpass
                        in the distance. My car is in the leftmost of three visible lanes travelling in this
                        direction; no intersection stop line is visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane beside a raised curb, with a paved
                        verge and trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another same-direction lane on the right; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible
                        immediately ahead of the hood; the hood hides its lower shaft and any possible lower
                        branches.
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        leftmost of three same-direction lanes. | roles: The broken white right boundary fits
                        a same-direction lane divider. The left line is visibly white despite its position at
                        the left roadway edge; its role follows the adjacent curb, not an assumed yellow
                        colour. | markings: The visible forward arrowhead agrees with the continuing lane, but
                        its hidden lower portion prevents confirmation that it is a straight-only rather than
                        a combined arrow. | unseen: No hidden arrow branches, distant stop line, or waiting
                        area have been assumed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also makes this a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the
                        obscured lower portion prevents determining whether another movement is also
                        indicated. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hood obscures the part of the arrow
                        where a combined left branch could appear.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hood obscures the part of the arrow
                        where a combined right branch could appear.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete arrow cannot be read because
                        its lower portion is hidden.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight travel and rightward crossing follow visible markings, leftward
                        crossing is prohibited, and movements requiring the obscured arrow detail remain
                        undecided.
Advice                  Continue straight in this lane; do not cross the solid left edge or mount the curb. A
                        rightward lane change is permitted by the broken divider if safe, but confirm the
                        complete lane arrows before selecting a turning movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1168, 19.69 s

culane_test__d100_05251327_0403_00630 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A barrier-lined elevated roadway continues ahead without a visible intersection or
                        lane ending. My car is in the left of two same-direction lanes. (lanes 2, mine 1,
                        full)
Step 2  Left            A continuous pale-yellow solid line runs beside a concrete barrier on the left; no
                        traffic lane lies between the line and barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and position 1 agree with a left roadway edge and a same-direction
                        lane to the right. | roles: The yellow solid left edge and white broken right lane
                        divider fit their assigned roles. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No markings or
                        intersection features beyond the visible road have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the concrete barrier also physically closes that side. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue following the roadway and do not cross the solid left edge toward the
                        barrier. You may change into the right lane across the broken white divider after
                        checking traffic; no intersection movement guidance or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 830, 12.13 s

culane_test__d100_05251327_0403_00930 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three visible lanes in this direction continues toward a
                        distant intersection. My car is in the leftmost lane beside the raised median. (lanes
                        3, mine 1, full)
Step 2  Left            A continuous white solid line borders the lane on the left, with a narrow paved strip
                        and raised landscaped median beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with a visible long dash and gap, separates my lane from another
                        lane travelling in the same direction; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead.
Step 4  Cross-check     position: The left median edge and the lane line on the right agree with my position
                        as lane 1 of three. | roles: The broken white right boundary fits a same-direction
                        lane line. The left boundary is visibly white despite being a left roadway edge, which
                        differs from the yellow left-edge colour specified in CN-5.4.3; its physical edge role
                        remains clear. | markings: The straight arrow is compatible with the lane boundaries;
                        no conflicting marking is visible in my lane. | unseen: No distant stop line or
                        additional marking hidden by vehicles has been inferred; the far approach is not fully
                        readable. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        with only the stated safe emergency exception. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight; do not cross the solid line beside the median.
                        If another movement is needed, change right only when safe and select a lane whose
                        markings permit it; the distant stopping position is not readable here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1018, 14.39 s

culane_test__d100_05251327_0403_01200 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road runs straight ahead between concrete barriers, with no
                        intersection or lane ending visible. My car is in the middle of three lanes travelling
                        in this direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the right; the concrete roadside barrier lies beyond
                        that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White Chinese pavement text is visible ahead in my lane,
                        including a character resembling 环; the complete message is not legible at this
                        distance and is partly obscured by traffic.
Step 4  Cross-check     position: Three lanes with my lane second from the left agrees with a same-direction
                        lane line on each side. | roles: Both boundaries are broken white lines, consistent
                        with crossable same-direction lane separators. | markings: The visible pavement text
                        does not conflict with either boundary; no directional arrow or marked waiting area is
                        identifiable in my lane. | unseen: The full pavement message and distant roadway
                        details are not inferred. The transverse dark strip is a pavement joint, not an
                        identified painted stop line. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            text:other: This is pavement text, but its incomplete reading supplies no identifiable
                        restriction on the seven assessed actions. [CN-5.14.1] "Pavement text markings are
                        generally white. They are arranged vertically and read from near to far along the
                        direction of travel ... or horizontally from left t"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
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
Step 7  Reflect         consistent; the crossable boundaries govern only lane changes, and the absence of
                        movement markings does not establish permission to turn.
Advice                  Continue following the roadway; either adjacent lane may be entered across the broken
                        white line after checking traffic and clearance. No intersection, turn assignment or
                        stopping line is visible, so do not infer turning permission from this image.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8875, out 1010, 13.09 s

culane_test__d100_05251327_0403_02340 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road curves gently left, with a fenced divider on the left and a sidewalk on
                        the right. My car is in the left lane of two visible same-direction lanes; no
                        intersection or lane ending is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A continuous white solid line follows the left side of my lane beside a raised curb
                        and fenced divider, with another carriageway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from another paved travel lane on the
                        right; there is no curb at this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 1 agree with a left roadway edge
                        and a lane divider on the right. | roles: The solid white right boundary fits a no-
                        crossing lane line. The left boundary is visibly white despite its left-edge position;
                        this differs from the prescribed yellow left-edge color, so its observed color is
                        retained. | markings: No arrows, words, symbols, transverse lines or marked waiting
                        areas are visible in my lane. | unseen: No unseen intersection layout or downstream
                        guidance has been inferred; the distant roadway is partly obscured by vehicles. |
                        result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left; the raised curb also forms a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane divider prohibits crossing into the adjacent
                        right lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid left edge line normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies beside it.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
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
Step 7  Reflect         consistent: both boundary-crossing actions follow the solid-line rules, and no
                        intersection movement permission is inferred from absent guidance.
Advice                  Stay between the solid boundaries and follow the leftward curve; do not change lanes
                        across either boundary. The visible roadside speed-limit sign shows 30 km/h; choose
                        any later turning lane only when downstream guidance becomes visible and a permitted
                        lane-change section is available.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 926, 14.15 s

culane_test__d100_05251327_0403_03870 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A narrow urban road runs alongside an elevated structure, with two apparent lanes in
                        the direction of travel. My car is in the left lane behind a sedan; the road continues
                        ahead, but the next junction and lane end are not visible. (lanes 2, mine 1, full)
Step 2  Left            A single solid white line follows a raised curb on the left, with a narrow paved strip
                        and wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white longitudinal line separates my lane from the lane to the right; only a short
                        continuous portion is visible between the sedan and the hood, so its overall solid or
                        broken pattern cannot be established.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left road edge and the adjacent lane on the right agree with my lane
                        being lane 1 of 2. | roles: The white left line visibly follows the curb; the white
                        right line separates same-direction lanes, but its pattern is unresolved. | markings:
                        No guidance markings or transverse lines are readable in the exposed part of my lane.
                        | unseen: The sedan and hood obscure much of the lane surface, and the next
                        intersection is not visible; no arrow, waiting area, or right-boundary dash pattern
                        has been inferred. | result: consistent
Step 5  Rule            left_boundary: Crossing the visible solid white boundary is normally prohibited; the
                        raised curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken line permits crossing and a solid line normally prohibits it,
                        but the visible portion does not establish which pattern applies. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies alongside it.
Step 6  change_right    not_determined (WRONG, label prohibited): The right lane-line pattern is partly
                        hidden, so crossing permission cannot be established.
Step 6  go_straight     not_determined: The lane end and any movement arrows governing it are not visible.
Step 6  turn_left       not_determined: The lane end and any movement arrows governing it are not visible.
Step 6  turn_right      not_determined: The lane end and any movement arrows governing it are not visible.
Step 6  u_turn          not_determined: The lane end and any movement or prohibition markings governing it are
                        not visible.
Step 6  enter_waiting_areanot_determined: No waiting area is visible, but the sedan and distant road geometry
                          obscure the area ahead where one could be marked.
Step 7  Reflect         consistent
Advice                  Remain within the lane and keep a safe following distance behind the braking sedan; do
                        not cross the left solid line or curb. Confirm the right boundary pattern and any
                        junction arrows before changing lanes or selecting a turning movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 998, 17.78 s

culane_test__d100_05251327_0403_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated structure and curves ahead. My car is in the
                        left of two same-direction lanes, following a sedan; the next intersection and the
                        lane's endpoint are not visible. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs along the left side of my lane beside a raised curb and narrow
                        paved walkway, with the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the paved traffic lane on the right; its
                        farther portion is hidden by the sedan ahead.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being the leftmost of two same-direction lanes. | roles: The right solid white line
                        fits a same-direction lane divider. The left edge paint appears white, although the
                        supplied standard specifies yellow for a left edge; its visible color is retained
                        rather than inferred from its position. | markings: No arrows, words, symbols,
                        transverse lines or waiting areas are visible in the exposed part of my lane. |
                        unseen: The sedan hides part of the lane surface and the farther right boundary; the
                        next intersection and any associated movement markings cannot be assessed. | result:
                        Consistent spatial interpretation; the observed left-edge color differs from the
                        supplied standard.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white same-direction lane divider prohibits crossing
                        into the lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb lies beside it.
Step 6  change_right    prohibited (correct): The visible solid white lane divider prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The lane endpoint and any movement arrows there are outside the
                        visible area or obscured.
Step 6  turn_left       not_determined: The lane endpoint and any movement arrows there are outside the
                        visible area or obscured.
Step 6  turn_right      not_determined: The lane endpoint and any movement arrows there are outside the
                        visible area or obscured.
Step 6  u_turn          not_determined: The lane endpoint and any movement restrictions there are outside the
                        visible area or obscured.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: visible solid boundaries prohibit lateral crossing, hidden endpoint
                        markings leave intersection movements undecided, and no visible waiting area governs
                        entry.
Advice                  Stay within the current lane without crossing either solid boundary, and maintain a
                        safe gap behind the sedan. Check the markings farther ahead before choosing an
                        intersection movement; no stop line is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 997, 17.19 s

culane_test__d100_05251627_0452_02850 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches a signal-controlled junction beneath an overpass. My
                        car is in the leftmost lane beside a median fence; traffic and the hood obscure parts
                        of the road ahead and to the right. (lanes None, mine 1, partial)
Step 2  Left            A solid yellow line runs beside a raised median base and metal fence, with opposing
                        traffic beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A worn white line appears continuous along the visible stretch separating my lane from
                        the same-direction lane occupied by the taxi; vehicles obscure its continuation ahead.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes lane position 1, and the lane line
                        on the right confirms another same-direction lane; the total lane count cannot be
                        established confidently. | roles: The yellow median-side edge and white same-direction
                        lane separator fit their assigned roles. | markings: No guidance marking is readable
                        in the exposed part of my lane; markings nearer the junction could be hidden by
                        traffic. | unseen: No arrows, stop line, or waiting area have been inferred from the
                        junction or nearby lanes. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid yellow boundary is normally prohibited, and the
                        median fence also physically prevents moving left. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white lane line prohibits crossing into the lane on
                        the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid yellow boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Traffic hides the approach markings that would establish permitted
                        movements.
Step 6  turn_left       not_determined: Traffic hides the approach markings that would establish permitted
                        movements.
Step 6  turn_right      not_determined: Traffic hides the approach markings that would establish permitted
                        movements.
Step 6  u_turn          not_determined: Traffic hides any lane-use arrow or prohibited-movement marking ahead.
Step 6  enter_waiting_areanot_determined: The junction area ahead is obscured, so the presence of a marked
                          left-turn waiting area cannot be established.
Step 7  Reflect         consistent
Advice                  Remain between the median and the solid white lane line; do not change lanes across
                        either visible boundary. Slow for the queue and signals, and confirm the lane arrows
                        and stopping position as they become visible before choosing a junction movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 890, 14.42 s

culane_test__d100_05251718_0469_00390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in a middle approach lane, with other traffic lanes on both sides;
                        the far-left lane layout is difficult to separate reliably in this view. (lanes None,
                        mine None, insufficient)
Step 2  Left            A continuous white line runs along my lane's left side toward the intersection, with
                        another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along my lane's right side toward the intersection, with
                        another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible directly ahead
                        of the hood; the lower shaft is obscured by the hood.; line:stop_line (full): A solid
                        white transverse stop line crosses my lane immediately before the pedestrian
                        crossing.; line:crosswalk (full): White zebra-crossing stripes cross the road
                        immediately beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate same-direction traffic, so my lane is neither the
                        leftmost nor the rightmost; an exact total and index are not assigned because the far-
                        left layout is unclear. | roles: The white solid lines fit no-crossing lane boundaries
                        on an intersection approach. | markings: The visible straight arrowhead agrees with a
                        through approach lane between solid white boundaries; the stop line precedes the
                        crosswalk. | unseen: The hood hides the lower part of the arrow, so a concealed
                        additional arrow branch cannot be excluded; no waiting area is visibly identified. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the
                        obscured lower portion prevents confidently excluding additional indicated movements.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the crosswalk, and it does not
                        determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hood obscures the lower arrow, where an
                        additional directional branch could be hidden.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hood obscures the lower arrow, where an
                        additional directional branch could be hidden.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete arrow cannot be inspected
                        because its lower portion is hidden.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: neither solid boundary may be crossed, the visible arrow permits straight
                        travel, and movements requiring inspection of the hidden arrow portion remain
                        undetermined.
Advice                  Remain between the solid white lines and use this lane for the visibly indicated
                        straight movement; do not assume a turn is permitted from the obscured arrow. Follow
                        the applicable traffic signal, keep the crosswalk clear, and stop before the stop line
                        when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1372, 23.22 s

culane_test__d100_05251718_0469_01320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road passes beneath a pedestrian footbridge and continues ahead, with no
                        intersection or lane ending visible. My car is in the left lane of two lanes
                        travelling in this direction. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb on the left, with a paved pedestrian area
                        and bridge supports beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a foreground dash and a gap before the next visible section,
                        separates my lane from another same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        leftmost of two same-direction lanes. | roles: The broken white right boundary fits a
                        same-direction lane divider. The left line visibly appears white despite its left-edge
                        position; its edge role is established by the adjacent curb, not inferred from colour.
                        | markings: No guidance arrows, text, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: The vehicle ahead obscures some pavement, and the next
                        intersection is not visible; no markings have been inferred beneath it or beyond the
                        visible road. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing the
                        left boundary, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies beside it.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
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
Step 7  Reflect         Consistent: boundary permissions govern only crossing their respective sides, and no
                        intersection movement permission is inferred from the absence of visible arrows.
Advice                  Stay clear of the left curb and solid edge line; a right lane change is permitted by
                        the dashed divider if the adjacent lane is clear. The next intersection and its
                        movement markings are not visible, so do not infer turn permissions from this image.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 913, 14.56 s

culane_test__d100_05251718_0469_02040 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes in this direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A raised concrete curb borders the planted median on the left; no painted boundary
                        line is clearly visible beside it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median curb on the left and a lane line on the right agree with being
                        lane 1 of two same-direction lanes. | roles: The physical median forms the left
                        roadway edge, and the broken white line separates same-direction lanes. | markings: No
                        guidance markings are visible within my lane, so there is no conflict with the
                        boundaries. | unseen: No distant intersection layout or markings hidden beneath
                        vehicles are inferred. | result: consistent
Step 5  Rule            left_boundary: A curb can provide the clear roadway outline without an edge line; the
                        raised median is a physical boundary, not a crossable route to the left. [CN-5.4.5]
                        "Where a non-motorized lane is needed and there is no separating facility between it
                        and the motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The raised median curb forms a physical edge that cannot be used
                        for a lane change.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the curb governs only crossing left, the broken lane line governs only
                        crossing right, and no intersection movement permission is inferred.
Advice                  Remain within the lane and do not cross the median curb. You may change into the right
                        lane across the broken white line after checking traffic; no visible markings
                        establish turn lanes or a stopping position ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 799, 11.59 s

culane_test__d100_05251718_0469_02250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with two lanes in this
                        direction. My car is in the leftmost lane beside the landscaped median; no
                        intersection or lane ending is clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb borders the lane on the left, with grass, hedges and trees
                        beyond it; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gap, separates my lane from the same-
                        direction lane occupied by the silver car; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb places my car in the leftmost lane, and the right lane line
                        separates the second same-direction lane, consistent with two lanes and ego lane index
                        1. | roles: The unpainted curb forms the left roadway edge, and the broken white line
                        fits a crossable same-direction lane separator. | markings: No guidance arrows, words,
                        symbols or transverse markings are visible in my lane. | unseen: No distant
                        intersection layout or hidden pavement markings have been inferred; traffic and
                        distance limit the view farther ahead. | result: consistent
Step 5  Rule            left_boundary: This passage explains why a clear curb edge may lack a painted edge
                        line; the physical curb itself is not a traversable lane boundary. [CN-5.4.5] "Where a
                        non-motorized lane is needed and there is no separating facility between it and the
                        motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The raised median curb is a physical roadway edge, not a
                        traversable lane boundary.
Step 6  change_right    allowed (correct): The broken white lane separator permits crossing under CN-5.2.1-2.
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
Step 7  Reflect         Consistent: the curb prevents leaving to the left, the broken white line permits
                        crossing to the right, and no unseen intersection movements have been inferred.
Advice                  Stay clear of the median curb. You may change right across the broken white line after
                        checking the silver car and other traffic; choose an intersection movement only after
                        its lane guidance becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 970, 13.91 s

culane_test__d100_05251718_0469_05070 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues toward traffic ahead. My car is in the
                        leftmost of two visible same-direction lanes; the distant intersection approach is
                        partly obscured by vehicles. (lanes 2, mine 1, full)
Step 2  Left            A raised curb borders the lane on the left, with planting beyond it; no distinct
                        painted longitudinal line can be confidently identified beside the curb.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and the lane line on the right agree with my lane being the
                        leftmost of two visible same-direction lanes. | roles: The white broken right boundary
                        fits a crossable same-direction lane line; the left curb forms a physical roadway
                        edge. | markings: No guidance markings are readable in the visible portion of my lane,
                        so there is no marking conflict. | unseen: No arrows or stop lines have been inferred
                        from the overhead sign; paint beside the left curb and markings farther ahead are not
                        resolved. | result: consistent
Step 5  Rule            left_boundary: A curb can define the roadway edge without a painted edge line; as a
                        raised physical boundary it is not an available lane-change route. [CN-5.4.5] "Where a
                        non-motorized lane is needed and there is no separating facility between it and the
                        motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The raised curb is a physical roadway boundary, not a
                        traversable lane-change opening.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     not_determined: The distant lane-end markings are obscured or too far away to
                        establish permitted movements.
Step 6  turn_left       not_determined: The distant lane-end markings are obscured or too far away to
                        establish permitted movements.
Step 6  turn_right      not_determined: The distant lane-end markings are obscured or too far away to
                        establish permitted movements.
Step 6  u_turn          not_determined: The distant lane-end markings are obscured or too far away to
                        establish permitted movements.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent; crossing the right boundary is permitted, the left curb is not a lane-
                        change route, and unresolved lane-end movements remain undetermined.
Advice                  Stay clear of the left curb; a rightward lane change is permitted across the broken
                        white line after checking traffic. Confirm the overhead lane-direction sign and
                        pavement arrows nearer the intersection before selecting a lane for your intended
                        movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1051, 18.61 s

culane_test__d100_05251718_0469_05190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road has three lanes in this direction, with traffic continuing
                        ahead and no clearly visible intersection or lane ending. My car is in the middle
                        lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; the roadside curb is beyond that lane, not at my
                        lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both boundaries are broken white lines, consistent with separation of same-direction
                        lanes. | markings: No visible arrows, words, symbols, transverse lines or marked
                        waiting areas conflict with the boundaries. | unseen: No markings are inferred beneath
                        vehicles or beyond the readable stretch; the next intersection and the lane's eventual
                        end are not visible. | result: consistent
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
Step 7  Reflect         Consistent: both lane changes are permitted by the visible broken boundaries, while no
                        visible marking determines intersection movements or waiting-area entry.
Advice                  You may remain in this lane or cross either broken white boundary after checking
                        traffic and blind spots. No visible marking assigns a turning movement or stopping
                        point; check guidance farther ahead before selecting a lane for a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 863, 12.33 s

culane_test__d100_05251947_0499_00840 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided roadway continues ahead beside an elevated road, with no intersection
                        or lane ending visible. My car is in the leftmost lane; three same-direction lanes
                        appear visible, although the far-right portion is dark. (lanes 3, mine 1, partial)
Step 2  Left            A continuous white solid line runs beside a raised concrete median barrier, with
                        opposing traffic beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and adjoining gaps, separates my lane from
                        another same-direction lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with my lane being leftmost; the total lane count is less certain because the far-
                        right roadway is dark. | roles: The broken white right boundary fits a crossable lane
                        line. The left boundary functions as a roadway edge beside the median, although its
                        visibly white paint differs from the yellow left-edge colour specified by CN-5.4.3. |
                        markings: No arrows, words, symbols, transverse lines or marked waiting areas are
                        discernible in my lane. | unseen: No intersection layout or distant lane-use marking
                        is inferred; the far-right lane count remains less certain. | result: Consistent apart
                        from the observed left-edge colour differing from the specified standard; the observed
                        white colour is retained.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the concrete barrier also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a concrete median lies beyond it.
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
Step 7  Reflect         Consistent: boundary decisions apply only to crossing their respective sides, and
                        absent movement markings do not establish permissions at an unseen intersection.
Advice                  Stay clear of the solid left edge and concrete median; a rightward lane change is
                        permitted by the broken line after checking traffic. Continue observing for downstream
                        direction markings, since no turn allocation or stopping point is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1004, 15.82 s

culane_test__d100_05251947_0499_04830 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad, divided urban road continues ahead at dusk; no intersection or lane ending is
                        clearly visible. My car is in the rightmost of three visible same-direction lanes.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A pale continuous line follows the raised curb beside the planted strip on the right,
                        although darkness makes the paint difficult to distinguish from the curb in places.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A small white marking farther ahead in my lane appears to be
                        a forward-pointing arrow, but its head and possible branches cannot be read reliably
                        at this distance.
Step 4  Cross-check     position: Three lanes with my lane third from the left agree with a same-direction
                        lane line on the left and a roadside curb on the right. | roles: The broken white left
                        boundary fits a crossable lane line; the pale right boundary and raised curb fit the
                        roadway edge. | markings: The apparent arrow does not conflict with the boundaries,
                        but its complete set of directions is not readable. | unseen: The apparent arrow is
                        provisional, not a confirmed straight-only instruction; the right-edge paint is also
                        partly obscured by darkness. The distant lane end is not readable. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The raised curb identifies a physical roadway edge rather than a
                        traversable lane boundary, so moving across it is prohibited under the physical-edge
                        definition. [CN-5.4.5] "Where a non-motorized lane is needed and there is no
                        separating facility between it and the motor vehicle lanes, a motor/non-motor
                        separation line shall be prov"
Step 5  Rule            arrow:straight: A guide arrow specifies the permitted directions, but this apparent
                        arrow is too indistinct to establish the complete movement permissions. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The raised roadside curb forms a physical edge, not a lane-
                        change route.
Step 6  go_straight     not_determined (WRONG, label prohibited): The apparent guide arrow and distant lane
                        end are insufficiently readable to confirm the governing direction.
Step 6  turn_left       not_determined (WRONG, label prohibited): The apparent arrow's heads cannot be read
                        reliably enough to determine whether left turns are included.
Step 6  turn_right      not_determined (WRONG, label allowed): The apparent arrow's heads cannot be read
                        reliably enough to determine whether right turns are included.
Step 6  u_turn          not_determined (WRONG, label prohibited): The distant guidance marking cannot be read
                        reliably enough to determine U-turn permission.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: lane-change decisions follow the visible boundaries, while movement
                        permissions remain undecided because the distant guidance marking is not reliably
                        readable.
Advice                  Keep clear of the right curb; a left lane change is permitted across the broken line
                        only when safe. Read the lane arrows and any intersection controls more closely before
                        choosing a turning lane; no stopping position is identifiable here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1160, 20.61 s

culane_test__d100_05252026_0512_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, divided urban road at night, with two visible lanes in this direction and
                        traffic ahead. My car is in the right-hand lane; the distant junction area is not
                        clear enough to read its pavement markings. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible dash and gaps, separates my lane from the same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane, with a narrow paved
                        strip and a raised roadside edge beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and position 2 agree with a lane line on the left and a roadway
                        edge line on the right. | roles: The broken white divider fits a same-direction lane
                        line, and the solid white right boundary fits an edge line. | markings: No readable
                        guidance marking is visible within my lane, so none contradicts the boundaries. |
                        unseen: No distant arrows, stop line, or waiting area has been inferred; darkness,
                        distance and traffic limit inspection of the lane ahead. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing to change
                        lanes when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant lane-end pavement is not readable, so any movement arrow
                        governing straight travel cannot be determined.
Step 6  turn_left       not_determined: The distant lane-end pavement is not readable, so any movement arrow
                        governing left turns cannot be determined.
Step 6  turn_right      not_determined: The distant lane-end pavement is not readable, so any movement arrow
                        governing right turns cannot be determined.
Step 6  u_turn          not_determined: The distant lane-end pavement is not readable, so any arrow or
                        prohibition governing U-turns cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked waiting area is visible ahead or directly left of my lane;
                          no visible marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted by the broken divider
                        only when safe. Read the junction arrows and applicable signs and signals as they
                        become clear before choosing a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 834, 11.16 s

culane_test__d100_05252026_0512_01020 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road at night, with opposing traffic to the left and same-direction
                        traffic ahead. My car is between two white lane dividers; darkness and glare obscure
                        the far-right roadway and the distant approach. (lanes None, mine 2, partial)
Step 2  Left            A white broken divider is visible to the left, with another same-direction lane beyond
                        it; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 2  Right           White separated dash segments form the right divider, with another same-direction lane
                        beyond; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane lies on either side, consistent with my lane being
                        second from the left; the total lane count is uncertain because the rightmost extent
                        is dark. | roles: The white broken boundaries fit same-direction lane dividers. |
                        markings: No readable arrow, word, symbol, marked area or transverse line is visible
                        in my lane. | unseen: The distant lane end and any markings there cannot be resolved;
                        no intersection layout or distant guidance is inferred. | result: consistent
Step 5  Rule            left_boundary: The visible broken white lane divider permits crossing into the
                        adjacent same-direction lane. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): The visible broken white lane divider is crossable under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane divider is crossable under CN-5.2.1-2.
Step 6  go_straight     not_determined: The distant lane end is obscured by darkness and glare, so any
                        governing directional marking cannot be established.
Step 6  turn_left       not_determined: The distant lane end and its directional markings are not readable.
Step 6  turn_right      not_determined: The distant lane end and its directional markings are not readable.
Step 6  u_turn          not_determined: The distant lane end and any governing directional or prohibition
                        marking are not readable.
Step 6  enter_waiting_areanot_applicable: No marking governs this action: no waiting area or adjacent two-way
                          left-turn lane is visible.
Step 7  Reflect         Consistent: lane changes are permitted by the visible broken dividers, while movements
                        at the obscured lane end remain undecided.
Advice                  Either visible broken divider may be crossed after checking adjacent traffic and blind
                        spots. Do not select a turning movement from this image alone; read the approach
                        arrows, signs and signals as they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 973, 15.71 s

culane_test__d100_05252026_0512_01350 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road at night, with vehicles ahead and opposing traffic beyond the
                        median on the left. Three same-direction lanes are discernible; my car is in the
                        rightmost lane, and no intersection or lane ending is clearly visible. (lanes 3, mine
                        3, full)
Step 2  Left            A broken white line with visible long segments and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane, with a paved strip and a
                        raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The rightmost position agrees with a lane line on the left and a roadway
                        edge line on the right. | roles: The broken white separator fits a same-direction lane
                        line; the solid white right-hand line fits a carriageway edge line. | markings: No
                        guidance arrows, words, symbols, transverse lines or marked waiting areas are
                        discernible in my lane. | unseen: No marking is inferred from the vehicles ahead;
                        darkness, windshield glare and distance limit observation farther along the road. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing, with an
                        exception for an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
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
Step 7  Reflect         Consistent: boundary decisions apply only to crossing their respective sides, and no
                        intersection movement permission is inferred from the absence of visible arrows.
Advice                  Remain inside the solid right edge line; a left lane change is permitted across the
                        broken line only after checking traffic. No visible marking establishes turn-lane
                        assignments or a stopping point ahead, so reassess as they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 973, 16.42 s

culane_test__d193_06042058_0527_02610 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, two-lane carriageway continues straight through a dark, enclosed road section,
                        with a concrete divider on the left. My car is in the right lane; no intersection,
                        ramp or lane ending is visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, tinted by the yellow lighting, has visible dashes and gaps and
                        separates my lane from another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, tinted by the lighting, borders my lane on the right, with a
                        narrow paved margin and dark roadside beyond; no raised curb is apparent at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego position 2 agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white lane divider and
                        solid white right edge line fit their observed roles. | markings: No arrows, words,
                        symbols, marked areas or transverse lines are visible in my lane. | unseen: No lane-
                        end layout or intersection movement marking is inferred from the distant roadway. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible movement marking governs this action.
Step 6  turn_left       not_applicable: No visible movement marking governs this action.
Step 6  turn_right      not_applicable: No visible movement marking governs this action.
Step 6  u_turn          not_applicable: No visible movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary decisions concern only crossing their respective sides, and no
                        intersection permissions are inferred from the absence of visible movement markings.
Advice                  Continue within the right lane; a left lane change is permitted by the dashed divider
                        only when safe. Do not cross the solid right edge line in normal driving; no visible
                        markings establish turning permissions or a stopping location ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 872, 13.28 s

culane_test__d193_06042058_0527_03240 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit road at night continues straight ahead, with no intersection or lane ending
                        visible. My car is in the right lane of two visible lanes travelling in this
                        direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from the
                        lane occupied by the white SUV; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip and
                        reflective posts beyond it; no raised curb is visible along the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my lane being the
                        second and rightmost of two same-direction lanes. | roles: The broken white separator
                        fits a same-direction lane line, and the solid white outer line fits a right edge
                        line. | markings: No guidance arrows, text, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No unseen intersection layout or distant lane-use
                        markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
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
Advice                  Stay within the right lane and do not cross the solid right edge line during normal
                        driving. A left lane change is permitted by the markings, but wait until the white SUV
                        has cleared and the adjacent lane is safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 785, 9.54 s

culane_test__d193_06051114_0632_02790 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection. My car is behind the
                        red car, with another same-direction lane to the left; worn markings and the broad
                        roadway make the total lane count uncertain. (lanes None, mine 2, partial)
Step 2  Left            A very faded white longitudinal line separates my lane from the lane beside the
                        median; its visible stretch is too worn to distinguish a continuous line from broken
                        segments confidently, and there is no curb at this boundary.
                        white none, curb no, lane_line, evidence partial
Step 2  Right           A faded white longitudinal line runs diagonally toward the red car's right side, with
                        more same-direction roadway beyond; wear makes its solid or broken pattern uncertain,
                        and there is no curb at this boundary.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (partial): A faded white forward-pointing arrow is visible in my lane
                        behind the red car; its straight shaft and forward head are discernible, though the
                        paint is worn.
Step 4  Cross-check     position: The lane lines on both sides indicate adjacent same-direction lanes; the
                        lane beside the median is to my left, placing my lane second from the left, but the
                        total count remains uncertain. | roles: The white paint fits same-direction lane
                        separators; neither boundary's crossing pattern can be read reliably. | markings: The
                        visible straight arrow agrees with a through lane between same-direction lanes; no
                        conflicting marking is discernible. | unseen: No stop line or waiting area is
                        identifiable. Boundary patterns remain unresolved rather than inferred from the
                        intersection approach. | result: consistent
Step 5  Rule            left_boundary: A broken line permits crossing and a solid line normally prohibits it,
                        so the unreadable pattern leaves crossing this boundary undecided. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: Crossing permission depends on whether this worn line is broken or
                        solid, which cannot be established confidently. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight guide arrow directs my car straight ahead rather than
                        left, right or into a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 6  change_left     not_determined (WRONG, label prohibited): The left lane-line pattern is too worn to
                        determine crossing permission under CN-4.2.2-a.
Step 6  change_right    not_determined (WRONG, label prohibited): The right lane-line pattern is too worn to
                        determine crossing permission under CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The discernible straight arrow allows straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn from this
                        lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn from this
                        lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No identifiable waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         Consistent: the readable arrow governs intersection movements, while uncertain
                        boundary patterns leave both crossing actions undecided.
Advice                  Remain in this lane for straight travel and obey the traffic signals. Do not turn from
                        this lane or assume either faded boundary permits a lane change; identify the
                        appropriate turn lane and its crossing markings before moving over.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1268, 22.61 s

culane_test__d193_06051114_0632_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road with two lanes in this direction continues ahead; no
                        intersection or lane ending is visible. My car is in the left lane beside the central
                        separator fence. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line runs beside the raised central separator and metal fence, with
                        opposing traffic beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Worn white broken line segments separate my lane from the lane occupied by the black
                        sedan; the sedan obscures part of the farther line.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood, but the hood hides the lower shaft and any possible branches.
Step 4  Cross-check     position: The separator on the left and an adjacent same-direction lane on the right
                        agree with my car being lane 1 of 2. | roles: The broken white right boundary fits a
                        same-direction lane line. The left line visibly appears white despite lying at the
                        central separator; its edge role follows the physical separator, not an assumed yellow
                        colour. | markings: The visible forward arrowhead agrees with the lane continuing
                        ahead, but its hidden lower portion prevents excluding additional directional
                        branches. | unseen: No hidden arrow branches or distant intersection markings are
                        asserted. The right boundary is partly obscured. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing left, and the
                        raised separator also physically blocks that movement. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible broken white lane line permits crossing into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the
                        obscured remainder prevents determining whether the arrow permits any additional
                        movement. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a physical separator lies beyond.
Step 6  change_right    allowed (correct): The identifiable broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed: The visible forward arrowhead permits straight travel under CN-5.13.1.
Step 6  turn_left       not_determined: The hood hides the part of the arrow where a left branch could occur.
Step 6  turn_right      not_determined: The hood hides the part of the arrow where a right branch could occur.
Step 6  u_turn          not_determined: The incomplete arrow prevents establishing whether an additional
                        U-turn indication exists.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: straight travel and crossing the broken right boundary are supported,
                        crossing left is prohibited, and movements dependent on hidden arrow branches remain
                        undecided.
Advice                  You may continue straight; do not cross the left separator. A right lane change is
                        permitted by the visible broken line, but check the black sedan and surrounding
                        traffic first; confirm the complete lane arrows before planning a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1044, 16.78 s

culane_test__d193_06051123_0635_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road approaches a broad intersection with a pedestrian crossing. My
                        car is in the leftmost of two visible same-direction motor-vehicle lanes. (lanes 2,
                        mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane to the stop line, with
                        opposing-direction roadway beyond and no physical divider.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs from beside the hood to the stop line, separating my
                        lane from another same-direction lane; there is no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white transverse stop line spans my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): Broad white zebra-crossing
                        stripes cross the roadway immediately beyond the stop line.
Step 4  Cross-check     position: The yellow center line on my left places my lane leftmost, and the white
                        lane line on my right separates the second same-direction lane. | roles: The solid
                        yellow center line and solid white lane separator agree with their assigned roles. |
                        markings: The stop line and crossing agree with an intersection approach; no lane-use
                        arrow or marked waiting area is visible. | unseen: The hood hides the closest
                        pavement; no arrow or other marking has been inferred beneath it, and distant
                        intersection details are not treated as lane guidance. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits crossing the left
                        boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when yielding or waiting to
                        proceed, without specifying a permitted movement. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers zebra crossings; this marking
                        identifies the pedestrian crossing and does not determine any of the seven movement
                        actions.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane separator prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid boundaries; do not change lanes on this approach. No visible
                        arrow establishes which intersection movements this lane serves, so check applicable
                        signs and signals, keep the pedestrian crossing clear, and stop before the stop line
                        when required.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1074, 14.74 s

culane_test__d193_06051123_0635_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road continues ahead on a gentle bend; no intersection or lane ending
                        is clearly visible. My car is in the single visible motor-vehicle lane of its
                        direction, with a narrower roadside strip to the right. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line runs along the left of my lane, with opposing-
                        direction roadway beyond it.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs along the right of my lane, separating it from a
                        narrow paved roadside strip; a raised sidewalk curb lies beyond that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and white roadway edge line on the right
                        agree with one motor-vehicle lane in my direction and ego lane index 1. | roles: The
                        solid yellow center line separates opposing directions, while the solid white edge
                        line separates my lane from the roadside strip. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No hidden
                        lane-end markings or distant intersection movements have been inferred; the roadside
                        strip's precise use is not established. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing to
                        the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white longitudinal edge line normally prohibits crossing to
                        the right, with an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The single solid yellow center line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action;
                        the center line governs crossing the boundary, not a movement at a future
                        intersection.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the yellow center line and white right edge line; do not cross either
                        during ordinary driving. No visible lane-use marking establishes turning permissions
                        at a future intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 856, 11.49 s

culane_test__d193_06051123_0635_00990 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road continues ahead, with no clearly visible intersection or lane
                        ending. My car is in the leftmost of two apparent lanes in its direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A single broken yellow line, with visible long segments and gaps, separates my lane
                        from opposing traffic; there is no curb along this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A single broken white line, with visible segments and gaps, separates my lane from a
                        paved lane to the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line places my lane leftmost, and the white lane line
                        indicates another lane on the right, consistent with two lanes and index 1. | roles:
                        The broken yellow centre line and broken white same-direction lane line fit their
                        assigned roles. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are discernible in my lane. | unseen: No unseen intersection movement
                        restrictions or special designation for the lane to the right have been assumed. |
                        result: consistent
Step 5  Rule            left_boundary: The broken yellow centre line permits crossing to overtake, turn or
                        make a U-turn when this does not affect safety. [CN-5.1.1] "The crossable centre line
                        separates traffic flows in opposite directions. It means vehicles may cross the line
                        to overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): CN-5.1.1 permits crossing the broken yellow centre line when safe,
                        although opposing traffic lies beyond it.
Step 6  change_right    allowed (correct): CN-5.2.1-2 permits crossing the broken white lane line.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action
                        at the next intersection; the centre line governs only crossing the left boundary
                        here.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in your lane unless a safe lane change is needed; crossing left would enter
                        opposing traffic space. No visible arrows determine intersection movements, and no
                        stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 887, 11.84 s

culane_test__d193_06051123_0635_01980 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches an intersection ahead. My car is in the middle of three
                        lanes travelling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Three same-direction lanes and position 2 agree with lane lines on both
                        sides. | roles: Both white solid boundaries fit same-direction no-crossing lane lines
                        on an intersection approach. | markings: The straight-only arrow agrees with the solid
                        approach boundaries; arrows in adjacent lanes do not govern my lane. | unseen: No
                        distant stop line or additional marking is identifiable with confidence; none is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing the left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing the right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow allows straight travel and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane line prohibits crossing
                        under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane line prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight, obeying the intersection signals. For a
                        turn, select an appropriately marked lane before the solid-line approach; do not cross
                        either visible solid boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 883, 10.73 s

culane_test__d193_06051123_0635_02160 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a broad signalized intersection. My car is in the
                        rightmost approach lane, beside a striped island on the right; the full lane count to
                        the left is uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A continuous solid white line separates my lane from the adjacent same-direction lane
                        on the left, with no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white outline curves along the right side of my lane, with white diagonal
                        channelizing stripes beyond it and a raised roadside island farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow has a single head pointing right, with no straight-
                        ahead or left branch.; line:stop_line (full): A transverse solid white stop line
                        crosses the lane just before the pedestrian crossing.; line:crosswalk (full): White
                        zebra-crossing bars extend across the lane ahead of the stop line.
Step 4  Cross-check     position: The left lane line confirms an adjacent same-direction lane, and the right
                        edge confirms the rightmost position; the total number of approach lanes cannot be
                        counted confidently. | roles: The solid white left boundary fits an intersection
                        approach lane line, and the solid white right outline fits the roadway edge beside
                        channelization. | markings: The right-only arrow agrees with the rightmost approach
                        lane and its curved right edge; the stop line precedes the crosswalk. | unseen: No
                        exact lane count or numerical lane index is asserted; the diagonal striped area is
                        outside my lane and is not listed as an in-lane marking. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing it, apart from a
                        safe emergency exception. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-only guide arrow permits a right turn and excludes straight,
                        left-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when yielding or waiting to
                        proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers a crosswalk; it identifies the
                        pedestrian crossing and does not determine any of the seven movement permissions.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing left under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  go_straight     prohibited (correct): The right-only arrow excludes going straight under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes turning left under CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-only arrow permits turning right under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn only; do not cross either solid boundary or drive into
                        the striped island. Obey the applicable signal, stop before the stop line when
                        required, and watch for pedestrians and crossing traffic.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1320, 20.33 s

culane_test__d193_06051123_0635_03690 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the straight-ahead lane, with a left-turn lane to its left and
                        two lanes to its right. (lanes 4, mine 2, full)
Step 2  Left            Closely spaced solid white strokes form the left boundary, with a left-turn lane
                        beyond and no curb.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line extends along the right side of my lane toward the intersection,
                        with another traffic lane beyond and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.; line:stop_line (full): A transverse solid white stop line crosses my lane
                        immediately before the pedestrian crossing.; line:crosswalk (full): White pedestrian-
                        crossing stripes extend across my lane beyond the stop line.
Step 4  Cross-check     position: Lane 2 of 4 agrees with having same-direction lanes on both sides. | roles:
                        The white longitudinal boundaries separate same-direction traffic; their solid strokes
                        indicate a no-crossing approach section. | markings: The straight-only arrow agrees
                        with the solid approach boundaries; the left-turn arrow lies in the adjacent lane, not
                        mine. | unseen: No unseen arrows, waiting areas or distant markings have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal strokes prohibit ordinary crossing of the left
                        boundary; the supplied lane-line passage does not specifically describe this paired-
                        white form. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The single straight arrow permits straight travel from this lane and
                        excludes left turns, right turns and U-turns. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car should stop when required to
                        yield or wait. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: The stripes identify a pedestrian crossing; no supplied passage
                        specifically governs crosswalks, and this marking does not determine the seven
                        movement actions.
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid boundary to
                        reach a turn lane. Obey the traffic signal, stop before the stop line when required,
                        and watch for pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1328, 19.78 s

culane_test__d193_06051411_0691_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road curves gently left, with a physical median fence on the left and shops
                        and parked vehicles on the right. My car is beside the median; faint pavement traces
                        do not establish the number of same-direction lanes, and no intersection or lane
                        ending is visible. (lanes None, mine 1, partial)
Step 2  Left            A continuous pale white line runs beside the raised base of a metal median fence, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Faint light-colored pavement traces appear to the right of my path, with more paved
                        space and parked vehicles beyond, but they are too worn to establish a continuous
                        boundary or a dash-and-gap pattern.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        none
Step 4  Cross-check     position: The median edge establishes that my lane is leftmost, but the unclear right
                        boundary prevents a reliable lane count. | roles: The solid line follows the physical
                        median edge; its apparent white color does not match the prescribed yellow for a left
                        edge line, so its color has not been inferred from its position. | markings: No
                        readable arrows, words, symbols, transverse lines or marked waiting areas are visible
                        in my lane. | unseen: No right-boundary pattern, additional travel lane or distant
                        intersection marking has been assumed. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing, and
                        the physical median also prevents an ordinary leftward departure. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The right boundary cannot be identified reliably, so no marking-
                        specific crossing permission or prohibition can be established.
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a median fence lies immediately beyond it.
Step 6  change_right    not_determined (WRONG, label allowed): The right boundary is too indistinct to
                        determine whether crossing it is permitted.
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
Advice                  Follow the road beside the median without crossing the solid left boundary. Before
                        moving right, establish the usable lane boundary and check for parked vehicles,
                        pedestrians and traffic; no visible markings establish turn-lane choices or a stopping
                        point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1033, 19.32 s

culane_test__d193_06051603_0727_01080 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           My car is on a single-lane elevated branch separated from the parallel roadway on the
                        left by a painted taper leading to a physical divider. The branch continues ahead; no
                        intersection or lane end is visible. (lanes 1, mine 1, full)
Step 2  Left            A worn solid white line borders a diagonally hatched separation area on the left,
                        which narrows toward a physical divider ahead; another roadway lies beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous raised concrete barrier forms the right edge; no separate painted
                        boundary line is clearly visible beside it.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges, consistent with my lane being the only
                        lane on this separated branch. | roles: The left white line outlines the branch beside
                        the separation area, rather than dividing adjacent ordinary lanes; the right boundary
                        is a physical barrier. | markings: No arrows, words, symbols or transverse lines are
                        visible in my lane. The diagonal hatching is outside its left boundary. | unseen: No
                        hidden arrows or distant intersection markings have been inferred; no painted line is
                        asserted along the right barrier. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, and the separation
                        area and divider are not an adjacent travel lane. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        as a physical roadway edge it does not permit a rightward lane departure.
Step 6  change_left     prohibited (correct): The solid white left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The concrete barrier physically closes the right side of the
                        lane.
Step 6  go_straight     not_applicable: No marking governs this action; the visible road continues without a
                        marked intersection movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain on this separated branch without crossing the left solid line or hatched
                        separation area, and keep clear of the right barrier. No turn-selection arrow or
                        stopping line is visible; follow the road and check the signs ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 844, 13.67 s

culane_test__d193_06051603_0727_01620 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane elevated ramp curving left, with concrete barriers on both
                        sides. No intersection or lane ending is visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A pale yellow continuous solid line follows the foot of a raised concrete barrier on
                        the left; no adjacent traffic lane lies between the line and barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A pale white continuous solid edge line follows the concrete barrier on the right,
                        with a narrow paved margin between the travel surface and barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Road edges on both sides agree with a single lane, which is both the
                        leftmost and rightmost lane of this direction. | roles: The yellow left edge and white
                        right edge fit their roadway-edge roles; neither is a divider between adjacent traffic
                        lanes. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in the lane. | unseen: No markings or lane configuration beyond the
                        visible bend are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing; the concrete
                        barrier also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing; the concrete
                        barrier also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): Crossing the solid left boundary is normally prohibited by
                        CN-4.2.2-a, and a concrete barrier lies beyond it.
Step 6  change_right    prohibited (correct): Crossing the solid right boundary is normally prohibited by
                        CN-4.2.2-a, and a concrete barrier lies beyond it.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs the
                        movement at a subsequent intersection.
Step 6  turn_left       not_applicable: No marking governs this action; the ramp's leftward curvature is not a
                        left-turn arrow.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the single ramp lane and follow its leftward curve; do not cross either
                        solid edge line. The visible chevron signs reinforce the bend, and no stop line is
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8875, out 843, 12.45 s

culane_test__d193_06051734_0757_00000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, three-lane expressway continues straight ahead, with no intersection, ramp
                        or lane ending visible. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from the same-
                        direction lane occupied by the white car on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane line on each
                        side. | roles: Both boundaries are broken white lines, consistent with crossable same-
                        direction lane dividers. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane. | unseen: No distant lane endpoint or
                        hidden pavement marking has been inferred. | result: consistent
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
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent: both lane changes follow the crossable boundaries, while no visible
                        movement or waiting-area marking governs the other actions.
Advice                  Continue in the middle lane; either broken white boundary may be crossed after
                        checking for a safe gap, particularly around the white car ahead on the right. No
                        intersection, turn guidance or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8875, out 764, 9.63 s

culane_test__d193_06051734_0757_02430 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight, with guardrails and shoulders on both sides
                        and no visible intersection or ramp. My car is in the middle of three lanes travelling
                        in this direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another
                        traffic lane on the right; its nearest portion is obscured by the hood, and no curb
                        forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane line on each
                        side. | roles: Both white broken boundaries fit crossable same-direction lane lines. |
                        markings: No visible arrows, words, symbols, or marked areas conflict with the
                        boundaries; the transverse pavement seam is not a painted stop line. | unseen: No
                        hidden markings or intersection movements have been inferred; visible stretches
                        establish both boundary patterns. | result: consistent
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
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent; permission to cross the lane boundaries does not establish permission for
                        turns or a U-turn.
Advice                  Continue along the expressway in your lane; either broken white boundary permits a
                        lane change when traffic conditions make it safe. No intersection, turn lane, waiting
                        area, or stopping line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 859, 11.5 s

culane_test__d193_06051734_0757_04050 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A single-lane ramp curves right toward an overpass, with guardrails on both sides. My
                        car is in the only visible travel lane; no intersection or lane ending is visible.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line borders the lane on the left, with a narrow paved margin
                        and a raised guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line curves right along the lane boundary, with a paved
                        shoulder and a guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Edge lines on both sides agree with one visible travel lane and an ego lane
                        index of 1; the pavement beyond the right line is a shoulder rather than another
                        marked travel lane. | roles: Both lines mark roadway edges and are visibly solid
                        white. The left line's white colour differs from the yellow left-edge colour specified
                        by CN-5.4.3, but its observed colour is not changed to fit that rule. | markings: No
                        arrows, text, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No markings or lane configuration beyond the visible curve are
                        inferred. | result: The geometry is consistent; the observed left-edge colour differs
                        from the supplied colour convention.
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing, with an exception
                        for a safe emergency crossing; the guardrail also physically bounds the road.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, with an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a.
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
Step 7  Reflect         Consistent: the solid boundaries prohibit ordinary crossing, while the absence of
                        movement markings does not establish permission for any intersection movement.
Advice                  Stay between the solid white lines and follow the ramp's right-hand curve, reinforced
                        by the roadside chevron signs. Do not use the shoulder as another lane; no stop line
                        or intersection movement guidance is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 931, 13.08 s

culane_test__d193_06060642_0768_00360 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, tree-lined urban road with opposing traffic to the left and a landscaped
                        curb to the right. My car is in the rightmost of two lanes in its direction; no
                        intersection or lane ending is clearly visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line runs beside the right road edge, with visible painted segments and
                        gaps; a raised curb and landscaped strip lie immediately beyond it.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 2 agree with a lane line on the
                        left and a roadway edge on the right. | roles: The broken white left line fits a
                        crossable same-direction divider; the white right line fits a right-hand edge line. |
                        markings: No arrows, words, symbols, transverse lines or marked waiting areas are
                        visible in my lane. | unseen: No markings beyond the clearly visible road stretch or
                        at an unseen intersection have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white edge marking permits crossing the painted line, but
                        this permission does not make the raised curb beyond it a drivable route. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white edge line permits crossing the
                        paint under CN-4.2.2-a; the curb beyond remains a physical obstacle.
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
Step 7  Reflect         Consistent: crossing permissions concern the painted boundaries only, and no
                        intersection movement has been inferred from the absence of arrows.
Advice                  Remain in your lane unless a safe left lane change is needed; the broken left divider
                        permits it. Although the right edge paint is crossable, there is no usable lane beyond
                        it and the raised curb must be avoided; no visible marking establishes turn
                        permissions or a stopping point ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        ['change_right allowed across a curb']
Tokens                  in 8875, out 1074, 18.17 s

culane_test__d193_06060642_0768_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently right, with no intersection or lane ending clearly
                        visible ahead. My car is in the rightmost of two lanes travelling in this direction.
                        (lanes 2, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb lies along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane beside a raised curb, with planted
                        vegetation and a separate roadside paved area beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 2 agree with a lane line on the
                        left and a road edge on the right. | roles: The broken white line fits a crossable
                        same-direction lane divider; the solid white line beside the curb fits the right
                        roadway edge. | markings: No guidance arrows, words, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: No markings or lane-end features have
                        been inferred beyond the visible road stretch. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent left lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white edge line normally prohibits crossing to the right,
                        with only a safe emergency exception; the adjacent curb is also a physical road edge.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
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
Advice                  Follow the rightward curve within your lane; a left lane change is permitted by the
                        broken divider if traffic conditions are safe. Do not cross the solid right edge
                        toward the curb; no visible markings establish turn permissions or a stopping point
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 846, 10.93 s

culane_test__d193_06060642_0768_03060 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs beside an elevated roadway, with a junction approach visible
                        in the distance. My car is in the rightmost of three visible motor-vehicle lanes; a
                        paved roadside strip lies beyond the solid line on the right. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from the lane
                        occupied by the green bus; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved roadside strip, with a raised
                        sidewalk curb farther beyond the strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white directional arrow is visible far ahead in my
                        lane; a rightward head appears visible, but its full shape and any additional head
                        cannot be resolved confidently at this distance.
Step 4  Cross-check     position: Three motor-vehicle lanes and my position as lane 3 agree with a same-
                        direction lane line on the left and a roadway edge line on the right. | roles: The
                        broken white left boundary fits a crossable lane divider; the solid white right
                        boundary fits a carriageway edge. | markings: The distant arrow does not visibly
                        contradict the boundaries, but its complete movement indication cannot be checked. |
                        unseen: The roadside strip's precise use is not established, and no additional arrow
                        head, stop line, crosswalk or waiting area is inferred from the distant junction. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid longitudinal edge line is normally prohibited, with
                        an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The apparent rightward arrow head indicates a right turn, but the
                        unresolved remainder prevents determining the complete set of permitted movements.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2,
                        subject to a safe gap.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant arrow is only partially readable, so a straight-ahead head
                        cannot be confirmed or excluded.
Step 6  turn_left       not_determined: The full distant arrow cannot be resolved sufficiently to establish
                        its complete directional restriction.
Step 6  turn_right      allowed: The visible rightward arrow head indicates this movement under CN-5.13.1.
Step 6  u_turn          not_determined: The full distant arrow cannot be resolved sufficiently to establish
                        its complete directional restriction.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking governs this action.
Step 7  Reflect         consistent; unresolved arrow details leave the other end-of-lane movements
                        undetermined rather than prohibited.
Advice                  Remain inside the solid right edge line; a left lane change is possible only with a
                        safe gap, especially beside the bus. Confirm the complete arrow and junction signs as
                        you approach before choosing your movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1278, 24.25 s

culane_test__d193_06060748_0790_02970 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A wide divided multilane road with heavy traffic continuing ahead; no intersection or
                        lane ending is visible. My car is in the middle of five lanes travelling in this
                        direction. (lanes 5, mine 3, full)
Step 2  Left            A broken white line separates my lane from another same-direction lane on the left; a
                        long dash and the gap ahead are visible, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from another same-direction lane on the right; a
                        dash and gap are visible, although traffic obscures the more distant continuation, and
                        there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes lie on each side, consistent with lane 3 of 5 and
                        lane-line boundaries on both sides. | roles: Both boundaries are broken white lines,
                        consistent with crossable separators between same-direction lanes. | markings: No
                        readable guidance markings are visible within my lane, so there is no conflict with
                        the boundaries. | unseen: No distant lane-end markings are inferred; vehicles obscure
                        parts of the road ahead. | result: consistent
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
Step 6  go_straight     not_applicable: No visible marking governs this movement.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Neither broken boundary prohibits a lane change, but change lanes only with a safe gap
                        in this dense traffic. No visible lane-use arrow or stop line establishes an upcoming
                        turn assignment or stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 913, 13.95 s

culane_test__d193_06060919_0820_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with vehicles parked along the right-hand
                        curb; no intersection or lane ending is clearly visible. My car is in the single
                        discernible moving lane in this direction. (lanes 1, mine 1, full)
Step 2  Left            A worn yellow longitudinal marking lies to the left, with opposing traffic beyond it;
                        its visible stretches are too faint and interrupted to establish a reliable solid or
                        broken pattern.
                        yellow none, curb no, center_line, evidence partial
Step 2  Right           No painted boundary is discernible on the right; a raised roadside curb is visible in
                        places, with parked vehicles obscuring much of the road edge ahead.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One moving lane in this direction agrees with a center line on the left and
                        the roadside edge on the right; the parked vehicles do not establish another moving
                        lane. | roles: The yellow paint fits an opposing-traffic separator, but its crossing
                        pattern is unresolved; the curb identifies the right road edge. | markings: No
                        readable arrows, words, symbols, transverse lines or waiting areas are visible in my
                        lane. | unseen: The center-line pattern and the obscured portions of the right edge
                        cannot be established; no intersection markings are inferred beyond the visible road.
                        | result: consistent
Step 5  Rule            left_boundary: Crossing permission depends on whether the yellow boundary is solid or
                        broken, which cannot be reliably established here. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: No supplied passage expressly regulates crossing a raised curb; as a
                        physical road edge, it is not a traversable lane-change boundary.
Step 6  change_left     not_determined (WRONG, label allowed): The center-line pattern is unclear, so the
                        crossing permission under CN-4.2.2-a remains undetermined.
Step 6  change_right    prohibited (correct): The raised curb forms a physical road edge, not a lane available
                        for crossing.
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
Advice                  Keep within the visible roadway and do not assume the worn yellow center marking
                        permits crossing. Proceed cautiously past parked vehicles and pedestrians; movement
                        permissions at the next intersection are not established by this view.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1051, 19.32 s

culane_test__d193_06060925_0822_01260 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs alongside an elevated structure, with no intersection or
                        lane ending visible ahead. My car is in the rightmost of three lanes travelling in
                        this direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with long painted segments and visible gaps separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right edge of my lane, with a narrow paved
                        margin and a raised curb supporting a metal fence beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my lane being lane 3 of
                        3. | roles: The broken white line separates same-direction lanes, and the solid white
                        line follows the right roadway edge. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No markings are
                        inferred beneath vehicles or beyond the visible road; the next intersection is not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted across the broken
                        white line after checking traffic. No visible markings establish turn permissions at
                        the next intersection, so check the guidance as it comes into view.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 862, 12.13 s

culane_test__d193_06060925_0822_02700 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad, divided urban road continues straight ahead, with no nearby intersection or
                        lane ending visible. My car is in the third of four same-direction lanes, counted from
                        the left. (lanes 4, mine 3, full)
Step 2  Left            A broken white line, with visible long painted segments and gaps, separates my lane
                        from another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from
                        another same-direction lane on the right; the roadside curb lies beyond that adjacent
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego lane index 3 agree with same-direction lane lines on both
                        sides: two lanes lie to the left and one to the right. | roles: Both boundaries are
                        broken white lines, consistent with crossable same-direction lane dividers. |
                        markings: No guidance arrows, words, symbols, transverse lines or marked waiting areas
                        are discernible in my lane. | unseen: No markings or intersection movements have been
                        inferred beyond the visible road stretch. | result: consistent
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
Step 7  Reflect         Consistent: both lane changes are permitted by the visible broken lane lines, while no
                        visible marking governs the intersection movements or entry to a waiting area.
Advice                  You can remain in this lane or cross either broken divider after checking adjacent
                        traffic and blind spots. No turn assignment or stopping point is visible; follow the
                        markings and signs that become visible farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 966, 13.99 s

culane_test__d193_06060925_0822_04140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward an overpass.
                        My car is in the rightmost lane; no intersection stop line is visible ahead. (lanes 3,
                        mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faint continuous white line follows the right roadside beside a raised curb and
                        barrier, with no additional motor-vehicle lane beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow immediately ahead of the hood has one head
                        pointing straight forward.
Step 4  Cross-check     position: The lane line on the left and roadside edge on the right agree with my lane
                        being the third and rightmost of three lanes. | roles: The broken white separator fits
                        a same-direction lane line, and the solid white roadside line fits a right edge line.
                        | markings: The straight arrow agrees with the continuing lane; no conflicting marking
                        or waiting area is visible. | unseen: No markings beyond the visible road stretch or
                        beneath vehicles are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight and does not
                        permit left, right or U-turn movements from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits a safe lane change under
                        CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right boundary normally prohibits crossing under
                        CN-4.2.2-a; a raised roadside edge also lies beyond it.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line when safe. Do
                        not cross the right roadside boundary; for any turn, find an appropriately marked lane
                        rather than turning from this straight-only lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1045, 16.5 s

culane_test__d193_06060925_0822_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight beneath a pedestrian footbridge, with a bus
                        stop along the right side. My car is in the middle of three visible same-direction
                        lanes; no intersection or lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another
                        traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken white line with visible dashes and gaps separates my lane from the lane
                        beside the bus stop; the roadside curb lies beyond that lane, not at my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 3. | roles:
                        Both white broken boundaries fit separation of same-direction lanes. No readable
                        pavement text establishes a special-lane restriction on the right. | markings: No
                        guidance marking is readable inside my lane; the visible arrow to the left belongs to
                        the adjacent lane. | unseen: The distant continuation and any markings at the next
                        intersection cannot be resolved; no directions have been inferred from them. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane line is crossable under
                        CN-5.2.1-2; no special-lane marking is established.
Step 6  go_straight     not_applicable: No visible marking in my lane governs this movement.
Step 6  turn_left       not_applicable: No visible marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No visible marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No visible marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Either visible broken boundary may be crossed when safe, but check for traffic and any
                        bus-lane signs before moving right near the bus stop. The next intersection's movement
                        restrictions and stopping position are not visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8875, out 924, 14.17 s

culane_test__d193_06060925_0822_04680 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight, with a side-road junction visible on the
                        right. My car is in the rightmost of three same-direction lanes. (lanes 3, mine 3,
                        full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right side of my lane, with a narrow paved strip and
                        a raised landscaped curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A worn but readable white arrow in my lane has one head
                        pointing straight ahead.
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 3 agree with a lane line on
                        the left and a roadway edge on the right. | roles: The broken white left boundary fits
                        a crossable same-direction lane line; the solid white right boundary fits the right
                        roadway edge. | markings: The straight-only arrow is consistent with the lane
                        continuing ahead; no conflicting word, arrow or waiting area is visible. | unseen: No
                        hidden markings are inferred; the distant roadway beyond the visible lane markings is
                        not used to infer additional instructions. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing to the right,
                        apart from a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white right boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed: The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not include a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not include a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not include a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane; a left lane change is permitted across the broken
                        line when safe, but do not cross the solid right edge. For another movement, select an
                        appropriately marked lane in advance and watch for traffic entering from the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8875, out 1206, 20.14 s

culane_test__d193_06060925_0822_05310 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with a planted median on the left and a raised
                        roadside strip separating the main carriageway from a parallel road on the right. My
                        car is in the rightmost of three visible same-direction lanes; no intersection or lane
                        ending is clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A faded broken white line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right of my lane, with a narrow paved margin and a
                        raised curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my car occupying lane 3
                        of 3. | roles: The broken white line separates same-direction lanes, and the solid
                        white line marks the right roadway edge. | markings: No guidance marking is readable
                        within my lane, so there is no conflicting lane-use instruction. | unseen: No arrow,
                        intersection stop line, or waiting area has been inferred from the distant roadway;
                        the curb lies beyond the painted right boundary rather than forming the lane boundary
                        itself. | result: consistent
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
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the solid right edge line; a left lane change is permitted by the broken
                        line when traffic conditions make it safe. No visible lane-use arrow or stop line
                        establishes turning permissions or a stopping position ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 853, 11.79 s

culane_test__d37_05181608_0235_03090 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection. My car follows a taxi in a
                        narrow right-side approach lane, with a painted separation area and traffic to the
                        left and a low metal barrier to the right; the total approach-lane count is unclear.
                        (lanes None, mine None, insufficient)
Step 2  Left            A solid white diagonal line borders my lane on the left, with white diagonal
                        separation markings and a large yellow traffic barrel beyond it; the barrel obscures
                        part of the nearer boundary.
                        white solid, curb no, other, evidence partial
Step 2  Right           A solid white line runs along the right side toward the intersection, beside a low
                        metal barrier separating this lane from the roadside space.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white line is visible ahead of the taxi,
                        although the taxi hides its central portion.; line:crosswalk (partial): Broad white
                        pedestrian-crossing stripes extend across the approach beyond the transverse line;
                        some stripes are obscured by the taxi and other road users.
Step 4  Cross-check     position: The right physical edge places this lane at the right side of the motor-
                        vehicle approach, but the painted separation area and foreground obstruction prevent a
                        reliable total lane count or index. | roles: The right white line fits a roadway edge;
                        the left white line borders a painted separation area rather than directly separating
                        opposing traffic. | markings: The stop line and crossing are compatible with an
                        intersection approach. No lane-use arrow can be read in the exposed portion of my
                        lane. | unseen: The taxi hides much of the lane pavement, including the area where a
                        direction arrow could be painted; no arrow or permitted direction is inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal boundary normally prohibits crossing to
                        the left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing, and the physical
                        barrier also prevents a normal departure to that side. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            line:stop_line: The stop line identifies where my car should stop when required to
                        yield or wait. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically governs crosswalks, and this marking
                        does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The visible solid white boundary normally prohibits crossing
                        under CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a, and a metal barrier occupies this side.
Step 6  go_straight     not_determined: The taxi obscures the pavement where a lane-use arrow could determine
                        this movement.
Step 6  turn_left       not_determined: The taxi obscures the pavement where a lane-use arrow could determine
                        this movement.
Step 6  turn_right      not_determined: The taxi obscures the pavement where a lane-use arrow could determine
                        this movement.
Step 6  u_turn          not_determined: The taxi obscures the pavement where a lane-use or prohibited-movement
                        marking could determine this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid boundaries and do not cross the painted separation area or the
                        right-side barrier. Confirm this lane's permitted direction when the taxi reveals the
                        pavement, obey the signals, and stop before the stop line when required while keeping
                        the crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8875, out 1249, 20.78 s

culane_test__d37_05181608_0235_03720 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with a fenced median on the left and buildings
                        along both sides. My car is in the leftmost lane; at least one same-direction lane
                        lies to the right, but the far-right lane arrangement is unclear. (lanes None, mine 1,
                        partial)
Step 2  Left            A solid white painted line follows the raised median edge on the left, with a metal
                        fence and opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments with intervening gaps separate my lane from the same-
                        direction lane on the right; vehicles obscure parts of the line farther ahead.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes my lane as leftmost, and the broken
                        lane line on the right establishes another same-direction lane; the total count
                        remains uncertain. | roles: The broken white right boundary fits a same-direction lane
                        line. The left boundary is visibly white despite occupying a position where the
                        supplied rules prescribe yellow; its physical median-edge role remains clear. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        the exposed portion of my lane. | unseen: No yellow colour has been inferred for the
                        left line. Vehicles and distance hide some pavement ahead, and no intersection-end
                        markings are claimed. | result: consistent
Step 5  Rule            left_boundary: The solid line normally prohibits crossing the left boundary, which is
                        also physically bounded by the raised median. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised median lies beyond.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary decisions concern crossing the visible lane edges only, and no
                        permission for an unseen intersection movement is inferred.
Advice                  Stay clear of the median; change right across the broken line only after checking the
                        nearby white hatchback and other traffic. No visible arrows establish turn
                        permissions, so reassess the markings and signs as the next intersection comes into
                        view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1123, 21.44 s

culane_test__d37_05181608_0235_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A congested multilane urban road approaches a signal-controlled intersection. My car
                        is behind a brown sedan, with same-direction traffic on both sides; vehicles obscure
                        the outer lanes and much of the intersection approach. (lanes None, mine None,
                        insufficient)
Step 2  Left            A continuous white line runs along the left of my lane, with another lane of queued
                        vehicles beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane toward the silver sedan, with
                        another lane of same-direction traffic beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines and same-direction vehicles on both sides establish that my lane
                        is an interior lane, but obscured outer boundaries prevent a reliable total lane count
                        or index. | roles: Both white solid boundaries fit no-crossing lines separating same-
                        direction lanes. | markings: No guidance marking can be read on the exposed pavement
                        in my lane; traffic hides the pavement farther ahead. | unseen: No arrows, stop line,
                        waiting area, or exact lane count have been inferred from the obscured approach. |
                        result: consistent
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
Step 6  go_straight     not_determined: Queued vehicles hide the approach pavement where a movement arrow
                        could determine this action.
Step 6  turn_left       not_determined: Queued vehicles hide the approach pavement where a movement arrow
                        could determine this action.
Step 6  turn_right      not_determined: Queued vehicles hide the approach pavement where a movement arrow
                        could determine this action.
Step 6  u_turn          not_determined: Queued vehicles hide the approach pavement where an arrow or
                        prohibited-movement marking could determine this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: both crossing prohibitions follow from visible solid lane lines,
                        intersection movements remain undecided because relevant pavement is obscured, and no
                        visible waiting area governs entry.
Advice                  Stay between the solid white lines and leave space behind the sedan. Confirm this
                        lane's arrows and the applicable signal as the queue advances; the image does not
                        establish an appropriate lane for any particular intersection movement or a stopping
                        position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 899, 13.32 s

culane_test__d37_05181608_0235_05340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A broad urban road with multiple same-direction lanes has dense queued traffic ahead.
                        My car is between two visible lane lines behind a dark sedan; traffic hides the lane
                        end and the outer limits of the carriageway. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line runs along my lane's left side, with another traffic lane beyond
                        it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along my lane's right side, with another traffic lane beyond
                        it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction traffic lies on both sides, so my lane is an interior lane;
                        the complete lane count and its numerical position cannot be established. | roles:
                        Both white solid boundaries fit no-crossing lines separating same-direction lanes. |
                        markings: No guidance marking is readable on the exposed pavement in my lane; vehicles
                        conceal the pavement farther ahead. | unseen: No arrows, stop line, waiting area, or
                        lane-end geometry have been inferred behind the traffic. | result: consistent
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
Step 6  go_straight     not_determined: Traffic conceals the lane-end pavement and any arrow that would govern
                        this movement.
Step 6  turn_left       not_determined: Traffic conceals the lane-end pavement and any arrow or prohibited-
                        turn marking.
Step 6  turn_right      not_determined: Traffic conceals the lane-end pavement and any arrow or prohibited-
                        turn marking.
Step 6  u_turn          not_determined: Traffic conceals the lane-end pavement and any arrow or prohibited-U-
                        turn marking.
Step 6  enter_waiting_areanot_determined: The area ahead and farther to the left is obscured, preventing
                          confirmation of any marked waiting area.
Step 7  Reflect         consistent
Advice                  Stay within the solid white boundaries and leave a safe gap behind the sedan. Confirm
                        lane arrows, signs, signals, and any stop line as traffic clears before choosing an
                        intersection movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 831, 12.49 s

culane_test__d37_05181919_0299_02970 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A divided urban road with three visible motor-vehicle lanes in this direction
                        continues toward a distant intersection. My car is in the rightmost motor-vehicle
                        lane, beside a roadside strip used by vehicles and two-wheelers. (lanes 3, mine 3,
                        full)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a paved roadside strip
                        and a black car beyond it; the sidewalk curb is farther right, not at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white forward-pointing arrow is painted directly ahead in my
                        lane; its head and stem are visible behind the car ahead.
Step 4  Cross-check     position: Three motor-vehicle lanes and position 3 agree with a same-direction lane
                        line on the left and a roadway edge line on the right. | roles: The broken white left
                        boundary fits a crossable lane line; the solid white right boundary fits a right-hand
                        carriageway edge line. | markings: The straight arrow agrees with the lane continuing
                        forward; no conflicting guidance marking is visible. | unseen: The car ahead obscures
                        some pavement, and distant intersection markings cannot be read; no stop line or
                        waiting area has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, except in a
                        safe emergency; no visible feature establishes a more specific exception. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow allows proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and watch for the black car entering from the roadside.
                        If another movement is needed, select an appropriately marked lane where crossing is
                        permitted; do not cross the solid right edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1115, 18.16 s

culane_test__d37_05181919_0299_03120 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in the
                        middle of three visible lanes travelling in this direction, with vehicles on both
                        sides and ahead. (lanes 3, mine 2, full)
Step 2  Left            A continuous solid white line separates my lane from the lane occupied by the taxi on
                        the left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from the traffic lane on the right;
                        there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrow is immediately ahead of the
                        hood; its forward-pointing head is clear, but the lower shaft is hidden by the hood.;
                        arrow:straight (partial): A smaller white straight-ahead arrow is visible farther
                        ahead in the same lane, just behind the queued vehicles.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being the middle lane of three
                        same-direction lanes. | roles: Both boundaries are solid white, consistent with no-
                        crossing lane lines on an intersection approach. | markings: The visible arrows both
                        point straight ahead and agree with each other and with the guide-lane boundaries. |
                        unseen: The hood hides the nearest arrow's lower shaft, and distant vehicles obscure
                        portions of the intersection approach; no unseen stop line or waiting area is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-ahead arrow designates straight travel rather than left
                        turns, right turns or U-turns. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The farther straight-ahead arrow repeats the lane's straight-only
                        direction. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The readable straight arrow heads designate straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows do not designate a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrows do not designate a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrows do not designate a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         Consistent: the arrows govern intersection movements, the solid boundaries govern lane
                        departures, and no hidden stop line or waiting area is assumed.
Advice                  Remain in this lane for straight travel and do not cross either solid boundary to
                        reach a turning lane. Obey the signals and queued traffic; the stop line is not
                        clearly visible, so approach cautiously and stop before it when required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1143, 15.96 s

culane_test__d37_05190927_0395_02340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an intersection, with a truck directly ahead and
                        other traffic to the right. My car is in the leftmost lane beside a planted median;
                        vehicles obscure the full width of the carriageway. (lanes None, mine 1, partial)
Step 2  Left            A solid white painted line runs beside a raised median curb, with planting and fencing
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from traffic travelling in the same direction on
                        the right; its farther portion is obscured by vehicles, and there is no curb along it.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left agrees with my lane being leftmost, and the
                        right lane line confirms another same-direction lane to the right; the total lane
                        count is obscured. | roles: The solid white right boundary fits a no-crossing lane
                        line. The left paint appears white despite its median-side position; its edge role
                        follows the visible curb rather than an assumed yellow colour. | markings: No guidance
                        markings can be read in the exposed portion of my lane; the truck hides the pavement
                        farther ahead. | unseen: No arrows, stop line, or total lane count have been inferred
                        from the surrounding traffic. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing left, and the
                        raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent same-
                        direction lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 6  change_left     prohibited (correct): The visible solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  turn_left       not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  turn_right      not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  u_turn          not_determined: The truck hides the approach pavement where a governing arrow or
                        prohibition could be marked.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid boundaries and maintain a safe gap behind the truck. Confirm
                        this lane's arrows and the intersection controls when they become visible before
                        choosing a movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 964, 15.03 s

culane_test__d37_05190927_0395_02430 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signalized intersection with a pedestrian
                        crossing. My car is in the leftmost approach lane, beside a raised traffic island;
                        vehicles obscure parts of the farther roadway. (lanes 3, mine 1, partial)
Step 2  Left            A raised traffic island with a pole borders the left side; a faint yellow-looking
                        continuous pavement line follows its edge, although glare and the pole obscure part of
                        it.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A solid white line runs toward the intersection on the right, separating my lane from
                        another same-direction lane, with no curb along it.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.; line:stop_line (full): A
                        transverse solid white line crosses my lane immediately before the pedestrian
                        crossing.; line:crosswalk (partial): Broad white pedestrian-crossing stripes extend
                        across my lane ahead, partly obscured by the truck.
Step 4  Cross-check     position: The island on the left and same-direction lane on the right support the
                        leftmost-lane position. Three approach lanes appear present, but the bus and
                        foreground cropping make the total less certain. | roles: The faint yellow line beside
                        the island fits a left roadway edge; the solid white line on the right fits an
                        intersection approach lane divider. | markings: The visible straight arrowhead agrees
                        with a straight-ahead guide lane bounded by a solid white approach line. No
                        conflicting word, arrowhead or waiting area is visible. | unseen: The arrow shaft,
                        portions of the island-edge paint and part of the pedestrian crossing are obscured;
                        their evidence levels are reduced. | result: consistent
Step 5  Rule            left_boundary: The visible solid edge marking normally prohibits crossing to the left,
                        where the raised island also forms a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane divider prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The forward-pointing guide arrow permits straight travel and restricts
                        this lane to that indicated movement. [CN-5.13.1] "Guide arrows indicate the direction
                        of travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The transverse white stop line identifies where to stop when yielding
                        or waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically governs pedestrian-crossing stripes;
                        they identify the pedestrian crossing and do not determine any of the seven movement
                        actions.
Step 6  change_left     prohibited (correct): The solid left-edge marking normally prohibits crossing under
                        CN-4.2.2-a, and a raised island lies beyond it.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The identifiable straight arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        permit a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        permit a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible arrowhead identifies the lane movement despite its hidden
                        shaft, and neither the stop line nor the crosswalk is used to decide turning or lane-
                        changing permissions.
Advice                  Continue straight from this lane when signals and crossing traffic permit; do not
                        cross either boundary here. If required to stop, stop before the transverse white line
                        and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 1424, 24.1 s

culane_test__d37_05190927_0395_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A narrow, tree-lined urban two-way street continues ahead, with parked vehicles along
                        the right and oncoming vehicles to the left. My car is in the single visible travel
                        lane of its direction; no intersection or lane ending is clearly visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A faint yellow line appears continuous along the left of my lane, partly obscured by
                        the cyclist and vehicles, with opposing traffic beyond and no curb at the line.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two closely spaced, continuous white lines run along the right of my lane, separating
                        it from parked vehicles; the vehicles obscure the roadside beyond.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One travel lane in my direction agrees with an opposing-traffic centre line
                        on the left and a parking-side roadway edge on the right. | roles: The visible yellow
                        centre line and white parking-side edge lines fit their respective roles. | markings:
                        No readable arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: The left line is faint and partly occluded, and parked vehicles
                        hide the roadside beyond the right boundary; no hidden curb or distant intersection
                        marking is inferred. | result: consistent
Step 5  Rule            left_boundary: The visible single solid yellow centre line prohibits crossing into the
                        opposing side. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The continuous white boundary normally prohibits crossing into the
                        parking-side space, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The visible solid yellow centre line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the centre line governs crossing the left boundary, not movement at an unseen
                        intersection.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary-crossing prohibitions are kept separate from intersection
                        movements, which have no visible governing markings.
Advice                  Remain between the visible boundaries and slow down for the cyclist immediately ahead-
                        left and the close vehicle on the right. No turn guidance or stopping line is visible;
                        do not infer permission for a turn at an intersection beyond view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8875, out 938, 14.2 s
```
