# Reasoning of lane run 20261116_132837_laneR_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight toward an overpass, with traffic ahead and
                        no visible intersection or lane ending. My car is in the rightmost of three same-
                        direction travel lanes, beside a paved roadside strip. (lanes 3, mine 3, full)
Step 2  Left            A single broken white line, with visible dashes and gaps, separates my lane from
                        another same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from a greenish paved roadside strip, with
                        a guardrail farther beyond rather than at the line itself.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on my left and roadway edge line on my right agree with my
                        position as lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white outer boundary fits a right edge line. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No marking is inferred beneath the vehicles ahead or beyond the visible road;
                        the distant lane end cannot be inspected. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits my car to cross into
                        the adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white edge line normally prohibits crossing onto the
                        roadside strip, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change one lane left across the broken white line
                        when safe; do not cross the solid right edge line in normal driving. No turn guidance
                        or stopping point is visible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9111, out 854, 14.0 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues downhill toward an underpass; no intersection or
                        lane ending is visible. My car is in the rightmost lane, but the vehicle on the left
                        obscures part of the carriageway, preventing a reliable total lane count. (lanes None,
                        mine None, insufficient)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a narrow paved
                        shoulder and then a guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line confirms another same-direction lane on the left, while
                        the right edge line confirms that my lane is rightmost; its numerical index remains
                        uncertain because the total lane count is obscured. | roles: The broken white
                        separator fits a same-direction lane line, and the solid white line beside the
                        shoulder fits a right roadway edge. | markings: No guidance arrows, words, symbols,
                        transverse lines, or waiting areas are visible in my lane. | unseen: No numerical lane
                        count or hidden guidance marking has been inferred; the distant roadway is partly
                        obscured by traffic. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid white boundary onto the shoulder is normally
                        prohibited, with an exception for a safe emergency crossing. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current lane toward the underpass, keeping clear of the shoulder
                        beyond the solid white edge line. A left lane change is permitted by the broken line,
                        but check the adjacent vehicles and blind spot before moving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9111, out 1147, 26.43 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided highway continues straight ahead, with two travel lanes and an emergency
                        stopping lane on the right. My car is in the right-hand travel lane; no intersection
                        or lane ending is visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, appearing yellowish under the image's colour cast, has visible
                        long dashes and gaps and separates my lane from another travel lane; no curb forms
                        this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, appearing yellowish under the image's colour cast, separates
                        my lane from a paved emergency shoulder; the guardrail is beyond the shoulder rather
                        than at this boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two travel lanes and ego position 2 agree with a lane divider on the left
                        and a roadway edge adjoining an emergency shoulder on the right. | roles: The broken
                        white lane divider and solid white emergency-shoulder edge fit their respective roles.
                        | markings: No arrows, words, symbols or transverse markings are visible in my lane. |
                        unseen: No intersection, lane-end markings or markings beyond the visible road have
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid emergency-stopping-lane edge is not for routine crossing;
                        the stated exception permits broken-down and rescue vehicles to cross when using that
                        lane. [CN-5.4.7] "The edge line at an emergency stopping lane shall be solid. Note:
                        broken-down and rescue vehicles may cross the solid line when using the emergency
                        stopping lan"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to a safe gap.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid emergency-shoulder edge does not
                        permit routine entry under CN-5.4.7.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane, or change left only after checking carefully for the truck and
                        other traffic. Keep out of the emergency shoulder during ordinary driving and observe
                        the overhead lane and speed signs.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 9111, out 827, 13.05 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban elevated roadway continues ahead, with no intersection or lane ending
                        visible. My car is in the rightmost of three apparent same-direction lanes; vehicles
                        partly obscure the far-left roadway. (lanes 3, mine 3, partial)
Step 2  Left            Orange broken paint, with several long segments and clear gaps, separates my lane from
                        the lane carrying the white sedan on the left; there is no curb here.
                        other dashed, curb no, lane_line, evidence full
Step 2  Right           Broken orange segments lie immediately inside a continuous white line along the right
                        edge; beyond the white line is a narrow paved strip and a raised bridge barrier.
                        other dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane lies to the left and the roadway edge lies to the
                        right, consistent with the rightmost lane; the total count is less certain because
                        vehicles obscure the far-left portion. | roles: The orange broken markings provide
                        temporary longitudinal guidance; the additional solid white line on the right marks
                        the paved roadway edge. | markings: No readable arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: No intersection movement
                        restrictions or hidden markings have been inferred; the orange and white lines on the
                        right are described separately rather than treated as a conventional same-colour
                        broken-solid pair. | result: consistent
