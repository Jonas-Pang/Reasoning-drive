# Reasoning of lane run 20261116_004611_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward a distant
                        signalized intersection. My car is in the middle lane, with a marked bus lane to the
                        right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken yellow line, with visible long painted segments and gaps, separates my lane
                        from the lane bearing bus-use text on the right; there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane on
                        the left and a reserved lane on the right. | roles: The broken white left boundary
                        fits a crossable lane line. The yellow right boundary differs from the white bus-lane
                        line described in the supplied rule, but the adjacent bus-use text supports its
                        special-lane role rather than an opposing-traffic role. | markings: No guidance
                        marking is readable within my lane; the bus-use text belongs to the adjacent lane. |
                        unseen: The distant intersection approach is too small and affected by glare to
                        establish its lane arrows or transverse markings; none have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The adjacent bus lane is reserved against entry by an ordinary car,
                        despite its crossable-looking boundary and the observed color difference from the
                        rule's specification. [CN-6.9.1] "The bus lane line shows that vehicles other than
                        buses shall not enter the lane. It consists of a broken white line and white text. The
                        broken line has 5 m segm"
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label not_determined): The adjacent bus lane prohibits entry by
                        this ordinary car under CN-6.9.1.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant approach markings that would determine left-turn
                        permission cannot be read.
Step 6  turn_right      not_determined: The distant approach markings that would determine right-turn
                        permission cannot be read.
Step 6  u_turn          not_determined: The distant approach markings that would determine U-turn permission
                        cannot be read.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; a safe left lane change is permitted, but do not enter
                        the bus lane on the right. Reassess the intersection arrows, signs and signals when
                        closer, and stop at the designated line if required.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 10766, out 947, 16.85 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road continues toward a distant signalized intersection.
                        My car is in the second lane from the left; a further paved lane or reserved strip
                        lies to the right, but its designation is not readable. (lanes 3, mine 2, partial)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A yellow broken line with broad dashes and clear gaps separates my lane from a paved
                        strip on the right; no curb forms this immediate boundary, and the strip's designation
                        is not readable.
                        yellow dashed, curb no, unknown, evidence partial
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible at the bottom
                        of my lane, but its lower portion is hidden by the dashboard, so additional branches
                        cannot be checked.
Step 4  Cross-check     position: The left lane line establishes another same-direction lane to my left,
                        consistent with position 2; the apparent third lane's status remains uncertain. |
                        roles: The broken white left boundary fits a crossable same-direction lane line; the
                        yellow right boundary does not establish an ordinary same-direction lane line, so its
                        role is left unknown. | markings: The visible forward arrowhead supports straight
                        travel, but its concealed lower portion prevents excluding other permitted directions.
                        | unseen: No bus designation, additional arrow branch, stop line, or waiting area is
                        claimed; distant and dashboard-hidden markings cannot be fully inspected. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: A broken longitudinal line is crossable in general, but this does not
                        resolve whether the space beyond is reserved or otherwise restricted. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, while the
                        hidden remainder leaves any additional permitted movements unresolved. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    not_determined (correct): The line is broken, but the unreadable designation of the
                        right-hand strip leaves entry restrictions unresolved.
Step 6  go_straight     allowed (contested, correct): The visible straight arrowhead permits continuing
                        straight under CN-5.13.1.
Step 6  turn_left       not_determined: The arrow's lower portion is hidden, so a possible left branch cannot
                        be checked.
Step 6  turn_right      not_determined: The arrow's lower portion is hidden, so a possible right branch cannot
                        be checked.
Step 6  u_turn          not_determined: The partially hidden arrow does not provide enough evidence to
                        establish its complete movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; a safe left lane change is permitted by the broken
                        white line. Avoid entering the right-hand strip until its designation is clear, and
                        verify the complete arrows and intersection controls before attempting any turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1167, 22.77 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with three lanes in this direction and
                        a fenced median on the left. My car is in the middle lane; the rightmost lane is
                        identified as a bus lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the
                        rightmost lane, where pavement text and a roadside bus-lane sign identify a bus lane;
                        there is no curb on this boundary.
                        white dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane on each side, including the
                        bus lane on the right. | roles: The broken white left boundary fits a crossable same-
                        direction lane line; the broken white right boundary fits a bus-lane boundary. |
                        markings: No guidance marking is readable in my lane; the bus-lane pavement text lies
                        to its right. | unseen: No unseen arrow or intersection marking is inferred; the
                        distant roadway is partly obscured by traffic. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing left when safe.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The bus-lane boundary prohibits this ordinary car from entering the
                        reserved lane despite its broken pattern. [CN-6.9.1] "The bus lane line shows that
                        vehicles other than buses shall not enter the lane. It consists of a broken white line
                        and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The adjacent bus lane is reserved, so CN-6.9.1
                        prohibits entering it.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the middle lane, or change left across the broken line when safe;
                        do not enter the reserved bus lane on the right. The bus-lane sign displays
                        06:00–22:00; reassess turn guidance when approaching the next intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 866, 12.71 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight beside an elevated structure on the right; no
                        intersection or lane ending is visible. My car is in the leftmost of three same-
                        direction lanes, alongside a raised median fence. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs beside a raised concrete median supporting a metal
                        fence, with opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right lane divider agree with my lane being the
                        leftmost of three same-direction lanes. | roles: The broken white right boundary fits
                        a same-direction lane divider. The left paint is visibly white despite its left-edge
                        location; the physical median establishes its edge role, so it is not relabelled
                        yellow. | markings: No guidance markings are visible within my lane; the irregular
                        pale pavement seam is not a lane-use marking. | unseen: No intersection layout or
                        markings beyond the visible road stretch are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, and a raised median also physically bounds this side. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action; the left boundary governs crossing it, not an unseen intersection movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line after
                        checking traffic and blind spots. Do not cross the solid left edge or median; turn-
                        lane selection cannot be established from this view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 904, 16.02 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A straight urban divided road runs beside an elevated structure and construction
                        fencing. My car is in the leftmost lane; no intersection or lane ending is visible
                        ahead, and vehicles obscure some of the roadway to the right. (lanes None, mine 1,
                        partial)
Step 2  Left            A continuous solid white line runs beside a raised concrete edge topped by a metal
                        fence, with construction screening beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane occupied by vehicles.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The physical left edge establishes that my lane is leftmost, and the right
                        lane line establishes at least one additional same-direction lane; the total count is
                        uncertain. | roles: The broken white right boundary fits a same-direction lane
                        divider. The left line is visibly white despite being at the left roadway edge; its
                        edge role follows the adjacent physical barrier, not an assumed paint color. |
                        markings: No guidance arrows, words, symbols, transverse lines or marked waiting areas
                        are identifiable in my visible lane. | unseen: The total lane count and any
                        intersection beyond the visible road are not inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line prohibits ordinary crossing to the left,
                        where a raised physical edge also blocks departure. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits changing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid white boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a raised fenced edge lies beyond.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the solid left boundary or approach the
                        fenced edge. A right lane change is permitted by the markings, but wait for a safe gap
                        around the nearby vehicles.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 924, 16.82 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a planted median on the left and
                        shops and roadside vehicles on the right. My car is in the middle of three same-
                        direction lanes; no intersection or lane ending is clearly visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with visible painted segments and intervening gaps, separates my
                        lane from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from another same-direction lane on the right;
                        segments and gaps are visible, although scooters obscure part of its continuation, and
                        there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both boundaries are broken white lines, consistent with separators between same-
                        direction lanes. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are discernible in my lane. | unseen: Vehicles obscure portions of the
                        road ahead; no markings or intersection layout are inferred beneath or beyond them. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to surrounding traffic.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the broken boundaries permit lane changes, while no unseen intersection
                        movements or markings have been inferred.
Advice                  Continue straight in this lane; either dashed boundary may be crossed only after
                        checking that the adjacent lane is clear. Be especially cautious of the scooters on
                        the right, and reassess turn guidance when an intersection becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 890, 15.08 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues toward a pedestrian overpass; no intersection or lane
                        end is clearly visible. My car is in the middle of three same-direction lanes, with a
                        marked bus lane on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single yellow broken line, with long painted segments and clear gaps, separates my
                        lane from a lane carrying white bus-lane text on the right; there is no curb at this
                        boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The ordinary lane on the left and reserved lane on the right agree with my
                        position as lane 2 of 3. | roles: The broken white left boundary fits a crossable
                        same-direction lane line. The yellow right boundary is unusual for a same-direction
                        bus-lane boundary, but the bus-lane text beyond it identifies the reserved lane; its
                        observed color is retained. | markings: No guidance marking is clearly visible in my
                        own lane; the bus-lane text is outside it. | unseen: The vehicle ahead obscures some
                        pavement, and distant markings and the eventual intersection approach cannot be read;
                        no hidden arrow or stop line is inferred. | result: Consistent, with the nonstandard
                        color of the bus-lane boundary explicitly noted.
Step 5  Rule            left_boundary: The broken white same-direction lane line permits changing left when
                        safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The bus-lane restriction prohibits an ordinary car from entering the
                        reserved lane on the right, despite its broken boundary and nonstandard yellow color.
                        [CN-6.9.1] "The bus lane line shows that vehicles other than buses shall not enter the
                        lane. It consists of a broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): The adjacent bus lane is reserved, so CN-6.9.1
                        prohibits entering it.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the reserved-lane rule overrides the crossability of its broken boundary,
                        and no intersection movement permission is inferred from unseen markings.
Advice                  Continue in this lane or change left only when safe; do not enter the bus lane on the
                        right. Reassess turn permissions when the intersection approach and its markings
                        become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 945, 16.71 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight beside an elevated roadway on the left. My
                        car is in the middle of three visible same-direction lanes; no intersection or lane
                        ending is discernible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long segments and gaps separates my lane from the
                        lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane containing the white car on the
                        right; its farther portions are partly obscured by traffic, and there is no curb at
                        this boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with my lane being lane 2 of 3. |
                        roles: The white broken boundaries fit same-direction lane separators. | markings: No
                        readable guidance marking is visible in my lane, so none contradicts the boundaries. |
                        unseen: No distant intersection markings or reserved-lane status are inferred; traffic
                        obscures portions of the right boundary and the distant roadway. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The visible broken white same-direction lane line permits crossing
                        into the lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either visible broken boundary permits a lane change,
                        but check surrounding traffic, especially the white car on the right. No visible
                        intersection markings establish a turning lane or stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 851, 13.8 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues toward an overpass, with no intersection or lane ending
                        visible. My car is in the leftmost of two lanes in its direction, beside a broken
                        yellow line separating the opposing side. (lanes 2, mine 1, full)
Step 2  Left            A single yellow broken line, with several visible dashes and gaps, runs along my left;
                        pavement continues beyond it toward a raised roadside edge and guardrail.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A single white broken line, with clear long dashes and gaps, separates my lane from
                        another traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line makes my lane the leftmost in its direction, and the
                        white lane line separates it from the second lane on the right. | roles: The broken
                        yellow centre line and broken white same-direction lane line fit their assigned roles.
                        | markings: No guidance markings are visible inside my lane; markings beyond its
                        boundaries do not govern its movements. | unseen: No intersection layout or markings
                        beyond the visible road have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken yellow centre line may be crossed to overtake, turn or make
                        a U-turn only when doing so does not affect safety. [CN-5.1.1] "The crossable centre
                        line separates traffic flows in opposite directions. It means vehicles may cross the
                        line to overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (contested, label prohibited): CN-5.1.1 permits crossing the broken yellow
                        centre line when safe, but this enters the opposing side rather than another same-
                        direction lane.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow or other marking restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        movement at its end; the centre line governs only crossing the left boundary.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or move right across the broken white line when safe.
                        Crossing left would enter the opposing side and requires a clear, safe opportunity; no
                        intersection turning guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1066, 21.77 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a fenced median on the left and a
                        reserved bus lane on the right. My car is in the middle of three lanes in this
                        direction; no intersection stop line or lane ending is visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken yellow line with multiple visible dashes and gaps separates my lane from the
                        right-hand lane, which has large white pavement text and a roadside bus-lane sign;
                        there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three same-direction lanes agrees with a lane
                        boundary on each side. | roles: The broken white left boundary fits a crossable lane
                        line. The right boundary is visibly yellow, unlike the white bus-lane line specified
                        in the supplied passage; the adjacent bus-lane sign and pavement text identify its
                        reserved-lane role without changing the observed color. | markings: No guidance
                        marking is visible within my lane; the large white text is beyond my right boundary
                        and belongs to the adjacent lane. | unseen: No distant arrow, stop line, or
                        intersection layout has been inferred; the road farther ahead is partly obscured by
                        vehicles and distance. | result: Consistent, with the right boundary's observed yellow
                        color retained despite its difference from the supplied bus-lane specification.
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on my left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The adjacent lane is identified as a reserved bus lane, so my ordinary
                        car must not enter it despite the broken boundary and its nonstandard yellow color.
                        [CN-6.9.1] "The bus lane line shows that vehicles other than buses shall not enter the
                        lane. It consists of a broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): The adjacent reserved bus lane prohibits entry by my
                        ordinary car under CN-6.9.1.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking in my lane restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the reserved-lane restriction overrides the apparent crossability of the
                        right boundary, and no adjacent-lane text is used to restrict movements from my lane.
Advice                  Continue in this lane, or change left across the broken white line only when safe; do
                        not enter the bus lane on the right. Its sign displays reservation periods of
                        7:00–9:00 and 16:00–19:00, but this assessment treats it as reserved; reassess turn
                        options when intersection markings become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 980, 17.08 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road with opposing traffic separated by a metal median fence; my car is in
                        the leftmost lane behind an SUV. Three same-direction lanes are visible, including a
                        marked bus lane at the far right; the next intersection is not clearly visible. (lanes
                        3, mine 1, full)
Step 2  Left            A raised median edge and metal fence run along the left, with opposing traffic beyond;
                        glare prevents reliable identification of any paint beside the median.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with visible segments and gaps, separates my lane from another
                        same-direction lane; there is no curb along this line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median on the left and a same-direction lane line on the right agree
                        with being lane 1 of 3. | roles: The broken white right boundary fits a same-direction
                        lane separator; the physical median defines the left roadway edge, but its paint
                        cannot be assessed. | markings: No guidance marking can be read in my lane; the bus-
                        lane text farther right is outside it. | unseen: No hidden paint color or arrow is
                        inferred. Glare and the SUV obscure portions of my lane, and the intersection approach
                        is not readable. | result: consistent
Step 5  Rule            left_boundary: No supplied passage directly governs crossing this physical median
                        barrier; its physical boundary prohibits moving left across it.
Step 5  Rule            right_boundary: The broken white same-direction lane line permits changing into the
                        adjacent ordinary lane when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     prohibited (correct): The raised median and fence form a physical boundary that cannot
                        be crossed.
Step 6  change_right    allowed (correct): CN-5.2.1-2 permits crossing the broken white lane separator into
                        the adjacent ordinary lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The intersection approach and any movement arrows there are obscured
                        or too distant to read.
Step 6  turn_right      not_determined: The intersection approach and any movement arrows there are obscured
                        or too distant to read.
Step 6  u_turn          not_determined: The intersection approach and any movement restrictions there cannot
                        be read.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or cross the broken white line into the adjacent ordinary lane
                        only when safe; do not cross the median or enter the far-right reserved bus lane.
                        Reduce speed for the glare and check the intersection arrows, signs and signals before
                        selecting a turning lane.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 952, 16.83 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues toward an overpass, with no intersection or lane
                        ending visible. My car is in the leftmost of three lanes in this direction. (lanes 3,
                        mine 1, full)
Step 2  Left            A continuous white line borders the narrow left shoulder, with orange broken segments
                        immediately alongside it on the lane side; a concrete median barrier lies beyond the
                        shoulder.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           An orange broken line, with clearly visible dashes and gaps, separates my lane from
                        another lane travelling in the same direction; there is no curb at this boundary.
                        other dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being the first of three same-direction lanes. | roles: The orange broken right
                        boundary is consistent with temporary lane guidance. The white solid left edge is
                        visibly white, despite the prescribed yellow colour for a left edge; the orange
                        segments beside it are recorded without treating the two different-coloured markings
                        as a standard broken-solid pair. | markings: No readable arrows, words, symbols,
                        transverse lines or waiting areas are visible in my lane. | unseen: No pavement bus
                        designation or lane-use arrow is inferred from the roadside bus-lane sign. The distant
                        roadway beyond the overpass is not resolved. | result: consistent
Step 5  Rule            left_boundary: The continuous white edge line normally prohibits crossing to the left
                        shoulder. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            left_boundary: The adjacent orange segments provide temporary guidance, but do not
                        clearly establish permission to cross the continuous white edge. [CN-4.3.2-c] "c)
                        Orange markings: temporary guidance in work zones."
Step 5  Rule            right_boundary: The orange boundary denotes temporary guidance. [CN-4.3.2-c] "c)
                        Orange markings: temporary guidance in work zones."
Step 5  Rule            right_boundary: The broken right boundary permits crossing into the adjoining lane
                        when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 6  change_left     prohibited (contested, correct): Crossing the continuous left edge line is normally
                        prohibited by CN-4.2.2-a.
Step 6  change_right    allowed (WRONG, label prohibited): The orange broken right boundary permits crossing
                        under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  The pavement markings permit continuing straight or changing right when safe; do not
                        cross the solid left edge onto the shoulder. The roadside sign indicates a weekday
                        bus-lane restriction from 17:00–19:00, so check whether it applies now and leave this
                        lane to the right if required.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 10766, out 1054, 19.63 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight beneath a pedestrian footbridge, with no
                        intersection or lane ending visible. My car is in the middle of three same-direction
                        lanes; the lane on the right is marked for buses. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with clearly visible long segments and gaps, separates my lane
                        from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken line with pale white foreground segments and yellow-looking portions farther
                        ahead separates my lane from a lane containing bus text and a bus; no curb forms this
                        boundary.
                        white dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane on
                        the left and a bus lane on the right. | roles: The broken white left line fits a
                        crossable lane divider. The broken right boundary and adjacent bus text support a bus-
                        lane boundary, although its colour is not uniform enough in the image to establish
                        confidently throughout. | markings: No guidance marking is visible inside my lane; the
                        bus text belongs to the adjacent right lane. | unseen: No arrow, stop line, waiting
                        area or intersection is inferred beyond the visible road; uncertainty in the right
                        boundary's colour is retained. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The adjacent bus lane is reserved, so my ordinary car may not enter it
                        despite the broken boundary. [CN-6.9.1] "The bus lane line shows that vehicles other
                        than buses shall not enter the lane. It consists of a broken white line and white
                        text. The broken line has 5 m segm"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): The adjacent lane is a reserved bus lane, which an
                        ordinary car may not enter under CN-6.9.1.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight, and my
                        lane does not visibly end.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the bus-lane restriction overrides the crossability of its broken
                        boundary, and no intersection movement is inferred from unseen markings.
Advice                  Continue straight in this lane, or change left when safe; do not enter the bus lane on
                        the right. The roadside bus sign displays operating times, but the adjacent lane is
                        treated as reserved for this assessment.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 933, 15.52 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow branch roadway curving gently right, separated from the main
                        carriageway by a painted gore and a raised planted island. One motor-vehicle lane is
                        visible on this branch, with a strip used by bicycles and scooters beside the shops on
                        the right; its eventual junction is not visible. (lanes 1, mine 1, full)
Step 2  Left            A solid white line borders the painted diagonal-striped gore on the left and leads
                        toward a raised island curb; yellow paint is also visible along the island-side edge.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the paved strip beside the shops, with
                        short yellow painted segments running alongside it on my side; no curb stands at this
                        line.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane between two roadway edges agrees with the car being
                        in lane 1; the main carriageway beyond the island is separate. | roles: The white
                        right boundary fits motor/non-motor separation, and the white left line outlines the
                        gore before the island; the additional yellow segments are visible but their purpose
                        is unclear. | markings: No readable arrow, word, symbol, transverse line or waiting
                        area is visible within my lane; the diagonal hatching is outside its left boundary. |
                        unseen: No destination or movement arrow is inferred from the roadside sign, and no
                        marking is inferred beyond the visible curve. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary prohibits ordinary crossing to the
                        left, where the gore and then the raised island lie. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white longitudinal boundary prohibits ordinary
                        crossing into the roadside strip. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left boundary prohibits crossing
                        under CN-4.2.2-a, and a raised island lies beyond it.
Step 6  change_right    prohibited (WRONG, label not_determined): The continuous white right boundary
                        prohibits crossing under CN-4.2.2-a; the unclear yellow segments do not remove that
                        restriction.
Step 6  go_straight     allowed (contested, correct): No visible in-lane arrow restricts continuing along this
                        curving lane.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the solid boundaries govern only crossing them, continuing means following
                        the lane's curve, and roadside signs have not been treated as pavement arrows.
Advice                  Follow the branch around the island without crossing either solid boundary, watching
                        for scooters and cyclists. The roadside sign indicates right-turn routing, but the
                        eventual junction and its pavement guidance are not visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1085, 23.8 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight beneath a pedestrian overpass, with
                        traffic ahead and no visible intersection or lane ending. My car is in the rightmost
                        of three lanes in this direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved shoulder and
                        a guardrail farther beyond it; no curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 3 agree with a same-direction lane on the
                        left and the roadway edge on the right. | roles: The broken white left line fits a
                        crossable lane divider, and the solid white right line fits the right carriageway
                        edge. | markings: No guidance markings are visible on the pavement in my lane; the
                        overhead arrows are signs, not pavement markings. | unseen: No markings are inferred
                        beneath vehicles or beyond the visible road stretch. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        adjacent lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows
                        in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane line permits crossing
                        under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge line normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this through lane, or change left across the broken line only when safe;
                        do not cross the solid right edge onto the shoulder in normal driving. Maintain a safe
                        following distance and observe the overhead lane and speed signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 856, 13.05 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signalized intersection. My car is in the rightmost
                        of three same-direction lanes, behind an SUV, with a raised verge and a separate non-
                        motorized path on the right. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from another same-direction lane on the left;
                        visible painted segments and gaps are partly crossed by shadows, and there is no curb
                        on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane beside a raised curb and
                        planted verge, beyond which is a separate paved path.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): A white longitudinal marking resembling the shaft of a
                        guidance arrow is visible immediately behind the SUV, but its head and any branches
                        are hidden, so its directional meaning cannot be read.
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge on the right. | roles: The broken white left boundary fits a
                        crossable lane line; the solid white right boundary and curb fit the right roadway
                        edge. | markings: The partially visible pavement marking cannot establish permitted
                        intersection movements; arrows visible in neighboring lanes do not govern my lane. |
                        unseen: No arrowhead, branches, stop line, crosswalk, or waiting area are asserted
                        behind the SUV or in the obscured intersection approach. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane boundary permits changing left
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing right, and the
                        raised curb also prevents an ordinary lane-change path. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            symbol:other: No passage assigns a directional meaning to this unreadable fragment; if
                        it is a guide arrow, its hidden heads must be seen before its permitted movements can
                        be determined.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2,
                        subject to safety.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a, with a raised curb beyond it.
Step 6  go_straight     not_determined (contested, label allowed): The SUV hides the head of an apparent
                        guidance marking that could restrict this movement.
Step 6  turn_left       not_determined: The apparent guidance marking's hidden head and branches leave
                        permission for a left turn undecided.
