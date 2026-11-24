# Reasoning of lane run 20261116_132827_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues toward an overpass, with no intersection or lane
                        ending visible. My car is in the rightmost of three same-direction traffic lanes,
                        beside a paved shoulder. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from the adjacent
                        same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved shoulder, with a
                        guardrail farther beyond the shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on my left and roadway edge line on my right agree with my
                        position as lane 3 of 3. | roles: The broken white line fits a same-direction lane
                        divider, and the solid white line fits the right roadway edge. | markings: No guidance
                        markings are visible within my lane, so none conflict with the boundaries. | unseen:
                        No distant intersection layout or markings hidden beneath vehicles have been inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid white boundary onto the shoulder is normally
                        prohibited, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change one lane left across the broken white line when safe;
                        do not cross the solid right edge onto the shoulder in normal driving. A bus-lane sign
                        concerns the farther-left lane; no turning guidance or stopping point is visible for
                        my lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 841, 15.81 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane road continues toward an overpass, with traffic ahead and no visible
                        intersection or lane ending. My car is in the rightmost lane; vehicles partly obscure
                        the lanes farther left. (lanes 3, mine 3, partial)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved shoulder and
                        a guardrail beyond it rather than a curb at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The apparent three-lane layout places my car in lane 3, consistent with a
                        lane line on the left and a roadway edge on the right; vehicles partly obscure the
                        far-left layout. | roles: The broken white left line fits a same-direction lane
                        divider, and the solid white right line fits a right roadway edge. | markings: No
                        guidance marking is visible in my lane, so none conflicts with the boundaries. |
                        unseen: The total lane count is tentative because vehicles obscure part of the left-
                        hand roadway; no hidden arrows or distant intersection markings are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to cross into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken line only after checking
                        traffic and clearance. Do not cross the solid right edge line onto the shoulder during
                        ordinary driving; no turn assignment or stopping location is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 948, 20.61 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight ahead, with two travel lanes and an emergency
                        shoulder on the right. My car is in the right-hand travel lane; no intersection or
                        lane ending is visible. (lanes 2, mine 2, full)
Step 2  Left            A pale white broken line, with visible long dashes and gaps, separates my lane from
                        another travel lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous pale yellow-looking line separates my lane from the paved emergency
                        shoulder; the guardrail is beyond the shoulder, not at this line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two travel lanes and ego lane 2 agree with a lane divider on the left and an
                        emergency-shoulder edge on the right. | roles: The broken white left line fits a same-
                        direction lane divider. The right line appears yellowish, which does not match the
                        prescribed white right edge line; its visible position beside the emergency shoulder
                        establishes its role without recoloring the observation. | markings: No pavement
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No hidden pavement markings or intersection movements have been
                        inferred; overhead arrows and numbers are signs, not lane paint. | result: Spatially
                        consistent; the apparent right-edge paint color differs from the prescribed color.
Step 5  Rule            left_boundary: The broken white same-direction lane divider permits crossing into the
                        left lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 5  Rule            right_boundary: The solid emergency-stopping-lane edge is not for routine crossing;
                        the passage permits crossing by broken-down and rescue vehicles using that lane.
                        [CN-5.4.7] "The edge line at an emergency stopping lane shall be solid. Note: broken-
                        down and rescue vehicles may cross the solid line when using the emergency stopping
                        lan"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid emergency-shoulder edge prohibits
                        routine entry under CN-5.4.7.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-turn pavement marking governs this
                        action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-turn pavement marking governs this
                        action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-turn pavement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral crossing, and no unseen intersection or
                        pavement arrow has been used to decide a movement.
Advice                  Continue in this lane, or change left across the broken line only after checking the
                        nearby truck and other traffic; do not enter the emergency shoulder routinely. The
                        overhead sign for this lane displays a maximum of 100 km/h and minimum of 60 km/h;
                        observe signs and actual traffic conditions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1016, 23.61 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An elevated urban road continues ahead with traffic and a barrier on the right; no
                        intersection or lane ending is visible. My car is in the rightmost of three visible
                        same-direction lanes. (lanes 3, mine 3, partial)
Step 2  Left            Orange broken paint, with distinct long dashes and gaps, separates my lane from the
                        occupied lane on the left; no curb forms this boundary.
                        other dashed, curb no, lane_line, evidence full
Step 2  Right           Orange broken paint runs along the right of my lane, immediately inside a continuous
                        white line; a narrow roadside strip and raised barrier lie farther right.
                        other dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes are discernible, although vehicles and the image edge partly
                        obscure the far-left extent; a lane line on my left and an edge boundary on my right
                        fit the rightmost position. | roles: Orange broken markings provide temporary
                        guidance; the right orange marking lies immediately inside an existing white solid
                        roadway edge. | markings: No readable arrows, words, symbols or transverse markings
                        are visible in my lane. | unseen: The distant pavement is partly obscured by vehicles;
                        no intersection movements or additional markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The orange paint identifies temporary guidance rather than an opposing-
                        traffic yellow centre line. [CN-4.3.2-c] "c) Orange markings: temporary guidance in
                        work zones."