Step 5  Rule            left_boundary: The broken orange boundary may be crossed when safe; its orange colour
                        denotes temporary work-zone guidance under CN-4.3.2-c. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken orange line itself is crossable, but moving out onto the
                        strip beyond also requires crossing the adjacent solid white edge line, which is
                        normally prohibited. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken orange lane boundary permits crossing under CN-4.2.2-a.
Step 6  change_right    prohibited (WRONG, label not_determined): Leaving the lane to the right would cross
                        the adjacent solid white edge line, normally prohibited by CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the right-side decision accounts for both visible lines, while the
                        longitudinal boundaries do not determine intersection turning movements.
Advice                  Continue in this lane, or change left across the broken orange line only after
                        checking traffic. Keep inside the solid white right edge; no intersection turn
                        guidance or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 9224, out 1157, 29.46 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with no intersection or lane ending clearly
                        visible. My car is in the rightmost of three same-direction lanes, marked for bus use.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken yellow line, with several visible dashes and gaps, separates my lane from
                        another same-direction traffic lane; there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with yellow rectangular dashes
                        immediately alongside it on my lane's side; a paved margin and a concrete barrier lie
                        beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (partial): White Chinese bus-reservation wording is painted longitudinally in
                        my lane; the visible characters read as part of 公交专用, with the nearest portion cut off
                        by the hood.
Step 4  Cross-check     position: Two traffic lanes lie to my left, and the roadway edge lies to my right,
                        consistent with lane 3 of 3. | roles: The yellow broken left boundary and bus wording
                        identify a reserved lane, although its yellow paint differs from the white bus-lane
                        line described in the supplied passage. The solid white right line fits a roadway
                        edge. | markings: The bus wording agrees with the reserved-lane boundary treatment; no
                        directional arrow or waiting area is visible. | unseen: The obscured part of the bus
                        wording, reservation times, and markings beyond the visible road stretch are not
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The visible broken boundary permits crossing out of my lane into the
                        adjacent ordinary lane. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 5  Rule            right_boundary: Crossing the solid white boundary onto the paved margin is normally
                        prohibited. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            text:bus: The bus-reservation wording identifies a lane that an ordinary car may not
                        use while reserved, but does not itself prohibit leaving it across a broken boundary.
                        [CN-6.9.1] "The bus lane line shows that vehicles other than buses shall not enter the
                        lane. It consists of a broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (contested, correct): The broken left boundary permits leaving the reserved
                        lane under CN-4.2.2-a.
Step 6  change_right    prohibited (contested, label allowed): The solid white right boundary normally
                        prohibits crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight; the bus wording does not govern this movement classification.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the straight-ahead classification does not authorize ordinary-car use of
                        the reserved lane, and the boundary decisions apply only to leaving the lane.
Advice                  As an ordinary car, leave the bus-reserved lane to the left across the broken boundary
                        when safe. Do not cross the solid white edge line onto the paved margin; no stop
                        position is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 9278, out 1128, 26.02 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a single motor-vehicle lane on a physically separated urban roadway
                        approaching an underpass. A narrow strip used by scooters runs along the right; no
                        intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line runs beside a raised concrete barrier on the left, with a
                        separate carriageway beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates the lane from a narrow paved strip occupied by
                        scooters, with a raised roadside curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The two edge boundaries enclose one motor-vehicle lane, consistent with lane
                        count 1 and ego position 1; the roadway beyond the left barrier is separate. | roles:
                        The right solid white line fits a motor/non-motor separation edge. The left paint
                        appears white despite the supplied standard specifying yellow for a left carriageway
                        edge; its physical position beside the barrier establishes its edge role. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in the lane.
                        | unseen: No markings inside the dark underpass or beyond the visible stretch are
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing, and the
                        concrete barrier also physically prevents leaving the lane to the left. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing into the
                        roadside strip; the supplied edge-line passages provide no crossing exception for
                        ordinary driving here. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a concrete barrier lies beside it.
Step 6  change_right    prohibited (correct): The solid white right boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue within the solid boundaries toward the underpass; do not move into the
                        scooter strip or toward the left barrier. Watch for scooters and follow the overhead
                        signs and signals as they become readable.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8305, out 908, 19.81 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow urban road continues straight past roadside shelters and bicycle parking,
                        with a pedestrian crossing ahead. My car is in the right-hand of two apparent same-
                        direction lanes; no intersection or lane ending is clearly visible. (lanes 2, mine 2,
                        full)