Step 6  turn_right      not_determined: The apparent guidance marking's hidden head and branches leave
                        permission for a right turn undecided.
Step 6  u_turn          not_determined: The apparent guidance marking's hidden head and branches leave
                        permission for a U-turn undecided.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Keep clear of the right curb; a left lane change is permitted across the visible
                        broken line only when safe. Leave enough distance to read the marking hidden by the
                        SUV before choosing an intersection movement, and obey the traffic signals and any
                        stop line revealed ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1226, 25.75 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the rightmost motor-vehicle lane; vehicles obscure the full
                        extent of the lanes to the left. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line separates my lane from another same-direction lane on the left;
                        there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right edge of my lane beside a raised curb and planted
                        strip, with a separate paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow with one forward-pointing head is painted
                        immediately ahead of my car.; line:stop_line (full): A transverse solid white stop
                        line crosses my lane beyond the arrow, before the pedestrian crossing.; line:crosswalk
                        (partial): White zebra-crossing stripes extend across my lane beyond the stop line,
                        partly obscured by the vehicle ahead.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, and the
                        right edge and curb establish that my lane is rightmost; the total count and numerical
                        index remain obscured. | roles: The solid white separator fits a same-direction lane
                        line, and the solid white line beside the curb fits the right roadway edge. |
                        markings: The straight arrow agrees with an intersection approach lane bounded by
                        solid lines; the stop line and pedestrian crossing do not contradict it. | unseen: No
                        total lane count or concealed marking is inferred; the crossing's occlusion is
                        recorded. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing to change left. [CN-6.2.1]
                        "The no-crossing lane line separates vehicles travelling in the same direction and
                        prohibits vehicles on the solid-line side from crossing. It has two forms: sin"
Step 5  Rule            right_boundary: The solid right boundary prohibits ordinary crossing, and the visible
                        curb is a physical edge rather than an available lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits straight travel and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not itself require an unconditional stop. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing; it
                        does not independently determine any of the seven actions.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a curb lies alongside it.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, obeying the traffic signal and watching for
                        pedestrians at the crossing. Do not cross either solid boundary; if required to stop,
                        stop before the white stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1152, 16.44 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road with queued traffic; my car is in the middle lane behind a dark
                        sedan. The lane continues ahead, but traffic obscures its distant markings and any
                        intersection approach. (lanes 3, mine 2, full)
Step 2  Left            A single continuous white line separates my lane from the lane containing the white
                        Tesla on the left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders a narrow strip of white diagonal channelizing
                        markings, with another continuous white outline and a traffic lane beyond; there is no
                        curb at this boundary.
                        white solid, curb no, other, evidence full
Step 3  Markings        area:channelizing (full): A narrow white diagonally hatched channelizing strip runs
                        immediately along the right boundary; its nearer portion is clearly visible.
Step 4  Cross-check     position: The lane to my left and the lane beyond the channelizing strip to my right
                        agree with three same-direction lanes and my position as lane 2. | roles: The solid
                        white left lane line separates same-direction traffic; the right solid white outline
                        belongs to a channelizing strip rather than an ordinary dashed lane separator. |
                        markings: The channelizing strip agrees with its solid outline. No lane-use arrow,
                        word, stop line or waiting area is readable in my lane. | unseen: The sedan hides
                        pavement ahead, so absence of distant arrows or transverse markings cannot be
                        established. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The channelizing outline prohibits my car from crossing into or
                        through the hatched strip on the right. [CN-6.6.1-3] "Channelizing lines show that
                        vehicles must follow the set path and may not drive on or across the lines. ...
                        Channelizing lines separating traffic in the same d"
Step 5  Rule            area:channelizing: My car must follow the defined path and must not drive on or across
                        the channelizing markings. [CN-6.6.1-3] "Channelizing lines show that vehicles must
                        follow the set path and may not drive on or across the lines. ... Channelizing lines
                        separating traffic in the same d"
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid-outlined channelizing strip prohibits crossing under
                        CN-6.6.1-3.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        the existing lane; its side boundaries do not prohibit this.
Step 6  turn_left       not_determined: Traffic obscures the distant lane pavement where a governing turn
                        arrow could appear.
Step 6  turn_right      not_determined: Traffic obscures the distant lane pavement where a governing turn
                        arrow could appear.
Step 6  u_turn          not_determined: Traffic obscures the distant lane pavement where a governing arrow or
                        prohibition could appear.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight means continuing along the visible lane, not confirmed permission
                        for a movement at an obscured intersection.
Advice                  Stay within the solid boundaries and keep off the hatched strip. Follow the queue
                        cautiously and reassess turn permissions and any stopping requirement when the hidden
                        pavement and intersection controls become visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1104, 23.14 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. There are four
                        lanes in this direction, and my car is in the second lane from the left. (lanes 4,
                        mine 2, full)
Step 2  Left            A single broken white line, with clearly visible dashes and gaps, separates my lane
                        from another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with clearly visible dashes and gaps, separates my lane
                        from another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): The nearer white arrow has one head pointing straight ahead.;
                        arrow:straight (full): A smaller white straight-ahead arrow is visible farther along
                        my lane.
Step 4  Cross-check     position: The second of four lanes has a same-direction lane immediately on each side,
                        consistent with both boundaries being lane lines. | roles: Both boundaries are broken
                        white lines, consistent with crossable same-direction lane dividers. | markings: The
                        two straight-ahead arrows agree; the turning arrows in neighboring lanes do not apply
                        to my lane. | unseen: No distant stop line or crosswalk is identified because the
                        intersection pavement is too far away to resolve reliably. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The nearer straight-ahead arrow permits straight travel and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The farther straight-ahead arrow repeats the restriction to straight
                        travel. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): Both arrows indicate straight travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signals. For a turn,
                        move safely across the broken divider into the appropriately marked lane before the
                        intersection; do not turn directly from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1031, 14.63 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. My car is in
                        the second of four lanes travelling in this direction. (lanes 4, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another traffic lane on the left;
                        there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another traffic lane on the right;
                        there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow has one head pointing straight ahead.;
                        arrow:straight (full): A second, smaller-looking white straight-ahead arrow is visible
                        farther along my lane.; line:stop_line (partial): A transverse white line is visible
                        at the distant end of the approach, although its detail is limited by distance.
Step 4  Cross-check     position: Lane 2 of 4 has a same-direction lane immediately on each side, consistent
                        with both boundaries being lane lines. | roles: The solid white paint fits no-crossing
                        lane lines on an intersection approach. | markings: Both straight-ahead arrows agree,
                        and the solid boundaries keep vehicles within their selected approach lanes. | unseen:
                        No special-lane designation or waiting area is visible in my lane; distant transverse
                        marking detail is limited and is reported as partial. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is for
                        straight-ahead travel. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        without independently requiring a stop on every approach. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): Both straight-ahead arrows permit this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and proceed straight only when the traffic signal
                        permits. Do not change lanes here; if required to stop, stop before the transverse
                        stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1187, 19.36 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection. My car is in the
                        middle of three lanes travelling in this direction, behind a white SUV. (lanes 3, mine
                        2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower part of the arrow is hidden, so additional branches
                        cannot be checked.
Step 4  Cross-check     position: Lane lines on both sides agree with my position as lane 2 of 3. | roles:
                        Both solid white lines fit boundaries between same-direction lanes. | markings: The
                        visible forward arrowhead agrees with continuing along this lane; the turning arrow to
                        the left is outside my lane. | unseen: The hood hides the lower part of my arrow, and
                        vehicles obscure portions of the approach ahead; no hidden branches, stop line or
                        waiting area are asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on my left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on my
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the hidden
                        remainder prevents confirming whether any additional direction is indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (WRONG, label allowed): CN-6.2.1 prohibits crossing the solid white left
                        lane line.
Step 6  change_right    prohibited (WRONG, label allowed): CN-6.2.1 prohibits crossing the solid white right
                        lane line.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hood hides the part of the arrow where
                        an additional directional branch could appear.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hood hides the part of the arrow where
                        an additional directional branch could appear.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete arrow is not visible, so an
                        additional U-turn indication cannot be checked.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: both lane changes are prohibited, straight travel is supported by the
                        visible arrowhead, and additional arrow-directed movements remain undecided because
                        the arrow is partly hidden.
Advice                  Stay between the solid white lines and continue straight when the applicable signal
                        and traffic permit. Do not assume a turning movement is permitted without seeing the
                        complete lane arrow; keep clear of the vehicle ahead and stop at the intersection stop
                        line if required.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1013, 16.07 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches a signal-controlled intersection. My car is in the
                        leftmost of two lanes travelling in this direction, beside the median fence. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid yellow line runs beside a continuous median fence on the left, with opposing
                        traffic beyond the fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A large white combined arrow has one head pointing
                        straight ahead and another pointing left.
Step 4  Cross-check     position: The median edge on the left and a lane line on the right agree with being
                        lane 1 of 2. | roles: The yellow median-side edge and solid white same-direction lane
                        separator fit their assigned roles. | markings: The straight-and-left arrow is
                        consistent with an intersection approach lane bounded by solid lines. | unseen: The
                        vehicle ahead and distance obscure parts of the approach; no hidden stop line,
                        additional arrow, or waiting area is asserted. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line prohibits normal crossing to the left, and
                        the median fence also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight_left: The combined arrow permits proceeding straight or turning left,
                        but does not permit a right turn or U-turn. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): The solid yellow boundary prohibits normal crossing
                        under CN-4.2.2-a, and a median fence lies alongside it.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The combined arrow permits straight travel under CN-5.13.1.