Step 5  Rule            left_boundary: The broken temporary boundary permits crossing to the lane on the left
                        when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            right_boundary: The broken orange boundary permits crossing that marking, but the
                        separate solid white line immediately beyond normally prohibits crossing farther onto
                        the roadside strip. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The orange broken lane boundary is crossable under CN-4.2.2-a.
Step 6  change_right    allowed (WRONG, label not_determined): The nearest orange broken boundary is crossable
                        under CN-4.2.2-a; this does not authorize crossing the separate solid white edge
                        beyond it.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: rightward permission applies only to crossing the nearest broken orange
                        marking, not the separate solid white edge or the physical barrier.
Advice                  Continue within the orange temporary guidance; change left only when a safe gap
                        exists. There is no usable traffic lane visible on the right: do not cross the solid
                        white roadway edge or approach the barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1191, 29.18 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead with no intersection or lane ending clearly
                        visible. My car is in the rightmost of three same-direction lanes, marked as a bus-
                        only lane. (lanes 3, mine 3, full)
Step 2  Left            A yellow broken line with visible long dashes and gaps separates my lane from another
                        same-direction traffic lane; there is no curb on this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with yellow dashes immediately
                        alongside it on my lane's side; beyond the white line is a paved margin and then a
                        concrete barrier.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (partial): White longitudinal Chinese text identifies a 公交专用 bus-only lane;
                        the nearest part of the inscription is cut off by the hood, while 交、专、用 are visible.
Step 4  Cross-check     position: Two same-direction lanes lie to the left, and the roadway edge lies to the
                        right, consistent with my lane being third of three. | roles: The white solid right
                        edge fits its role. The yellow broken left boundary is not the white bus-lane boundary
                        described in the supplied standard, but the pavement text establishes that this is a
                        special lane rather than an opposing-traffic boundary. | markings: The bus-only text
                        agrees with the special-lane interpretation. No directional arrow or transverse
                        stopping marking is visible in the readable stretch. | unseen: The nearest part of the
                        bus inscription and the distant continuation are obscured or too small to read; no
                        reserved hours or distant movement restrictions are inferred. | result: consistent
Step 5  Rule            left_boundary: The visible broken boundary permits crossing out of my lane; its yellow
                        paint does not match the white bus boundary specified in CN-6.9.1. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing onto the paved
                        roadside margin. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            text:bus: The bus-only designation prohibits an ordinary car from entering this
                        reserved lane, but does not itself prohibit leaving across a broken boundary.
                        [CN-6.9.1] "The bus lane line shows that vehicles other than buses shall not enter the
                        lane. It consists of a broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (contested, correct): The broken left boundary permits leaving the bus lane
                        under CN-4.2.2-a.
Step 6  change_right    prohibited (contested, label allowed): The solid white right boundary prohibits normal
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing along
                        the lane; the bus text does not govern this movement classification.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: permission to continue straight is not permission for an ordinary car to
                        occupy the reserved bus lane, and the broken left boundary permits leaving it.
Advice                  As an ordinary car, move safely into the general-traffic lane to the left across the
                        broken boundary rather than remaining in the bus-only lane. Do not cross the solid
                        white right edge; check signs for any operating-time restrictions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1108, 23.93 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road descends toward an underpass. My car is in a single motor-vehicle lane
                        on a physically separated carriageway, with a wider roadway beyond the left barrier
                        and a narrow strip used by two-wheelers on the right. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line runs beside a narrow paved margin and a concrete barrier on
                        the left; another roadway lies beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from a narrow paved strip occupied by two-
                        wheelers, with a raised curb farther to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are edges of the single motor-vehicle lane on this separated
                        carriageway; the lanes beyond the left barrier are not adjacent lanes available for a
                        lane change. | roles: The right white solid line fits a motor/non-motor separation
                        edge. The left line visibly appears white despite the prescribed yellow color for a
                        left carriageway edge; its physical position beside the barrier establishes its edge
                        role. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are discernible in my lane. | unseen: No markings inside the dark underpass are
                        inferred, and the lane's eventual end is not visible. | result: Consistent spatial
                        interpretation; the observed white left edge is retained rather than recolored to fit
                        the standard.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing, and the
                        concrete barrier also prevents a leftward departure. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing into the
                        strip on the right. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left line prohibits normal crossing under CN-4.2.2-a,
                        and a concrete barrier lies alongside it.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane;
                        the edge lines do not prohibit forward travel.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the boundaries govern lateral departures only, continuing forward is
                        unrestricted by visible markings, and no unseen intersection movements are inferred.