Step 2  Left            A single solid white line separates my lane from the paved lane on the left, with no
                        curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A raised curb with a yellow-painted face borders my lane on the right, with parked
                        bicycles and scooters beyond it; no separate longitudinal pavement line is visible.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A thin transverse white line crosses my lane immediately before
                        the pedestrian crossing.; line:crosswalk (full): White pedestrian-crossing stripes
                        extend across my lane ahead.
Step 4  Cross-check     position: The white lane divider on my left and curb on my right agree with my
                        position in the rightmost of two same-direction lanes. | roles: The solid white
                        divider fits a no-crossing lane line. The yellow paint is on the roadside curb, not an
                        opposing-traffic centre line. | markings: The transverse line and pedestrian crossing
                        agree with each other. No directional arrow, word, or waiting area is visible in my
                        lane; the partial arrow at the lower left is outside it. | unseen: No direction has
                        been inferred from the adjacent lane's partially visible arrow, and no intersection
                        geometry beyond the visible road has been assumed. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The yellow-painted curb prohibits roadside parking; crossing to the
                        right is also precluded by the physical curb rather than by this parking rule.
                        [CN-6.3.1] "The no-parking line shows that roadside parking is prohibited. It is a
                        solid yellow line painted on the face and top of the curb and shows the extent where
                        park"
Step 5  Rule            line:stop_line: The white stop line identifies where to stop when yielding or waiting,
                        but does not itself require an unconditional stop. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        under the supplied action definitions it does not determine any of the seven
                        movements.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The raised curb forms a physical boundary that cannot be used
                        for a lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the
                        transverse stop line does not independently require a full stop.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane without crossing the solid white divider or mounting the
                        curb. Approach the pedestrian crossing cautiously, yield as necessary, and stop before
                        the transverse line if required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 8691, out 1128, 22.3 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A busy urban road carries several lanes of traffic in the same direction, with a
                        painted channelizing separation developing on the left of my lane. My car is behind
                        the white sedan; traffic obscures the road farther ahead, and the total lane count
                        across the separated roadway is uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line runs along the left of my lane, with white diagonal hatching
                        farther ahead beyond it and other same-direction traffic to the left; there is no curb
                        on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with a long dash and intervening gap visible, separates my lane
                        from another traffic lane on the right; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction traffic lies beyond both boundaries; the channelized
                        separation and traffic prevent a reliable total lane count and numerical lane
                        position. | roles: The white solid left boundary and white broken right boundary are
                        consistent with separation of same-direction traffic. | markings: No guidance marking
                        is readable inside my lane; the diagonal hatching is outside its left boundary. |
                        unseen: No arrow or transverse marking is inferred beneath the vehicles ahead, and the
                        lane's eventual end is not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white same-direction boundary prohibits my car from crossing
                        to the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent lane
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left boundary prohibits crossing
                        under CN-6.2.1.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane without crossing the solid white boundary or the hatched
                        separation on the left; a rightward lane change is permitted by the broken line if
                        safe. Keep a safe following distance and reassess turn guidance when the pavement
                        ahead becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 9111, out 1027, 21.67 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road continues straight ahead, with two motor-vehicle
                        lanes in this direction and a roadside non-motorized strip on the right. My car is in
                        the leftmost motor-vehicle lane; no intersection or lane ending is visible. (lanes 2,
                        mine 1, full)
Step 2  Left            A continuous white painted line runs beside a raised curb and planted median on the
                        left; traffic on the other carriageway is beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another motor-vehicle lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge on the left and a same-direction lane on the right
                        agree with my lane being lane 1 of 2. | roles: The broken white right boundary fits a
                        crossable lane line. The left boundary visibly has white paint beside a median curb,
                        although the supplied standard specifies yellow for a left edge line; its observed
                        color is retained. | markings: No arrows, words, symbols, transverse lines, or waiting
                        areas are visible in my lane. | unseen: No markings are inferred beneath vehicles or
                        beyond the visible road; the next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        where a raised median curb also forms a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median curb lies beside it.