Step 6  turn_left       allowed (correct): The combined arrow permits a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The combined arrow does not include a right turn.
Step 6  u_turn          prohibited (WRONG, label allowed): The combined arrow does not include a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight or turn left; do not cross either solid
                        boundary. Obey the intersection signals and stop at the applicable stop line when
                        required, allowing space behind the vehicle ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 952, 16.23 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the leftmost of two visible lanes in this direction, behind a
                        white SUV. (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs beside a metal median fence, with opposing traffic
                        beyond; the fence physically bounds this side of my lane.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another lane travelling in the same
                        direction, with no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white stopping line is partly visible beside
                        the SUV near the crossing; its middle is obscured.; line:crosswalk (partial): White
                        pedestrian-crossing stripes extend across the approach ahead, partly obscured by the
                        SUV.
Step 4  Cross-check     position: The median boundary on the left and the same-direction lane line on the
                        right agree with lane 1 of 2. | roles: The yellow median-side edge and solid white
                        same-direction separator fit their assigned roles. | markings: The stopping line and
                        crossing agree with an intersection approach; no lane-use arrow can be read in my
                        lane. | unseen: The SUV hides part of the lane near the intersection, including
                        pavement where a guidance arrow could be present; no hidden arrow or waiting area is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The solid yellow boundary normally prohibits crossing, and the median
                        fence also physically prevents a leftward departure. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white same-direction lane line prohibits crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            line:stop_line: The line identifies where to stop when yielding or waiting to proceed,
                        without independently requiring a stop on every approach. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers pedestrian-crossing markings,
                        and this marking does not independently decide any of the seven actions.
Step 6  change_left     prohibited (correct): The solid yellow boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence blocks departure.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined (contested, label allowed): No visible arrow restricts continuing
                        straight, but the SUV obscures the approach pavement that could contain a governing
                        arrow.
Step 6  turn_left       not_determined: A governing lane-use arrow cannot be established because the SUV
                        obscures part of the approach.
Step 6  turn_right      not_determined: A governing lane-use arrow cannot be established because the SUV
                        obscures part of the approach.
Step 6  u_turn          not_determined: A governing arrow or prohibited-movement marking cannot be established
                        on the obscured approach pavement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the solid boundaries and confirm your lane's permitted direction when the
                        obscured pavement becomes visible. Follow the traffic signals, keep the pedestrian
                        crossing clear, and stop before the stopping line when required.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1124, 19.72 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road approaches a split beneath Dashan Bridge. My car is in the rightmost
                        motor-vehicle lane, marked for a right turn, with a painted dividing island on its
                        left and a non-motorized strip on its right. (lanes 3, mine 3, full)
Step 2  Left            A solid white line forms the near edge of a narrow, tapered painted island leading
                        toward the bridge support; other same-direction motor lanes lie beyond it.
                        white solid, curb no, other, evidence full
Step 2  Right           A broken white line, with a long foreground segment and visible gaps between segments
                        farther ahead, separates my lane from the roadside strip used by a scooter; the raised
                        sidewalk curb is beyond that strip.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has a single head pointing right, with no
                        straight-ahead head.
Step 4  Cross-check     position: Three motor lanes and my position as the third agree with the other motor
                        lanes beyond the left dividing island and the non-motorized strip beyond the right
                        edge line. | roles: The solid white island outline separates same-direction paths; the
                        broken white right edge separates motor and non-motorized traffic travelling in the
                        same direction. | markings: The right-only arrow agrees with the path passing to the
                        right of the painted island and bridge support; arrows in the lanes to the left do not
                        govern my lane. | unseen: No stop line or waiting area is visible; details farther
                        beneath and beyond the bridge are obscured by shade and distance. | result: consistent
Step 5  Rule            left_boundary: The channelizing island outline requires my car to follow the
                        designated path without driving on or across it. [CN-6.6.1-3] "Channelizing lines show
                        that vehicles must follow the set path and may not drive on or across the lines. ...
                        Channelizing lines separating traffic in the same d"
Step 5  Rule            right_boundary: The broken right boundary may be crossed, although this does not
                        designate the non-motorized strip as an ordinary motor-vehicle travel lane.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            arrow:right: The single right-turn arrow permits a right turn and excludes straight,
                        left-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited: The solid channelizing island outline may not be crossed under CN-6.6.1-3.
Step 6  change_right    allowed: The broken white right boundary is crossable under CN-4.2.2-a; the space
                        beyond is a non-motorized strip.
Step 6  go_straight     prohibited (WRONG, label allowed): The right-only arrow does not show straight ahead
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The right-only arrow does not show a left turn under CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The right-only arrow does not show a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Follow this lane to the right without crossing the painted island; a straight-ahead
                        movement requires a different lane selected before the solid separation. Keep clear of
                        the scooter and pedestrians on the right, and observe the posted 4 m bridge clearance.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1264, 25.43 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection. My car is in the
                        leftmost of three visible lanes travelling in this direction, beside a median fence.
                        (lanes 3, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left side of my lane, with a narrow strip
                        and a physical median fence immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        the adjacent same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has a forward-pointing head and
                        a straight stem, with no visible turning branch.
Step 4  Cross-check     position: The left physical median edge and the same-direction lane on the right agree
                        with my lane being lane 1 of 3. | roles: The broken white right boundary fits a same-
                        direction lane line. The left boundary is visibly white despite being at the median-
                        side edge; its colour is reported as seen rather than inferred from its position. |
                        markings: The straight arrow is compatible with the continuing lane and its
                        boundaries; no conflicting guidance marking is readable. | unseen: The intersection
                        pavement is too distant to identify a stop line or other small markings reliably; none
                        has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the median fence also physically blocks that movement. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane and do not cross the median-side boundary. If you
                        need another movement, change right only when safe and select a lane with the
                        appropriate guidance; obey the intersection signals and stop at the stop line if
                        required.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1028, 18.17 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the leftmost of two visible motor-vehicle lanes in this
                        direction, beside the median fence. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane beside a physical median fence;
                        yellow paint is visible farther left beneath the fence, with opposing traffic beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another motor-vehicle lane on the right,
                        with no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow has a single forward-pointing head.;
                        line:stop_line (full): A transverse solid white stop line crosses my lane before the
                        pedestrian crossing.; line:crosswalk (full): White zebra-crossing stripes cross the
                        roadway immediately beyond the stop line.
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with lane 1 of 2. | roles: The right solid white line fits an intersection approach
                        lane line. The left line visibly appears white despite its left-edge position; the
                        median fence establishes its edge role, so its color is not relabeled yellow. |
                        markings: The straight-only arrow agrees with a through approach lane; the stop line
                        precedes the crosswalk. No waiting area is visible. | unseen: No hidden arrow heads,
                        reserved-lane designations, or waiting areas have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid boundary normally prohibits crossing, and the median fence
                        also physically prevents moving left. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent lane.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The single straight arrow permits straight travel and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not itself require an unconditional stop. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this pedestrian-
                        crossing marking does not determine any of the seven lane actions.
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies alongside it.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane when the signal and crossing conditions permit; do
                        not cross either solid boundary. If required to stop, stop before the stop line and
                        keep the pedestrian crossing clear; turning requires choosing an appropriate lane
                        earlier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1159, 18.19 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection with a pedestrian crossing.
                        My car is in the leftmost of three visible same-direction approach lanes, beside a
                        fenced central divider. (lanes 3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a narrow paved buffer, yellow
                        markings and a physical divider fence beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction approach lane
                        on the right; no curb separates these lanes.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow has one head pointing straight ahead.;
                        line:stop_line (full): A solid white transverse stop line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): White zebra-crossing stripes
                        span my lane beyond the stop line.
Step 4  Cross-check     position: The left roadway edge and the same-direction lane on the right agree with my
                        position as lane 1 of 3. | roles: The solid white right boundary fits an intersection
                        approach lane line. The left boundary is visibly white despite its position beside the
                        central divider; its edge role follows the physical layout, not an assumed yellow
                        colour. | markings: The straight-only arrow agrees with a bounded through approach
                        lane; the stop line precedes the crosswalk, and no left-turn waiting area is visible.
                        | unseen: No hidden arrow heads, reserved-lane markings or waiting areas have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: Crossing this solid longitudinal boundary is normally prohibited, and
                        the divider beyond it is not a usable lane. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits changing into the adjacent lane
                        across it. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The single straight arrow permits straight travel and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not independently require every vehicle to stop. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the zebra crossing; it
                        identifies pedestrian crossing space and does not determine the seven movement
                        permissions.
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a, with a divider fence beyond.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane only to proceed straight; do not cross either solid boundary to
                        reposition for a turn. Obey the applicable traffic signal, stop before the stop line
                        when required, and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1222, 19.77 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A two-way urban street with roadside buildings, bicycles and scooters; a yellow
                        crosshatched box covers an access area ahead. My car is in the single visible lane of
                        its direction near the bottom of the photo. (lanes 1, mine 1, full)
Step 2  Left            A single broken yellow line, with visible painted segments and gaps, separates my lane
                        from oncoming traffic; no curb forms this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A raised curb borders the right side, partly obscured by a scooter, with sidewalk and
                        bicycles beyond; no separate painted boundary is visible along the near stretch.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        area:grid (full): A yellow crosshatched box extends across my lane and the opposing
                        side at the access ahead.
Step 4  Cross-check     position: The centre line on the left and curb on the right agree with one lane of my
                        direction and my position as its leftmost lane. | roles: The broken yellow line fits
                        an opposing-traffic centre line; the curb forms the roadway edge without a visible
                        painted edge line. | markings: The crosshatched box does not indicate a turning
                        direction and does not conflict with either boundary. | unseen: No arrows, stop
                        markings or waiting areas are identified; the scooter obscures part of the right edge,
                        and distant markings are not used to infer additional near-field lanes. | result:
                        consistent
Step 5  Rule            left_boundary: My car may cross the broken centre line to overtake or manoeuvre only
                        when doing so does not affect safety. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: No supplied passage expressly regulates crossing a curb; as a physical
                        roadway boundary, it is not a permitted driving path.
Step 5  Rule            area:grid: The grid identifies an area that must be kept clear of stopping, although
                        its visible yellow colour differs from the white specified in the passage.
                        [CN-6.8.1-2] "The grid marking shows an area where stopping for any reason is
                        prohibited. It is placed at intersections and accesses that need emergency entry and
                        exit but ca"
Step 6  change_left     allowed (WRONG, label not_determined): The broken yellow centre line permits crossing
                        under CN-5.1.1 when safe; opposing traffic must be respected.
Step 6  change_right    prohibited (WRONG, label not_determined): The raised curb is a physical roadway
                        boundary, not a crossable lane boundary.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight; the grid
                        does not govern direction.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action
                        at the next intersection.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane and enter the crosshatched box only when you can clear it
                        without stopping. Do not drive over the right curb, and exercise particular caution
                        around the scooters, pedestrians and crossing vehicle.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1020, 18.84 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues straight ahead, with two motor-vehicle lanes in this
                        direction. My car is in the leftmost lane; the next intersection and the end of this
                        lane are not clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing traffic space
                        beyond it and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction motor-vehicle lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white hollow diamond is painted centrally in my lane in the
                        foreground.; symbol:other (full): Another smaller white hollow diamond is visible
                        farther ahead in my lane.
Step 4  Cross-check     position: The center line on the left and the lane line on the right agree with my car
                        occupying lane 1 of two same-direction lanes. | roles: The solid yellow line fits an
                        opposing-traffic boundary, and the broken white line fits a crossable same-direction
                        lane boundary. | markings: The hollow diamonds do not conflict with either boundary.
                        No lane-use arrow, reserved-lane text, or waiting area is visible in my lane. |
                        unseen: No intersection stop line or distant lane-end guidance is claimed; these
                        cannot be resolved in the photo. The diamonds are not treated as evidence of an HOV
                        lane. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            symbol:other: No supplied passage specifically defines this hollow-diamond warning
                        marking, and it governs none of the seven actions.
Step 5  Rule            symbol:other: No supplied passage specifically defines the repeated hollow-diamond
                        warning marking, and it governs none of the seven actions.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the center line governs crossing the left boundary, not an unseen intersection
                        movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight without crossing the solid yellow center line. A right lane change
                        is permitted by the dashed line, but check the nearby sedan and other traffic;
                        approach the diamond warning markings cautiously and reassess turn guidance nearer the
                        next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 10766, out 1066, 15.37 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated roadway toward a signalized intersection. My car
                        is in the rightmost motor-vehicle lane, beside a curbside non-motorized lane; the far-
                        left roadway is cropped, so the total lane count and numerical lane index are
                        uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another motor-vehicle lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white line is solid alongside my car, with a short broken section visible farther
                        ahead, separating my lane from a curbside strip with cyclists and red pavement; the
                        sidewalk curb is beyond that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow has a forward-running stem that bends right and ends
                        in a right-pointing head, with no straight-ahead head.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane on my left; the
                        right motor/non-motor separation confirms that mine is the rightmost motor-vehicle
                        lane. The cropped far-left side prevents a reliable total count. | roles: The solid
                        white left line fits a same-direction lane boundary, and the white right line fits a
                        motor/non-motor separation. | markings: The right-only arrow is consistent with the
                        intersection approach and does not authorize crossing either side boundary. | unseen:
                        No stop line or additional arrow is identifiable beyond the vehicles ahead; none is
                        inferred. The right boundary changes pattern farther ahead rather than being uniformly
                        solid. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on my left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: Crossing the solid stretch is normally prohibited, while the visibly
                        broken stretch may be crossed. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-only guide arrow allows a right turn and excludes straight,
                        left-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited: CN-6.2.1 prohibits crossing the solid white left lane line.
Step 6  change_right    allowed: CN-4.2.2-a permits crossing at the visible broken section only, not along the
                        solid foreground section.
Step 6  go_straight     prohibited (correct): The right-only arrow does not show straight ahead.
Step 6  turn_left       prohibited (correct): The right-only arrow does not show a left turn.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the right-boundary crossing permission applies only to its visible broken
                        section, and the right-only arrow governs intersection movements rather than lane
                        changes.
Advice                  Use this lane for a right turn, yielding to cyclists and pedestrians beside it; do not
                        cross either solid boundary. Any rightward crossing is permitted by the line only at
                        its broken section, and you must still follow the applicable traffic signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1296, 26.91 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signalized intersection. My car is in the leftmost
                        lane beside a concrete median, behind a truck; vehicles obscure the outer lanes and
                        the pavement ahead. (lanes None, mine 1, partial)
Step 2  Left            A continuous white solid line runs beside a raised concrete median barrier, with
                        opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane occupied
                        by a white car and vehicles farther ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right support
                        position 1; vehicles prevent a reliable total lane count. | roles: The solid white
                        right boundary fits a no-crossing lane line. The left paint visibly appears white
                        despite its median-side position; its edge role follows the physical barrier, not an
                        assumed yellow colour. | markings: No guidance marking can be read reliably in my
                        lane; the truck obscures much of the approach pavement. | unseen: No arrow direction,
                        stop line, crosswalk across my lane, or waiting area is inferred from the obscured
                        pavement or adjacent lanes. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing, and the
                        concrete median also physically prevents a leftward departure. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent same-
                        direction lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left boundary prohibits normal
                        crossing under CN-4.2.2-a, and a concrete barrier lies beside it.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane line prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     not_determined (contested, label allowed): The truck hides the approach pavement where
                        a lane-use arrow could restrict this movement.
Step 6  turn_left       not_determined: The truck hides any lane-use arrow or prohibited-turn marking that
                        would decide this movement.
Step 6  turn_right      not_determined: The truck hides any lane-use arrow or prohibited-turn marking that
                        would decide this movement.
Step 6  u_turn          not_determined: The truck hides any lane-use arrow or prohibited-U-turn marking that
                        would decide this movement.
Step 6  enter_waiting_areanot_determined: The truck obscures the area ahead where a left-turn waiting area
                          could be marked.
Step 7  Reflect         consistent: both visible solid boundaries prohibit crossing, while movements dependent
                        on obscured approach markings remain undetermined.
Advice                  Stay between the solid boundaries and leave enough distance behind the truck to reveal
                        the lane arrows and stopping position. Confirm the permitted movement before entering
                        the intersection, and obey the applicable traffic signal.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 990, 19.33 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection, with an elevated
                        roadway alongside the right side. My car is in the middle of three same-direction
                        lanes. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible long painted segments and intervening gaps,
                        separates my lane from the traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long painted segments and intervening gaps,
                        separates my lane from the traffic lane on the right; the roadside curb is beyond that
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being lane 2 of 3. | roles: The
                        white broken boundaries fit lines separating same-direction traffic lanes. | markings:
                        The straight-only arrow agrees with the lane boundaries; no conflicting guidance
                        marking is visible. | unseen: Vehicles and distance obscure the far end of the
                        approach; no hidden stop line, additional arrow, or waiting area is inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The visible broken white left lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white right lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight; for a turn, select a lane with the appropriate
                        guidance while crossing is still permitted and safe. The signals ahead appear red:
                        stop behind the stop line when it becomes visible and leave space behind queued
                        vehicles.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 954, 15.01 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection, with an elevated
                        structure alongside the right side. My car is in the middle of three same-direction
                        lanes, behind a taxi. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in my lane near the
                        car, with one forward-pointing head and no branches.
Step 4  Cross-check     position: Three lanes and ego position 2 agree with same-direction lane boundaries on
                        both sides. | roles: Both white solid lines fit no-crossing lane lines on an
                        intersection approach. | markings: The straight-only arrow is consistent with the
                        approach lane and its solid boundaries. | unseen: The taxi and distance obscure parts
                        of the lane farther ahead; no additional arrow, stop line, crosswalk, or waiting area
                        is asserted there. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits continuing straight and
                        restricts this lane against left turns, right turns, and U-turns. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to continue straight; do not cross either solid boundary or turn
                        from this lane. The visible signals are red, so stop behind the taxi and before the
                        intersection stop line when it becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 904, 12.02 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches a distant signalized intersection. My car is in the
                        third of four same-direction lanes, behind a white sedan; traffic obscures the distant
                        approach markings. (lanes 4, mine 3, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes with my lane third from the left agree with two lanes to my left
                        and one to my right. | roles: Both white broken boundaries fit crossable separators
                        between same-direction lanes. | markings: No guidance markings are visible inside my
                        lane, so none contradict the boundaries. | unseen: No arrows, words, stop line or
                        waiting area are inferred beneath the vehicles or on the obscured distant approach. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: Traffic obscures the distant intersection approach where a lane-use
                        arrow could determine this movement.
Step 6  turn_right      not_determined: Traffic obscures the distant intersection approach where a lane-use
                        arrow could determine this movement.
Step 6  u_turn          not_determined: Traffic obscures the distant intersection approach where a directional
                        or prohibited-movement marking could determine this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: lane changes apply only to the visible broken boundaries, continuing
                        straight is unrestricted by visible markings, and intersection turns remain unresolved
                        because the distant approach is obscured.
Advice                  You may continue along this lane or change lanes across either visible broken white
                        line when safe. Check the approach arrows as traffic clears before choosing a turning
                        lane, and obey the intersection signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1007, 17.89 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban arterial approaches an intersection in the distance. My car is in the
                        leftmost of four lanes travelling in this direction, beside the central separation.
                        (lanes 4, mine 1, full)
Step 2  Left            A continuous white stripe immediately borders my lane on the left, with two continuous
                        yellow stripes and another white stripe farther left; opposing traffic is beyond this
                        narrow central separation.
                        white solid, curb no, center_line, evidence partial
Step 2  Right           A broken white line, with a clearly visible long dash and gap, separates my lane from
                        another same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white bent arrow ahead in my lane has a single head pointing
                        left.
Step 4  Cross-check     position: The central separation on the left and a same-direction lane line on the
                        right agree with my lane being the first of four. | roles: The left boundary is a
                        compound central separation: its nearest stripe is white, while the paired yellow
                        stripes farther left identify the opposing-flow separation; the dashed white right
                        boundary fits a same-direction lane line. | markings: The left-only pavement arrow
                        agrees with the leftmost lane's indicated function; no conflicting pavement marking is
                        readable. | unseen: The central separation's precise construction and the distant lane
                        end are not clear; no stop line, crosswalk or waiting area is asserted. | result:
                        consistent
Step 5  Rule            left_boundary: The continuous stripe immediately beside my lane normally prohibits
                        crossing the left boundary. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:left: The single left arrow designates a left turn, not straight travel, a right
                        turn or a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid stripe at the central separation prohibits normal
                        crossing under CN-4.2.2-a.
Step 6  change_right    allowed (correct): The dashed white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     prohibited (contested, label allowed): The left-only arrow does not permit straight
                        travel from this lane.
Step 6  turn_left       allowed: The visible left arrow permits a left turn.
Step 6  turn_right      prohibited: The left-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The visible arrow shows left only, not a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a left turn; to continue straight, change safely into a through lane
                        across the broken white line before any solid approach markings begin. Do not cross
                        the central separation, and obey the intersection signals and any stop line as they
                        become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 10766, out 1106, 22.9 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban two-way road approaches a distant intersection. My car is in the
                        leftmost of three apparent lanes in this direction; traffic partly obscures the far
                        approach and the rightmost road edge. (lanes 3, mine 1, partial)
Step 2  Left            Two continuous yellow lines, flanked by white painted strips, separate my lane from
                        opposing traffic; there is no raised curb.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line with visible long segments and gaps separates my lane from another
                        same-direction lane, with no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (partial): A white directional arrow immediately ahead is partly hidden by
                        the hood; its visible head is consistent with the left-turn arrow farther ahead.;
                        arrow:left (full): Farther ahead in my lane, a white arrow has a bent shaft and a
                        left-pointing head.
Step 4  Cross-check     position: The center line on the left establishes that my lane is leftmost; the broken
                        lane line on the right establishes another same-direction lane. Three lanes appear
                        present, although the outer edge is partly obscured. | roles: The double solid yellow
                        marking fits an opposing-traffic center line, and the broken white marking fits a
                        same-direction lane divider. | markings: The repeated left-turn arrows agree with each
                        other; the broken right boundary permits leaving this turn lane before the
                        intersection. | unseen: The near arrow is partly hood-obscured, and the distant lane
                        end and any stop line or waiting area cannot be resolved. No such distant markings are
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line prohibits crossing to the left.
                        [CN-6.1.2] "A double solid yellow line prohibits vehicles in both directions from
                        crossing. It is generally used on roads with two or more motor-vehicle lanes in one
                        direct"
Step 5  Rule            right_boundary: The broken white lane divider permits changing to the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:left: The near left-turn arrow indicates left-turn travel only, corroborated by
                        the complete arrow ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 5  Rule            arrow:left: The complete left-turn arrow permits turning left and excludes straight,
                        right-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): CN-6.1.2 prohibits crossing the double solid yellow center line.
Step 6  change_right    allowed (correct): CN-5.2.1-2 permits crossing the broken white lane divider when
                        safe.
Step 6  go_straight     prohibited (correct): The left-only arrow under CN-5.13.1 does not permit straight
                        travel.
Step 6  turn_left       allowed (correct): The left-turn arrow under CN-5.13.1 permits turning left.
Step 6  turn_right      prohibited: The left-only arrow under CN-5.13.1 excludes a right turn.
Step 6  u_turn          prohibited: The left-only arrow under CN-5.13.1 does not show a U-turn.
Step 6  enter_waiting_areanot_determined: The distant intersection area is obscured and too small to determine
                          whether a left-turn waiting area exists.
Step 7  Reflect         consistent
Advice                  Remain in this lane to turn left; for straight travel, move safely into an
                        appropriately marked lane to the right while the divider is broken. Do not cross the
                        double yellow lines, and check the signals and the obscured intersection markings
                        before proceeding.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:left_u_turn', 'arrow:straight']), actions True, unsafe
                        [], citation accepted, contradictions []
Tokens                  in 10766, out 1263, 24.24 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road runs alongside an elevated roadway and approaches a distant
                        signalized intersection. My car is in the middle of five same-direction lanes. (lanes
                        5, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the right; the roadside fence is farther right, not at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has one head pointing straight
                        forward.
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: Both boundaries are broken white lines,
                        consistent with crossable same-direction lane separators. | markings: The straight-
                        only arrow is compatible with the lane boundaries; no conflicting word, symbol or
                        marked waiting area is visible in my lane. | unseen: The distant intersection pavement
                        is too small to identify additional markings or a stop line reliably; none is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits crossing into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane separator permits crossing into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight; for a turn, move safely across the broken
                        lines into an appropriately marked lane before the intersection. Watch adjacent
                        traffic and obey the signals ahead, stopping at the stop line if required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1126, 20.62 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road approaches a signal-controlled intersection, with an elevated
                        roadway alongside the left side. My car is in the third of four same-direction lanes.
                        (lanes 4, mine 3, full)
Step 2  Left            A single solid white line runs along the left of my lane to the intersection approach,
                        with another same-direction lane beyond and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, separating it from another
                        same-direction lane; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible near the far end of my
                        lane.; line:stop_line (full): A transverse white stop line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): White pedestrian-crossing
                        stripes extend across my lane at the intersection.
Step 4  Cross-check     position: Two lanes lie to my left and one to my right, consistent with lane lines on
                        both sides and my position as lane 3 of 4. | roles: Both white solid boundaries
                        separate same-direction lanes and fit intersection-approach guide lane lines. |
                        markings: The straight arrow agrees with a through guide lane bounded by solid white
                        lines; no conflicting words or marked waiting area are visible. | unseen: No movement
                        permission has been inferred from neighboring arrows or roadside signs. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing the left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing the right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-ahead arrow permits proceeding straight and restricts
                        this lane against left turns, right turns and U-turns. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not itself require a full stop on every approach. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: The stripes identify a pedestrian crossing; no supplied passage covers
                        crosswalks or assigns them a restriction on the seven assessed actions.
Step 6  change_left     prohibited (correct): Crossing the solid white left lane line is prohibited by
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): Crossing the solid white right lane line is prohibited by
                        CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight and do not cross either solid boundary. Obey the
                        traffic signal, stop before the stop line when required, and watch for pedestrians at
                        the crossing; turning requires choosing an appropriate lane before the solid-line
                        approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions True,
                        unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1189, 18.74 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. My car is in
                        the middle through lane, with two same-direction lanes on either side. (lanes 5, mine
                        3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from the
                        adjacent lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible segments and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb is farther away, beyond other
                        lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white forward-pointing arrow is visible ahead in my lane,
                        with a straight head and no visible turning branch.; line:crosswalk (partial): A
                        distant row of white pedestrian-crossing stripes crosses the approach ahead; the
                        individual stripes are small at this distance.
Step 4  Cross-check     position: Lane 3 of 5 agrees with having same-direction lane boundaries on both sides
                        and two lanes beyond each side. | roles: Both boundaries are broken white lines,
                        consistent with same-direction lane dividers. | markings: The straight arrow is
                        consistent with a through lane; the crossing ahead does not change its indicated
                        direction. | unseen: No pavement wording, turn branch, waiting area, or clearly
                        resolved stop line is asserted; distant crossing details are limited. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow allows proceeding straight and excludes
                        left turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers pedestrian-crossing stripes,
                        and this transverse marking does not determine any of the seven lane-movement actions.
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight, obeying the intersection signals and keeping
                        the pedestrian crossing clear. For a turn, select an appropriately marked lane before
                        the intersection while lane changes remain permitted; check the roadside turn
                        restrictions as well.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1422, 28.47 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. My car is in a
                        straight-ahead lane, with two same-direction lanes to the left and two to the right.
                        (lanes 5, mine 3, full)
Step 2  Left            A continuous white line forms the left boundary, with repeated short slanted white
                        teeth projecting toward the adjacent lane on its left; there is no curb at this
                        boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from another motor-vehicle lane on
                        the right, with no curb at the line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in the foreground has one head pointing
                        straight ahead.; arrow:straight (full): A second, smaller white straight-ahead arrow
                        is visible farther ahead in my lane.; line:stop_line (partial): A transverse white
                        line is faintly visible at the end of the approach lane, immediately before the
                        pedestrian crossing.; line:crosswalk (full): White pedestrian-crossing stripes extend
                        across my path at the intersection.
Step 4  Cross-check     position: The third of five lanes has same-direction lanes on both sides, consistent
                        with both boundaries being lane lines. | roles: Both boundaries are white and
                        continuous, consistent with no-crossing lane boundaries on an intersection approach;
                        the teeth on the left project into the neighboring lane. | markings: Both arrows in my
                        lane indicate straight ahead and agree with each other; no turning arrow or waiting
                        area is visible in my lane. | unseen: The distant stop line is faint and is therefore
                        recorded with partial evidence; no direction is inferred from the neighboring lane's
                        toothed boundary. | result: consistent
Step 5  Rule            left_boundary: The continuous white lane boundary prohibits my car from crossing to
                        the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The foreground straight-ahead arrow permits proceeding straight and
                        restricts this lane against left turns, right turns and U-turns. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The repeated straight-ahead arrow confirms the same straight-only lane
                        movement. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to wait or yield,
                        without itself requiring a stop on every approach. [CN-6.4.1-2] "The stop line marks
                        where vehicles stop when yielding or waiting to proceed. It is a solid white line.
                        ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers pedestrian-crossing markings;
                        this crossing does not independently determine any of the seven requested actions.
Step 6  change_left     prohibited (correct): The continuous white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): Both straight-ahead arrows permit this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows do not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrows do not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrows do not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid boundary.
                        Obey the intersection signals, stopping before the stop line when required and keeping
                        the pedestrian crossing clear; turning requires an appropriate lane selected before
                        the solid-line section.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1470, 27.09 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road with three motor-vehicle lanes in this direction approaches a
                        signal-controlled intersection. My car is in the middle lane; vehicles obscure part of
                        the distant approach. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        motor-vehicle lane on the right; a separate continuous white line lies farther right,
                        not at my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane across each boundary. | roles:
                        Both white broken boundaries fit crossable same-direction lane lines. | markings: No
                        readable guidance marking is visible in my lane, so none contradicts the boundaries. |
                        unseen: No arrows, stop line, or waiting area are inferred beneath vehicles or on the
                        distant obscured approach. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The distant approach is partly obscured, so any lane-use arrow
                        governing the intersection movement cannot be established.
Step 6  turn_right      not_determined: The distant approach is partly obscured, so any lane-use arrow
                        governing the intersection movement cannot be established.
Step 6  u_turn          not_determined: The distant approach is partly obscured, so any lane-use arrow or
                        prohibited-movement marking cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: lane changes follow the visible broken boundaries, straight travel is
                        unrestricted by visible markings, and obscured intersection turn permissions remain
                        undecided.
Advice                  Continue in the middle lane for now; either visible dashed boundary may be crossed
                        only after checking traffic and blind spots. Check the intersection arrows, signs and
                        signals as they become clear before selecting a turning lane, and stop at the stop
                        line if required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 896, 15.72 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road with opposing traffic separated by a median fence continues ahead, with
                        roadside access on the right. My car is in the middle of three visible lanes in this
                        direction; no clear intersection stop line or lane ending is visible. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with several visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with three lanes and ego lane
                        index 2. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: Distant pavement is partly obscured by traffic; no
                        markings or intersection layout are inferred there. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane line is crossable under
                        CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane line is crossable under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken boundary may be crossed after checking
                        that the adjacent lane is clear. Watch especially for the cyclist ahead on the right,
                        and check later lane arrows and signs before choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 10766, out 819, 11.72 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane urban expressway continues beneath an overpass, with traffic ahead
                        and a signed exit 700 m away. My car is in the rightmost of three lanes, beside a
                        paved shoulder. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from another traffic lane on the left; a dash
                        and a gap are visible ahead, and white lozenge-shaped markings flank portions of the
                        line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with white lozenge-shaped
                        markings alongside it and a paved shoulder leading to a concrete barrier beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated white elongated lozenge-shaped markings run along the
                        inside margins of my lane in the foreground; no directional arrow or readable pavement
                        text is visible.
Step 4  Cross-check     position: The lane line on the left and shoulder edge on the right agree with my lane
                        being the third and rightmost lane. | roles: The broken white left line fits a same-
                        direction lane divider, and the solid white right line fits a carriageway edge. |
                        markings: The repeated marginal lozenges do not indicate a turning direction and do
                        not conflict with the boundaries. | unseen: No intersection, stop line, waiting area,
                        or directional arrow is visible; none is inferred beyond the visible stretch. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            symbol:other: No supplied passage specifically defines these repeated marginal
                        lozenges, and they do not authorize or prohibit any of the seven actions.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits crossing
                        under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible directional marking restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change left across the broken divider only when safe; do not
                        cross the solid right edge onto the shoulder. Maintain a safe following distance and
                        follow the upcoming exit signs rather than treating the shoulder as an exit lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1078, 21.44 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight, with no intersection or lane ending visible.
                        My car is in the third of four lanes in this direction, behind a white SUV. (lanes 4,
                        mine 3, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego lane index 3 agree with two lanes to the left and one to
                        the right, with lane lines on both sides. | roles: Both boundaries are broken white
                        lines, consistent with separators between same-direction lanes. | markings: No arrows,
                        words, symbols, transverse lines or marked waiting areas are visible in my lane. |
                        unseen: The SUV obscures some pavement ahead, and the next intersection is not
                        visible; no markings or intersection layout are inferred there. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken white boundary may be crossed for a safe
                        lane change after checking traffic. No turn guidance or stopping point is visible, so
                        reassess the markings when approaching an intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 10766, out 891, 14.18 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with no nearby intersection or lane
                        ending visible. My car is in the rightmost lane, which has bus-reservation pavement
                        text. (lanes 3, mine 3, full)
Step 2  Left            A yellow broken line, with several visible dashes and gaps, separates my lane from
                        another same-direction motor lane; there is no curb on this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side, with yellow broken segments
                        immediately alongside it on my lane's side; a paved roadside strip and a raised curb
                        lie farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (partial): Large white numerals near the hood are partly hidden and appear
                        to form a time inscription, but the complete inscription cannot be read.; text:bus
                        (partial): White Chinese bus-reservation text runs along the lane; 公交 is visible,
                        while the farther characters are less distinct.
Step 4  Cross-check     position: Three lanes and a rightmost ego position agree with a same-direction
                        special-lane boundary on the left and a roadway edge on the right. | roles: The white
                        solid right edge fits its role. The yellow broken bus-lane delineation does not match
                        the white bus-lane line described in the supplied rule, so its observed color is
                        retained rather than changed. | markings: The bus text supports identifying my lane as
                        reserved; the partly visible numerical inscription cannot establish its reservation
                        hours. No directional arrow or waiting area is visible. | unseen: The complete time
                        inscription and distant lane termination are not readable; neither has been inferred.
                        | result: Consistent spatial interpretation, with a noted color mismatch between the
                        observed special-lane delineation and the supplied bus-lane specification.
Step 5  Rule            left_boundary: The visible broken boundary permits crossing out of my lane to the
                        left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: The continuous white edge line normally prohibits crossing onto the
                        roadside strip. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            text:other: This pavement inscription conveys information, but its incomplete reading
                        establishes neither reservation hours nor a movement permission. [CN-5.14.1] "Pavement
                        text markings are generally white. They are arranged vertically and read from near to
                        far along the direction of travel ... or horizontally from left t"
Step 5  Rule            text:bus: The bus-reservation text identifies a lane ordinary cars must not use while
                        reserved, although leaving it follows the boundary type. [CN-6.9.1] "The bus lane line
                        shows that vehicles other than buses shall not enter the lane. It consists of a broken
                        white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (contested, correct): The broken left boundary permits leaving this reserved
                        lane under CN-4.2.2-a.
Step 6  change_right    prohibited (contested, correct): Crossing the solid white right edge is prohibited
                        under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, label prohibited): No visible directional arrow restricts
                        continuing straight; the bus text does not govern this movement action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: permission to continue straight describes directional markings only, not
                        permission for an ordinary car to occupy this reserved bus lane.
Advice                  For an ordinary car, move safely left across the broken boundary into a general-
                        traffic lane rather than continue using the bus lane; its reservation hours cannot be
                        read here. Do not cross the solid right edge, and check signs and subsequent
                        intersection markings before choosing a turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 10766, out 1289, 26.47 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway continues ahead, with a median barrier on the left and a
                        guardrail on the right; no intersection or lane ending is visible. My car is in the
                        third of four lanes in this direction. (lanes 4, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken line with pale yellow-looking paint and visible gaps separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes to the left and one to the right agree with my position as lane 3
                        of 4 and with both boundaries separating same-direction lanes. | roles: The broken
                        white left boundary fits a crossable lane line. The right boundary appears yellow
                        rather than the standard white for same-direction separation; its location and
                        surrounding traffic establish its lane-line role, not a center-line role. | markings:
                        No arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No distant intersection layout or concealed markings are inferred; the
                        right boundary's unusual visible color is retained rather than changed to match its
                        role. | result: Geometrically consistent; the right boundary has an apparent color
                        mismatch with standard same-direction lane-line coloring.
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing to change
                        lanes when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The visible broken longitudinal line permits crossing, despite its
                        atypical apparent color for a same-direction divider. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken longitudinal boundary permits crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow or visible lane ending restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: broken boundaries govern lane changes only, and no unseen intersection
                        movements or waiting areas are inferred.
Advice                  Continue in your lane; either visible broken boundary permits a lane change after
                        checking traffic and clearance. No turning location or stopping line is visible, and
                        the unusually yellow-looking right divider warrants attention.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1034, 20.12 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues ahead on a gentle bend, with barriers on both sides
                        and no visible intersection or lane ending. My car is in the third of four lanes in
                        this direction. (lanes 4, mine 3, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego lane index 3 agree with two lanes to the left and one to
                        the right, with lane lines immediately on both sides. | roles: Both boundaries are
                        broken white lines, consistent with same-direction lane dividers. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No hidden markings or distant intersection movements have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along my lane, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; either adjacent lane may be entered across the broken white
                        divider after checking traffic and blind spots. No turn lane, waiting area or stopping
                        point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 838, 13.7 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, three-lane carriageway continues through a gentle left bend, with
                        guardrails on both sides and no intersection or lane ending visible. My car is in the
                        middle lane. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane across each
                        boundary. | roles: Both boundaries are broken white lines, consistent with crossable
                        same-direction lane lines. | markings: No arrows, words, symbols, transverse lines or
                        marked areas are visible in my lane. | unseen: No hidden lane-end markings or
                        movements at an unseen intersection have been inferred. | result: consistent
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
Step 6  go_straight     allowed (contested, correct): No marking restricts continuing along my lane, and no
                        lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane through the gentle left bend; either broken white boundary
                        permits a lane change when safe. Check adjacent traffic carefully, particularly in the
                        strong sun glare.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 746, 10.15 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban expressway approaches a fork, with the roadway ahead curving right and
                        a painted separation developing to the left. My car is in the middle of three same-
                        direction lanes near the bottom of the image. (lanes 3, mine 2, full)
Step 2  Left            A continuous white line borders my lane on the left and leads toward a diagonally
                        hatched separation ahead; another same-direction lane lies beyond it, with no curb
                        directly bordering my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line curves right along my lane, with another paved traffic lane
                        beyond it and a concrete roadside barrier farther right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane line
                        on each side. | roles: Both white solid boundaries fit no-crossing lane lines
                        separating same-direction traffic. | markings: No arrows, words, symbols or transverse
                        markings are visible within my lane; the diagonal hatching lies outside its left
                        boundary. | unseen: No hidden arrows or distant intersection markings are inferred;
                        vehicles obscure some pavement farther ahead. | result: consistent
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
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane; its
                        rightward curve is not a turning instruction.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines and follow your lane around the rightward curve;
                        do not cross either boundary or the hatched separation. Check the overhead destination
                        signs and maintain a safe following distance.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 988, 18.81 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight ahead, with guardrails and traffic in all
                        three lanes. My car is in the middle lane; no intersection, ramp or lane ending is
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane across
                        each boundary. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No visible in-lane arrows, words, symbols or marked areas conflict
                        with the boundaries. | unseen: No hidden lane-end markings or distant intersection
                        features have been inferred. | result: consistent
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
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the middle lane. Either broken boundary permits a lane change,
                        but check mirrors, blind spots and gaps in the adjacent traffic before moving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 743, 10.1 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, three-lane roadway continues straight toward a distant overpass, with
                        traffic ahead. My car is in the rightmost lane; a paved shoulder and guardrail lie to
                        its right. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved shoulder, with a
                        guardrail beyond the shoulder rather than directly at the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white left line fits a
                        crossable same-direction lane separator; the solid white right line fits the right
                        roadway edge. | markings: No identifiable guidance marking in my lane conflicts with
                        the boundaries. | unseen: No lane-end layout is inferred beyond the visible road;
                        traffic obscures parts of the distant pavement. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing onto the
                        shoulder, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken line only when safe; do not
                        cross the solid right edge onto the shoulder in normal driving. Maintain a safe gap to
                        the traffic ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 797, 12.92 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           My car is on a single-lane ramp curving left between barriers, with vehicles ahead and
                        reddish pavement sections in the lane. No intersection or lane ending is visible.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous pale white line follows the left side beside a concrete barrier, with
                        repeated short white rectangular blocks on the lane side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line borders a paved shoulder on the right, with repeated white
                        rectangular blocks on the lane side and a barrier beyond the shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white rectangular blocks run along both margins
                        inside the lane; no directional arrow or wording is visible.
Step 4  Cross-check     position: One lane with roadway edges on both sides agrees with my lane being lane 1
                        of 1; the pavement beyond the right edge line is a shoulder. | roles: Both continuous
                        lines follow roadway edges. The observed white left edge does not match the yellow
                        left-edge colour prescribed by CN-5.4.3, but its visible colour has not been changed
                        to fit that rule. | markings: The repeated marginal blocks do not indicate a turning
                        movement or conflict with the single-lane ramp layout. | unseen: No movement arrow,
                        stop marking or waiting area is visible; the road beyond the bend is not assessed. |
                        result: Consistent geometrically; the visible left-edge colour differs from the
                        prescribed colour.
Step 5  Rule            left_boundary: The continuous edge line normally prohibits crossing to the left, where
                        a physical barrier also prevents leaving the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The continuous edge line normally prohibits crossing onto the right
                        shoulder. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            symbol:other: No supplied passage specifically defines these repeated marginal blocks,
                        and they do not authorize or prohibit any of the seven actions.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge line prohibits normal crossing
                        under CN-4.2.2-a, and a barrier lies beside it.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits normal crossing onto the
                        shoulder under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the ramp; following
                        its leftward curve is continuing in the lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the boundaries govern only lateral departures, and continuing along the
                        curved ramp is not treated as a left turn.
Advice                  Stay within the solid edge lines and follow the ramp around the left bend at a
                        cautious speed. Keep clear of the right shoulder and maintain space behind the
                        vehicles ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1007, 19.6 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road curves gently right, with traffic ahead and no visible
                        intersection or lane ending. My car is in the rightmost of three lanes in this
                        direction, beside a paved shoulder. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane; additional short white blocks flank the line, and there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane, with repeated short white blocks beside it; a
                        paved shoulder and then a metal guardrail lie beyond the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white rectangular or slanted blocks run along both
                        sides of my lane, forming a visual narrowing pattern; no readable directional arrow or
                        pavement word is visible.
Step 4  Cross-check     position: Three lanes and ego lane index 3 agree with a same-direction lane line on
                        the left and a roadway edge line on the right. | roles: The broken white left line
                        fits a crossable lane separator, and the solid white right line fits the right roadway
                        edge. | markings: The repeated white blocks do not indicate a turning movement and do
                        not conflict with either boundary. | unseen: No distant intersection layout or hidden
                        directional marking is inferred; the guardrail is beyond the shoulder, not the
                        immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing onto the
                        shoulder, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            symbol:other: No supplied passage specifically covers these repeated white blocks, and
                        they do not independently permit or prohibit any of the seven actions.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid right boundary normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane, and
                        no lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along this lane through the right-hand curve, or change left across the
                        broken line only when safe; do not cross the solid right line onto the shoulder in
                        normal driving. Maintain space from traffic ahead and observe the posted 60 speed-
                        limit sign.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1019, 17.93 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway continues ahead, with three lanes in this direction and a
                        shoulder on the right. My car is in the middle lane; no intersection or lane ending is
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; the solid shoulder edge line and guardrail
                        lie farther right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with being in lane 2 of 3. | roles: Both
                        boundaries are broken white lines separating same-direction lanes, consistent with
                        their lane-line roles. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane. | unseen: No unseen lane-end markings or
                        distant restrictions have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow or other marking restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the middle lane. Either adjacent lane may be entered across the
                        broken white line after checking traffic and blind spots; keep clear of the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 747, 9.3 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined multilane road continues ahead with a gentle left bend; no
                        intersection or lane ending is visible. My car is in the middle of three lanes
                        travelling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane line on each side. | roles:
                        Both white broken boundaries fit crossable same-direction lane lines. | markings: No
                        arrows, words, symbols, transverse markings or waiting areas are visible in my lane. |
                        unseen: No unseen lane-end or intersection features have been inferred. | result:
                        consistent
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
                        under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts continuing along my lane, and no
                        lane ending is visible.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either adjacent lane may be entered across its broken
                        white line after checking traffic and blind spots. No turn guidance, waiting area or
                        stopping point is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 757, 11.17 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, three-lane carriageway curves gently left, with a median barrier on the
                        left and a shoulder and noise barrier on the right. My car is in the rightmost lane;
                        no intersection, ramp or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved shoulder and
                        then a guardrail beyond it; no curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes lie to my left and none to my right, consistent with lane 3 of 3,
                        a left lane line and a right roadway edge line. | roles: The broken white separator
                        fits a same-direction lane line, and the solid white line beside the shoulder fits a
                        right edge line. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are visible in my lane. | unseen: No intersection layout or markings
                        beyond the visible road stretch are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing to the adjacent lane on the
                        left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The white line marks the edge of the motor-vehicle carriageway, with a
                        shoulder beyond it. [CN-5.4.1] "The carriageway edge line marks the edge of motor
                        vehicle lanes or non-motorized vehicle lanes, or the boundary between motor vehicle
                        lanes and non-motorized ve"
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along my lane, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane through the gentle left curve, or change left across the broken
                        line when safe. Do not cross the solid right edge line onto the shoulder during normal
                        driving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 898, 13.17 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A barrier-lined urban carriageway curves left ahead, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous white line follows the concrete barrier on the left, with repeated white
                        rectangular blocks just inside the lane and a separated roadway beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from another paved lane on the right, with
                        repeated white rectangular blocks on my side of the line and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Repeated white rectangular blocks run along both margins inside
                        my lane, forming a visual narrowing pattern.; symbol:other (partial): A group of
                        closely spaced pale transverse bands crosses my lane ahead; these are not a zebra
                        crossing or a single stop line.
Step 4  Cross-check     position: The left physical edge and the lane divider on the right agree with my car
                        occupying lane 1 of 2. | roles: The white solid right divider fits a same-direction
                        no-crossing lane line. The left white line visibly follows the physical roadway edge;
                        its observed colour is retained despite the usual yellow left-edge convention. |
                        markings: The rectangular blocks and transverse bands provide no directional arrow,
                        turn restriction or waiting area, and do not contradict the boundaries. | unseen: No
                        arrow, word, stop line or waiting area is inferred beyond the visible curve; the
                        transverse bands are not completely clear. | result: consistent
Step 5  Rule            left_boundary: The solid edge line normally prohibits crossing to the left, where a
                        concrete barrier also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white same-direction lane divider prohibits crossing into
                        the right lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            symbol:other: No supplied passage specifically covers the repeated rectangular visual-
                        narrowing markings, and they do not govern any of the seven actions.
Step 5  Rule            symbol:other: No supplied passage specifically covers these transverse bands, and they
                        do not establish a mandatory stop or a permitted direction.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge line prohibits normal crossing
                        under CN-4.2.2-a, and a concrete barrier lies alongside it.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): No directional marking restricts continuing along my
                        lane around the curve.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the leftward curve without crossing either solid
                        boundary. Slow for the curve and transverse bands, and observe the visible 30 km/h
                        speed-limit sign; no mandatory stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1079, 17.44 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow, single-lane ramp or separated carriageway continues ahead between
                        guardrails, with a coach directly ahead. No intersection, merge point or lane end is
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous pale yellow solid line borders the lane on the left, with a narrow paved
                        margin, raised curb and metal guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line borders the lane on the right, with a paved shoulder,
                        raised curb and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges, consistent with one lane and the ego
                        vehicle occupying lane 1. | roles: The yellow left edge and white right edge fit their
                        respective edge-line roles; both are visibly solid. | markings: No guidance markings
                        are visible within the lane, and no marked waiting area is visible. | unseen: The
                        coach hides part of the pavement ahead; no markings beneath it or beyond the visible
                        stretch are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing it, apart from a
                        safe emergency exception. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, apart from a safe emergency exception. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): Crossing the solid left boundary is normally prohibited by
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): Crossing the solid right boundary is normally prohibited by
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along the lane;
                        the edge lines govern crossing, not forward travel.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the single lane without crossing either solid edge line. Keep a safe
                        following distance behind the coach, which obscures the pavement ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 829, 11.92 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An elevated, divided multilane road continues straight ahead, with no intersection,
                        ramp or lane ending visible. My car is in the second of four general-traffic lanes
                        from the left; an emergency lane lies farther right. (lanes 4, mine 2, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of four general-
                        traffic lanes. | roles: Both boundaries are broken white lines, consistent with
                        separating lanes travelling in the same direction. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        distant intersection or unseen lane-use marking has been inferred; overhead sign
                        arrows are not pavement arrows. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; either adjacent lane may be entered across the broken white
                        line after checking traffic. Follow the overhead lane-specific speed signs and keep
                        out of the emergency lane during ordinary driving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 780, 11.15 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided roadway continues toward an overpass; no intersection or lane ending
                        is clearly visible. My car is in the left of two same-direction lanes, beside a
                        planted median, with parked vans in the right lane. (lanes 2, mine 1, full)
Step 2  Left            A faded single solid yellow line runs alongside a raised planted-median curb, with
                        another carriageway beyond the median.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single worn but continuous solid white line separates my lane from the lane
                        containing parked vans; there is no curb at this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right same-direction lane line agree with my lane
                        being lane 1 of 2. | roles: The yellow left edge line and white same-direction
                        separator fit their assigned roles; both appear solid. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        markings are inferred beneath vehicles or beyond the visible roadway; the next
                        intersection and its approach markings are not identifiable. | result: consistent
Step 5  Rule            left_boundary: The solid yellow edge line normally prohibits crossing to the left, and
                        the raised median is also a physical boundary. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white same-direction lane line prohibits crossing into the
                        right lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (WRONG, label not_determined): The solid yellow boundary prohibits normal
                        crossing under CN-4.2.2-a, and a raised median lies beside it.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane line prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane; the solid boundaries govern crossing, not forward travel.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: neither boundary may be crossed normally, and the absence of movement
                        arrows does not establish permission to turn at an unseen intersection.
Advice                  Continue straight within this lane without crossing either solid boundary, watching
                        for parked vehicles and cyclists to the right. Reassess turn guidance when an
                        intersection comes into view; no stopping location is marked in the visible lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 895, 15.1 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight, with a planted divider on the left and a roadside
                        strip used by scooters on the right. My car is in the single motor-vehicle lane of
                        this separated carriageway; the distant intersection approach is partly obscured by
                        traffic. (lanes 1, mine 1, full)
Step 2  Left            A solid white line runs beside the raised concrete edge of a planted divider, with a
                        separate carriageway beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A faded solid white line separates my lane from the roadside strip occupied by
                        scooters; the raised sidewalk curb is beyond that strip, not immediately beside my
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane in this separated carriageway agrees with edge
                        boundaries on both sides; the roadway beyond the planted divider is not an adjacent
                        lane accessible from my lane. | roles: The right white line fits a motor/non-motor
                        separation edge. The left white line visibly follows a physical divider; its observed
                        colour is retained rather than inferred to be yellow. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are readable in my lane. | unseen: The
                        vehicle ahead obscures part of the lane, and distant intersection markings cannot be
                        resolved; no hidden markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The raised divider provides a physical roadway edge rather than a
                        crossable lane boundary, so moving left across it is prohibited. [CN-5.4.5] "Where a
                        non-motorized lane is needed and there is no separating facility between it and the
                        motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The solid longitudinal line normally prohibits crossing into the
                        roadside strip. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): The raised concrete divider physically closes the left edge; it
                        is not an available lane-change boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): Crossing the solid white right boundary is
                        prohibited by CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundaries govern only lateral departures, and no unseen intersection
                        arrows or waiting areas have been assumed.