Advice                  Continue within the solid boundaries toward the underpass; do not cross left toward
                        the barrier or right into the two-wheeler strip. Watch the two-wheelers and obey the
                        posted signs and signals as you approach the darker section.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 966, 19.31 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow urban road continues straight past bus shelters on the left and a raised
                        sidewalk with parked bicycles on the right. My car is in the right-hand of two same-
                        direction lanes, approaching a pedestrian crossing; no intersection or lane ending is
                        clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A single solid white line separates my lane from the paved lane on the left, with no
                        curb between them.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A raised curb borders my lane on the right, with a yellow-orange face and a pale white
                        strip along its top; parked bicycles and scooters stand on the sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A thin solid white transverse line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): White zebra-crossing bars
                        extend across my lane ahead.
Step 4  Cross-check     position: Two same-direction lanes and ego position 2 agree with a lane divider on the
                        left and the roadway curb on the right. | roles: The solid white left divider fits a
                        no-crossing same-direction lane line; the white strip and raised curb define the right
                        roadway edge. | markings: The transverse line and zebra crossing are compatible; no
                        directional arrow, STOP word, or waiting area is visible in my lane. | unseen: The
                        partial arrow at the bottom left belongs to the adjacent lane and is not attributed to
                        my lane; no distant intersection configuration is inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white same-direction lane divider prohibits my car from
                        crossing to the left. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 5  Rule            right_boundary: The raised curb defines the physical roadway edge, not a crossable
                        route onto the sidewalk. [CN-5.4.5] "Where a non-motorized lane is needed and there is
                        no separating facility between it and the motor vehicle lanes, a motor/non-motor
                        separation line shall be prov"
Step 5  Rule            line:stop_line: The white stop line identifies where to stop when yielding or waiting,
                        but does not alone require a full stop. [CN-6.4.1-2] "The stop line marks where
                        vehicles stop when yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers zebra crossings; this marking
                        identifies a pedestrian crossing and does not determine any of the seven movement
                        permissions.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The raised curb is a physical roadway edge, not a traversable
                        lane boundary.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the stop
                        line alone does not require a full stop.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current lane without crossing the solid left divider or the right
                        curb. Approach the pedestrian crossing cautiously and, if stopping to yield, stop
                        before the transverse white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1086, 21.45 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in the left lane of a two-lane branch running beside a wider, congested
                        carriageway on the left. A painted separation widens between the roads; no
                        intersection or lane ending is clearly visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line borders the lane on the left, with a narrow white-hatched
                        separation beyond it and vehicles on the adjacent carriageway farther left; no curb
                        forms this boundary.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with a visible long dash and gap, separates this lane from
                        another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The car is in lane 1 of the two-lane branch: its left boundary borders the
                        painted separation, and its right boundary separates the second lane. | roles: The
                        broken white right boundary fits a same-direction lane line. The solid white left
                        boundary visibly outlines the branch beside the painted separation; its color is
                        observed, not inferred from its position. | markings: No arrow, word, symbol, or
                        transverse line is visible in the car's lane. The hatching is outside its left
                        boundary. | unseen: Traffic obscures the more distant pavement, so no markings or
                        intersection layout are inferred there. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary prohibits ordinary crossing to the
                        left, except for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left boundary prohibits ordinary
                        crossing under CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow restricts continuing along this
                        lane, and no lane ending is visible.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along this branch without crossing the solid left boundary or the hatched
                        separation. A right lane change is permitted by the broken line when safe; keep a safe
                        gap behind the car ahead and check later markings before choosing a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 935, 20.26 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road continues straight ahead, with no intersection or
                        lane ending visible. My car is in the leftmost of two motor-vehicle lanes; a separate
                        roadside strip lies beyond the solid line on the far right. (lanes 2, mine 1, full)
Step 2  Left            A solid white painted line runs beside a raised curb and planted median on the left,
                        with another carriageway beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with distinct long dashes and gaps, separates my lane from
                        another motor-vehicle lane travelling in the same direction; there is no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge on the left and a same-direction lane on the right
                        agree with my position as lane 1 of 2. | roles: The broken white right boundary fits a
                        same-direction lane line. The left boundary is visibly white despite occupying a left-
                        edge position where CN-5.4.3 specifies yellow; its curb-side location identifies its
                        edge role. | markings: No guidance arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: No distant intersection layout or markings
                        hidden by vehicles have been inferred. | result: The observed white left-edge paint is
                        retained rather than changed to the prescribed yellow; the lane interpretation is
                        otherwise consistent.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits changing into the
                        adjacent right lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action; the left
                        boundary governs crossing, not a movement at a future intersection.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern only crossing their respective sides, and no unseen
                        intersection movements have been assigned permission.