Step 6  change_right    allowed (correct): The broken white lane line permits a right lane change under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line after checking
                        for traffic. Do not cross the left solid line or median curb; choose lanes for any
                        later turn when its guidance becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9224, out 912, 16.49 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is within a broad signal-controlled urban intersection, following the silver
                        car toward the far-side crosswalk. No lane boundaries delimit the immediate
                        intersection pavement, so the number of lanes and the car's lane index cannot be
                        counted near the bottom of the image. (lanes None, mine None, insufficient)
Step 2  Left            No painted longitudinal boundary or curb is visible immediately to the left of the
                        car's path across the intersection; opposing vehicles are farther left ahead.
                        none none, curb no, unknown, evidence partial
Step 2  Right           No painted longitudinal boundary or curb delimits the immediate right side of the
                        car's path across the intersection; a taxi is ahead to the right, and the roadside
                        curb is much farther right.
                        none none, curb no, unknown, evidence partial
Step 3  Markings        line:crosswalk (partial): White zebra-crossing stripes extend across the roadway
                        ahead, with the portion directly in the car's path partly obscured by the silver car.
Step 4  Cross-check     position: Neither a lane count nor an index can be established on the unmarked
                        intersection pavement; no boundary role implies a conflicting position. | roles: No
                        immediate longitudinal paint is visible, so neither side is assigned a lane-line,
                        center-line or edge-line role. | markings: The crosswalk does not establish lane
                        direction or conflict with the absence of visible lane boundaries; no lane-use arrow
                        is visible. | unseen: No hidden arrow, boundary pattern or lane count has been
                        inferred from the vehicles ahead. | result: consistent
Step 5  Rule            left_boundary: No supplied passage governs an absent painted boundary or curb, so no
                        left-crossing permission or prohibition is established here.
Step 5  Rule            right_boundary: No supplied passage governs an absent painted boundary or curb, so no
                        right-crossing permission or prohibition is established here.
Step 5  Rule            line:crosswalk: No supplied passage covers crosswalks, and under the task definitions
                        this marking governs none of the seven actions.
Step 6  change_left     not_applicable: No painted boundary or curb governs crossing the immediate left side
                        of the car's path.
Step 6  change_right    not_applicable: No painted boundary or curb governs crossing the immediate right side
                        of the car's path.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight; the
                        crosswalk does not govern this movement.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: straight travel is unrestricted by the visible markings, and the other
                        actions are not assigned permissions from absent boundaries or arrows.
Advice                  Continue on a predictable straight path toward the receiving roadway, watching for
                        pedestrians on the partly obscured crosswalk. The signals ahead appear green, but the
                        unmarked intersection does not establish a marked lane-change or turning permission.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6935, out 1027, 20.49 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road with two motor-vehicle lanes in this direction continues toward
                        a distant junction. My car is in the leftmost lane beside the median fence. (lanes 2,
                        mine 1, full)
Step 2  Left            A continuous solid yellow line runs beside a raised median edge and white metal fence,
                        with opposing traffic beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane occupied by the black car; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (partial): The nearer group of worn, pale rectangular paint blocks forms
                        several transverse rows across my lane.; symbol:other (partial): A second group of
                        small pale rectangular blocks forms transverse rows farther ahead in my lane.
Step 4  Cross-check     position: Two same-direction lanes and ego position 1 agree with a median edge on the
                        left and a lane divider on the right. | roles: The solid yellow left edge and broken
                        white same-direction divider fit their assigned roles. | markings: The transverse
                        block groups do not conflict with either boundary; no readable lane-use arrow or
                        waiting area is visible. | unseen: The worn block groups are not assigned a more
                        specific meaning, and markings obscured by vehicles or distance are not inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line normally prohibits crossing, and the median
                        barrier also prevents a normal leftward departure. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            symbol:other: No supplied passage specifically covers these transverse rectangular
                        blocks, and they do not govern any of the seven actions.
Step 5  Rule            symbol:other: No supplied passage specifically covers the farther transverse
                        rectangular blocks, and they do not govern any of the seven actions.