Advice                  Continue within the lane without crossing either boundary, watching for scooters near
                        the right edge. Reassess the intersection markings and signs when they become visible;
                        no turn permission or stopping position can be read here.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 915, 16.98 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beneath a pedestrian overpass, with no
                        intersection or lane ending visible. My car is in the leftmost of two same-direction
                        motor-vehicle lanes, beside a raised planted median. (lanes 2, mine 1, full)
Step 2  Left            A single solid yellow line runs beside the raised curb of a planted median; no
                        adjacent traffic lane lies immediately beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and an adjacent same-direction lane on the right
                        agree with my lane being lane 1 of 2. | roles: The solid yellow left edge and broken
                        white same-direction lane divider fit their assigned roles. | markings: No guidance
                        markings are visible within my lane, so there is no conflict with the boundaries. |
                        unseen: No distant intersection layout or markings hidden by vehicles have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid yellow boundary is normally prohibited, and the
                        raised median also physically blocks movement to the left. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): The solid yellow left boundary prohibits
                        normal crossing under CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits crossing
                        under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action;
                        the left boundary governs crossing it, not a movement at a future intersection.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change right across the broken white line only after
                        checking for vehicles and riders. Do not cross the solid yellow line or raised median;
                        no visible intersection markings establish turn permissions.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 827, 11.82 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow urban roadway continues straight beneath a height-restriction frame; no
                        intersection or lane ending is visible. My car occupies the single motor-vehicle lane,
                        with a raised divider on the left and a strip used by a two-wheeler on the right.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous pale white line runs beside a raised curb and fenced divider, with a
                        separate roadway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from a narrow paved strip occupied by a
                        two-wheeler; the sidewalk curb lies beyond that strip, not directly beside my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane bounded by roadway edges agrees with my lane being
                        both leftmost and rightmost. | roles: The right solid white line fits a motor/non-
                        motor separation edge. The left line appears white despite its left-edge position; its
                        observed color is retained rather than inferred from the prescribed color. | markings:
                        No arrows, words, transverse lines or marked waiting areas are visible in my lane. |
                        unseen: No hidden lane-end layout or distant turn guidance has been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing, and the raised
                        curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing into the
                        strip on the right. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb forms the edge.
Step 6  change_right    prohibited (correct): The solid white right boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the solid boundaries and keep clear of the two-wheeler on the right.
                        Check that your vehicle clears the posted 2.5 m height restriction before passing
                        beneath the frame; no turn guidance or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 863, 14.22 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues ahead beside a raised divider and beneath a pedestrian-
                        overpass stairway. My car follows a taxi in the leftmost lane of this separated
                        roadway; the use of the paved strip to the right is unclear. (lanes None, mine 1,
                        partial)
Step 2  Left            A continuous raised concrete divider forms the left boundary, with another carriageway
                        beyond it; no painted boundary line is clearly visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A worn white line appears continuous along the right side of my lane, with a paved
                        strip beyond it and a sidewalk curb farther right; no deliberate dash-and-gap pattern
                        is visible.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The raised divider establishes my lane as leftmost; the total motor-vehicle
                        lane count remains uncertain because the use of the strip beyond the white line is not
                        identifiable. | roles: The physical divider fits a roadway edge. The white line could
                        separate same-direction lanes or mark a motor/non-motor boundary, so its precise role
                        is left unknown. | markings: No readable arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane. | unseen: No designation is assigned to
                        the right-hand strip; the taxi obscures part of the lane ahead, and the next
                        intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: No supplied passage specifically authorizes crossing a physical
                        divider; its function as a raised boundary prohibits moving left across it.
Step 5  Rule            right_boundary: The visible solid white longitudinal line normally prohibits crossing
                        to the right. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 6  change_left     prohibited (correct): The raised concrete divider physically closes the left side of
                        my lane.
Step 6  change_right    prohibited (correct): The right boundary appears solid, so CN-4.2.2-a prohibits normal
                        crossing.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-turn marking governs this
                        movement.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-turn marking governs this
                        movement.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-turn marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue behind the taxi within the divider and the white line; do not cross either
                        boundary. The image does not establish turn permissions or a stopping location at the
                        next intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 946, 18.2 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a raised planted median on the
                        left and a sidewalk on the right. My car is in the left of two same-direction motor-
                        vehicle lanes; no intersection or lane ending is clearly visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A solid white painted line runs beside the raised median curb, with planting and the
                        opposing carriageway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from
                        another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 1 agree with a median edge on the left
                        and a lane divider on the right. | roles: The broken white right boundary fits a same-
                        direction lane line. The left boundary is visibly white despite being a left roadway
                        edge, where CN-5.4.3 prescribes yellow; its edge role is established by the median
                        curb. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No distant intersection layout or hidden pavement
                        marking is inferred; windshield glare obscures some pavement immediately ahead of the
                        hood. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median is a physical edge rather than an adjacent usable lane.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The solid left boundary prohibits normal crossing
                        under CN-4.2.2-a, and a raised median lies beyond.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line only after
                        checking traffic; do not cross the solid line toward the median. The roadside sign
                        displays 50 km/h; no visible markings establish turning permissions at a future
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 858, 13.85 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight ahead, with a planted raised divider on the left and
                        a narrow strip used by scooters on the right. My car is in the single visible motor-
                        vehicle lane; no intersection or lane ending is clearly visible. (lanes 1, mine 1,
                        full)
Step 2  Left            A continuous raised concrete divider borders the lane on the left, with planting and
                        another roadway beyond; no distinct painted boundary line can be confidently
                        identified at its base.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A continuous solid white line separates my lane from a narrow paved strip occupied by
                        scooters, with a raised sidewalk farther right; no curb lies directly along the white
                        line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane, indexed 1, agrees with a divider at its left edge
                        and a motor/non-motor separation line at its right edge. | roles: The right solid
                        white line fits a motor/non-motor separation boundary; the raised divider physically
                        defines the left edge regardless of indistinct paint at its base. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No paint color or pattern is inferred at the divider base, and no
                        markings are inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: No supplied passage explicitly governs crossing a raised divider; as a
                        physical lane edge it is not available for a leftward lane change.