Advice                  Continue straight in this lane; a right lane change is permitted by the dashed line
                        when traffic allows, but do not cross the solid left edge or median. No intersection
                        turn guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 934, 19.0 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is within a broad urban signal-controlled intersection, facing a zebra
                        crossing and the road continuing ahead. The intersection foreground has no visible
                        lane separators, so the number of approach lanes and the ego lane's index cannot be
                        established. (lanes None, mine None, insufficient)
Step 2  Left            No painted boundary or curb defines the left side of the car's path in the
                        intersection foreground; opposing vehicles and a median farther ahead provide context
                        but do not establish a continuous boundary here.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           No painted boundary or curb defines the immediate right side of the car's path across
                        the intersection; a taxi and the distant roadside curb do not establish the ego lane's
                        boundary.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (partial): White zebra-crossing stripes extend across the path ahead,
                        with the central portion partly hidden by the silver car.
Step 4  Cross-check     position: Neither a lane count nor an ego lane index can be verified because lane
                        boundaries are not marked through the visible intersection. | roles: Both boundary
                        roles remain unknown; no unseen lane or centre line is inferred from vehicle
                        positions. | markings: The visible crossing is compatible with the intersection scene;
                        no readable lane-use arrow, word, or waiting area is visible in the car's path. |
                        unseen: No boundary pattern, arrow underneath a vehicle, or approach-lane assignment
                        has been inferred. | result: consistent
Step 5  Rule            left_boundary: No identifiable left boundary is visible, so no boundary-specific
                        crossing permission or prohibition can be established.
Step 5  Rule            right_boundary: No identifiable right boundary is visible, so no boundary-specific
                        crossing permission or prohibition can be established.
Step 5  Rule            line:crosswalk: No supplied passage covers crosswalks, and under the task definitions
                        this transverse marking does not determine any of the seven actions.
Step 6  change_left     not_determined: The left lane boundary and the space it separates cannot be identified
                        in this unmarked intersection.
Step 6  change_right    not_determined: The right lane boundary and the space it separates cannot be
                        identified in this unmarked intersection.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight, and the
                        road continues ahead.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: lateral changes remain undetermined because the boundaries cannot be
                        identified, and no turn permission is inferred from the traffic signals or other
                        vehicles.
Advice                  Continue cautiously along the established forward path without assuming an adjacent
                        lane is available, and watch for pedestrians at the crossing. The signals appear
                        green, but check the applicable signal and traffic before proceeding; this view does
                        not establish a turning-lane assignment.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation none_needed, contradictions []
Tokens                  in 10766, out 1022, 21.56 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road with opposing traffic separated by a central fence continues toward a
                        distant junction. My car is in the leftmost of two lanes in this direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid yellow line runs beside a raised central divider with a white metal fence;
                        opposing traffic is beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with visible long segments and gaps separates my lane from another
                        same-direction lane occupied by a dark sedan.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (partial): The nearer group of transverse rows of small, pale rectangular
                        blocks spans my lane, resembling a transverse warning or rumble marking.; symbol:other
                        (partial): A second group of transverse rows of small, pale rectangular blocks crosses
                        my lane farther ahead.
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with lane 1 of 2. | roles: The solid yellow line fits the left roadway edge beside the
                        divider; the broken white line fits a crossable same-direction lane boundary. |
                        markings: The transverse block markings do not indicate a turning direction and do not
                        conflict with the boundaries. | unseen: No arrow, readable pavement word, stop line or
                        waiting area is identifiable in my lane; the distant pavement is partly obscured by
                        traffic and distance. The exact identity of the transverse block markings is
                        uncertain. | result: consistent
Step 5  Rule            left_boundary: The solid yellow boundary normally prohibits crossing to the left, and
                        the physical divider also prevents an ordinary lane change. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            symbol:other: No supplied passage specifically covers this transverse block marking;
                        it establishes no permission or prohibition for the seven assessed actions.
Step 5  Rule            symbol:other: No supplied passage specifically covers the farther transverse block
                        marking; it establishes no permission or prohibition for the seven assessed actions.
Step 6  change_left     prohibited (correct): The solid yellow boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a physical divider lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to a safe gap.
Step 6  go_straight     allowed (contested, label not_determined): No visible arrow restricts continuing
                        straight along my lane.
Step 6  turn_left       not_determined: The distant lane-end pavement is obscured, so any movement-defining
                        arrow there cannot be assessed.
Step 6  turn_right      not_determined: The distant lane-end pavement is obscured, so any movement-defining
                        arrow there cannot be assessed.
Step 6  u_turn          not_determined: The distant lane-end pavement is obscured, so any movement-defining
                        arrow there cannot be assessed.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent: boundary-crossing decisions follow the visible lines, straight travel
                        remains unrestricted by visible markings, and obscured lane-end turn guidance is not
                        guessed.