Step 6  change_left     prohibited (correct): The solid yellow left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median barrier lies immediately beyond.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to a safe gap.
Step 6  go_straight     allowed (contested, label not_determined): No visible lane-use arrow restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement pavement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement pavement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement pavement marking governs this
                        action; the median boundary governs lateral crossing only.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane without crossing the median boundary. A rightward lane change is
                        permitted by the dashed line, but wait for clearance from the black car; approach the
                        transverse markings cautiously and check junction signs and markings as they become
                        readable.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9224, out 1090, 19.78 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A single-lane ramp descends between concrete barriers and bends gently right ahead. My
                        car is in its only travel lane; no intersection or lane ending is visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A continuous solid white line runs along the left side, with a narrow paved margin and
                        a concrete barrier immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved shoulder, with a concrete
                        barrier farther to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edge lines, consistent with one travel lane and
                        my lane being both leftmost and rightmost. | roles: The continuous lines bound the
                        ramp rather than separate travel lanes. Both appear white; the left line's observed
                        color differs from the yellow left-edge color specified by CN-5.4.3, but its color is
                        not inferred from that rule. | markings: No readable lane-use arrow, word, symbol,
                        waiting area or stop marking is visible. Thin transverse pavement bands ahead are not
                        clearly identifiable as guidance markings. | unseen: No movement instruction or
                        intersection beyond the visible bend is assumed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        left; the edge-line passages provide no ordinary crossing permission here.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: The solid longitudinal boundary normally prohibits crossing right onto
                        the shoulder. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a concrete barrier lies beyond it.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits ordinary crossing onto the
                        shoulder under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the ramp; the solid
                        edge lines govern crossing, not forward travel.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and follow the ramp's rightward bend; do not move
                        onto the shoulder. Observe the visible 40 km/h sign for this ramp; the 30 km/h sign is
                        beside the separate roadway to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8305, out 899, 18.12 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight beneath an overpass, with no intersection
                        or lane ending visible. My car is in the leftmost of two lanes in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous solid yellow line borders the lane on the left, with a narrow paved
                        margin, raised edge and metal median guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being lane 1 of 2. | roles: The solid yellow left edge and broken white same-direction
                        lane divider fit their assigned roles. | markings: No guidance markings are visible
                        within my lane; markings in the adjacent right lane do not govern my lane. | unseen:
                        No hidden intersection, lane ending or distant marking has been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, so my car may not
                        move left across it in ordinary driving. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left edge prohibits ordinary crossing under
                        CN-4.2.2-a, with a physical median barrier beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in your lane, or change right across the broken white line after
                        checking traffic. Do not cross the solid yellow left edge toward the median barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9224, out 812, 13.88 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway continues straight ahead, with three travel lanes and a
                        right-side emergency lane. My car is in the leftmost travel lane; no intersection,
                        ramp or lane ending is visible. (lanes 3, mine 1, full)
Step 2  Left            A single continuous pale yellow line runs along the left edge beside a narrow paved
                        strip and median guardrail; glare reduces the paint's colour clarity.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        the adjacent same-direction lane, with no curb between them.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        first of three same-direction travel lanes. | roles: The continuous left edge marking
                        beside the median and broken white same-direction divider fit their assigned roles. |
                        markings: No arrows, words, symbols or transverse markings are visible in my lane;
                        overhead sign arrows are not pavement markings. | unseen: Glare makes the left paint
                        colour less certain, so its evidence is partial; no markings beyond the visible road
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: The continuous longitudinal line normally prohibits crossing to the
                        left, and the median guardrail is also a physical limit. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The continuous left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a median guardrail beyond.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight, and the
                        lane visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line only when
                        clear; do not cross the left boundary. Observe the overhead passenger-car lane
                        restriction and posted speed limits, and keep out of the emergency lane during normal
                        driving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 9224, out 882, 16.33 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in the
                        third of four same-direction lanes, with a straight-ahead arrow in its lane. (lanes 4,
                        mine 3, full)
Step 2  Left            A continuous white line separates my lane from the lane on the left; short transverse
                        teeth project from its far side, and there is no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another motor-vehicle lane on the right,
                        with no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in front of the hood has one head pointing
                        straight ahead.; line:stop_line (full): A transverse solid white stop line crosses my
                        lane just before the pedestrian crossing.; line:crosswalk (full): Broad white
                        pedestrian-crossing stripes extend across my lane immediately beyond the stop line.