Step 5  Rule            right_boundary: The solid longitudinal line normally prohibits crossing into the strip
                        on the right, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The raised concrete divider physically prevents a leftward lane
                        change.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white boundary prohibits normal
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the motor-vehicle lane, keeping clear of the divider and the solid
                        white boundary beside the scooters. No turn guidance or stopping line is visible;
                        reassess when the next junction comes into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 898, 16.58 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight beside an elevated roadway, with three motor-vehicle
                        lanes in this direction and a separated roadside non-motorized strip on the right. My
                        car is in the middle motor-vehicle lane; no intersection or lane ending is clearly
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the right; the solid white roadside line and curb are farther
                        right, not my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small, distant white arrow in my lane points straight
                        ahead; its details are softened by distance.
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane line
                        on each side. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane separators. | markings: The visible straight arrow is
                        consistent with the continuing lane and does not conflict with either boundary. |
                        unseen: The distant arrow has reduced detail, and the eventual intersection and lane
                        endpoint are not visible; no stop line or waiting area is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction motor-vehicle lane when safe. [CN-5.2.1-2] "The crossable lane line
                        separates traffic flows in the same direction and is placed between lanes of the same
                        direction. It is a broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits straight travel and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white right lane line permits crossing
                        under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): The identifiable straight arrow permits straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent motor-vehicle lane may be entered
                        across the broken line after checking traffic. For a turn, find an appropriately
                        marked lane rather than turning from this straight-only lane, and reassess markings as
                        the distant approach becomes clearer.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1067, 17.28 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight toward an overhead pedestrian bridge; no intersection
                        or lane end is clearly visible. My lane is the single motor-vehicle lane, with a
                        separate non-motorized strip on its right. (lanes 1, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb on the left, with a planted strip beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous along the right of the arrow-marked lane, partly
                        obscured by a cyclist, with bicycles and scooters travelling in the strip beyond it.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A large white arrow has a single head pointing straight
                        ahead; its lower stem is hidden by the hood.
Step 4  Cross-check     position: One motor-vehicle lane agrees with edge boundaries on both sides; the strip
                        to the right is not another motor-vehicle lane. | roles: The right white separator
                        fits a motor/non-motor edge line. The left paint is visibly white despite the usual
                        yellow convention for a left edge; its curbside position supports the edge role
                        without changing the observed colour. | markings: The straight arrow agrees with the
                        continuing lane; no competing arrow, text or waiting area is visible. | unseen: The
                        cyclist obscures part of the right boundary and the hood hides the arrow's lower stem;
                        distant markings cannot be resolved. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line prohibits ordinary crossing to the left,
                        where a raised curb also forms a physical edge. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid longitudinal separator prohibits ordinary crossing
                        into the strip on the right. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The single straight arrow permits straight travel and restricts the
                        lane to that indicated movement. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left edge line prohibits ordinary crossing under
                        CN-4.2.2-a, and a curb lies immediately beyond.
Step 6  change_right    prohibited (contested, correct): The visible solid right separator prohibits ordinary
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The clearly visible straight arrowhead permits straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight within the motor-vehicle lane without crossing either solid
                        boundary. Give the cyclists and scooter riders ample clearance; no stop line is
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1106, 23.35 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban roadside carriageway runs between a raised planted divider on the left and
                        curbside parking on the right. My car is in its single visible travel lane behind a
                        sedan; traffic hides the distant lane end. (lanes 1, mine 1, full)
Step 2  Left            A continuous pale-yellow solid line runs beside a raised concrete planted divider,
                        with another carriageway beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous pale-yellow solid line separates my travel lane from a strip occupied by
                        parked cars; the sidewalk curb lies beyond that strip rather than directly beside my
                        lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One travel lane with edge boundaries on both sides is consistent with my
                        lane being the leftmost and only lane of this carriageway; the parked-car strip is not
                        counted as a travel lane. | roles: The left yellow edge line fits the divider edge.
                        The right line appears yellow despite its right-edge position, which does not fit the
                        prescribed white right-edge colour; its observed colour has not been changed to match
                        the rule. | markings: No arrows, words, symbols or transverse markings are visible on
                        the exposed pavement in my lane. | unseen: The sedan and queued traffic obscure the
                        pavement ahead, so markings at the distant lane end cannot be established. | result:
                        The geometric interpretation is consistent; the apparent right-edge colour discrepancy
                        is retained as observed.
Step 5  Rule            left_boundary: The solid line normally prohibits crossing left, and the raised divider
                        also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal line normally prohibits crossing right into the
                        parked-car strip. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): The visible solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a raised divider beyond.
Step 6  change_right    prohibited (contested, correct): The visible solid right boundary prohibits normal
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along the
                        lane; its solid side boundaries do not prohibit forward travel.
Step 6  turn_left       not_determined: Traffic hides the lane-end pavement where a movement-governing arrow
                        could be present.
Step 6  turn_right      not_determined: Traffic hides the lane-end pavement where a movement-governing arrow
                        could be present.
Step 6  u_turn          not_determined: Traffic hides the lane-end pavement where a movement-governing arrow
                        or prohibition could be present.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: solid boundaries govern only lateral crossing, straight travel remains
                        unrestricted by visible markings, and hidden lane-end guidance leaves turning
                        movements undecided.
Advice                  Continue within the solid boundaries and keep clearance from parked vehicles and
                        pedestrians on the right. Reassess turn guidance and any stopping requirements when
                        the traffic ahead reveals the lane end.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 10766, out 993, 19.16 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a planted median on the left and a
                        line of vehicles in the adjacent right lane. My car is in the leftmost of two visible
                        same-direction lanes; no intersection or lane ending is clearly visible. (lanes 2,
                        mine 1, full)
Step 2  Left            A continuous white line runs along the left side of my lane beside a raised curb and
                        planted median, with the opposite carriageway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the adjacent same-direction lane
                        occupied by vehicles; its farther stretch is partly obscured by the scooter and cars.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge on the left and an adjacent lane on the right agree
                        with my position as lane 1 of 2. | roles: The solid white right boundary fits a no-
                        crossing lane line. The left boundary is visibly white despite being a median-side
                        edge; its color does not match the prescribed yellow left edge, so the observed color
                        is retained. | markings: No readable arrows, words, symbols, marked areas or
                        transverse traffic lines appear in the visible portion of my lane. | unseen: The
                        distant lane end and any markings there cannot be resolved; none are inferred. |
                        result: Consistent, with the observed left-edge color discrepancy retained.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        where the raised median also forms a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent right
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The visible solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane; the longitudinal boundaries do not prohibit it.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: lane-change prohibitions follow the visible solid boundaries, while no
                        unseen intersection movement or marking is inferred.
Advice                  Continue within this lane without crossing either solid boundary, leaving space for
                        the scooter ahead. Turn-lane guidance and any stopping requirement at the next
                        intersection are not yet visible.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 972, 18.24 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road with opposing traffic separated by a metal median fence; two lanes
                        travel in our direction. My car is in the left lane behind the black sedan; the
                        distant lane end or intersection is obscured by traffic. (lanes 2, mine 1, full)
Step 2  Left            A yellow longitudinal line runs along the metal median fence on the left; visible
                        portions appear solid, but fence bases obscure parts of the paint, and opposing
                        traffic lies beyond.
                        yellow solid, curb yes, center_line, evidence partial
Step 2  Right           A broken white line, with multiple visible dashes and gaps, separates my lane from
                        another same-direction motor-vehicle lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two visible same-direction lanes and ego lane index 1 agree with the median
                        boundary on the left and a lane line on the right. | roles: The yellow median line
                        separates opposing traffic, and the broken white line separates same-direction lanes.
                        | markings: No guidance markings are visible within my lane; the overhead lane-
                        direction diagram is a sign, not a pavement marking. | unseen: The median fence
                        obscures parts of the left paint, and traffic hides the distant pavement and lane end;
                        no hidden arrows or stop lines are inferred. | result: consistent
Step 5  Rule            left_boundary: The visible solid yellow centre line prohibits crossing to the left;
                        the median fence also physically blocks that movement. [CN-6.1.4] "A single solid
                        yellow line prohibits vehicles in both directions from crossing. It is generally used
                        on two-lane two-way roads with limited sight distance or wh"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): The solid yellow centre line prohibits
                        crossing under CN-6.1.4, and a median fence blocks the boundary.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_determined: The distant lane-end pavement is hidden by traffic, so any arrow
                        governing a left turn cannot be checked.
Step 6  turn_right      not_determined: The distant lane-end pavement is hidden by traffic, so any arrow
                        governing a right turn cannot be checked.
Step 6  u_turn          not_determined: The distant lane-end pavement is hidden by traffic, so any marking
                        governing a U-turn cannot be checked.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change right across the broken white line when safe; do not
                        cross the median boundary. Check the lane-direction signs and markings farther ahead
                        before choosing a turning lane, and observe the posted 40 km/h limit.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 978, 17.56 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with two motor-vehicle lanes in this direction
                        and a non-motorized lane on the right. My car is in the rightmost motor-vehicle lane;
                        no intersection stop line or lane ending is clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with several dashes and intervening gaps visible, separates my
                        lane from another motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from pavement used by bicycles and
                        scooters on the right; no curb forms the immediate boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two motor-vehicle lanes and ego position 2 agree with a lane divider on the
                        left and a motor/non-motor edge line on the right. | roles: The broken white left line
                        fits a same-direction lane divider; the solid white right line fits a motor/non-motor
                        separation line. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are discernible in my lane. | unseen: The distant road surface is partly
                        obscured by vehicles and perspective; no unseen intersection markings or directions
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: This edge line marks the boundary between motor-vehicle and non-
                        motorized space. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle
                        lanes or non-motorized vehicle lanes, or the boundary between motor vehicle lanes and
                        non-motorized ve"
Step 5  Rule            right_boundary: Crossing this solid longitudinal boundary is normally prohibited,
                        except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits crossing
                        under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken line when safe; do not cross
                        the solid right boundary into the non-motorized lane. Check the markings and controls
                        nearer the next intersection before choosing a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 904, 14.77 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A tree-lined urban two-way road continues ahead, with one motor-vehicle lane in each
                        direction. My car is in the sole lane of its direction, beside a fenced-off non-
                        motorized corridor on the right; no intersection is clearly visible. (lanes 1, mine 1,
                        full)
Step 2  Left            A broken yellow line, with visible painted segments and gaps, separates my lane from
                        opposing traffic; there is no curb along this line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A low white physical fence separates my lane from the paved corridor on the right;
                        white paint is visible near its approaching end, but its complete line pattern is not
                        visible.
                        white none, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A forward-pointing white arrowhead is partly visible
                        immediately above the hood; the shaft and any possible additional branches are hidden.
Step 4  Cross-check     position: The yellow center line on the left and physical roadway edge on the right
                        agree with one motor-vehicle lane in my direction and ego lane index 1. | roles: The
                        broken yellow line fits a crossable center line; the white paint and fence on the
                        right fit separation from a non-motorized corridor, although the paint pattern is
                        incomplete. | markings: The visible forward arrowhead agrees with the continuing lane,
                        but the hood prevents determining whether the arrow also permits another movement. |
                        unseen: No complete right-side paint pattern or complete arrow shape is claimed; the
                        distant lane end is not readable. | result: consistent
Step 5  Rule            left_boundary: The broken yellow center line may be crossed to overtake when doing so
                        does not affect safety. [CN-5.1.1] "The crossable centre line separates traffic flows
                        in opposite directions. It means vehicles may cross the line to overtake, turn or make
                        a U-turn when this does"
Step 5  Rule            right_boundary: This passage recognizes physical separation at a roadway edge; it
                        provides no permission to cross the fence, which physically bounds the drivable lane.
                        [CN-5.4.5] "Where a non-motorized lane is needed and there is no separating facility
                        between it and the motor vehicle lanes, a motor/non-motor separation line shall be
                        prov"
Step 5  Rule            arrow:straight: The visible forward arrowhead indicates straight-ahead travel, but the
                        hidden remainder prevents determining whether another direction is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): The broken yellow center line permits crossing
                        under CN-5.1.1 when safe and without affecting opposing traffic.
Step 6  change_right    prohibited (WRONG, label not_determined): The physical fence forms the right edge and
                        cannot be crossed as a driving movement.
Step 6  go_straight     allowed (contested, correct): The visible forward arrowhead indicates straight-ahead
                        travel under CN-5.13.1.
Step 6  turn_left       not_determined: The arrow's lower portion is hidden, so a possible left-turn branch
                        cannot be checked.
Step 6  turn_right      not_determined: The arrow's lower portion is hidden, so a possible right-turn branch
                        cannot be checked.
Step 6  u_turn          not_determined: The complete arrow is hidden, so any additional U-turn indication
                        cannot be checked.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight travel follows the visible arrowhead, uncertain turning
                        permissions remain undecided, and the physical right boundary is not treated as
                        crossable.
Advice                  Continue straight within the lane and stay left of the fence. Crossing the yellow
                        broken line would enter opposing traffic space, so do so only when safe; confirm the
                        complete arrow and intersection controls before planning a turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1233, 26.47 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a distant intersection. My car is in the rightmost
                        motor-vehicle lane, beside a separated bicycle lane; traffic obscures the lanes
                        farther left. (lanes None, mine None, insufficient)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        same-direction traffic on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Two parallel solid white lines run beside my lane, with a bicycle lane beyond and
                        separator posts farther ahead; the sidewalk curb is beyond the bicycle lane, not
                        directly beside my lane.
                        white double_solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white right-turn arrow is visible farther ahead in my
                        lane; its right-pointing head is discernible, but the stem is indistinct at this
                        distance.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to the left, and the
                        right motor/non-motor boundary places my lane at the right edge of the motor
                        carriageway. The total lane count and numerical lane index cannot be established
                        through the traffic. | roles: The broken white left line fits a same-direction lane
                        divider; the solid white right lines fit the boundary to the bicycle lane. | markings:
                        The visible right-turn arrow is consistent with this rightmost motor-vehicle lane. No
                        conflicting words or marked waiting area can be identified. | unseen: The arrow stem
                        and distant intersection pavement are not fully resolved. No lane count, stop line, or
                        waiting area has been inferred from the overhead sign. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal boundary prohibits ordinary crossing into the
                        bicycle lane. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            arrow:right: The right-turn guide arrow permits a right turn from this lane and
                        excludes straight, left-turn, and U-turn movements. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  go_straight     prohibited (contested, label allowed): The identifiable right-turn arrow does not show
                        straight ahead.
Step 6  turn_left       prohibited: The identifiable right-turn arrow does not show a left turn.
Step 6  turn_right      allowed: The visible arrowhead indicates a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The identifiable right-turn arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         Consistent: boundary decisions apply only to crossing their respective sides, and
                        movement decisions follow the discernible right-turn arrowhead rather than the
                        overhead sign.
Advice                  Use this lane for a right turn; for another movement, move left safely while the
                        divider remains broken and select the appropriate lane. Do not cross the solid
                        boundary into the bicycle lane, and confirm the distant pavement markings and signals
                        as you approach.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1228, 25.59 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An undivided urban street continues ahead, with oncoming traffic to the left and a
                        sidewalk to the right. My car is in the single visible lane of its direction; no
                        intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faded yellow broken line, with visible long segments and gaps, runs along the left
                        of my lane; opposing traffic is beyond it and there is no curb.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A raised curb borders my lane on the right beside the paved sidewalk, with no separate
                        painted boundary visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line on the left and the roadside curb on the right agree
                        with one lane in my direction and my lane being its leftmost and rightmost lane. |
                        roles: The broken yellow line fits a crossable centre line; the curb forms the
                        physical road edge. | markings: No readable guidance markings appear within my lane in
                        the visible stretch. | unseen: No direction arrows, waiting areas or intersection
                        controls are inferred from the distant or vehicle-obscured pavement. | result:
                        consistent
Step 5  Rule            left_boundary: The broken yellow centre line permits crossing to overtake, turn or
                        make a U-turn only when safety is not affected. [CN-5.1.1] "The crossable centre line
                        separates traffic flows in opposite directions. It means vehicles may cross the line
                        to overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: No supplied passage expressly authorizes crossing a raised curb; this
                        physical roadway edge is not a traversable lane boundary.
Step 6  change_left     allowed (correct): CN-5.1.1 permits crossing the broken yellow centre line when safe,
                        but the space beyond carries opposing traffic.