Advice                  Continue in this lane for straight travel; do not cross the median boundary. A
                        rightward lane change is permitted by the dashed line, but the adjacent sedan must
                        clear first; check the junction’s arrows, signs and signals before selecting a turning
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1146, 22.29 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A single-lane, barrier-separated ramp descends and bends gently right ahead. My car is
                        in its only travel lane; a paved shoulder lies to the right, and no intersection or
                        lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid white line runs along the left, with a narrow paved margin and a
                        concrete barrier immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from a paved shoulder, with a concrete
                        barrier beyond the shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges rather than lane dividers, consistent with
                        one travel lane and ego lane index 1. | roles: Both lines are visibly solid white; the
                        left line's white paint is reported as seen, despite the cited standard normally
                        specifying yellow for a left edge. | markings: No readable arrows, words, symbols or
                        marked waiting areas are visible in my lane; the transverse strips ahead appear to be
                        roadway joints rather than guidance markings. | unseen: No movement restriction is
                        inferred from the distant bend, and no intersection or markings beyond visibility are
                        assumed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left;
                        the concrete barrier also physically bounds the roadway. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal line normally prohibits crossing onto the right
                        shoulder. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 6  change_left     prohibited (correct): The solid left edge line prohibits normal crossing under
                        CN-4.2.2-a, with a barrier immediately beyond.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits normal crossing onto the
                        shoulder under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the lane; the solid
                        boundaries govern crossing, not forward travel.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid edge lines and follow the ramp's rightward bend; do not move
                        onto the shoulder. Observe the visible 40 km/h speed-limit sign for this ramp.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 874, 16.2 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided highway continues beneath an overpass, with no intersection or lane ending
                        visible. My car is in the leftmost of two lanes in this direction. (lanes 2, mine 1,
                        full)
Step 2  Left            A single solid yellow line runs along the left edge of my lane, with a narrow paved
                        margin, raised median edge and metal guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another lane travelling in the same direction; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the same-direction lane to the right agree with my
                        car being in lane 1 of 2. | roles: The solid yellow left edge and broken white same-
                        direction divider fit their assigned roles. | markings: No arrows, words, symbols or
                        transverse markings are visible in my lane; there is no conflict with the boundaries.
                        | unseen: No intersection, lane-end marking or waiting area is inferred beyond the
                        visible road. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, so my car may not
                        move left across it in ordinary driving. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits changing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid yellow left boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a median guardrail lies beyond.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts continuing straight along this
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line after
                        checking traffic. Do not cross the solid yellow left edge; no turning or stopping
                        location is marked in the visible stretch.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 818, 14.08 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway continues straight, with no intersection, ramp or lane
                        ending visible. My car is in the leftmost of three travel lanes; an emergency shoulder
                        lies beyond the rightmost lane. (lanes 3, mine 1, full)
Step 2  Left            A pale yellow continuous solid line runs along the left of my lane, with a narrow
                        paved margin and median guardrail beyond it; glare reduces the paint's clarity.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction travel lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right same-direction lane line agree with my car
                        occupying lane 1 of three travel lanes. | roles: The pale yellow solid left edge and
                        broken white right lane separator fit their assigned roles. | markings: No pavement
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane; the overhead arrows are signs, not pavement markings. | unseen: Glare limits the
                        clarity of the left paint; no unseen intersection or distant pavement marking has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal left edge line normally prohibits crossing it,
                        except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The visible solid left edge line prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight, and the
                        lane continues ahead.
Step 6  turn_left       not_applicable: No pavement arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No pavement arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No pavement arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line after checking
                        traffic; do not cross the solid left edge. Observe the overhead passenger-car
                        restriction and posted lane speeds, and keep the emergency shoulder clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 865, 16.95 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in the
                        middle of three visible same-direction motor-vehicle lanes. (lanes 3, mine 2, full)
Step 2  Left            A continuous white line runs along the left of my lane, with short white tooth-like
                        bars projecting away from my lane into the adjacent lane; there is no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction motor-vehicle
                        lane on the right, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.; line:stop_line (full): A transverse solid white stop line crosses my
                        lane immediately before the pedestrian crossing.; line:crosswalk (partial): White
                        pedestrian-crossing stripes extend across my lane beyond the stop line; some of the
                        crossing is obscured by vehicles.