Step 4  Cross-check     position: Two lanes lie to my left and one to my right, consistent with lane-line
                        boundaries on both sides and an ego index of 3 among four lanes. | roles: Both
                        boundaries are white solid lines separating same-direction lanes; the teeth on the far
                        side of the left boundary face the adjacent lane. | markings: The straight-only arrow
                        agrees with a fixed-direction approach lane bounded by solid white lines; the stop
                        line precedes the crosswalk. | unseen: No direction or restriction has been inferred
                        from obscured markings in other lanes. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            arrow:straight: The single straight-ahead arrow allows proceeding straight and
                        excludes left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not independently require a full stop. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian-crossing
                        marking; under the task definitions it does not decide any of the seven actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight; do not cross either solid boundary to select a
                        turning lane here. Obey the applicable traffic signal, stop before the stop line when
                        required, and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 8432, out 1396, 29.24 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a zebra crossing
                        ahead. My car is between two white approach-lane boundaries; vehicles and the hood
                        obscure parts of the approach, so the total lane count and my lane's index cannot be
                        established reliably. (lanes None, mine None, insufficient)
Step 2  Left            A solid white longitudinal line with short diagonal teeth projecting to its left
                        separates my lane from another traffic lane; its nearest portion is obscured, and no
                        curb is visible.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A solid white line runs from beside the hood to the transverse stop line, with another
                        traffic lane beyond and no curb visible.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A broad solid white transverse stop line crosses my lane
                        immediately before the pedestrian crossing.; line:crosswalk (full): White zebra-
                        crossing stripes extend across the road immediately beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from adjacent lanes travelling in my
                        direction; my lane is therefore not an outside lane, but the obscured outer lanes
                        prevent a reliable count or index. | roles: The white solid boundaries fit same-
                        direction approach-lane separation; the diagonal teeth on the left indicate variable
                        guide-lane treatment. | markings: The stop line and zebra crossing agree with an
                        intersection approach. No lane-use arrow or waiting area is visible. | unseen: No
                        direction arrow, variable lane-direction display, or obscured lane count has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The toothed boundary indicates variable guide-lane treatment whose
                        direction is supplied by variable lane-direction signs; crossing its solid
                        longitudinal line is normally prohibited under CN-4.2.2-a. [CN-6.10.1-4-V] "... The
                        variable guide lane line marks a guide lane whose direction can change as needed; it
                        is placed on intersection approaches. ... No guide arrows shall be "
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            line:stop_line: This line identifies where to stop when required to yield or wait, but
                        does not independently require a stop. [CN-6.4.1-2] "The stop line marks where
                        vehicles stop when yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        it does not independently determine any of the seven actions.
Step 6  change_left     prohibited (correct): The left boundary has a solid longitudinal line, which
                        CN-4.2.2-a normally prohibits crossing.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight;
                        the stop line alone does not require stopping.
Step 6  turn_left       not_applicable: No marking in view governs this action.
Step 6  turn_right      not_applicable: No marking in view governs this action.
Step 6  u_turn          not_applicable: No marking in view governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary restrictions govern lane changes only, and the marking-only
                        straight-ahead result does not establish the direction currently assigned by a
                        variable lane-direction sign.
Advice                  Stay between the solid boundaries and check the applicable lane-direction signs and
                        traffic signals before proceeding, particularly because the left boundary has
                        variable-guide-lane teeth. If required to stop, stop before the transverse stop line
                        and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 8029, out 1244, 23.99 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road has three lanes in this direction, with a median barrier on the
                        left and a landscaped curb on the right. My car is in the middle lane, approaching a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No readable guidance marking is visible in my lane, so none
                        conflicts with the boundaries. | unseen: No distant pavement arrows or intersection
                        transverse markings are inferred; the intersection approach is too distant to inspect
                        fully. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent left lane
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent right
                        lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: crossing either visible broken lane boundary is permitted, and no
                        intersection turning permission is inferred from the distant sign or unreadable
                        pavement.
Advice                  Continue in the middle lane for now; either adjacent lane can be entered across the
                        visible broken line after checking traffic. Check the lane-direction signs and closer
                        pavement markings before the intersection, and obey its signals; no stopping position
                        is readable here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8370, out 844, 12.97 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction approaches a distant
                        intersection. My car is in the middle lane, with a median barrier to the far left and
                        a landscaped curb to the far right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane, with the roadside curb farther beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small, distant white forward-pointing arrow is visible
                        ahead in my lane; its straight head is discernible, although its shaft is indistinct
                        at this distance.
Step 4  Cross-check     position: The middle lane of three has a same-direction lane across each boundary,
                        agreeing with both boundaries being lane lines. | roles: Both white broken boundaries
                        fit crossable same-direction lane lines. | markings: The visible straight arrow agrees
                        with continuation of this lane; markings in neighboring lanes do not govern my lane. |
                        unseen: The distant arrow is recorded with partial evidence; no unreadable distant
                        words, stop line, or waiting area have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-ahead guide arrow indicates straight travel from this
                        lane rather than a left turn, right turn, or U-turn. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): The discernible straight arrow indicates straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not indicate a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not indicate a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not indicate a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible broken boundaries govern lane changes, while the identifiable
                        straight arrow governs movements from this lane.