Step 6  change_right    prohibited (correct): The raised roadside curb is a physical boundary and may not be
                        crossed as a lane change.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-turn marking governs this
                        movement.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-turn marking governs this
                        movement.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs the
                        movement at the next intersection; the centre line governs boundary crossing only.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the lane beside the right curb and keep clear of roadside users. Crossing
                        the broken yellow line is permitted only when safe and would enter opposing traffic;
                        the image does not establish turn permissions at a future intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1003, 21.55 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with a planted median on the left and a
                        curb and wall on the right. My car is in the middle of five same-direction lanes; no
                        lane ending or intersection stop line is clearly visible. (lanes 5, mine 3, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: Both white broken boundaries fit crossable same-
                        direction lane lines. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane. | unseen: No distant or vehicle-obscured
                        markings have been inferred; the next intersection's markings cannot be read. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking in view governs this action.
Step 6  turn_right      not_applicable: No marking in view governs this action.
Step 6  u_turn          not_applicable: No marking in view governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across the broken
                        white line after checking traffic and blind spots. For a turn or U-turn, follow the
                        lane arrows and controls when they become visible farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 894, 13.48 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection with a pedestrian crossing.
                        My car is in the rightmost visible motor-vehicle lane; vehicles obscure the lanes
                        farther left, so the total lane count and numerical lane index cannot be established.
                        (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another motor-vehicle lane on the
                        left; vehicles partly obscure its farther stretch, and no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from a narrow roadside strip used by two-
                        wheelers, with a yellow-painted raised sidewalk curb farther beyond the strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white combined arrow has one head pointing straight
                        ahead and another pointing right.; line:stop_line (partial): A transverse white stop
                        line crosses the lane immediately before the pedestrian crossing.; line:crosswalk
                        (full): Broad white pedestrian-crossing stripes extend across the lane just beyond the
                        stop line.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to the left, while
                        the right edge line bounds the motor-vehicle carriageway; the obscured left side
                        prevents a complete lane count. | roles: The solid white left line fits a same-
                        direction lane separator, and the solid white right line fits a motor/non-motor
                        separation edge. | markings: The straight-or-right arrow agrees with this rightmost
                        motor-vehicle lane; the stop line and crossing do not conflict with it. | unseen: No
                        total lane count or numerical index is inferred from the obscured lanes; the stop line
                        is only partly clear. | result: consistent
Step 5  Rule            left_boundary: The solid white lane separator prohibits crossing into the lane on the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing onto the
                        roadside strip. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The combined arrow permits straight and right movements,
                        excluding left turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The line identifies where to stop when required to yield or wait,
                        without independently requiring a stop for every movement. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, which
                        does not determine any of the seven lane-movement actions.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane line prohibits crossing
                        under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge line normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The straight head of the combined arrow permits continuing straight
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The combined arrow shows no left-turn movement and restricts
                        this lane to straight or right.
Step 6  turn_right      allowed (correct): The right-pointing head permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The combined arrow restricts this lane to straight or right, not
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, without crossing either solid
                        boundary. Obey the traffic signals, stop before the stop line when required, and watch
                        for pedestrians and two-wheelers before turning.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1176, 17.88 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way road descends toward an underpass, with three motor-vehicle lanes in
                        this direction. My car is in the middle lane; no intersection or lane ending is
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No markings are inferred beneath vehicles or beyond
                        the visible road; the next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane line is crossable under
                        CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane line is crossable under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane toward the underpass; either adjacent motor-vehicle lane
                        may be entered across the broken white line when safe. No turn guidance or stopping
                        point is visible, so reassess the markings when approaching an intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 10766, out 783, 10.57 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road descends toward an underpass, with three lanes in this direction.
                        My car is in the middle lane; no intersection or lane ending is visible. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the right; the roadside barrier is beyond that adjacent
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with same-direction lane lines on
                        both sides. | roles: Both boundaries are broken white lines, consistent with crossable
                        same-direction lane separators. | markings: No guidance markings are visible within my
                        lane; the hatched area farther left is outside it. | unseen: No hidden markings or
                        intersection movements have been inferred; the road beyond the visible stretch is not
                        assessed. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane through the underpass. Either adjacent lane may be entered
                        across its broken white separator after checking traffic; no lane change is required
                        by the visible markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 785, 10.83 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way road continues ahead, with two motor-vehicle lanes in this direction.
                        My car is in the rightmost motor-vehicle lane; the next intersection and lane end are
                        not clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with multiple visible dashes and gaps, separates my lane from
                        another same-direction motor lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad solid white line borders my lane on the right, with a narrow roadside strip
                        and a raised sidewalk farther beyond; no curb forms the immediate boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two motor lanes and ego position 2 agree with a lane line on the left and a
                        roadway edge line on the right. | roles: The broken white divider fits a same-
                        direction lane line, and the solid white right boundary fits an edge line. | markings:
                        No arrows, words, symbols, transverse lines or marked waiting areas are discernible in
                        my lane. | unseen: No lane-end marking or movement restriction is inferred from the
                        distant roadway; the exact use of the roadside strip is not established. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing to the roadside
                        strip, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The solid right boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane, or change left across the broken line only when safe; do
                        not cross the solid right boundary in normal driving. Check the markings, signs and
                        signals closer to the next intersection before choosing a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 854, 13.34 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           My car is in a narrow, single-lane access roadway between a planted divider and a
                        sidewalk beside a wall, following a van toward an elevated structure. No intersection
                        or lane ending is visible; the van obscures the road farther ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            An unpainted raised curb borders a planted hedge on the left, with a separate roadway
                        beyond; no painted longitudinal line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           An unpainted raised curb borders the sidewalk beside the wall on the right; no painted
                        longitudinal line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both sides are physical roadway edges, consistent with one lane and my lane
                        being both leftmost and rightmost on this separate roadway. | roles: The curbs define
                        roadway edges without painted lines; neither boundary is a lane divider or painted
                        centre line. | markings: No guidance markings are visible in my lane, so none
                        contradict the boundaries. | unseen: No markings are inferred beneath the van or
                        beyond the visible stretch; the next intersection and lane endpoint cannot be
                        inspected. | result: consistent
Step 5  Rule            left_boundary: This passage recognizes a curb as a clear roadway outline where an edge
                        line may be omitted; no supplied passage expressly governs crossing a curb, but the
                        raised physical edge is not a drivable lane-change boundary. [CN-5.4.5] "Where a non-
                        motorized lane is needed and there is no separating facility between it and the motor
                        vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: This passage recognizes a curb as a clear roadway outline where an
                        edge line may be omitted; no supplied passage expressly governs crossing a curb, but
                        the raised physical edge to the sidewalk is not a drivable lane-change boundary.
                        [CN-5.4.5] "Where a non-motorized lane is needed and there is no separating facility
                        between it and the motor vehicle lanes, a motor/non-motor separation line shall be
                        prov"
Step 6  change_left     prohibited (correct): The raised curb and planted divider form a physical roadway
                        edge, not a crossable lane boundary.
Step 6  change_right    prohibited (correct): The raised curb and sidewalk form a physical roadway edge, not a
                        crossable lane boundary.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane,
                        and no merge or lane ending is visible.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the curbs govern only lateral departures, and the absence of visible
                        directional markings does not establish permission to turn at an unseen intersection.
Advice                  Continue within the curbs, keeping a safe following distance behind the van; do not
                        attempt a lane change over either curb. Reassess turn guidance when the road ahead
                        becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 863, 13.4 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in the
                        rightmost lane beside a separating railing; the left side of the carriageway is
                        outside the image, so the total lane count and numerical lane index cannot be
                        established. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left, with no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous yellowish painted edge follows the raised base of a metal railing on the
                        right, with a separated roadside travel area beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has one head pointing right.; line:stop_line
                        (partial): A transverse white stop line is visible ahead of the arrow, immediately
                        before the pedestrian crossing; glare reduces its contrast.; line:crosswalk (full):
                        White zebra-crossing stripes extend across the lane at the intersection entrance.
Step 4  Cross-check     position: The lane line on the left and physical roadway edge on the right identify
                        the rightmost lane; they do not establish how many additional lanes lie outside the
                        image. | roles: The solid white left line fits a same-direction lane separator. The
                        right railing establishes a physical edge; its yellowish paint does not establish an
                        opposing-traffic boundary. | markings: The right-only arrow agrees with a rightmost
                        intersection approach lane. The stop line and crossing do not add permitted
                        directions. | unseen: No total lane count or numerical index is inferred from the
                        cropped carriageway. Glare makes the stop line less distinct. | result: consistent
Step 5  Rule            left_boundary: The solid white lane separator prohibits crossing into the adjacent
                        lane on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            right_boundary: The marking identifies the roadway edge, and the raised railing base
                        physically excludes a rightward lane change; this passage does not separately specify
                        curb-crossing permission. [CN-5.4.1] "The carriageway edge line marks the edge of
                        motor vehicle lanes or non-motorized vehicle lanes, or the boundary between motor
                        vehicle lanes and non-motorized ve"
Step 5  Rule            arrow:right: The single right-turn arrow permits a right turn and excludes straight,
                        left-turn and U-turn movements from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        without independently requiring a full stop on every approach. [CN-6.4.1-2] "The stop
                        line marks where vehicles stop when yielding or waiting to proceed. It is a solid
                        white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers a crosswalk, and under the
                        supplied definitions it does not determine any of the seven actions.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The raised railing base forms a physical boundary that cannot be
                        crossed as a lane change.
Step 6  go_straight     prohibited (correct): The right-only arrow does not show straight travel.
Step 6  turn_left       prohibited (correct): The right-only arrow does not show a left turn.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The right-only arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane only for a right turn; do not cross the solid left boundary or the
                        right-side railing. Obey the applicable traffic signal, stop before the stop line when
                        required, and watch for pedestrians at the crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1216, 21.39 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight beneath an overpass, with no intersection,
                        ramp or lane ending visible. My car is in the leftmost of three lanes in this
                        direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid line that appears white borders my lane on the left, with a narrow
                        paved strip and median guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car being in lane
                        1 of three. | roles: The broken white right boundary fits a same-direction lane
                        divider. The left line appears white despite occupying the left roadway edge, where
                        the supplied standard specifies yellow; its edge role follows the visible median-side
                        geometry, not an assumed paint color. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        intersection or lane endpoint is visible; no markings beyond the visible stretch are
                        inferred. | result: Consistent observations; the apparent white left edge line differs
                        from the standard's prescribed color.
Step 5  Rule            left_boundary: The solid longitudinal edge line prohibits ordinary crossing to the
                        left, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The solid left boundary prohibits ordinary crossing
                        under CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         Consistent: boundaries govern only their respective crossing actions, and no unseen
                        intersection movements have been inferred.
Advice                  Continue straight within your lane, or move right across the broken divider after
                        checking traffic. Do not cross the solid left edge line; no turn facility or stopping
                        point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 854, 14.52 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, multilane highway continues straight ahead, with guardrails and a paved
                        shoulder on the right. My car is in the rightmost of four same-direction lanes; no
                        intersection or lane ending is visible. (lanes 4, mine 4, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved shoulder with transverse white
                        bars; a guardrail stands beyond the shoulder rather than directly at the lane
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large blue circular pavement marking in my lane contains
                        the clearly readable number 60.; text:speed_limit (partial): Farther ahead is a red-
                        bordered circular speed marking in my lane, but its number is not confidently readable
                        at this distance.
Step 4  Cross-check     position: Four lanes and position four agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white left line fits a
                        crossable lane divider, and the solid white right line fits the right carriageway
                        edge. | markings: The speed markings do not conflict with either boundary. No
                        directional arrow or waiting area is clearly visible. | unseen: The distant speed-
                        limit number is left unread rather than guessed; the transverse shoulder markings are
                        outside my lane. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid longitudinal boundary normally prohibits crossing onto the
                        shoulder, with an emergency exception when safe. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            text:speed_limit: The readable 60 is a lane speed marking, but its blue circular
                        presentation differs from the passage's specified colours, so its precise minimum-or-
                        maximum meaning cannot be established from this passage alone. [CN-5.14.2] "Pavement
                        speed limit markings show the speed limit of a lane and are placed at the start of the
                        lane and at other suitable places where the maximum speed is lim"
Step 5  Rule            text:speed_limit: The farther marking concerns lane speed, but its unreadable number
                        prevents stating its numerical restriction. [CN-5.14.2] "Pavement speed limit markings
                        show the speed limit of a lane and are placed at the start of the lane and at other
                        suitable places where the maximum speed is lim"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid right edge line normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible directional marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-turn marking in my lane governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-turn marking in my lane governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line when safe; do
                        not cross the solid right edge onto the shoulder in normal driving. Check the speed
                        signs and the approaching pavement speed marking, whose number is not readable here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1270, 22.95 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with no clearly visible intersection or
                        lane ending. My car is in the middle of three lanes travelling in this direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A single broken line with yellow-looking paint, visible dashes and gaps separates my
                        lane from the lane occupied by the white minibus; no curb forms this boundary.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible dashes and gaps, separates my lane from the
                        lane occupied by the bus; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lane boundaries with a same-direction lane beyond each agree with my
                        position as lane 2 of 3. | roles: The right broken white line fits a same-direction
                        lane boundary. The yellow-looking left paint is atypical under the supplied colour
                        convention, but vehicles beyond it travel in the same direction and the physical
                        median is farther left; it is not interpreted as an opposing-traffic boundary. |
                        markings: No arrows, words, symbols, transverse lines or marked waiting areas are
                        discernible in my lane. | unseen: No bus-lane designation is inferred merely from the
                        bus. Distant markings and the eventual lane endpoint cannot be resolved. | result: The
                        left boundary has an observed colour-versus-role discrepancy; its visible broken
                        pattern and same-direction context are retained rather than inventing opposing
                        traffic.
Step 5  Rule            left_boundary: The visible broken longitudinal line may be crossed; its unusual colour
                        does not itself establish a crossing prohibition. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing to change
                        lanes when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): The broken left boundary permits crossing under CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.1-2;
                        no reserved-lane marking is visible.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: crossing permissions follow the observed broken boundaries, while no
                        intersection turn permission or bus-lane restriction is inferred from context alone.
Advice                  Continue straight in this lane; the visible broken boundaries permit a lane change
                        only when surrounding traffic leaves a safe gap. Check subsequent signs and markings
                        before planning a turn or entering a potentially reserved lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1068, 21.38 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues ahead with a gentle left bend; no intersection or
                        lane ending is visible. My car is in the middle of three lanes travelling in this
                        direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes with my car in lane 2 agrees with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No visible arrows, words, symbols, transverse lines or marked areas
                        in my lane contradict the boundaries. | unseen: No markings beyond the visible road
                        stretch or hidden by distant vehicles are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to cross into the lane on the
                        left when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line permits my car to cross into the lane on
                        the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action; no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action; no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane and follow the bend; no lane change is required. Either
                        dashed boundary may be crossed when safe, but check nearby vehicles, especially the
                        rider ahead on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 763, 10.49 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight ahead, with barriers separating opposing
                        traffic and lining the right roadside. My car is in the middle of three lanes in this
                        direction; no intersection or lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane beyond
                        each boundary. | roles: Both white broken boundaries fit crossable same-direction lane
                        lines. | markings: No guidance markings are visible within my lane, so none conflict
                        with the boundaries. | unseen: No lane-end markings or intersection layout are
                        inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent left lane
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent right
                        lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken white boundary permits a lane change,
                        but nearby vehicles require careful clearance checks. No turn lane, waiting area or
                        stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 741, 10.53 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined multilane road curves gently right, with no intersection or
                        lane ending visible. My car is in the rightmost of three same-direction lanes. (lanes
                        3, mine 3, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line borders my lane on the right, with a narrow paved
                        shoulder and a concrete barrier beyond it rather than a curb directly on the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white left line fits a
                        crossable lane divider, and the solid white right line fits the right carriageway
                        edge. | markings: No arrows, words, symbols, transverse lines or marked areas are
                        visible in my lane. | unseen: No markings are inferred beyond the visible road; no
                        intersection or lane end is visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right edge line normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No arrow or other in-lane marking restricts continuing
                        along the lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane around the right-hand curve, or change left across the broken
                        line when safe. Do not cross the solid right edge line onto the shoulder during normal
                        driving.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 945, 16.43 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues beneath several elevated roadways, with no
                        intersection or lane ending visible. My car is in the leftmost of three lanes
                        travelling in this direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with a narrow paved margin
                        and a metal median guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my car
                        occupying lane 1 of 3. | roles: The solid yellow left edge and broken white same-
                        direction separator fit their assigned roles. | markings: No guidance marking is
                        visible within my lane, so there is no conflict with the boundaries. | unseen: No
                        intersection markings or movements beyond the visible road stretch have been inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, so my car may not
                        leave the lane across it in ordinary driving. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits my car to change into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left boundary prohibits ordinary
                        crossing under CN-4.2.2-a, and a guardrail lies beyond it.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane line is crossable under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along my lane, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change right across the broken white line after checking for
                        traffic. Do not cross the solid yellow left edge toward the median guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 819, 12.87 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway continues ahead, with no visible intersection, ramp or
                        lane ending. My car is in the leftmost of four lanes in this direction; strong
                        sunlight reduces contrast. (lanes 4, mine 1, full)
Step 2  Left            A continuous yellow line runs along the left of my lane, with a narrow paved strip and
                        median guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane; there is no curb here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and same-direction lane on the right agree with my
                        lane being lane 1 of 4. | roles: The solid yellow left edge and broken white same-
                        direction divider fit their assigned roles. | markings: No arrows, words, symbols or
                        transverse markings are visible in my lane. | unseen: No lane-end features or
                        directions have been inferred beyond the visible highway stretch. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid left boundary is normally prohibited; the median
                        guardrail also prevents movement farther left. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The solid left edge prohibits normal crossing under CN-4.2.2-a,
                        with a median guardrail beyond.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken white line after checking
                        traffic; do not cross the solid left edge. Reduce speed as needed for the strong
                        glare, and follow applicable signs, which are not readable here.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 908, 16.15 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined multilane road continues straight ahead, with no
                        intersection, merge or lane ending visible. My car is in the third of four lanes in
                        this direction. (lanes 4, mine 3, full)
Step 2  Left            A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; the solid shoulder edge and concrete barrier
                        lie farther right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego lane index 3 agree with two lanes to the left and one to
                        the right, with lane lines on both sides. | roles: Both boundaries are broken white
                        lines, consistent with same-direction lane separators. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        distant lane-end features are inferred; the road continues beyond the readable
                        stretch. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across the broken
                        white line after checking traffic and signalling. No turn location or stopping point
                        is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 796, 11.99 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined road continues ahead with two lanes in this direction; no
                        intersection or lane ending is visible. My car is in the left lane, with a truck ahead
                        in the right lane. (lanes 2, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane, with a narrow paved
                        margin and a metal median barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego position 1 agree with a left roadway edge and a same-
                        direction lane to the right. | roles: The broken white right boundary fits a lane
                        line. The left line is visibly white despite being a left roadway edge; its role
                        follows the physical road layout, not an assumed paint color. | markings: No arrows,
                        words, symbols, transverse lines, or waiting areas are visible in my lane. | unseen:
                        No hidden lane-end markings or distant intersection features have been inferred. |
                        result: Consistent spatially; the observed white left edge differs from the yellow
                        left-edge color specified by CN-5.4.3.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits changing into the
                        lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left boundary prohibits ordinary
                        crossing under CN-4.2.2-a, with a median barrier beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral changes, and no unseen lane-end marking
                        is used to decide a turn.
Advice                  Continue straight within your lane and do not cross the solid left edge toward the
                        median barrier. A right lane change is permitted by the dashed line, but check the
                        truck, other traffic, and your blind spot before moving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 881, 15.2 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight ahead, with two lanes in this direction and an
                        emergency shoulder on the right. My car is in the leftmost travel lane; no
                        intersection or lane ending is visible. (lanes 2, mine 1, full)
Step 2  Left            A continuous solid white line borders my lane on the left, with a narrow paved margin
                        and median guardrail beyond it; the guardrail does not directly form the lane
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with multiple visible dashes and gaps, separates my lane from
                        another travel lane on the right, with no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): A white pavement inscription is partly hidden by the hood at the
                        bottom of my lane; the visible strokes resemble the character 小, but the complete
                        inscription cannot be read.
Step 4  Cross-check     position: Two travel lanes and ego position 1 agree with a left roadway edge and a
                        right lane divider. | roles: The broken white right boundary fits a same-direction
                        lane divider. The left edge paint visibly appears white, although the supplied
                        standard specifies yellow for a left edge; its edge role is supported by the median
                        margin and guardrail, not by an assumed paint color. | markings: The partially visible
                        inscription supplies no readable directional restriction; no lane-use arrow or waiting
                        area is visible. | unseen: The hidden portion of the pavement inscription has not been
                        reconstructed, and no arrow has been inferred from its isolated strokes. | result:
                        Consistent observations, with the left-edge color discrepancy explicitly retained.
Step 5  Rule            left_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits changing into the
                        adjacent right travel lane when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            text:other: This passage describes pavement text, but the incomplete inscription
                        supplies no readable restriction on the seven assessed actions. [CN-5.14.1] "Pavement
                        text markings are generally white. They are arranged vertically and read from near to
                        far along the direction of travel ... or horizontally from left t"
Step 6  change_left     prohibited (correct): The solid left longitudinal boundary prohibits ordinary crossing
                        under CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight along this ongoing lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral crossing, the incomplete text does not
                        establish a directional restriction, and not_applicable turn results are not
                        permission to turn on this expressway.
Advice                  Continue in your lane, or move into the right travel lane across the dashed divider
                        only when safe; do not cross the solid left edge. Follow the overhead lane and speed
                        signs, and keep the emergency shoulder clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 10766, out 1100, 20.77 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight ahead, with three traffic lanes and an
                        emergency shoulder on the right. My car is in the rightmost traffic lane; no
                        intersection, ramp or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved emergency shoulder; the
                        guardrail is beyond the shoulder, not at my lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 3 of 3 agrees with a same-direction lane line on the left and a roadway
                        edge line on the right. | roles: The broken white lane divider and solid white right
                        edge line fit their observed roles. | markings: No pavement arrows, words, symbols or
                        transverse markings are visible in my lane; overhead arrows are signs, not pavement
                        markings. | unseen: No hidden marking or unseen intersection layout has been inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        traffic lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The solid edge line beside the emergency stopping lane prohibits
                        ordinary crossing, with an exception for broken-down and rescue vehicles using that
                        lane. [CN-5.4.7] "The edge line at an emergency stopping lane shall be solid. Note:
                        broken-down and rescue vehicles may cross the solid line when using the emergency
                        stopping lan"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid emergency-shoulder edge line prohibits
                        ordinary crossing under CN-5.4.7.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this through lane, or change left across the broken line after checking
                        traffic. Do not cross the solid right edge into the emergency shoulder during ordinary
                        driving; observe the overhead lane and speed signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 806, 11.58 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues ahead, with no
                        intersection or lane ending clearly visible. My car is in the middle lane, behind the
                        dark sedan. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible painted segments and gaps separates my lane from the
                        lane occupied by the light-colored sedan; portions are obscured by vehicles, and there
                        is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible segments and gaps separates my lane from the right-
                        hand traffic lane occupied by the black Volkswagen; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White pavement lettering is visible ahead in my lane, but the
                        sedan obscures much of it and the remaining characters cannot be read reliably.
Step 4  Cross-check     position: Two lane-line boundaries agree with my position in lane 2 of 3, with one
                        same-direction lane on each side. | roles: Both boundaries are broken white lines,
                        consistent with same-direction lane separators. | markings: The partially obscured
                        lettering provides no readable movement instruction; no identifiable arrow or waiting
                        area is visible. | unseen: The obscured lettering has not been transcribed or treated
                        as a directional instruction; distant markings cannot be resolved. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing to the left
                        when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white same-direction lane line permits crossing to the
                        right when safe. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            text:other: This passage describes pavement text, but the unreadable lettering
                        supplies no established permission or prohibition for the seven actions. [CN-5.14.1]
                        "Pavement text markings are generally white. They are arranged vertically and read
                        from near to far along the direction of travel ... or horizontally from left t"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No identified directional marking restricts continuing
                        along the visible lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent; crossing permissions concern the broken boundaries only, and no
                        intersection turn permission is inferred from unreadable lettering.
Advice                  Continue in the middle lane; either broken boundary permits a lane change, but nearby
                        vehicles require a safe gap. Reassess the obscured pavement lettering as it becomes
                        visible, and do not infer turning permission at an unseen intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 10766, out 1131, 21.98 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, multilane highway continues straight ahead, with a median barrier on the
                        left and a shoulder on the right. My car is in the rightmost of three same-direction
                        lanes; no intersection or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved shoulder, with a guardrail
                        farther beyond the shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large white pavement number 60 is painted in my lane near
                        the car.; text:speed_limit (full): A yellow pavement number 100 is visible farther
                        ahead in my lane.
Step 4  Cross-check     position: The rightmost position agrees with a same-direction lane line on the left
                        and a roadway edge line on the right. | roles: The broken white lane divider and solid
                        white right edge fit their observed roles. | markings: The white 60 and yellow 100 are
                        compatible minimum and maximum speed markings; neither specifies a turning movement. |
                        unseen: No arrows, waiting areas, or intersection markings are identifiable; distant
                        pavement details are too small to read. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the solid right boundary onto the shoulder is normally
                        prohibited, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            text:speed_limit: The white 60 denotes the lane's minimum speed of 60 km/h.
                        [CN-5.14.2] "Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is lim"
Step 5  Rule            text:speed_limit: The yellow 100 denotes the lane's maximum speed of 100 km/h.
                        [CN-5.14.2] "Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is lim"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white boundary normally prohibits
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No directional marking restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and observe the marked 60–100 km/h speed range, subject
                        to conditions and posted controls. A left lane change is permitted when safe, but
                        check the nearby truck carefully; do not cross the solid right edge onto the shoulder
                        in normal driving.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1417, 30.17 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road leads onto a bridge beneath overhead lane-control signals. My car
                        is in a reversible lane, with opposing traffic to the left and two ordinary same-
                        direction lanes to the right. (lanes 3, mine 1, full)
Step 2  Left            Two parallel broken yellow lines form the left boundary, with visible painted segments
                        and gaps; opposing traffic lies beyond and there is no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel broken yellow lines form the right boundary, with segments and gaps
                        visible; a white marking runs alongside them on the adjacent-lane side, and there is
                        no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The reversible lane is the leftmost of the three lanes on this side of the
                        opposing traffic; two ordinary lanes lie to its right. | roles: Parallel broken yellow
                        lines on both sides fit the reversible-lane definition rather than ordinary same-
                        direction lane dividers. | markings: No readable arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: The lane's permitted
                        operating direction and the distant intersection layout cannot be established from
                        pavement markings alone. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible lane, in which
                        left turns and U-turns on the road section are prohibited except in special cases.
                        [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed on
                        both sides of it. Within a tidal lane on a road section, vehicles are prohibited from
                        turni"
Step 5  Rule            right_boundary: The broken boundary permits leaving my lane to the right when safe;
                        the reversible-lane identification is supplied by CN-5.3.1-2. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     not_determined (correct): The broken marking is crossable, but the space beyond
                        carries opposing traffic and is part of the lane-controlled roadway; its availability
                        for my car is not established.
Step 6  change_right    allowed (WRONG, label not_determined): CN-4.2.2-a permits crossing the broken boundary
                        to leave my lane for the ordinary same-direction lane.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-turn marking in my lane governs the movement at
                        the next intersection; the reversible-lane rule instead prohibits left turns on the
                        road section.
Step 6  turn_right      not_applicable: No marking governs this movement at the next intersection.
Step 6  u_turn          not_applicable: No arrow or prohibited-turn marking in my lane governs the movement at
                        the next intersection; the reversible-lane rule instead prohibits U-turns on the road
                        section.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         The next-intersection movements are kept separate from the reversible-lane road-
                        section restrictions, and crossing left remains undecided because the adjacent lane's
                        permitted operating direction is not established.
Advice                  Check the overhead lane-control indication before continuing in this reversible lane;
                        pavement permission to proceed does not establish that the lane is currently open. You
                        may leave across the broken right boundary when safe, but do not move left toward
                        opposing traffic or make a left turn or U-turn on this road section.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions ['change_left
                        not_determined with full evidence']
Tokens                  in 10766, out 1224, 28.15 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An undivided urban road with opposing traffic to the left continues straight ahead; no
                        intersection or lane ending is clearly visible. My car is in the middle of three lanes
                        travelling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside barrier is beyond that adjacent lane,
                        not at my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lane-line boundaries agree with my lane being lane 2 of 3, with a same-
                        direction lane on each side. | roles: Both boundaries are broken white lines,
                        consistent with crossable same-direction lane dividers. | markings: No guidance
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: Vehicles obscure some pavement farther ahead; no markings or intersection
                        layout are inferred behind them. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the left when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane on the right when safe. [CN-5.2.1-2] "The crossable lane line separates
                        traffic flows in the same direction and is placed between lanes of the same direction.
                        It is a broken white line."
Step 6  change_left     allowed (contested, correct): The visible broken white lane divider is crossable under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane divider is crossable under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either broken white boundary may be crossed after
                        checking surrounding traffic and blind spots. No turn allocation or stopping point is
                        visible, so reassess the markings as the road ahead becomes clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 840, 12.87 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road continues ahead, with opposing vehicles to the left, a taxi
                        ahead and an articulated bus alongside on the right. My car appears to occupy a
                        reversible lane; the bus obscures the right-hand carriageway extent, so the number of
                        lanes currently serving my direction cannot be established. (lanes None, mine None,
                        insufficient)
Step 2  Left            Two parallel broken yellow lines, with visible segments and gaps, run along the left
                        side; opposing vehicles are beyond them and no curb forms this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Short visible portions of paired yellow broken lines run along the right side beside
                        the bus, which hides much of their length; no curb is visible at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Paired broken yellow boundaries indicate a reversible lane rather than an
                        ordinary fixed-direction lane; its current directional lane count and index cannot be
                        reliably assigned. | roles: The double broken yellow pattern fits reversible-lane
                        boundaries, although the right boundary is partly obscured. | markings: No readable
                        arrow, word, symbol, transverse line or waiting area is visible in my lane. | unseen:
                        The bus hides much of the right boundary and roadway beyond; distant pavement markings
                        and the lane's eventual intersection termination cannot be read. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify my lane as reversible, in which
                        left turns and U-turns on the road section are prohibited except in special cases.
                        [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed on
                        both sides of it. Within a tidal lane on a road section, vehicles are prohibited from
                        turni"
Step 5  Rule            left_boundary: The broken boundary permits crossing, subject to safe operation and the
                        current traffic arrangement. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The partly visible paired broken yellow lines support identification
                        of my own lane as a reversible lane. [CN-5.3.1-2] "The tidal lane line marks a tidal
                        (reversible) lane and is placed on both sides of it. Within a tidal lane on a road
                        section, vehicles are prohibited from turni"
Step 5  Rule            right_boundary: The visible broken boundary permits leaving my reversible lane across
                        it, provided it is safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (WRONG, label prohibited): The broken left boundary is crossable under
                        CN-4.2.2-a, but opposing traffic beyond makes crossing unsafe at present.
Step 6  change_right    allowed (contested, label prohibited): The visible broken right boundary is crossable
                        under CN-4.2.2-a; the adjacent bus must first be clear.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       prohibited: No readable arrow or prohibited-turn marking establishes the movement at
                        the next intersection; the reversible-lane rule prohibits left turns on the road
                        section.
Step 6  turn_right      not_applicable: No visible marking governs a right turn at the next intersection.
Step 6  u_turn          prohibited: CN-5.3.1-2 prohibits U-turns within this reversible lane on the road
                        section.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         The broken boundaries permit crossing as markings, not as an assurance of safety; the
                        reversible-lane restriction prohibits left turns and U-turns on this road section, and
                        no unseen intersection movement permission is assumed.
Advice                  Continue straight only after confirming that the reversible lane is open in your
                        direction from its controlling signals or signs. Do not cross toward the approaching
                        traffic or move right alongside the bus; do not turn left or make a U-turn within this
                        reversible road section.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        ['turn_left, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 10766, out 1248, 26.13 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road carries traffic in both directions, with a yellow double-broken-line
                        lane to the left and another same-direction lane to the right. My car is in the
                        leftmost of two clearly visible ordinary lanes in its direction; the distant
                        intersection approach is partly obscured by traffic. (lanes 2, mine 1, full)
Step 2  Left            Two parallel broken yellow lines form the left boundary, with visible pavement gaps;
                        vehicles facing my car occupy the lane beyond, which also has yellow markings on its
                        far side.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line, with several visible dashes and gaps, separates my lane from the
                        same-direction lane occupied by the white minibus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the leftmost ordinary same-direction lane, beside a specially
                        marked lane on the left and another ordinary same-direction lane on the right. |
                        roles: The double broken yellow boundary fits a tidal-lane boundary, while the broken
                        white boundary fits a crossable same-direction lane divider. | markings: No arrows,
                        words, symbols, transverse lines or waiting areas can be identified in the visible
                        part of my lane. | unseen: No distant lane-use arrow or stop line is inferred through
                        the vehicles; the tidal lane's current operating instructions are not readable. |
                        result: consistent
Step 5  Rule            left_boundary: The double broken yellow lines identify a tidal lane; under the
                        reserved-lane instruction, my ordinary car must not enter it. [CN-5.3.1-2] "The tidal
                        lane line marks a tidal (reversible) lane and is placed on both sides of it. Within a
                        tidal lane on a road section, vehicles are prohibited from turni"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): The double broken yellow boundary borders a tidal lane, which is
                        treated as reserved and may not be entered.
Step 6  change_right    allowed (correct): The broken white same-direction lane line is crossable under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the tidal-lane restriction applies to vehicles inside that lane, not mine.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane or change right across the broken white line when safe; do not
                        enter the yellow-double-broken-line lane to the left. The roadside sign directs left-
                        turning vehicles into the auxiliary road, so check the upcoming access and lane
                        guidance before preparing a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1150, 24.39 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight beside a bus station. My car is in a reversible lane,
                        with opposing traffic to the left and a bus lane to the right; the distant
                        intersection approach is partly obscured. (lanes 2, mine 1, partial)
Step 2  Left            Two parallel broken yellow lines run along the left side, with visible paired segments
                        and gaps; oncoming vehicles are beyond them and there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Paired broken yellow markings run along the right side toward the bus station; their
                        farther portions are less distinct, and the lane beyond contains bus-lane lettering.
                        yellow double_dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrowhead is visible immediately
                        ahead of the hood, with its lower shaft hidden.
Step 4  Cross-check     position: The apparent arrangement is my reversible lane at the left of the currently
                        forward-running lanes, with a bus lane on its right; the directional lane count
                        depends on the reversible allocation. | roles: Paired broken yellow boundaries fit a
                        reversible lane, rather than ordinary same-direction lane dividers. | markings: The
                        visible straight arrow agrees with continuing along this lane; no turn arrow or
                        waiting area is visible. | unseen: The arrow shaft is hidden by the hood, the right
                        boundary is less distinct, and distant pavement markings are obscured; no stop line is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow boundary identifies a reversible lane, in
                        which left turns and U-turns are prohibited on the road section. [CN-5.3.1-2] "The
                        tidal lane line marks a tidal (reversible) lane and is placed on both sides of it.
                        Within a tidal lane on a road section, vehicles are prohibited from turni"
Step 5  Rule            left_boundary: The broken boundary permits leaving my lane across it, subject to safe
                        traffic conditions. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The bus lane beyond this boundary is reserved, so an ordinary car may
                        not enter it. [CN-6.9.1] "The bus lane line shows that vehicles other than buses shall
                        not enter the lane. It consists of a broken white line and white text. The broken line
                        has 5 m segm"
Step 5  Rule            arrow:straight: The identifiable straight-ahead arrow permits straight travel and does
                        not permit turning movements. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (WRONG, label prohibited): The broken yellow boundary permits leaving the
                        reversible lane under CN-4.2.2-a; oncoming traffic makes crossing unsafe at present.
Step 6  change_right    prohibited (contested, correct): The adjacent bus lane is reserved under CN-6.9.1.
Step 6  go_straight     allowed (correct): The visible straight arrow indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not indicate a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not indicate a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not indicate a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: permission to cross the broken left boundary is not a finding that
                        crossing into the visible oncoming traffic is safe.
Advice                  Continue straight only while the reversible-lane signal permits your direction. Stay
                        out of the bus lane and do not move left into the visible oncoming traffic; follow the
                        overhead lane-control indications.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 10766, out 1255, 26.92 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road continues straight past a station platform on the left, with
                        no intersection or lane ending clearly visible. My car is in the middle of three
                        visible lanes, between paired broken yellow lines indicating a reversible lane; its
                        current operating direction is not visible. (lanes 3, mine 2, partial)
Step 2  Left            Two parallel yellow broken lines, with repeated painted segments and gaps, separate my
                        lane from another lane on the left; no curb forms this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with repeated painted segments and gaps, separate my
                        lane from a lane on the right containing large yellow pavement text; no curb forms
                        this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the middle of three visible lane spaces, consistent with a
                        reversible lane bounded on both sides by special-lane lines; the number currently
                        assigned to my direction cannot be confirmed. | roles: The paired broken yellow lines
                        on both sides fit the reversible-lane definition, rather than ordinary same-direction
                        lane dividers. | markings: No readable arrow, word, symbol or transverse marking is
                        visible inside my lane; the large pavement text on the right lies outside it. |
                        unseen: The reversible lane's current operating direction and the distant end of the
                        lane are not visible; neither has been inferred. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines mark the reversible lane, whose vehicles
                        may not turn left or make a U-turn on this road section except in special cases.
                        [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed on
                        both sides of it. Within a tidal lane on a road section, vehicles are prohibited from
                        turni"
Step 5  Rule            left_boundary: The broken boundary permits crossing when leaving my reversible lane,
                        subject to safe conditions and the operating direction of the adjacent lane.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: The paired broken yellow lines identify the other side of the
                        reversible lane, in which left turns and U-turns are prohibited except in special
                        cases. [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed
                        on both sides of it. Within a tidal lane on a road section, vehicles are prohibited
                        from turni"
Step 5  Rule            right_boundary: The broken boundary permits crossing when leaving my reversible lane,
                        subject to safe conditions and any reservation applying to the adjacent lane.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (contested, correct): The broken left boundary permits leaving my lane under
                        CN-4.2.2-a; the reversible-lane marking does not itself prohibit leaving.
Step 6  change_right    not_determined (contested, label prohibited): The broken right boundary permits
                        leaving my lane, but the adjacent lane's large pavement text is only partly visible
                        and its possible reservation cannot be established.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane; its current operating direction must still be checked.
Step 6  turn_left       prohibited: CN-5.3.1-2 prohibits left turns from within a reversible lane on a road
                        section except in special cases.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking in my lane governs a
                        right turn.
Step 6  u_turn          prohibited: CN-5.3.1-2 prohibits U-turns within a reversible lane on a road section
                        except in special cases.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: broken boundaries permit leaving rather than entering the reversible lane,
                        the uncertain reservation on the right prevents a definite right-change decision, and
                        straight-ahead permission does not establish that the reversible lane is currently
                        open.
Advice                  Confirm that the reversible lane is open in your direction before continuing; its
                        markings prohibit left turns and U-turns here. Check the adjacent lanes' operating
                        direction and reservation before crossing either broken boundary, particularly the
                        text-marked lane on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['change_right
                        not_determined with full evidence', 'turn_left, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 10766, out 1243, 22.16 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road carries queued traffic toward a distant junction obscured by
                        vehicles and sun glare. My car is immediately right of a lane bounded by paired broken
                        yellow lines; the full number of same-direction lanes and my index cannot be
                        established reliably. (lanes None, mine None, insufficient)
Step 2  Left            Two parallel yellow broken lines, with visible gaps in both lines, run along my left;
                        another traffic lane lies beyond, and no curb forms this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The special-lane boundary on the left and ordinary lane line on the right
                        fit the visible neighboring lanes, but the full lane count and ego index remain
                        uncertain. | roles: Paired broken yellow lines fit a tidal-lane boundary; the broken
                        white line fits separation of ordinary same-direction lanes. | markings: No readable
                        guidance markings are visible within my lane, so none contradict the boundaries. |
                        unseen: No distant arrows, stop line, or waiting area is inferred through the traffic
                        and glare; the tidal lane's current operating direction is not established. | result:
                        consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a tidal lane, which is treated
                        as reserved across this boundary, so my ordinary car must not change into it.
                        [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed on
                        both sides of it. Within a tidal lane on a road section, vehicles are prohibited from
                        turni"
Step 5  Rule            right_boundary: The broken white lane line permits changing to the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The paired broken yellow special-lane boundary
                        identifies an adjacent reserved tidal lane; entry is prohibited.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken white line only when safe; do
                        not enter the tidal lane on the left. Reduce speed for the queue and glare, and
                        reassess junction arrows, signals, and stopping requirements when they become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 964, 17.83 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way road approaches a signalized intersection. My car is in the middle of
                        three visible lanes in this direction, behind a coach; the intersection approach is
                        partly obscured by traffic. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with long dashes and gaps separates my lane from another same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken white line, with visible dashes and gaps, separates my lane from a
                        reddish-paved lane occupied by cars on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow directly ahead points straight forward, with no
                        visible turning branch.
Step 4  Cross-check     position: Lane lines on both sides agree with my position as lane 2 of 3. | roles:
                        Both white broken boundaries fit separation of same-direction lanes. | markings: The
                        straight-ahead arrow is consistent with the lane continuing toward the intersection. |
                        unseen: The coach and other traffic obscure the distant pavement and any stop line. No
                        reserved-lane designation is readable in the right lane; reddish pavement alone is not
                        treated as one. | result: consistent
Step 5  Rule            left_boundary: The broken white same-direction lane line permits crossing into the
                        lane on the left. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The visible broken white lane line permits crossing to the right; no
                        readable reserved-lane marking establishes a separate restriction. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2; no
                        visible marking establishes that the adjacent lane is reserved.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, obeying the signals ahead and stopping before the
                        stop line when required. For a turn, select an appropriately marked lane before the
                        intersection; check the reddish right lane for any reserved-use signs or markings
                        before entering it.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1060, 19.23 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road with reversible-lane control signs overhead and an
                        intersection in the distance. My car is immediately right of paired yellow broken
                        lines; the reversible lanes' current direction and the distant lane end cannot be
                        established from the pavement view. (lanes None, mine None, insufficient)
Step 2  Left            Two parallel yellow broken lines, with visible gaps, separate my lane from the
                        vehicle-occupied lane on the left; there is no curb along this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another motor-vehicle lane on the right, without a curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Another ordinary lane is visible on my right, while reversible lanes lie to
                        my left; their direction prevents a reliable total count or left-based index. | roles:
                        Paired broken yellow lines fit a reversible-lane boundary, and the broken white right
                        boundary fits a same-direction lane divider. | markings: No readable guidance marking
                        is visible within my lane; markings in the roadside lane are outside it. | unseen: No
                        arrow or stop line is inferred beneath vehicles or at the distant intersection. |
                        result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible lane; under the
                        reserved-lane definition, my ordinary car must not change into it. [CN-5.3.1-2] "The
                        tidal lane line marks a tidal (reversible) lane and is placed on both sides of it.
                        Within a tidal lane on a road section, vehicles are prohibited from turni"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The paired broken yellow boundary borders a
                        reversible special lane, which is treated as reserved.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: Vehicles and distance obscure the intersection approach where a
                        movement arrow could decide this action.
Step 6  turn_right      not_determined: Vehicles and distance obscure the intersection approach where a
                        movement arrow could decide this action.
Step 6  u_turn          not_determined: Vehicles and distance obscure any movement marking at the lane end.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane or change right only when safe; do not enter the reversible lane
                        on the left. Follow the overhead lane controls and check the intersection arrows and
                        stopping position as they become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1129, 26.33 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a broad urban intersection, approaching a zebra crossing with traffic
                        continuing ahead. Glare, worn markings and the open intersection pavement prevent a
                        reliable count of the lanes or identification of the car's lane position. (lanes None,
                        mine None, insufficient)
Step 2  Left            No continuous left boundary can be traced beside the car; glare and traffic obscure
                        the pavement, and no curb directly bounding this lane is visible.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           Faint white broken-looking paint is visible to the right on the intersection pavement,
                        but its segments and alignment cannot be traced confidently as this lane's boundary;
                        no curb directly bounds the lane.
                        white dashed, curb no, unknown, evidence partial
Step 3  Markings        line:crosswalk (partial): A row of broad white zebra-crossing stripes crosses the path
                        ahead, with some portions obscured by vehicles and riders.
Step 4  Cross-check     position: Neither boundary establishes a reliable lane count or lane index; both
                        numbers remain unknown. | roles: The faint white paint on the right could be
                        intersection guidance, but its role and complete pattern cannot be established. |
                        markings: The visible crosswalk does not establish lane-use directions; no readable
                        arrow, pavement word or waiting area is visible in the car's path. | unseen: No unseen
                        arrow, stop line or lane allocation is inferred; the right-hand broken pattern is only
                        tentative. | result: consistent
Step 5  Rule            left_boundary: No identifiable boundary is available to establish whether crossing to
                        the left is permitted.
Step 5  Rule            right_boundary: The faint paint cannot confidently be classified as a crossable lane
                        boundary, so it does not establish permission to change right.
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and under the
                        supplied definitions this marking does not decide any of the seven actions.
Step 6  change_left     not_determined (correct): The left boundary is not identifiable, leaving crossing
                        permission undecided.
Step 6  change_right    not_determined (correct): The right-hand paint's boundary role and pattern are
                        uncertain, leaving crossing permission undecided.
Step 6  go_straight     allowed (contested, label not_determined): No visible lane-use arrow restricts
                        continuing straight; the crosswalk does not govern this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: uncertain boundaries do not authorize lane changes, and the crosswalk is
                        not treated as a directional restriction.
Advice                  Continue cautiously along the established traffic path rather than making a lateral
                        move across uncertain boundaries. Green signals are visible ahead, but watch for
                        pedestrians, cyclists and other vehicles at the crossing; this image does not
                        establish a suitable turning lane.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation none_needed, contradictions []
Tokens                  in 10766, out 1049, 20.08 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road continues toward a distant signal-controlled junction beneath
                        overhead lane-control displays. My car is in the left of two clearly visible ordinary
                        lanes in this direction, immediately right of a separately marked reversible lane.
                        (lanes 2, mine 1, full)
Step 2  Left            Two parallel yellow broken lines, with aligned gaps visible ahead, separate my lane
                        from a lane occupied by a taxi; no curb forms this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A single broken white line, with long dashes and clear gaps, separates my lane from
                        another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the leftmost ordinary lane, with a separately controlled
                        reversible lane on its left and another ordinary lane on its right; this agrees with
                        the boundary roles. | roles: The paired broken yellow lines fit a reversible-lane
                        boundary, and the broken white line fits a crossable same-direction lane divider. |
                        markings: No arrows, words, symbols or transverse markings are readable in my lane, so
                        none contradict the boundaries. | unseen: No distant or vehicle-obscured pavement
                        marking is inferred; the overhead displays are context, not pavement arrows. | result:
                        consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible lane, which is
                        treated as reserved across this boundary and therefore may not be entered by my
                        ordinary car. [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is
                        placed on both sides of it. Within a tidal lane on a road section, vehicles are
                        prohibited from turni"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): The paired broken yellow boundary borders a
                        reversible special lane, treated as reserved under the special-lane decision
                        convention.
Step 6  change_right    allowed (correct): The broken white lane divider is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible in-lane arrow restricts continuing straight,
                        and neither boundary governs this movement.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken white line when safe; do not
                        enter the reversible lane on the left. Follow the overhead lane-control displays and
                        upcoming signals, and check later pavement arrows before choosing a turning movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1006, 17.7 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues toward a distant intersection. My car is between paired broken
                        yellow lines marking a reversible lane; the permitted directions of the adjacent lanes
                        and the reversible lane's current operating direction cannot be established from the
                        photo. (lanes None, mine None, insufficient)
Step 2  Left            Two parallel yellow broken lines, with visible segments and gaps, bound my lane on the
                        left; another paved lane lies beyond, with no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with visible segments and gaps, bound my lane on the
                        right; another paved lane with large pavement text lies beyond, with no curb at this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The paired broken yellow boundaries identify my lane as a reversible lane,
                        so a reliable count and index among lanes currently travelling in my direction cannot
                        be assigned. | roles: The double broken yellow lines on both sides fit reversible-lane
                        boundaries. | markings: No readable guidance marking appears inside my lane; the large
                        text to the right is outside its boundary. | unseen: No operating direction or distant
                        intersection marking is inferred; the far end of the lane is too distant to inspect
                        reliably. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible lane, within which
                        left turns and U-turns are prohibited on the road section except in special cases.
                        [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed on
                        both sides of it. Within a tidal lane on a road section, vehicles are prohibited from
                        turni"
Step 5  Rule            left_boundary: The broken boundary permits crossing to leave my lane when safe,
                        subject to the adjacent lane being open to my direction. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The paired broken yellow lines identify the other boundary of the
                        reversible lane. [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and
                        is placed on both sides of it. Within a tidal lane on a road section, vehicles are
                        prohibited from turni"
Step 5  Rule            right_boundary: The broken boundary permits crossing to leave my lane when safe,
                        subject to the adjacent lane being open to my direction. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken left boundary permits leaving this reversible lane under
                        CN-4.2.2-a; the adjacent lane's operating direction must be checked separately.
Step 6  change_right    allowed (contested, label prohibited): The broken right boundary permits leaving this
                        reversible lane under CN-4.2.2-a; the adjacent lane's operating direction must be
                        checked separately.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane; its
                        current operating direction must be checked separately.
Step 6  turn_left       not_determined: The reversible-lane rule prohibits left turns on the road section, but
                        the requested movement is at the next intersection, whose lane-use markings are too
                        distant to read.
Step 6  turn_right      not_determined: The lane-use markings at the distant intersection cannot be read.
Step 6  u_turn          not_determined: The reversible-lane rule prohibits U-turns on the road section, but
                        the requested movement is at the next intersection, whose lane-use markings are too
                        distant to read.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: broken boundaries permit leaving the lane, while unreadable intersection
                        guidance leaves turning movements undecided; marking permissions do not establish the
                        reversible lane's current operating direction.
Advice                  Check the reversible-lane control signals and adjacent traffic directions before
                        continuing or crossing either broken boundary. Do not turn left or make a U-turn along
                        this road section; check the intersection's guidance before choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1208, 20.78 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road runs between concrete roadside barriers, with no intersection or lane
                        ending visible. My car is in the central reversible lane, between paired broken yellow
                        lines; its current assigned direction cannot be established from the photo. (lanes
                        None, mine 1, partial)
Step 2  Left            Two parallel broken yellow lines, with visible segments and gaps, separate my lane
                        from the lane on the left; there is no curb along this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel broken yellow lines, with visible segments and gaps, separate my lane
                        from the lane on the right; there is no curb along this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the central reversible lane, to the left of the ordinary right-
                        hand traffic lane; counting it as available in my direction would depend on its
                        current assignment, so the directional lane count is uncertain. | roles: Paired broken
                        yellow lines on both sides match the specified reversible-lane boundary form. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane; this does not conflict with the reversible-lane boundaries. | unseen: No
                        current reversible-lane assignment or distant intersection markings are inferred;
                        vehicles obscure part of the road ahead. | result: consistent
Step 5  Rule            left_boundary: This paired broken yellow boundary identifies my lane as reversible,
                        where left turns and U-turns are prohibited on the road section except in special
                        cases. [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and is placed
                        on both sides of it. Within a tidal lane on a road section, vehicles are prohibited
                        from turni"
Step 5  Rule            left_boundary: The broken boundary permits crossing out of my lane, subject to safe
                        traffic conditions. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: This paired broken yellow boundary confirms that my car is inside a
                        reversible lane. [CN-5.3.1-2] "The tidal lane line marks a tidal (reversible) lane and
                        is placed on both sides of it. Within a tidal lane on a road section, vehicles are
                        prohibited from turni"
Step 5  Rule            right_boundary: The broken boundary permits crossing out of my lane, subject to safe
                        traffic conditions. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (WRONG, label prohibited): The broken left boundary permits leaving my lane
                        under CN-4.2.2-a; this is not permission to enter opposing traffic.
Step 6  change_right    allowed (WRONG, label not_determined): The broken right boundary permits leaving my
                        lane under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane; its
                        current directional assignment must be checked separately.
Step 6  turn_left       prohibited: CN-5.3.1-2 prohibits left turns within a reversible lane on this road
                        section.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: CN-5.3.1-2 prohibits U-turns within a reversible lane on this road
                        section.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: crossing permissions describe the markings only, not the safety of
                        entering adjacent traffic, and straight-ahead permission does not establish the
                        reversible lane's current assignment.
Advice                  Check the reversible-lane controls before proceeding: a vehicle ahead appears to face
                        toward your car. Do not enter opposing traffic; leave to the ordinary right-hand lane
                        only when safe, and do not turn left or make a U-turn here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['turn_left, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 10766, out 1161, 20.67 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road approaches a distant intersection. My car is in the left of two ordinary
                        same-direction lanes, with a separately marked reversible lane to the left and a bus
                        in the ordinary lane to the right. (lanes 2, mine 1, full)
Step 2  Left            Two parallel broken yellow lines, with repeated paired dashes and gaps, border my lane
                        on the left; another similarly bounded strip lies beyond, and there is no curb at this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from the lane
                        occupied by the bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow directly ahead has one forward-pointing head and
                        no turn branch.
Step 4  Cross-check     position: The right lane line agrees with another ordinary same-direction lane on the
                        right. The left special-lane boundary separates the reversible lane, which is not
                        counted as an ordinary lane of my direction. | roles: The paired broken yellow lines
                        fit a reversible-lane boundary, and the broken white line fits a crossable same-
                        direction lane divider. | markings: The straight arrow agrees with continuing along my
                        lane; no visible word, turn arrow, or waiting area contradicts it. | unseen: No
                        direction is assumed for the reversible lane. Vehicles and distance obscure the far
                        approach, so no additional distant pavement markings or stop line are claimed. |
                        result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible lane; under the
                        reserved-special-lane instruction, my ordinary car must not enter it. [CN-5.3.1-2]
                        "The tidal lane line marks a tidal (reversible) lane and is placed on both sides of
                        it. Within a tidal lane on a road section, vehicles are prohibited from turni"
Step 5  Rule            right_boundary: The broken white lane divider permits crossing into the adjacent
                        ordinary same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line
                        separates traffic flows in the same direction and is placed between lanes of the same
                        direction. It is a broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits straight travel and excludes
                        left turns, right turns, and U-turns from my lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The paired broken yellow boundary borders a reserved reversible
                        lane, which my ordinary car must not enter.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the special-lane restriction overrides the apparent crossability of its
                        broken boundary, and the arrow governs movements rather than lane changes.
Advice                  Remain in this lane to continue straight, and do not enter the reversible lane on the
                        left. A rightward lane change is permitted by the divider when safe; check the bus and
                        other traffic, and obey the intersection signals and any stop line as they become
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1108, 20.64 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road with a fenced median approaches an intersection beneath elevated
                        structures. My car is in the middle lane of five lanes travelling in this direction.
                        (lanes 5, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible segments and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead and no turning branch.
Step 4  Cross-check     position: Two lanes lie on either side of my lane, consistent with lane 3 of 5 and
                        lane-line boundaries on both sides. | roles: Both white broken boundaries fit
                        separators between same-direction lanes. | markings: The straight arrow agrees with
                        the through lane; the arrow in the neighbouring right lane is outside my lane. |
                        unseen: The distant end of the approach is partly obscured by vehicles; no hidden stop
                        line, additional arrow or waiting area has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            arrow:straight: The straight-only guide arrow allows continuing straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to continue straight, obeying the intersection signals. For a turn,
                        move safely across a broken boundary into an appropriately marked lane before reaching
                        any solid approach lines; do not turn directly from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1194, 24.21 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in the
                        straight-ahead lane, with queued lanes to the left and a right-turn lane to the right.
                        (lanes 4, mine 3, full)
Step 2  Left            A solid white line, with short white teeth projecting toward the adjacent lane on its
                        left, separates my lane from a same-direction lane; there is no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the same-direction lane on the right;
                        there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.;
                        line:stop_line (partial): A transverse white stop line is faintly visible near the far
                        end of my lane, immediately before the pedestrian crossing.; line:crosswalk (full):
                        White pedestrian-crossing stripes extend across my lane at the intersection.
Step 4  Cross-check     position: Two same-direction lanes to the left and one to the right agree with lane 3
                        of 4 and lane-line boundaries on both sides. | roles: Both boundaries are white solid
                        separators between same-direction lanes. The teeth on the left project into the
                        neighboring variable guide lane, not into my lane. | markings: The straight arrow
                        agrees with the ordinary through lane between the solid boundaries; neighboring lane
                        text and arrows do not govern my lane. | unseen: The distant stop line is faint and is
                        assigned partial evidence; no hidden words or additional arrowheads are assumed. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white separator prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white separator prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow allows proceeding straight and excludes
                        left turns, right turns and U-turns from my lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to wait or yield,
                        but does not itself require a full stop on every approach. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically governs the pedestrian crossing, and
                        it does not determine any of the seven lane-movement actions.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white left lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white right lane boundary
                        prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight and do not cross either solid boundary. Obey
                        the traffic signals, stopping before the stop line when required and keeping the
                        pedestrian crossing clear; a turn requires choosing an appropriate lane before the
                        solid-line section.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions False,
                        unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1391, 27.37 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight ahead, with a median fence on the left and a
                        bus near the right curb. My car is in the second of four visible same-direction lanes;
                        no intersection or lane ending is clearly visible. (lanes 4, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from the lane
                        beside the median; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from the lane
                        occupied by the dark car; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second of four lanes has a same-direction lane immediately on each side,
                        consistent with both boundaries being lane lines. | roles: Both white broken
                        boundaries fit same-direction crossable lane lines. | markings: No guidance markings
                        are readable in the visible portion of my lane, so none contradict the boundaries. |
                        unseen: The truck and distance obscure the farther pavement; no markings or
                        intersection layout are inferred there. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane line permits crossing
                        under CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent white broken boundary may be crossed
                        only when a safe gap is available. Watch the nearby vehicles and reassess turn-lane
                        guidance when the pavement farther ahead becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 10766, out 833, 12.15 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is at a broad signal-controlled urban intersection, immediately before a zebra
                        crossing, with several vehicles ahead and alongside. Traffic and the hood obscure the
                        approach lane layout, so the number of lanes and the car's lane index cannot be
                        reliably counted. (lanes None, mine None, insufficient)
Step 2  Left            A curved broken white guide line, with visible short segments and gaps, runs ahead
                        between the black sedan on the left and the white car ahead; its continuation beside
                        the car is obscured, and no curb is visible on this immediate boundary.
                        white dotted, curb no, lane_line, evidence partial
Step 2  Right           The immediate right boundary is obscured by the nearby taxi and other vehicles; no
                        paint pattern or physical edge can be identified reliably.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (full): Broad white zebra-crossing stripes extend across the path
                        immediately ahead.
Step 4  Cross-check     position: The visible guide line and vehicles indicate another same-direction traffic
                        stream on the left, but the full lane count and ego position remain unresolved. |
                        roles: The broken white line is compatible with same-direction intersection guidance;
                        the right boundary cannot be classified. | markings: The crosswalk does not specify a
                        permitted turning direction, and no readable lane-use arrow is visible. | unseen: No
                        hidden boundary pattern or lane-use arrow has been inferred; 'none' on the right
                        records the absence of identifiable paint, not a confirmed unmarked boundary. |
                        result: consistent
Step 5  Rule            left_boundary: The broken intersection guide line guides the traffic path through the
                        junction, but its obscured continuation does not establish whether the immediate left
                        boundary may be crossed. [CN-5.6.1-2] "The intersection guide line guides vehicles
                        straight on and through turns and is placed inside an at-grade intersection. It is a
                        curved or straight broken line "
Step 5  Rule            right_boundary: No identifiable right boundary is available to determine whether
                        crossing it is permitted.
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and this marking
                        does not determine any of the seven movement permissions.
Step 6  change_left     not_determined (correct): The visible broken guide line does not reveal the immediate
                        left boundary through the obscured approach stretch.
Step 6  change_right    not_determined (correct): The taxi and other traffic hide the boundary that would
                        decide this action.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight, and the
                        crosswalk does not govern this permission.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        movement.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        movement.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         Consistent: neither hidden side boundary is treated as crossable, and the crosswalk is
                        not used to infer turning permissions or a mandatory full stop.
Advice                  Maintain the current traffic path and avoid lateral movement until the boundaries and
                        adjacent traffic are clear. Watch for pedestrians at the crossing and obey the signal
                        applicable to your movement; this image does not establish a turning lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1125, 23.73 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A busy urban two-way road with three apparent lanes in this direction. My car is in
                        the middle lane; queued vehicles obscure the distant approach and any intersection
                        markings. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible painted segments and gaps runs along the left of my
                        lane, with another same-direction lane beyond and no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane containing the red taxi; portions
                        farther ahead are hidden by vehicles, and there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with my lane being second of
                        three. | roles: The white broken boundaries fit same-direction lane separators. |
                        markings: No guidance arrow, word, symbol, or transverse marking can be identified in
                        the exposed portion of my lane. | unseen: The lane end and pavement beneath the queued
                        vehicles cannot be inspected; no markings there are assumed absent. The channelized
                        strip farther right is outside my lane. | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits crossing into the adjacent
                        same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: The visible broken white lane separator permits crossing into the
                        adjacent same-direction lane when safe. [CN-5.2.1-2] "The crossable lane line
                        separates traffic flows in the same direction and is placed between lanes of the same
                        direction. It is a broken white line."
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under
                        CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_determined: Vehicles hide the lane-end pavement where a movement-restricting arrow
                        could be marked.
Step 6  turn_right      not_determined: Vehicles hide the lane-end pavement where a movement-restricting arrow
                        could be marked.
Step 6  u_turn          not_determined: Vehicles hide the lane-end pavement where an arrow or prohibited-
                        movement marking could govern a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          identifiable in view.
Step 7  Reflect         consistent
Advice                  Continue cautiously in your lane; either visible broken separator may be crossed only
                        after checking adjacent traffic. Do not assume this lane permits a turn until the
                        obscured approach markings become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1390, 35.46 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with overhead lane-direction signs and traffic
                        in the distance. My car is in the rightmost lane, which has variable-lane pavement
                        text and toothed longitudinal markings. (lanes 4, mine 4, full)
Step 2  Left            A continuous white line with repeated short diagonal teeth separates my lane from
                        another same-direction lane; there is no curb on this side.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line with repeated inward-facing diagonal teeth runs beside a
                        raised curb, with landscaping and a sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): White Chinese characters read 可变车道, meaning variable lane, along my
                        lane.
Step 4  Cross-check     position: Four same-direction lanes and position 4 agree with a same-direction lane on
                        my left and the roadway edge on my right. | roles: The white left separator and white
                        right edge fit their positions; their toothed treatment identifies a variable guide
                        lane. | markings: The variable-lane text agrees with the toothed boundaries; no
                        readable pavement direction arrow is visible in my lane. | unseen: No direction arrow,
                        stop line, or waiting area has been inferred from the distant signs or vehicles. |
                        result: consistent
Step 5  Rule            left_boundary: This variable guide lane has a direction controlled by variable lane-
                        direction signs; its continuous boundary does not provide a lane-change opening.
                        [CN-6.10.1-4-V] "... The variable guide lane line marks a guide lane whose direction
                        can change as needed; it is placed on intersection approaches. ... No guide arrows
                        shall be "
Step 5  Rule            left_boundary: The solid white same-direction separator prohibits crossing to the lane
                        on my left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The continuous white boundary prohibits ordinary crossing, and the
                        raised curb is a physical road edge. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            text:other: The variable-lane text identifies a lane whose direction can change and
                        must be checked against its variable lane-direction signs. [CN-6.10.1-4-V] "... The
                        variable guide lane line marks a guide lane whose direction can change as needed; it
                        is placed on intersection approaches. ... No guide arrows shall be "
Step 6  change_left     prohibited (contested, label allowed): The solid white lane separator prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right boundary prohibits ordinary crossing, with
                        a raised curb beyond it.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        the lane; the variable lane-direction signs must also be checked.
Step 6  turn_left       not_applicable: No pavement arrow or prohibited-turn marking governs this movement.
Step 6  turn_right      not_applicable: No pavement arrow or prohibited-turn marking governs this movement.
Step 6  u_turn          not_applicable: No pavement arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary restrictions govern crossing only, and the straight-ahead result
                        describes pavement markings rather than overriding variable lane-direction signs.
Advice                  Stay within the solid boundaries and check the overhead variable lane-direction signs
                        before proceeding; signs take priority over conflicting pavement guidance. Do not
                        cross the solid left separator or move right over the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 1346, 27.32 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is behind
                        the white SUV, with same-direction traffic on both sides; vehicles obscure the far-
                        left roadway, preventing a reliable total lane count and lane index. (lanes None, mine
                        None, insufficient)
Step 2  Left            A continuous white line bounds my lane on the left, with repeated short slanted white
                        teeth extending into the adjacent lane; vehicles travel beyond it, and no curb forms
                        this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane occupied by the coach on the right;
                        no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in the foreground has one head pointing straight
                        ahead.; line:stop_line (partial): A transverse solid white stop line is visible ahead,
                        with its portion directly behind the SUV obscured.; line:crosswalk (partial): Broad
                        white pedestrian-crossing stripes extend across the road beyond the stop line, partly
                        hidden by the SUV and other traffic.
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, confirming that my lane has
                        another lane on each side; the obscured far-left extent prevents assigning an exact
                        index or total count. | roles: Both white solid boundaries fit same-direction lane
                        separation. The teeth on the left extend away from my lane and do not make my lane a
                        variable guide lane. | markings: The straight arrow agrees with a through approach
                        lane bounded by solid white lines; the stop line and crossing are compatible with the
                        intersection ahead. | unseen: No hidden arrow, pavement text, waiting area, or exact
                        lane count is inferred; the SUV obscures some pavement near the intersection. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not itself require a stop on every approach. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing, and
                        it does not determine any of the seven requested actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible straight arrow permits straight travel under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight; do not cross either solid boundary or turn
                        from this lane. Follow the traffic signals, stop before the stop line when required,
                        and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1277, 21.37 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           My car is in a single motor-vehicle lane on a physically separated side carriageway
                        approaching a signal-controlled junction. A recovery truck blocks the farther view; a
                        bicycle lane is on the right and the main carriageway is beyond the planted divider on
                        the left. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line follows a raised curb beside a planted divider, with another
                        carriageway beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the space used by cyclists on the
                        right; no curb lies on this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow has one head pointing straight ahead.
Step 4  Cross-check     position: Both boundaries are carriageway edges rather than ordinary lane dividers,
                        consistent with one motor-vehicle lane on this separated carriageway. | roles: The
                        right white line fits a motor/non-motor separation edge. The left paint is visibly
                        white despite its left-edge position; its curb and divider establish its edge role
                        without assuming yellow paint. | markings: The straight-only arrow is consistent with
                        the visible lane continuing ahead; no conflicting marking is visible. | unseen: The
                        truck hides the farther pavement, so no additional arrow, stop line, crosswalk or
                        waiting area is asserted there. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line prohibits ordinary crossing to the left,
                        where a raised divider also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid motor/non-motor separation edge line prohibits ordinary
                        crossing to the right. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a raised divider lies beyond it.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The visible straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay within this lane and proceed straight as signals and conditions permit; do not
                        cross either solid boundary or turn from this lane. Leave space behind the recovery
                        truck, watch the cyclists, and check for a stop line when the obscured pavement
                        becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 992, 17.0 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow, two-way residential street continues ahead between buildings and trees. My
                        car is in the sole motor-vehicle lane in its direction, with opposing traffic to the
                        left and a narrow roadside strip to the right; the next intersection is not clearly
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing scooters
                        beyond it and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from a
                        narrow roadside strip; a raised sidewalk curb lies beyond that strip, not at the line
                        itself.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and the roadside edge line on the right
                        agree with one motor-vehicle lane in my direction, indexed 1. | roles: The solid
                        yellow line separates opposing flows; the broken white line marks the right edge of
                        the motor-vehicle lane. | markings: No readable guidance marking is visible within my
                        lane. | unseen: The vehicle ahead and distance obscure the farther pavement and any
                        markings at the next intersection; no unseen arrow or stop line is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing to
                        the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The broken white boundary permits crossing the line, without itself
                        granting permission to drive along the roadside strip. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    allowed (correct): The broken white edge line permits crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The intersection approach and any movement markings there are obscured
                        by distance and the vehicle ahead.
Step 6  turn_right      not_determined: The intersection approach and any movement markings there are obscured
                        by distance and the vehicle ahead.
Step 6  u_turn          not_determined: The intersection approach and any movement markings there are obscured
                        by distance and the vehicle ahead.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: rightward crossing permission concerns only the broken boundary, while
                        intersection turns remain undecided because the relevant pavement is not visible.
Advice                  Continue within your lane and do not cross the solid yellow center line; watch for
                        scooters and pedestrians on both sides. The broken right edge does not establish
                        another motor-vehicle lane; reassess turn markings and any stop requirement when the
                        intersection becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 923, 16.61 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection. My car is in the
                        rightmost of three lanes in this direction, beside a raised sidewalk. (lanes 3, mine
                        3, full)
Step 2  Left            A continuous white line separates my lane from another same-direction lane on the
                        left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white edge marking runs beside a raised curb and paved sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow ahead has a forward-pointing head and a
                        branch pointing right.; line:stop_line (partial): A transverse white stop line is
                        visible near the intersection, although its full extent is difficult to distinguish at
                        this distance.; line:crosswalk (partial): White pedestrian-crossing stripes extend
                        across the approach ahead.
Step 4  Cross-check     position: Two lanes lie to my left and the sidewalk lies to my right, consistent with
                        lane 3 of 3 and the assigned lane-line and edge-line roles. | roles: The solid white
                        left line fits a no-crossing same-direction lane boundary; the white right line and
                        curb fit the roadway edge. | markings: The straight-or-right arrow is consistent with
                        the rightmost approach lane; the stop line and crossing do not conflict with it. |
                        unseen: No waiting area or additional lane-use text is visible; the transverse
                        markings are distant and are reported with partial evidence. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid right edge line prohibits ordinary crossing, and the raised
                        curb is a physical roadway boundary. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The arrow permits straight-ahead and right-turn movements,
                        excluding left turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        but does not independently require every vehicle to stop. [CN-6.4.1-2] "The stop line
                        marks where vehicles stop when yielding or waiting to proceed. It is a solid white
                        line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this marking does
                        not determine any of the seven requested actions.
Step 6  change_left     prohibited (WRONG, label allowed): CN-6.2.1 prohibits crossing the solid white left
                        lane line.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid right edge line prohibits ordinary
                        crossing under CN-4.2.2-a, and a raised curb lies beyond it.
Step 6  go_straight     allowed (contested, correct): The straight-or-right arrow permits going straight under
                        CN-5.13.1.
Step 6  turn_left       prohibited: The straight-or-right arrow does not permit a left turn.
Step 6  turn_right      allowed: The straight-or-right arrow permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-or-right arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern only crossing their respective sides, the arrow
                        governs intersection movements, and the stop line alone does not turn permitted
                        movements into stop_first.
Advice                  Stay in this lane for straight travel or a right turn; do not cross either solid
                        boundary. A red signal is visible ahead: obey the applicable signal, stop before the
                        stop line when required, and watch for pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right', 'line:crosswalk', 'line:stop_line'], missed []), actions
                        False, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 1273, 21.46 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection and pedestrian
                        crossing. My car is in the rightmost of three same-direction lanes, beside a raised
                        traffic island. (lanes 3, mine 3, partial)
Step 2  Left            A single solid white line separates my lane from the same-direction lane occupied by
                        the white car on the left; there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right side of my lane, beside a raised paved
                        island and its curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible directly
                        ahead; the bottom of its shaft is obscured by the hood.; line:stop_line (full): A
                        solid white transverse stop line crosses my lane before the pedestrian crossing.;
                        line:crosswalk (full): Broad white zebra-crossing stripes cross my lane beyond the
                        stop line.
Step 4  Cross-check     position: The left lane line and right roadway edge place my car in the rightmost
                        lane; three lanes appear present, although the white car obscures part of the left-
                        side layout. | roles: The solid white left line fits a same-direction lane separator;
                        the solid white right line and raised island fit a roadway edge. | markings: The
                        visible straight arrow is consistent with the approach lane and its stop line and
                        crosswalk; the hood prevents checking the arrow's complete lower portion. | unseen:
                        The lane count is less certain because of the adjacent car, and no hidden arrow branch
                        is assumed absent. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid right boundary prohibits ordinary crossing, and the raised
                        island is not a drivable continuation of the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but its
                        obscured lower portion prevents confidently excluding an additional directional
                        branch. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required to yield or wait,
                        rather than independently requiring a stop on every approach. [CN-6.4.1-2] "The stop
                        line marks where vehicles stop when yielding or waiting to proceed. It is a solid
                        white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers zebra crossings; this
                        pedestrian-crossing marking does not independently decide the seven requested actions.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane separator prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid right boundary prohibits ordinary
                        crossing under CN-4.2.2-a, with a raised island beyond it.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hood obscures the lower arrow portion,
                        so a possible additional branch cannot be checked.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hood obscures the lower arrow portion,
                        so a possible additional branch cannot be checked.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete arrow configuration is
                        obscured, preventing a definitive movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid boundaries; straight travel is visibly indicated, while turn
                        permissions cannot be fully read. Obey the applicable traffic signal and stop before
                        the stop line when required, keeping the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 10766, out 1343, 24.4 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow two-way urban street continues ahead between buildings and roadside parked
                        vehicles. My car follows a bus in the single lane of our direction; the bus hides the
                        farther roadway, and no intersection or lane end is visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing traffic
                        beyond it and no curb on the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with parked cars and a
                        roadside curb farther beyond; the curb does not form the immediate lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane in our direction agrees with a centre line on the left and a
                        roadway edge line on the right. | roles: The solid yellow centre line separates
                        opposing traffic; the solid white edge line separates the travel lane from roadside
                        parking space. | markings: No guidance markings are visible within the exposed part of
                        my lane. | unseen: The bus hides the pavement ahead, including any possible downstream
                        arrows or transverse markings; none have been inferred. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow centre line prohibits my car from crossing to
                        the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white boundary normally prohibits crossing to the right,
                        except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The single solid yellow centre line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane; its solid boundaries do not prohibit doing so.
Step 6  turn_left       not_determined: The lane end and any movement markings there are hidden behind the
                        bus.
Step 6  turn_right      not_determined: The lane end and any movement markings there are hidden behind the
                        bus.
Step 6  u_turn          not_determined: The lane end and any movement markings there are hidden behind the
                        bus; the centre line governs crossing the boundary, not an unseen intersection
                        movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the solid boundaries and keep enough distance behind the bus to see
                        the road ahead. Do not cross either boundary for an ordinary lane change; reassess
                        turn guidance and any stopping requirement once the hidden roadway becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 10766, out 879, 15.19 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a narrow, single-lane descending roadway bounded by concrete barriers
                        and railings. The road continues ahead; no intersection or lane ending is clearly
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous yellow edge line runs beside a raised concrete barrier topped with a
                        metal barrier and screening; no adjacent accessible lane is visible.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white edge line runs beside a raised concrete wall topped with railings,
                        with a separated walkway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane with edge boundaries on both sides is consistent with the car being
                        in lane 1 of 1. | roles: The solid yellow left edge and solid white right edge fit
                        their roadway-edge roles. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in the lane. | unseen: No movement restrictions have
                        been inferred from the distant signs or the unseen intersection beyond the visible
                        roadway. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line prohibits ordinary crossing to the
                        left, where a physical barrier also bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid longitudinal edge line prohibits ordinary crossing to the
                        right, where a physical wall also bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left edge line prohibits ordinary crossing under
                        CN-4.2.2-a, and a concrete barrier blocks that side.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits ordinary crossing under
                        CN-4.2.2-a, and a concrete wall blocks that side.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane; the edge boundaries govern crossing, not forward travel.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this single lane; do not cross either solid edge line or attempt to
                        move past the barriers. Reassess turn choices and any stopping requirements when the
                        road ahead and its controls become clearly visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 10766, out 840, 13.87 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with two motor-vehicle lanes in this direction
                        and a bicycle lane along the right side. My car is in the right-hand motor-vehicle
                        lane; a pedestrian crossing is visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line with visible long segments and gaps separates my lane from the
                        motor-vehicle lane occupied by the blue car; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white line is continuous beside the foreground red bicycle-lane pavement, with
                        separated white segments farther ahead; bicycles and scooters are beyond it, and no
                        curb separates them from my lane.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        line:crosswalk (partial): White pedestrian-crossing stripes extend across my lane
                        ahead, with part of the crossing obscured by vehicles.
Step 4  Cross-check     position: Two motor-vehicle lanes and ego position 2 agree with a same-direction lane
                        line on the left and a motor/non-motor separation boundary on the right. | roles: The
                        broken white left line fits a crossable lane divider; the white right line fits a
                        motor/non-motor separation line, with its foreground section continuous and farther
                        sections broken. | markings: The crossing does not conflict with either boundary; the
                        bicycle symbol is outside my lane and is not an ego-lane marking. | unseen: No lane-
                        use arrow or waiting area is visible; distant pavement and part of the crossing are
                        obscured, and the right boundary's transition is not fully clear. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 5  Rule            right_boundary: Crossing the continuous foreground section is normally prohibited; the
                        broken sections farther ahead are crossable under this line rule. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers pedestrian crossings, and this
                        marking does not determine any of the seven requested actions.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.1-2.
Step 6  change_right    prohibited (correct): The continuous white boundary beside the car prohibits normal
                        crossing under CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible ego-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible ego-lane arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible ego-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the right-change prohibition applies to the continuous foreground
                        boundary, not the broken sections farther ahead, and the bicycle symbol outside my
                        lane does not govern my movements.
Advice                  Continue in this lane, or change left across the broken divider only when safe; do not
                        cross the continuous right boundary into the bicycle lane. Watch for pedestrians at
                        the crossing and cyclists or scooters alongside; turn-lane instructions at the next
                        intersection are not readable here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 10766, out 1153, 23.07 s
```