Step 4  Cross-check     position: Two lane-line boundaries agree with my lane being second of three same-
                        direction motor-vehicle lanes. | roles: Both boundaries are white solid lines
                        separating same-direction lanes. The teeth on the far side of the left boundary relate
                        to the adjacent lane, not to my lane. | markings: The straight arrow agrees with a
                        through guide lane bounded by solid white lines; the stop line precedes the pedestrian
                        crossing. | unseen: No additional arrows or words are inferred beneath vehicles, and
                        the partially obscured crosswalk is identified only from its visible stripes. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            arrow:straight: The single straight arrow permits straight travel and excludes left
                        turns, right turns and U-turns from my lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when required to yield
                        or wait, but does not independently require a full stop on every approach.
                        [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or waiting to
                        proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically governs crosswalk markings; the
                        crossing does not independently decide any of the seven lane actions.
Step 6  change_left     prohibited (correct): Crossing the solid white left lane boundary is prohibited by
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): Crossing the solid white right lane boundary is prohibited by
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane when the applicable signal and crossing conditions
                        permit; do not cross either solid boundary to change lanes here. If required to stop,
                        stop before the white stop line and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1176, 19.44 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection with a broad
                        pedestrian crossing. My car is immediately before the stop line; vehicles and the hood
                        obscure parts of the approach, so the total lane count and my lane's index cannot be
                        established reliably. (lanes None, mine None, insufficient)
Step 2  Left            A continuous white line with repeated short oblique projections runs along the left of
                        my lane toward the stop line; another traffic lane lies beyond it, with no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs from beside the hood toward the stop line on my right,
                        with another traffic lane beyond it and no curb; the visible stretch is short.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        line:stop_line (full): A broad solid white transverse stop line crosses my lane
                        immediately ahead.; line:crosswalk (partial): Broad white pedestrian-crossing stripes
                        extend across the roadway beyond the stop line, with some stripes obscured by
                        vehicles.
Step 4  Cross-check     position: Lane lines and adjacent traffic space establish that my lane has another
                        lane on each side, but do not establish the total count or its exact index. | roles:
                        Both white boundaries fit separation of same-direction lanes; the oblique projections
                        on the left indicate variable guide-lane treatment. | markings: The stop line and
                        pedestrian crossing agree with an intersection approach. No readable lane-use arrow is
                        visible; a variable guide lane's direction must be obtained from its associated lane-
                        direction sign. | unseen: The lane-direction display cannot be read, the hood hides
                        the nearest pavement, and vehicles obscure portions of the approach; no hidden arrow
                        or permitted direction has been inferred. | result: consistent
Step 5  Rule            left_boundary: The projected guide-lane boundary indicates variable lane operation
                        whose direction is supplied by a variable lane-direction sign, rather than a pavement
                        arrow; its continuous boundary must not be crossed. [CN-6.10.1-4-V] "... The variable
                        guide lane line marks a guide lane whose direction can change as needed; it is placed
                        on intersection approaches. ... No guide arrows shall be "
Step 5  Rule            left_boundary: The solid white same-direction boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The visible solid white same-direction boundary prohibits crossing to
                        the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            line:stop_line: The transverse line identifies where to stop when required to yield or
                        wait, but does not by itself require a full stop on every approach. [CN-6.4.1-2] "The
                        stop line marks where vehicles stop when yielding or waiting to proceed. It is a solid
                        white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically governs pedestrian crossings; the
                        crossing identifies pedestrian space and does not independently determine the seven
                        requested actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The visible solid white right lane boundary prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     not_determined (contested, label allowed): Variable guide-lane operation is indicated,
                        but the lane-direction sign that determines its current movement cannot be read.
Step 6  turn_left       not_determined: The current direction of the variable guide lane cannot be read from
                        its associated sign.
Step 6  turn_right      not_determined: The current direction of the variable guide lane cannot be read from
                        its associated sign.
Step 6  u_turn          not_determined: The current direction of the variable guide lane cannot be read from
                        its associated sign.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: solid boundaries prohibit lateral crossing, while the unreadable variable-
                        lane direction leaves intersection movements undetermined; the stop line alone does
                        not impose stop_first.
Advice                  Stay between the solid boundaries and confirm the variable lane's current direction
                        from its lane-control sign before proceeding. Obey the applicable signal, stop before
                        the stop line when required, and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1356, 31.3 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban arterial has three lanes in this direction, with an intersection
                        approach in the distance. My car is in the middle lane; a barrier separates opposing
                        traffic on the left. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One same-direction lane on each side agrees with three lanes total and ego
                        lane index 2. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No guidance marking within my lane is sufficiently clear to
                        identify; distant pavement details cannot be reliably read. | unseen: No distant
                        arrow, stop line, or waiting area has been inferred from the signs or surrounding
                        lanes. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No identifiable pavement arrow restricts continuing
                        straight along the visible lane.
Step 6  turn_left       not_determined: The distant intersection-end pavement markings are too small to
                        determine whether this lane permits a left turn.
Step 6  turn_right      not_determined: The distant intersection-end pavement markings are too small to
                        determine whether this lane permits a right turn.