Advice                  Remain in this lane to travel straight, subject to the intersection signals. For a
                        turn, select the appropriately indicated lane while crossing is still permitted,
                        checking adjacent traffic and the lane-direction signs.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 8773, out 1110, 22.29 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection. My car is in the
                        third of four visible lanes in this direction, between lanes with sawtooth-edged guide
                        markings. (lanes 4, mine 3, full)
Step 2  Left            A continuous white line borders my lane on the left, with short tooth-like projections
                        on its far side; another same-direction lane lies beyond, with no curb at this
                        boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with short tooth-like
                        projections on its far side; another same-direction lane lies between it and the
                        roadside curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A small white straight-ahead arrow is visible farther ahead in
                        my lane.
Step 4  Cross-check     position: Two same-direction lanes lie to my left and one to my right, consistent with
                        lane 3 of 4 and lane-line boundaries on both sides. | roles: Both white continuous
                        boundaries separate same-direction lanes; their outward-facing teeth border the
                        adjacent guide lanes. | markings: The straight arrow in my lane is consistent with a
                        fixed-direction lane between the adjacent sawtooth-marked lanes; the adjacent pavement
                        words are not in my lane. | unseen: No unreadable distant stop line or other
                        intersection marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: The continuous white lane boundary prohibits my car from crossing left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The continuous white lane boundary prohibits my car from crossing
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits straight travel and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (contested, label allowed): The solid white left lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (contested, label allowed): The solid white right lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid boundary. Follow
                        the intersection signals; a turn requires a suitable lane reached where changing lanes
                        is permitted.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 8366, out 1395, 31.75 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road with four lanes in this direction approaches an intersection
                        farther ahead. My car is in the third lane from the left, the second lane from the
                        right. (lanes 4, mine 3, full)
Step 2  Left            A broken white line with visible painted segments and gaps separates my lane from
                        another same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible painted segments and gaps separates my lane from the
                        rightmost same-direction lane; the roadside curb is beyond that adjacent lane, not on
                        my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.
Step 4  Cross-check     position: Four lanes and position three agree with another same-direction lane on each
                        side of my lane. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane dividers. | markings: The straight-only arrow agrees
                        with a through lane; the straight-and-right arrow farther right belongs to the
                        adjacent lane. | unseen: No obscured markings have been inferred; traffic and distance
                        limit inspection of the far approach, and no stop line or waiting area is
                        identifiable. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits straight travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight. For a right turn, move safely across the broken
                        line into the rightmost lane with the straight-and-right arrow; for a left turn, reach
                        the marked left-turn lane before any solid approach lines, and obey the intersection
                        signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8773, out 981, 16.1 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road continues straight beneath traffic signals, with a median
                        fence on the left and a bus in the far-right lane. My car is in the second lane from
                        the left; four same-direction lanes appear present, although the bus obscures the far-
                        right roadway edge. (lanes 4, mine 2, partial)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying an interior lane,
                        second from the left; the total lane count is less certain because of the bus. |
                        roles: Both white broken boundaries fit same-direction lane separators. | markings: No
                        readable arrow, word, symbol, transverse line or waiting area is visible in my lane. |
                        unseen: The obscured far-right roadway edge is not treated as directly observed, and
                        no distant or vehicle-hidden marking is inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane line permits crossing
                        under CN-5.2.1-2; the bus is farther right, not directly across this boundary.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken boundaries govern lane changes only, and no turn permission is
                        inferred from the absence of arrows.
Advice                  Continue straight in this lane, or change one lane left or right only after checking
                        for a safe gap, especially near the taxi and bus. The visible through signal is green
                        and the left-turn signal is red; no stop line or turn guidance is readable in your
                        lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 8370, out 1005, 18.45 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A two-way urban road curves gently left, with a side-road opening on the right ahead.
                        My car is in the leftmost of two visible lanes in its direction. (lanes 2, mine 1,
                        full)