Step 6  u_turn          not_determined: The distant intersection-end pavement markings are too small to
                        determine whether this lane permits a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may continue along this lane or change lanes across the visible broken lines when
                        safe. Confirm the pavement arrows closer to the intersection before selecting a
                        turning lane, and obey the approach signs and signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 943, 17.89 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban arterial approaches a distant intersection. My car is in the middle of
                        three lanes in this direction, with opposing traffic beyond the median barrier. (lanes
                        3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; the roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white straight-ahead arrow is visible farther ahead
                        in my lane; distance limits its detail.
Step 4  Cross-check     position: Lane lines on both sides agree with my position as lane 2 of 3. | roles:
                        Both white broken boundaries fit separators between same-direction lanes. | markings:
                        The visible straight-ahead arrow agrees with a through lane bounded by crossable lane
                        lines. | unseen: The intersection pavement and lane end are too distant and partly
                        obscured by vehicles to inventory additional markings or a stop line reliably. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits straight travel from this lane
                        rather than left, right or U-turn movements. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          identifiable.
Step 7  Reflect         Consistent: the broken boundaries govern lane changes, while the identifiable
                        straight-ahead arrow governs intersection movements; no unseen stop requirement is
                        inferred.
Advice                  Remain in this lane to continue straight; change lanes only while the broken boundary
                        continues and traffic permits. For another movement, select the appropriately signed
                        and marked lane in advance, and obey the intersection signals and any stop line as
                        they become visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1067, 20.63 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban arterial approaches an intersection. My car is in a through lane, with
                        two apparent motor-vehicle lanes to its left and one to its right; the far-right
                        roadway layout is less clear. (lanes 4, mine 3, partial)
Step 2  Left            A continuous white line borders my lane on the left, with repeated short white teeth
                        projecting toward the adjacent lane; another same-direction lane lies beyond, with no
                        curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with repeated short white teeth
                        projecting toward the adjacent lane; pavement and another same-direction lane lie
                        beyond, rather than a curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A small white arrow farther ahead in my lane has a forward-
                        pointing head and no visible turning branch.
Step 4  Cross-check     position: Same-direction lanes on both sides agree with an interior ego lane; the
                        apparent position is third from the left, although the far-right lane count is less
                        certain. | roles: The white continuous boundaries fit same-direction lane separators
                        that prohibit crossing; their short lateral teeth do not make the longitudinal lines
                        broken. | markings: The straight arrow agrees with continuing between the two
                        boundaries. Text and other markings in adjacent lanes do not govern my lane. | unseen:
                        The distant intersection surface is not clear enough to identify a stop line or other
                        transverse markings; none are asserted. The function of the outward teeth is not
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white same-direction lane boundary prohibits my car from
                        crossing left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white same-direction lane boundary prohibits my car from
                        crossing right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (contested, label allowed): The solid white lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (contested, label allowed): The solid white lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane without crossing either solid boundary. For another
                        movement, select an appropriately marked lane where lane changes are permitted; obey
                        the intersection signals and stop at the stop line when required.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1361, 32.45 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad, divided urban road approaches an intersection beyond the traffic ahead. My
                        car is in a through lane, with one lane to its right; glare makes the total number of
                        lanes on the left uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A broken white line, with visible painted segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from
                        the rightmost traffic lane; the yellow-painted roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead, with no turning branch.
Step 4  Cross-check     position: Same-direction lanes are visible on both sides, consistent with both
                        boundaries being lane lines. My lane is second from the right, but glare prevents a
                        confident total lane count and left-based index. | roles: Both white broken boundaries
                        fit crossable same-direction lane lines. | markings: The straight-only arrow agrees
                        with a through lane between two ordinary traffic lanes; the straight/right arrow is in
                        the adjacent right lane, not mine. | unseen: No stop line or waiting area can be
                        identified ahead through the traffic, and none is inferred. The uncertain far-left
                        lane layout is not assigned a count. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible marked waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: the broken boundaries govern only lane changes, and the straight-only
                        arrow governs the intersection movements.
Advice                  Stay in this lane to continue straight. For a right turn, move safely into the
                        adjacent straight/right lane while its boundary remains broken; for other turns, find
                        the appropriate marked lane, and obey the intersection signals and stopping position
                        when visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1461, 37.65 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban arterial continues straight beneath traffic signals, with opposing
                        traffic behind a median fence on the left. My car is in the second lane from the left;
                        a further traffic lane and a bus-occupied outer lane lie to the right. (lanes 4, mine
                        2, partial)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, visible in the foreground and again ahead, separates my lane from
                        the lane occupied by the yellow taxi; the bus is farther right, and no curb forms my
                        lane's boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My position as lane 2 agrees with a same-direction lane on each side; the
                        outermost right-hand extent is partly hidden by the bus, making the total lane count
                        less certain. | roles: Both white broken boundaries fit ordinary same-direction lane
                        separators. | markings: No readable guidance marking appears within my lane; markings
                        farther right do not govern my lane. | unseen: No arrows, stop lines or waiting areas
                        are inferred from the distant or vehicle-obscured pavement. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane separator permits crossing to
                        change left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white same-direction lane separator permits crossing into
                        the immediately adjacent lane on the right when safe. [CN-5.2.1-2] "The crossable lane
                        line separates traffic flows in the same direction and is placed between lanes of the
                        same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label not_determined): The nearest right boundary is a broken white
                        lane line permitting crossing under CN-5.2.1-2; the bus-occupied outer lane is not
                        immediately adjacent.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking in view governs this action.
Step 6  turn_right      not_applicable: No marking in view governs this action.
Step 6  u_turn          not_applicable: No marking in view governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change across either broken white boundary only
                        after checking surrounding traffic. The forward signal is green, but this image does
                        not establish turn permissions or a stopping position at the next intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1056, 24.15 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban two-way road curves gently left, with a distant junction ahead. My car
                        is in the leftmost of three visible lanes in its direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid yellow line curves ahead on the left, with opposing-direction roadway
                        beyond it and no curb along the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line makes my lane the leftmost lane of my direction, and
                        the broken white boundary confirms another same-direction lane on the right. | roles:
                        The solid yellow centre line and broken white same-direction lane line fit their
                        assigned roles. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are discernible in my lane. | unseen: No distant intersection markings
                        or hidden markings beneath vehicles are inferred. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow centre line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The broken white lane line permits my car to cross into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid yellow centre line prohibits crossing under CN-6.1.4.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane; the
                        centre line does not govern this movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along the curve without crossing the solid yellow line; a rightward lane
                        change is permitted after checking traffic, especially the scooter to the right.
                        Choose any turning lane using clearer guidance closer to the junction and obey its
                        signs and signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1011, 23.68 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined multilane road continues straight ahead, with no visible
                        intersection, ramp or lane ending. My car is in the second of five travel lanes
                        counted from the left; an emergency shoulder lies beyond the rightmost lane. (lanes 5,
                        mine 2, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another travel lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long dashes and gaps, separates my lane from
                        another travel lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Large white Chinese pavement lettering occupies the foreground
                        of my lane, but the hood and lower image limit obscure part of the inscription, so the
                        complete wording cannot be read.
Step 4  Cross-check     position: The second lane of five has another same-direction lane on each side,
                        consistent with both boundaries being lane lines. | roles: Both boundaries are broken
                        white lines, consistent with crossable same-direction lane separators. | markings: The
                        partially visible pavement text does not establish a directional restriction; no
                        identifiable lane-use arrow or waiting area is visible. | unseen: The obscured
                        pavement wording has not been completed or treated as an arrow, and no unseen
                        intersection markings are assumed. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            text:other: This passage describes pavement text presentation; the incompletely
                        readable inscription establishes no restriction on the seven assessed actions.
                        [CN-5.14.1] "Pavement text markings are generally white. They are arranged vertically
                        and read from near to far along the direction of travel ... or horizontally from left
                        t"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across the broken
                        white line after checking traffic and clearance. Follow the overhead lane and speed
                        signs, and do not treat the emergency shoulder as a travel lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 979, 16.57 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, elevated multilane road continues straight toward overhead signs, with
                        concrete barriers along both sides. My car is in the second of four lanes in this
                        direction; no intersection or lane ending is visible. (lanes 4, mine 2, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second lane of four has a same-direction lane to its left and two to its
                        right, consistent with lane-line boundaries on both sides. | roles: Both boundaries
                        are broken white lines, consistent with crossable same-direction lane separators. |
                        markings: No arrows, words, symbols or marked areas are visible in my lane; nothing
                        conflicts with the boundaries. | unseen: No unseen markings or lane-end restrictions
                        are inferred. The transverse bands across the foreground are bridge joints, not
                        guidance markings. | result: consistent
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
Step 6  go_straight     allowed (contested, correct): No arrow or other marking restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across the broken
                        white line when safe. Check the overhead signs for route guidance; no marked stopping
                        point or turning area is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1025, 21.42 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gpt-6.1-sol | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road has three lanes in this direction and a signalized intersection
                        in the distance. My car is in the middle lane, behind the dark sedan. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from the lane
                        occupied by the taxi; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from the rightmost
                        lane occupied by the scooter; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead
                        and no branching heads.
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: The straight-only arrow is consistent with the lane boundaries; no
                        conflicting word or marked area is visible in my lane. | unseen: No hidden markings
                        are inferred; the sedan obscures some pavement ahead and the distant intersection
                        markings cannot be read. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing to the left
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing to the
                        right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            arrow:straight: The straight-only guide arrow allows proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow indicates this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken boundary may be crossed when safe,
                        checking especially for the taxi and scooter. For a turn or U-turn, find an
                        appropriately designated lane rather than turning from this one; obey the signals
                        ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 874, 14.42 s
```