Step 2  Left            A single solid yellow line curves ahead along the left of my lane, with opposing-
                        direction roadway beyond and no curb on this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and a same-direction lane line on the
                        right agree with my lane being lane 1 of 2. | roles: The single solid yellow line fits
                        a no-crossing center line, and the broken white line fits a crossable same-direction
                        lane line. | markings: No arrows, words, symbols, transverse lines or waiting areas
                        are visible in my lane. | unseen: No hidden arrows or intersection markings have been
                        inferred; the assessment covers the visible road. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): CN-6.1.4 prohibits crossing the single solid yellow center line.
Step 6  change_right    allowed (correct): CN-5.2.1-2 permits crossing the broken white lane line.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action at the next intersection; the center
                        line governs crossing the left boundary only.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane following the road's leftward curve; do not cross the solid
                        yellow center line. A rightward lane change is permitted when safe, but check
                        carefully for the scooter and other traffic; no visible lane-use arrows establish
                        turning permissions ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8706, out 930, 16.22 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined expressway continues straight ahead beneath overhead lane
                        signs; no intersection, exit or lane ending is visible. My car is in the second of
                        five same-direction travel lanes, with an emergency lane farther right. (lanes 5, mine
                        2, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another travel lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another travel lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Large white Chinese pavement lettering is partially visible
                        immediately ahead of the hood; the complete inscription is cropped or obscured and
                        cannot be read reliably.
Step 4  Cross-check     position: The second-of-five position agrees with ordinary travel lanes immediately on
                        both sides. | roles: Both white broken boundaries fit same-direction lane dividers. |
                        markings: The partially visible pavement lettering does not establish a directional
                        arrow or conflict with either boundary; no waiting area is visible. | unseen: The
                        obscured inscription is not reconstructed, and no intersection or movement arrows
                        beyond the visible stretch are assumed. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent left
                        lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent right
                        lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            text:other: No supplied passage covers this incomplete inscription, and ordinary
                        pavement text does not itself govern any of the seven actions.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-turn marking governs this action, and
                        no intersection is visible.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-turn marking governs this action, and
                        no intersection is visible.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-turn marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the broken boundaries govern only lane changes, the incomplete text grants
                        no movement permission, and no intersection-turn permission is inferred.
Advice                  Continue straight in this lane; either adjacent travel lane may be entered across its
                        broken divider after checking traffic. Follow the overhead lane and speed signs, keep
                        out of the emergency lane, and do not infer a turning opportunity from this expressway
                        scene.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8370, out 992, 16.62 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined elevated road continues straight toward overhead signs, with
                        no visible intersection or lane ending. My car is in the second of four lanes
                        travelling in this direction. (lanes 4, mine 2, full)
Step 2  Left            A single broken white line, with visible dashes and gaps, separates my lane from
                        another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible dashes and gaps, separates my lane from
                        another traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane lies to my left and two lie to my right, consistent with lane 2 of
                        4 and lane-line boundaries on both sides. | roles: Both boundaries are broken white
                        lines, consistent with separators between same-direction lanes. | markings: No arrows,
                        words, symbols, waiting areas or transverse traffic markings are visible in my lane;
                        the transverse bridge joint is not a traffic marking. | unseen: No hidden lane-use
                        marking or distant intersection arrangement has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the lane
                        continues ahead.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane; either adjacent lane may be entered across the
                        broken white line when safe. No stop marking is visible, and the distant overhead
                        signs are too small to read reliably.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8370, out 847, 13.49 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test R | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road has three lanes in this direction, with a signalized intersection
                        visible in the distance. My car is in the middle lane behind a dark car. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        left lane occupied by a taxi; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from the
                        right lane occupied by a motor scooter; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible in my lane immediately
                        behind the dark car.
Step 4  Cross-check     position: Lane lines on both sides agree with being lane 2 of three lanes in this
                        direction. | roles: Both white broken boundaries fit crossable lines separating lanes
                        travelling in the same direction. | markings: The straight-ahead arrow is consistent
                        with the lane layout; no conflicting marking or waiting area is visible. | unseen: No
                        hidden markings are inferred; the lead car and distance obscure the pavement farther
                        ahead, including the intersection approach. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-ahead guide arrow allows straight travel from my lane and
                        excludes left turns, right turns and U-turns. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight-ahead arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not indicate a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not indicate a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not indicate a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and obey the signals ahead. Lane changes are permitted
                        across the visible broken lines only when safe; check carefully for the taxi and
                        scooter, and use a suitably marked lane if you intend to turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 8773, out 908, 13.56 s
```
