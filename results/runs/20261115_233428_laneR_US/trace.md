# Reasoning of lane run 20261115_233428_laneR_US

```text
bdd100k_val__b2afce7f-0cb9967a | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided roadway has two lanes in this direction and continues ahead without a
                        visible intersection or lane ending. My car is in the right-hand lane. (lanes 2, mine
                        2, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line borders my lane on the right, with a narrow paved shoulder and a
                        metal guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane 2 agree with a lane line on the left and a roadway
                        edge line on the right. | roles: The broken white line fits separation of same-
                        direction lanes; the solid white line fits a right roadway edge. | markings: No
                        arrows, words, symbols, transverse lines, or waiting areas are visible in my lane. |
                        unseen: No markings or intersection details beyond the visible roadway are inferred;
                        the guardrail is beyond the shoulder, not the immediate lane boundary. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent lane with
                        care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white edge line identifies the roadway edge and does not
                        itself prohibit crossing onto the shoulder. [US-3B.09-01-02] "If used, edge line
                        pavement markings shall delineate the right or left edges of a roadway. ... Right edge
                        line pavement markings, if used, shall consist of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (contested, label prohibited): US-3B.09-01-02 defines this as an edge line
                        without prohibiting crossing; this is not permission to use the shoulder as a travel
                        lane.
Step 6  go_straight     allowed (contested, correct): No marking restricts continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue in the right lane, or change left across the broken white line when safe. The
                        right side is a narrow shoulder beside a guardrail, not another travel lane; no
                        intersection or stopping location is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 775, 10.89 s

bdd100k_val__b459e707-2d208c56 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A paved road climbs toward a crest through a built-up area; no intersection or lane
                        ending is clearly visible. My car is in the right lane of two apparent lanes traveling
                        in this direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line with several visible dashes and gaps separates my lane from the
                        paved lane on the left; no curb is present.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous yellow line borders my lane on the right, with a narrow paved
                        roadside strip and unraised dirt verge beyond it.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The white lane line on the left and roadway edge on the right agree with my
                        car occupying lane 2 of 2. | roles: The broken white line fits a same-direction lane
                        boundary. The right boundary functions visually as a roadway edge, but its yellow
                        paint is inconsistent with the supplied US requirement for a white right edge line. |
                        markings: No arrows, words, symbols, waiting areas, or transverse markings are visible
                        in my lane. | unseen: No markings beyond the crest or at an unseen intersection are
                        inferred. | result: The observed geometry is consistent; the yellow right-edge paint
                        is retained as an observed nonstandard color rather than reclassified as white.
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent lane with
                        care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: An edge line delineates the roadway edge without itself prohibiting
                        crossing, although this observed yellow right edge does not match the passage's
                        required white color. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (WRONG, label prohibited): The edge line identifies the roadway edge;
                        US-3B.09-01-02 imposes no crossing prohibition, though the space beyond is roadside
                        rather than another traffic lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         Consistent: boundary decisions concern crossing only, and the absence of turn guidance
                        is not treated as permission for turns.
Advice                  Continue within your lane; a left lane change is permitted by the broken white marking
                        when safe. The right line borders roadside space, not another travel lane, so remain
                        inside it for normal driving and reassess conditions beyond the crest.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6694, out 951, 19.44 s

bdd100k_val__b5046f1e-b1ef44b9 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A downtown street approaches a signalized intersection and crosswalk. My car is in the
                        middle of three apparent same-direction lanes; the lane on the right has bus-related
                        pavement lettering. (lanes 3, mine 2, partial)
Step 2  Left            A single solid white line runs along the left of my lane, with another paved lane and
                        vehicles beyond it; the construction barrier is farther left, not on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from
                        the right-hand lane bearing bus-related lettering.
                        white dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        text:only (partial): Worn white lettering ahead reads ONLY, with parts of the letters
                        faint.; arrow:straight (partial): A faint white directional arrow is visible beyond
                        the lettering; it appears to point straight, but its head is not clear enough to
                        exclude another movement.; line:crosswalk (partial): White crosswalk stripes extend
                        across my lane at the intersection, partly obscured by the vehicle ahead.
Step 4  Cross-check     position: A lane on each side agrees with the apparent middle-lane position; the exact
                        use of the left-side paved space is less certain. | roles: The solid white left lane
                        line fits separation of same-direction lanes. The broken white right boundary and
                        adjacent bus lettering support a special-lane boundary. | markings: ONLY is compatible
                        with a single-direction arrow, but the worn arrowhead prevents a confident
                        determination of that direction. | unseen: The arrow's complete head, portions of the
                        lettering, and parts of the intersection markings are unclear; no stop line or
                        additional arrowhead is inferred. | result: consistent
Step 5  Rule            left_boundary: Crossing this single solid white lane line is discouraged rather than
                        prohibited. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The adjacent bus lane is a preferential lane, which is treated as
                        reserved and unavailable for this ordinary car. [US-3E.01-01] "Preferential lanes are
                        established for one or more of a wide variety of special uses, including, but not
                        limited to, high-occupancy vehicle (HOV) lanes, electro"
Step 5  Rule            text:only: ONLY supplements an exclusive single-movement designation but does not
                        identify the movement without the arrow. [US-3B.21-04] "Where through lanes
                        approaching an intersection become mandatory turn lanes, ONLY word pavement markings
                        should be used in addition to signs and the required la"
Step 5  Rule            arrow:straight: The arrow governs permitted intersection movements, but its unclear
                        head prevents a reliable movement decision. [US-3B.23-01] "Lane-use arrow markings are
                        used to indicate the mandatory or permissible movements in certain lanes and in two-
                        way left-turn lanes."
Step 5  Rule            line:crosswalk: No supplied passage covers crosswalk conduct; this marking identifies
                        the pedestrian crossing and does not independently decide the seven actions.
Step 6  change_left     allowed (contested, label prohibited): US-3B.06-05-06 discourages but does not
                        prohibit crossing the single solid white lane line.
Step 6  change_right    prohibited (correct): The right boundary leads into an apparent reserved bus lane,
                        which an ordinary car must not enter.
Step 6  go_straight     not_determined (contested, label allowed): The worn arrowhead is not clear enough to
                        establish the permitted movement.
Step 6  turn_left       not_determined: The worn arrowhead is not clear enough to establish whether a left-
                        turn movement is shown.
Step 6  turn_right      not_determined: The worn arrowhead is not clear enough to establish whether a right-
                        turn movement is shown.
Step 6  u_turn          not_determined: The worn arrowhead is not clear enough to establish its complete
                        movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Avoid the reserved lane on the right; crossing the solid white line to the left is
                        discouraged. Confirm the worn lane-use arrow before choosing an intersection movement,
                        obey the signal, and keep the crosswalk clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'text:only'], missed []), actions True, unsafe
                        [], citation None, contradictions []
Tokens                  in 7533, out 1306, 24.76 s

bdd100k_val__b6decb24-82234e11 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A wide urban avenue approaches a signalized intersection. My car is in an unmarked
                        through lane, with a turn-marked lane to the left and a bus occupying the lane to the
                        right; the far-left channelized and curbside layout makes the complete lane count
                        uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from the adjacent
                        lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the lane
                        occupied by the bus on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): White transverse crosswalk markings are visible across my
                        lane at the intersection ahead, partly obscured by distance and traffic.
Step 4  Cross-check     position: Both boundaries indicate adjacent same-direction lanes. The exact total and
                        my numerical position remain uncertain because the far-left layout is difficult to
                        resolve. | roles: The white broken boundaries fit same-direction lane separation. |
                        markings: No readable arrow or word is visible within my lane; the left-turn arrow and
                        ONLY marking lie in the adjacent lane to the left. | unseen: No bus-only designation
                        is readable in the lane on the right, so the presence of a bus alone is not treated as
                        evidence of a reserved lane. Distant transverse markings are only partially resolved.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The broken white lane line permits crossing with care into the
                        adjacent lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is
                        not discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and this
                        transverse marking does not determine any of the seven requested actions.
Step 6  change_left     allowed (correct): The broken white lane boundary permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The broken white lane boundary permits crossing with care under
                        US-3B.06-05-06; the bus itself does not establish a reserved-lane marking.
Step 6  go_straight     allowed (correct): No visible arrow in my lane restricts continuing straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking in my lane governs this action;
                        the visible left-turn arrow belongs to the adjacent lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking in my lane governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane for straight travel; the visible left-turn guidance belongs to
                        the lane on the left. Although the broken boundaries permit lane changes, check for
                        lane restrictions and surrounding traffic, particularly the bus, and obey the signal
                        while yielding to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6096, out 1525, 36.7 s

bdd100k_val__b7719f1d-e6e580dd | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A multilane divided freeway continues ahead through a concrete-barrier work zone, with
                        merging traffic indicated on the right. There appear to be five same-direction lanes,
                        including the narrowing auxiliary lane on the right; my car is in the fourth lane from
                        the left, behind the white SUV, although the far-left lane layout is less clear.
                        (lanes 5, mine 4, partial)
Step 2  Left            A broken white line with long gaps separates my lane from another same-direction
                        traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A dotted white line of short, closely spaced segments separates my lane from a
                        narrowing paved auxiliary lane on the right; a separate solid white edge line and
                        concrete barrier lie farther right.
                        white dotted, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car being in an interior lane,
                        immediately left of the right auxiliary lane; the exact count farther left is less
                        certain. | roles: Both white boundaries separate same-direction lanes; the short
                        dotted right boundary fits an auxiliary-lane transition. | markings: No arrows, words,
                        symbols, transverse lines, or waiting areas are visible in my lane. | unseen: The
                        distant lane layout and pavement obscured by vehicles are not inferred; the total lane
                        count is qualified. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        left lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The dotted white lane line warns of a downstream lane-function change
                        and does not prohibit crossing into the adjacent auxiliary lane. [US-3A.04-01-DE] "D.
                        A dotted lane line provides warning of a downstream change in lane function. E. A
                        dotted line used as a lane line or edge line extension guides vehicles thro"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The dotted white lane line warns of a lane transition under
                        US-3A.04-01-DE but does not prohibit crossing.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight in my lane, and
                        my lane does not visibly end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your current lane and leave room for traffic merging from the narrowing
                        lane on the right. Both lane boundaries permit crossing, but avoid entering the
                        narrowing auxiliary lane unnecessarily and check surrounding traffic before changing
                        lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6389, out 1159, 28.62 s

bdd100k_val__b775af1c-bb5afbe3 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban street approaches a signalized intersection. My car is in the rightmost of
                        two approach lanes, behind an SUV near the stop line. (lanes 2, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another approach lane on the left; no
                        curb is present along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white edge marking follows the right side of my lane beside a raised curb and
                        sidewalk, curving around the intersection corner.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A white curved right-turn arrow is painted in my lane; the SUV
                        obscures part of its upper portion, but the right-pointing head is visible.;
                        line:stop_line (partial): A broad solid white transverse stop line crosses my lane
                        ahead of the arrow, partly obscured by the SUV.
Step 4  Cross-check     position: Two approach lanes and my position as lane 2 agree with a same-direction
                        lane on my left and the roadway edge on my right. | roles: The white solid separator
                        fits a lane line, and the white line beside the curb fits a right edge line. |
                        markings: The right-turn arrow agrees with the lane's position beside the right
                        corner; the stop line marks the intersection approach. | unseen: The SUV hides
                        portions of the arrow and stop line; no additional hidden markings are assumed. |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the single solid white lane line is discouraged, not
                        prohibited. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The white edge line delineates the roadway edge; the raised curb
                        beyond it is a physical boundary that my car must not cross. [US-3B.09-01-02] "If
                        used, edge line pavement markings shall delineate the right or left edges of a
                        roadway. ... Right edge line pavement markings, if used, shall consist of a no"
Step 5  Rule            arrow:right: The right-turn lane-use arrow permits a right turn and restricts this
                        lane from straight, left-turn, or U-turn movements. [US-3B.23-01] "Lane-use arrow
                        markings are used to indicate the mandatory or permissible movements in certain lanes
                        and in two-way left-turn lanes."
Step 5  Rule            line:stop_line: The stop line identifies where to stop when the signal or another
                        applicable control requires stopping; it does not independently require a stop.
                        [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which vehicles
                        are required to stop in compliance with a STOP sign ... or some other traffic control
                        device "
Step 6  change_left     allowed (contested, label prohibited): US-3B.06-05-06 discourages but does not
                        prohibit crossing the single solid white lane line.
Step 6  change_right    prohibited (contested, correct): The raised curb at the right roadway edge prevents
                        leaving the lane across that boundary.
Step 6  go_straight     prohibited (correct): The identifiable right-turn-only arrow does not show a straight
                        movement.
Step 6  turn_left       prohibited (correct): The right-turn arrow does not permit a left turn.
Step 6  turn_right      allowed (correct): The identifiable right-turn arrow permits a right turn under
                        US-3B.23-01.
Step 6  u_turn          prohibited (correct): The right-turn arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn, yielding to pedestrians and other conflicting traffic;
                        do not continue straight from it. A left lane change is discouraged but not prohibited
                        by the solid white separator; obey the signal and stop behind the stop line whenever
                        required.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 7401, out 1074, 17.04 s

bdd100k_val__b9db357e-cd30a8ae | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street approaches a signalized intersection, with my car behind a
                        silver hatchback. Another same-direction lane is visible on the left; vehicles obscure
                        whether the space on the right is a travel lane or parking. (lanes None, mine 2,
                        partial)
Step 2  Left            A white line appears solid along the visible foreground stretch on the left, with
                        another same-direction lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           The vehicles on the right obscure the boundary; no continuous painted boundary or
                        physical edge can be reliably identified.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        none
Step 4  Cross-check     position: The visible lane to the left supports ego lane index 2, but the obscured
                        right side prevents a reliable total lane count. | roles: The white left boundary fits
                        separation of same-direction lanes; the right boundary's role remains unknown. |
                        markings: No guidance marking can be read in my lane; the hatchback hides much of its
                        pavement and intersection approach. | unseen: No hidden arrows, stop line, or waiting
                        area have been inferred; the right-side attributes indicate lack of observation, not
                        confirmed absence. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line discourages crossing but does not prohibit
                        changing left with care. [US-3B.06-05-06] "Where crossing the lane line markings with
                        care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 5  Rule            right_boundary: The obscured boundary cannot be matched to a marking rule, so
                        permission to cross it remains undetermined.
Step 6  change_left     allowed (contested, correct): US-3B.06-05-06 discourages, but does not prohibit,
                        crossing the visible solid white lane line.
Step 6  change_right    not_determined (contested, correct): The boundary and the function of the space beyond
                        it are obscured.
Step 6  go_straight     not_determined (contested, label allowed): The hatchback hides the pavement where a
                        movement-restricting arrow could be present.
Step 6  turn_left       not_determined: Any lane-use arrow governing this movement is hidden by traffic.
Step 6  turn_right      not_determined: Any lane-use arrow governing this movement is hidden by traffic.
Step 6  u_turn          not_determined: Any arrow or prohibited-movement marking governing this movement is
                        hidden by traffic.
Step 6  enter_waiting_areanot_determined: Traffic obscures the lane end, preventing confirmation of a waiting
                          area ahead.
Step 7  Reflect         consistent
Advice                  Keep a safe following distance and confirm lane arrows and the stop line as traffic
                        clears. Crossing the left solid white line is discouraged rather than prohibited; do
                        not move right until its boundary and the use of that space are clear, and obey the
                        traffic signals.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6438, out 1081, 22.17 s

bdd100k_val__bc05c126-d00aeb9c | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with parked vehicles along both sides. My car
                        is in the leftmost general-traffic lane of its direction, beside a red bus lane on the
                        right. (lanes 2, mine 1, full)
Step 2  Left            Two solid yellow lines border my lane beside a yellow diagonally hatched central
                        buffer, with opposing traffic space beyond; there is no curb.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line separates my lane from a red-painted lane with a visible BUS
                        marking; there is no curb at this boundary.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center boundary makes my lane the leftmost of my direction; the bus lane
                        on the right is the second same-direction lane. | roles: The yellow double-solid
                        center boundary separates opposing directions, and the white solid boundary separates
                        my lane from the same-direction bus lane. | markings: No guidance markings are visible
                        within my lane; the BUS marking and central hatching lie outside it. | unseen: No
                        distant intersection markings or obscured pavement markings have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The double-solid yellow center boundary prohibits crossing for passing,
                        so my car must not move left across it. [US-3B.01-04] "The center line markings on
                        two-lane, two-way roadways shall be one of the following: A. Two-direction passing
                        zone markings consisting of a normal width broken"
Step 5  Rule            right_boundary: The adjacent bus lane is a preferential lane and, under the supplied
                        reserved-lane definition, my ordinary car must not change into it. [US-3E.01-01]
                        "Preferential lanes are established for one or more of a wide variety of special uses,
                        including, but not limited to, high-occupancy vehicle (HOV) lanes, electro"
Step 6  change_left     prohibited (correct): The double-solid yellow center boundary prohibits crossing for
                        passing under US-3B.01-04.
Step 6  change_right    prohibited (contested, correct): The adjacent bus lane is reserved, so entering it is
                        prohibited regardless of the single solid white boundary.
Step 6  go_straight     allowed (contested, correct): No arrow or other marking in my lane restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue in the current general-traffic lane; do not cross the yellow center boundary
                        or enter the bus lane. No visible marking in your lane establishes turn permissions or
                        a stopping point.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6964, out 843, 13.87 s

bdd100k_val__bca36352-5de70a3f | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided urban roadway has two visible lanes in this direction, with a work-zone
                        taper and barrels ahead on the right. My car is in the right-hand lane behind the
                        yellow SUV. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from the adjacent
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a diagonally striped
                        paved buffer beyond it; the concrete roadside barrier is farther right, not at this
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and position 2 agree with a same-direction lane line on the left
                        and a roadway edge line on the right. | roles: The broken white line fits a same-
                        direction lane divider, and the solid white line fits the right roadway edge. |
                        markings: No guidance markings are visible inside my lane; the diagonal striping is
                        outside its right boundary. | unseen: The SUV obscures some pavement ahead; no hidden
                        arrows or lane-ending markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white edge line delineates the roadway edge; this passage
                        does not prohibit crossing it or designate the pavement beyond as a traffic lane.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (contested, label prohibited): The edge-line rule US-3B.09-01-02 does not
                        prohibit crossing, although the space beyond is a striped buffer rather than a traffic
                        lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane, and
                        no visible marking ends it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within your lane and watch the work-zone barrels ahead; a left lane change is
                        permitted when safe. The right edge line does not itself prohibit crossing, but the
                        striped buffer is not an additional travel lane and should be avoided.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 970, 17.27 s

bdd100k_val__bcbbfd82-add80c05 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided urban road at night approaches a signalized intersection. My car is in the
                        left of two apparent through lanes, beside a raised median; parked vehicles line the
                        right curb. (lanes 2, mine 1, partial)
Step 2  Left            A continuous pale yellow line runs beside a raised median on the left, with opposing
                        traffic beyond the median.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Faint white broken line segments and intervening gaps separate my lane from an
                        apparent same-direction lane on the right; darkness makes the nearer continuation
                        difficult to see.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right lane divider agree with my lane being the
                        leftmost of two apparent same-direction lanes. | roles: The yellow solid left edge and
                        white broken same-direction divider fit their assigned roles. | markings: No readable
                        guidance markings appear in my lane; the arrow across the median belongs to opposing
                        traffic. | unseen: The near right divider and distant intersection pavement are poorly
                        illuminated; no hidden arrows, stop lines, or waiting areas have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line identifies the left roadway edge, and the raised
                        median physically prevents a leftward lane change. [US-3B.09-03] "If used on the
                        roadways of divided highways or one-way streets, or on any ramp in the direction of
                        travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The visible broken white lane divider permits crossing with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 6  change_left     prohibited (correct): The raised median forms a physical boundary that cannot be
                        crossed as a lane change.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits crossing with care
                        under US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant intersection pavement is too dark to establish whether a
                        lane-use arrow governs this movement.
Step 6  turn_right      not_determined: The distant intersection pavement is too dark to establish whether a
                        lane-use arrow governs this movement.
Step 6  u_turn          not_determined: The distant intersection pavement is too dark to establish whether an
                        arrow or prohibited-movement marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane for straight travel; change right only after checking traffic
                        and confirming the broken divider, and do not cross the median. Red signals are
                        visible ahead: prepare to stop and verify the intersection markings before choosing a
                        turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6823, out 917, 18.34 s

bdd100k_val__bd026bc5-9418706c | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban multilane street approaches a signalized intersection at East 44th Street. My
                        car is in the third of four visible same-direction travel lanes, behind the silver
                        car. (lanes 4, mine 3, full)
Step 2  Left            A single solid white line separates my lane from the adjacent lane occupied by the box
                        truck; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent lane occupied by the
                        black sedan; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white lane-use arrow has a single head pointing straight
                        ahead.; line:stop_line (full): A solid white transverse stop line crosses my lane
                        before the crosswalk.; line:crosswalk (partial): Broad white crosswalk stripes extend
                        across my lane beyond the stop line, with part obscured by the silver car.
Step 4  Cross-check     position: The third lane of four has one same-direction lane on its right and two on
                        its left, consistent with lane-line boundaries on both sides. | roles: Both boundaries
                        are white and separate same-direction traffic; their solid pattern is consistent with
                        intersection-approach lane lines. | markings: The straight arrow agrees with a through
                        lane continuing toward the intersection; the stop line and crosswalk do not conflict
                        with it. | unseen: The silver car obscures part of the crosswalk; no markings beneath
                        vehicles or beyond the visible approach are inferred. | result: consistent
Step 5  Rule            left_boundary: The single solid white lane line discourages, but does not prohibit,
                        crossing into the lane on the left. [US-3B.06-05-06] "Where crossing the lane line
                        markings with care is not discouraged or prohibited, the lane line markings shall
                        consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The single solid white lane line discourages, but does not prohibit,
                        crossing into the lane on the right. [US-3B.06-05-06] "Where crossing the lane line
                        markings with care is not discouraged or prohibited, the lane line markings shall
                        consist of a normal width broken white line. Wher"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight from this lane and
                        excludes left turns, right turns, and U-turns. [US-3B.23-01] "Lane-use arrow markings
                        are used to indicate the mandatory or permissible movements in certain lanes and in
                        two-way left-turn lanes."
Step 5  Rule            line:stop_line: The stop line identifies where to stop when the signal or another
                        applicable traffic control requires stopping; it does not independently require a
                        stop. [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which
                        vehicles are required to stop in compliance with a STOP sign ... or some other traffic
                        control device "
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this marking
                        identifies the pedestrian crossing and does not independently determine any of the
                        seven actions.
Step 6  change_left     allowed (contested, correct): US-3B.06-05-06 discourages but permits crossing the
                        single solid white lane line with care.
Step 6  change_right    allowed (contested, correct): US-3B.06-05-06 discourages but permits crossing the
                        single solid white lane line with care.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under US-3B.23-01.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under US-3B.23-01.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under US-3B.23-01.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under US-3B.23-01.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane; turning requires selecting an appropriately marked
                        lane beforehand. Crossing either solid white lane line is discouraged, and adjacent
                        vehicles must be considered; obey the signal and stop behind the stop line when
                        required, keeping the crosswalk clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 7097, out 1258, 19.58 s

bdd100k_val__be278041-2173a980 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A single-lane ramp runs between concrete barriers at dusk, alongside a larger roadway
                        on the right. My car is following the black car in the ramp lane; a striped separation
                        area and barrier nose are ahead on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line follows the left concrete barrier, with no adjacent traffic lane
                        beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line borders a white diagonally striped separation area on the right,
                        which narrows toward a crash cushion and concrete barrier separating the ramp from the
                        neighboring roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges, consistent with one ramp lane and ego
                        lane index 1. | roles: The solid yellow left edge and solid white right edge fit a
                        ramp traveling in one direction. | markings: No guidance marking is visible inside my
                        lane; the diagonal stripes are outside its right boundary. | unseen: No arrow, stop
                        line, or intersection movement restriction is inferred from the signs or the distant
                        roadway. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the ramp's left edge; the concrete
                        barrier physically prevents leaving the lane on that side. [US-3B.09-03] "If used on
                        the roadways of divided highways or one-way streets, or on any ramp in the direction
                        of travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The solid white line delineates the ramp's right edge rather than an
                        adjacent lane, and the downstream physical separator prevents a lane change to the
                        neighboring roadway. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 6  change_left     prohibited (correct): The left concrete barrier is a physical edge, not a crossable
                        lane boundary.
Step 6  change_right    prohibited (contested, label allowed): The right side leads into a striped separation
                        area ending at a crash cushion and concrete barrier, not an adjoining accessible lane.
Step 6  go_straight     allowed (contested, correct): No in-lane arrow restricts continuing along the ramp.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the lateral prohibitions follow from physical separation, not from
                        treating every solid edge line as a crossing prohibition.
Advice                  Follow the ramp between its edge lines, keeping clear of the striped area, crash
                        cushion, and barriers. The merge warning sign is context rather than a pavement
                        instruction to change lanes here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6517, out 938, 17.54 s

bdd100k_val__be4cbd00-97fec78b | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A multi-lane urban street at night approaches a signalized intersection. My car is in
                        the middle of three apparent same-direction travel lanes, with parked vehicles along
                        the street edges. (lanes 3, mine 2, partial)
Step 2  Left            A broken white line, with several visible dashes and gaps, separates my lane from
                        another travel lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with several visible dashes and gaps, separates my lane from
                        another travel lane on the right; the sidewalk curb is farther beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): White crosswalk bars are visible across the approach ahead,
                        although distance and darkness obscure their complete extent across my lane.
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying an interior lane,
                        apparently lane 2 of 3; the outer roadway layout is less clear in the darkness. |
                        roles: Both white broken boundaries fit their roles as separators of same-direction
                        travel lanes. | markings: The visible crosswalk does not conflict with the lane
                        boundaries. Small distant white pavement marks cannot be resolved well enough to
                        identify a lane-use arrow. | unseen: No arrow direction or separate stop line has been
                        inferred from the distant paint; lane-use guidance near the intersection remains
                        uncertain. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing to the left with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            right_boundary: The broken white lane line permits crossing to the right with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and under the
                        supplied definitions this transverse marking does not decide any of the seven actions.
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     not_determined (WRONG, label allowed): Possible lane-use guidance near the
                        intersection is too distant to resolve, so a movement restriction cannot be excluded.
Step 6  turn_left       not_determined (correct): The distant lane-use markings cannot be read well enough to
                        determine whether a left-turn arrow is present.
Step 6  turn_right      not_determined (correct): The distant lane-use markings cannot be read well enough to
                        determine whether a right-turn arrow is present.
Step 6  u_turn          not_determined (correct): The distant lane-use markings cannot be read well enough to
                        determine whether they govern U-turns.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: lane changes follow the visible broken boundaries, while intersection
                        movements remain undecided because distant lane-use guidance is unresolved.
Advice                  Either visible broken lane boundary permits a careful lane change, but confirm the
                        intersection lane-use markings before selecting a turn lane. The signals ahead are
                        red; stop at the applicable stop line, keeping the crosswalk clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6096, out 1141, 21.8 s

bdd100k_val__beccfad4-d24a29c5 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           My car is on a single-lane connector or ramp, descending toward a junction whose
                        details are distant. Concrete barriers and guardrails constrain the roadway, with a
                        raised curb continuing along the left farther ahead. (lanes 1, mine 1, full)
Step 2  Left            A worn yellow edge marking follows the left concrete barrier and then a raised curb;
                        it appears solid, although shadow and wear obscure portions.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A worn solid white line follows the right concrete barrier and the guardrail beyond
                        it, with a narrow paved strip between the line and barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane bounded by roadway edges on both sides agrees with my car being in
                        lane 1 of 1. | roles: The yellow left edge and white right edge fit a one-direction
                        connector; neither is a divider between adjacent travel lanes. | markings: No readable
                        arrows, words, symbols, waiting areas, or transverse markings are visible in my lane.
                        | unseen: The left marking's continuity is partly obscured, and markings at the
                        distant junction cannot be resolved; no unseen movement restrictions are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The yellow marking delineates the left roadway edge; the physical
                        barrier and curb, rather than the paint alone, prevent leaving my lane to the left.
                        [US-3B.09-03] "If used on the roadways of divided highways or one-way streets, or on
                        any ramp in the direction of travel, left edge line pavement markings shall consist of
                        a n"
Step 5  Rule            right_boundary: The solid white marking delineates the right roadway edge; the
                        physical barrier prevents leaving my lane to the right. [US-3B.09-01-02] "If used,
                        edge line pavement markings shall delineate the right or left edges of a roadway. ...
                        Right edge line pavement markings, if used, shall consist of a no"
Step 6  change_left     prohibited (correct): The left barrier and raised curb form a physical roadway edge
                        that cannot be crossed as a lane change.
Step 6  change_right    prohibited (correct): The right barrier and guardrail block movement beyond the
                        roadway edge.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other lane marking restricts
                        continuing along this lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within this single lane without attempting to cross either physical edge.
                        Reassess the distant junction as its markings and controls become readable; no
                        stopping point or turning assignment can be identified here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6517, out 888, 16.52 s

bdd100k_val__bf6315ee-a77e1bb2 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A city street at night approaches a signalized intersection with queued traffic. My
                        car is in the rightmost of two visible travel lanes, with parked vehicles along the
                        right side; traffic obscures the far end of the lane. (lanes 2, mine 2, partial)
Step 2  Left            A broken white line, with visible long painted segments and gaps, separates my lane
                        from a same-direction lane occupied by queued cars; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           White longitudinal paint separates my lane from parked vehicles on the right, but the
                        vehicles and darkness obscure enough of it that its continuity cannot be established;
                        no curb forms the immediate boundary of my travel lane.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on the left and parking beyond the right edge agree
                        with my lane being the rightmost of two visible travel lanes. | roles: The broken
                        white left boundary fits a same-direction lane line; the white right boundary fits the
                        edge beside parking, although its complete pattern is obscured. | markings: No
                        readable arrows, words, symbols, areas, or transverse lines are visible in my lane. |
                        unseen: The right boundary's full pattern and any markings at the traffic-obscured
                        intersection approach cannot be verified; the right boundary's solid classification is
                        tentative. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        same-direction lane. [US-3B.06-05-06] "Where crossing the lane line markings with care
                        is not discouraged or prohibited, the lane line markings shall consist of a normal
                        width broken white line. Wher"
Step 5  Rule            right_boundary: The white edge line delineates the roadway edge beside parking and
                        does not itself prohibit crossing it. [US-3B.09-01-02] "If used, edge line pavement
                        markings shall delineate the right or left edges of a roadway. ... Right edge line
                        pavement markings, if used, shall consist of a no"
Step 6  change_left     allowed (contested, correct): The broken white lane line permits crossing with care
                        under US-3B.06-05-06.
Step 6  change_right    allowed (contested, correct): The parking-side edge line does not itself prohibit
                        crossing under US-3B.09-01-02; parked vehicles remain physical obstacles.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: Traffic hides the lane-end pavement where a movement arrow could
                        determine this action.
Step 6  turn_right      not_determined: Traffic hides the lane-end pavement where a movement arrow could
                        determine this action.
Step 6  u_turn          not_determined: Traffic hides the lane-end pavement where a movement restriction could
                        determine this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent; permission to cross a painted boundary does not establish that the
                        occupied space beyond it is safe or available.
Advice                  Continue within the travel lane rather than entering the occupied parking strip;
                        change left only after checking traffic. Red signals are visible ahead: stop behind
                        the queue and verify lane-use markings as the intersection approach becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 1066, 21.42 s

bdd100k_val__bf6711ef-76e408aa | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           At night, the car is in the leftmost of two same-direction lanes on a divided urban
                        roadway beneath an overhead structure. Traffic and distant signals are ahead, but the
                        intersection approach is partly obscured by vehicles. (lanes 2, mine 1, full)
Step 2  Left            A continuous solid yellow line runs beside a raised concrete median barrier on the
                        left, with opposing traffic beyond the barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single continuous solid white line separates this lane from another same-direction
                        traffic lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): The white word ONLY is painted in the lane; its outer letters are
                        worn but recognizable.; arrow:straight (full): A white arrow beyond ONLY has one head
                        pointing straight ahead.
Step 4  Cross-check     position: The left median edge and the right lane separator agree with the car
                        occupying lane 1 of 2. | roles: The solid yellow left edge fits a divided roadway, and
                        the solid white separator fits adjacent same-direction lanes. | markings: ONLY agrees
                        with the single-movement straight arrow; neither conflicts with the boundaries. |
                        unseen: No stop line or waiting area is visible; vehicles and darkness obscure the
                        farther approach, so no additional markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the divided roadway's left edge; the
                        concrete barrier physically prevents leaving the lane to the left. [US-3B.09-03] "If
                        used on the roadways of divided highways or one-way streets, or on any ramp in the
                        direction of travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The single solid white lane line discourages crossing but does not
                        prohibit a careful lane change. [US-3B.06-05-06] "Where crossing the lane line
                        markings with care is not discouraged or prohibited, the lane line markings shall
                        consist of a normal width broken white line. Wher"
Step 5  Rule            text:only: ONLY supplements the arrow's exclusive single movement, which here is
                        straight ahead. [US-3B.21-04] "Where through lanes approaching an intersection become
                        mandatory turn lanes, ONLY word pavement markings should be used in addition to signs
                        and the required la"
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits straight travel and excludes
                        left turns, right turns, and U-turns from this lane. [US-3B.23-01] "Lane-use arrow
                        markings are used to indicate the mandatory or permissible movements in certain lanes
                        and in two-way left-turn lanes."
Step 6  change_left     prohibited (correct): The concrete median barrier at the yellow left edge prevents
                        crossing to the left.
Step 6  change_right    allowed (contested, correct): US-3B.06-05-06 discourages, but does not prohibit,
                        crossing the single solid white lane line.
Step 6  go_straight     allowed (contested, label not_determined): The straight arrow permits straight travel
                        under US-3B.23-01.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn under US-3B.23-01.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn under US-3B.23-01.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn under US-3B.23-01.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight; do not turn from it or cross the median
                        barrier. Crossing the solid white line is discouraged rather than prohibited, so
                        change right only when safe; obey the signals ahead and check for obscured stop or
                        crosswalk markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 7375, out 1069, 17.26 s

bdd100k_val__bfd64d5f-ec05de8b | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided multilane roadway continues ahead while an exit ramp branches to the right.
                        My car is in the rightmost of three through lanes, alongside the painted separation
                        from the exit. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a diagonally striped
                        paved gore and the diverging exit ramp beyond; no curb forms this boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes lie to my left and no through lane lies immediately to my right,
                        consistent with lane 3 of 3 and the observed boundary roles. | roles: The broken white
                        left line separates same-direction lanes; the solid white right line delineates the
                        through roadway edge beside the gore. | markings: No guidance markings are visible
                        within my lane; the diagonal gore markings are outside its right boundary. | unseen:
                        No hidden arrows or distant markings have been inferred; the vehicle ahead obscures a
                        small portion of pavement. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing to the adjacent left lane
                        with care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white edge line delineates the roadway edge; this passage
                        does not itself prohibit crossing it. [US-3B.09-01-02] "If used, edge line pavement
                        markings shall delineate the right or left edges of a roadway. ... Right edge line
                        pavement markings, if used, shall consist of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (contested, label prohibited): US-3B.09-01-02 identifies the roadway edge but
                        does not prohibit crossing it; this is not permission to drive through the gore.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action; the exit sign is context, not a lane-
                        use arrow.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: right-boundary crossing is classified only under the supplied edge-line
                        rule, not as authorization to traverse the gore or take the exit.
Advice                  Continue in this lane to remain on the main roadway; a left lane change is permitted
                        when safe. The exit branches right beyond the striped gore: do not treat the edge-line
                        classification as advice to cut across that area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 892, 14.38 s

bdd100k_val__c01c4d85-36b417ee | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A multi-lane road at night continues ahead, with a diagonally hatched paved strip on
                        the right. My car is in the lane immediately left of that strip; darkness prevents a
                        reliable count of all same-direction lanes. (lanes None, mine None, insufficient)
Step 2  Left            A broken white line, with several visible dashes and gaps, separates my lane from
                        another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line borders my lane on the right, with diagonal white hatching on
                        pavement beyond it and no curb at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line establishes at least one same-direction lane to my left;
                        the right edge line places my lane at the right edge of the traveled roadway. The
                        total lane count and index remain uncertain. | roles: The broken white left boundary
                        fits a same-direction lane separator; the solid white right boundary fits an edge
                        adjoining a hatched strip. | markings: No arrows, words, or transverse markings are
                        discernible in my lane. The visible hatching is outside its right boundary. | unseen:
                        No lane count, distant intersection layout, or hidden lane-use marking has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing to the adjacent lane with
                        care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white edge line delineates the roadway edge; this passage
                        does not itself prohibit crossing it or authorize treating the hatched strip as a
                        traffic lane. [US-3B.09-01-02] "If used, edge line pavement markings shall delineate
                        the right or left edges of a roadway. ... Right edge line pavement markings, if used,
                        shall consist of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (contested, label prohibited): The visible edge line delineates the roadway
                        edge under US-3B.09-01-02 but does not itself prohibit crossing.
Step 6  go_straight     allowed (contested, correct): No visible in-lane marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary-crossing permissions are not permissions to use the hatched strip
                        as a travel lane, and no unseen turn restriction has been inferred.
Advice                  Continue within your lane; a left lane change is permitted by the broken line when
                        safe. Do not treat the hatched strip on the right as a travel lane, and verify distant
                        markings and junction controls as visibility improves.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 1060, 20.85 s

bdd100k_val__c0a71f47-14439a44 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A two-way urban street at night, with parked cars along both sides and a signalized
                        intersection in the distance. My car is in the single visible travel lane in its
                        direction. (lanes 1, mine 1, full)
Step 2  Left            Two parallel solid yellow lines form the left boundary, with opposing traffic space
                        beyond.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           No painted boundary is visible on the right; parked cars occupy the roadside beside a
                        raised curb, whose farther portions are obscured by the cars and darkness.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and roadside curb on the right agree with one
                        travel lane in my direction and my lane being leftmost. | roles: The double solid
                        yellow lines fit a center line; the unpainted curb defines the roadside edge rather
                        than another travel lane. | markings: No readable lane-use arrows, words, symbols, or
                        transverse markings are visible in my lane. | unseen: Markings at the distant
                        intersection cannot be resolved in the darkness; none have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow center line prohibits crossing to the left for
                        passing. [US-3B.01-04] "The center line markings on two-lane, two-way roadways shall
                        be one of the following: A. Two-direction passing zone markings consisting of a normal
                        width broken"
Step 5  Rule            right_boundary: No supplied passage authorizes driving across a raised curb; under the
                        physical-edge definition, leaving the roadway across this boundary is prohibited.
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing for
                        passing under US-3B.01-04.
Step 6  change_right    prohibited (correct): The raised roadside curb is a physical edge, not a lane
                        available to enter.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_determined: Lane-use or prohibited-movement markings at the distant intersection
                        cannot be resolved.
Step 6  turn_right      not_determined: Lane-use or prohibited-movement markings at the distant intersection
                        cannot be resolved.
Step 6  u_turn          not_determined: Any pavement marking governing a U-turn at the distant intersection
                        cannot be resolved.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane, keeping clear of parked cars and avoiding crossing the
                        double yellow lines or curb. Before turning at the distant intersection, check the
                        closer pavement markings, signs, and signals; no stopping position is readable here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6473, out 785, 12.41 s

bdd100k_val__c0f5b0d0-17e0110c | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           At night, my car is on a single-lane ramp curving gently right toward congested
                        traffic. A barrier separates this ramp from traffic to the left, and a retaining wall
                        stands beyond the right shoulder. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left side, with a narrow margin and a raised
                        concrete barrier beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates the lane from a paved shoulder, with a retaining
                        wall farther to the right rather than directly at the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edge lines, consistent with a one-lane ramp and
                        ego lane index 1; the traffic beyond the left barrier is not another lane of this
                        ramp. | roles: The solid yellow left edge and solid white right edge fit their
                        respective ramp-edge roles. | markings: No readable arrows, words, symbols, or
                        transverse markings appear in my lane. | unseen: The distant connection is obscured by
                        traffic and darkness; no merge marking or intersection movement restriction is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid yellow marking delineates the ramp's left roadway edge, and
                        the visible concrete barrier prevents leaving the lane to the left. [US-3B.09-03] "If
                        used on the roadways of divided highways or one-way streets, or on any ramp in the
                        direction of travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The solid white marking delineates the right roadway edge; this edge-
                        line passage does not prohibit crossing onto the visible shoulder. [US-3B.09-01-02]
                        "If used, edge line pavement markings shall delineate the right or left edges of a
                        roadway. ... Right edge line pavement markings, if used, shall consist of a no"
Step 6  change_left     prohibited (correct): The raised concrete barrier beyond the yellow left edge
                        physically prevents leaving the ramp to the left.
Step 6  change_right    allowed (contested, label prohibited): The white right edge line delineates a
                        shoulder, and US-3B.09-01-02 does not prohibit crossing it.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the ramp; the edge
                        lines govern lateral departures, not forward travel.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent; rightward crossing is permitted by the observed markings only, not an
                        instruction to drive on the shoulder.
Advice                  Follow the ramp between its edge lines and prepare to slow for the queue ahead. Do not
                        cross toward the left barrier or use the right shoulder as a travel lane; the distant
                        connection is not clear enough to prescribe a merge.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6388, out 944, 18.08 s

bdd100k_val__c16d3fdb-a3a8c912 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided highway continues ahead with a gentle rightward bend. My car is in the left
                        of two same-direction lanes, beside a median-side shoulder. (lanes 2, mine 1, full)
Step 2  Left            A single solid yellow line borders my lane on the left, with a paved shoulder and
                        concrete median barrier beyond it.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A worn broken white line, with visible painted segments and gaps beside a dark
                        pavement seam, separates my lane from another same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car being in lane
                        1 of 2. | roles: The solid yellow left edge fits a divided highway, and the broken
                        white right divider separates same-direction lanes. | markings: No guidance markings
                        are visible within my lane; there is no conflict with the boundaries. | unseen: No
                        distant intersection layout or unreadable sign content has been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow left edge marks the roadway limit and restricts moving
                        left onto the median-side shoulder. [US-3B.09-03] "If used on the roadways of divided
                        highways or one-way streets, or on any ramp in the direction of travel, left edge line
                        pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent lane
                        with care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): The solid yellow left roadway edge restricts moving onto the
                        shoulder under US-3B.09-03.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No in-lane marking restricts continuing along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane, or change right across the broken white line after checking
                        traffic and blind spots. Do not move left onto the median shoulder; the distant sign
                        is not readable enough to determine route guidance.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 796, 13.32 s

bdd100k_val__c1e6340e-084ce27d | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided freeway at night continues toward an overpass. My car is in the leftmost
                        lane beside the median shoulder; at least one same-direction lane lies to the right,
                        but the far-right roadway edge is unclear. (lanes None, mine 1, partial)
Step 2  Left            A single solid yellow line runs along the left of my lane, with a narrow paved
                        shoulder and concrete median barrier beyond it.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           White broken line segments with visible gaps separate my lane from the adjacent lane
                        occupied by the bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge line agrees with my lane being leftmost, and the right lane
                        line establishes another same-direction lane; the total lane count remains uncertain.
                        | roles: The solid yellow left edge fits a divided freeway, and the broken white right
                        boundary fits separation of same-direction lanes. | markings: No arrows, words,
                        symbols, transverse lines, or marked waiting areas are visible in my lane. | unseen:
                        No far-right lane count or hidden downstream markings have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow left edge delineates the divided roadway's left limit
                        and restricts moving left across it onto the median shoulder. [US-3B.09-03] "If used
                        on the roadways of divided highways or one-way streets, or on any ramp in the
                        direction of travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The broken white lane line permits crossing into the adjacent same-
                        direction lane with care. [US-3B.06-05-06] "Where crossing the lane line markings with
                        care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 6  change_left     prohibited (correct): The solid yellow freeway left edge restricts crossing onto the
                        median shoulder under US-3B.09-03.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane and stay right of the yellow median edge. A rightward lane
                        change is permitted by the markings, but wait for a safe gap clear of the bus and
                        other traffic.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 855, 13.13 s

bdd100k_val__c39dc2ff-6976d19d | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A nighttime urban street approaches a signalized intersection. My car is in the left
                        of two same-direction lanes, with a sidewalk on the left and another traffic lane on
                        the right. (lanes 2, mine 1, full)
Step 2  Left            A raised curb borders the lane on the left, with a sidewalk beyond; no painted
                        longitudinal line is clearly visible beside it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent lane occupied by the
                        yellow taxi.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A large white curved arrow has a single head pointing left.;
                        symbol:bike (partial): A white bicycle symbol with shared-lane chevrons appears near
                        the right side of my lane.; text:only (full): The white word ONLY is painted beyond
                        the arrow.; line:stop_line (partial): A transverse white line appears before the
                        intersection crossing; distance and vehicles obscure its complete extent.;
                        line:crosswalk (partial): White crosswalk markings extend across the approach ahead,
                        partly obscured by vehicles.
Step 4  Cross-check     position: The left curb and right lane separator agree with my lane being the leftmost
                        of two same-direction lanes. | roles: The white right separator fits a same-direction
                        lane line; the curb forms the left roadway edge. | markings: The left arrow and ONLY
                        agree on a single left-turn movement. The bicycle marking does not supply another
                        motor-vehicle movement. | unseen: No hidden arrow heads or additional lanes are
                        inferred; the bicycle and transverse markings have reduced evidence because of
                        darkness, distance, and occlusion. | result: consistent
Step 5  Rule            left_boundary: No supplied passage directly governs crossing this unpainted raised
                        curb; as a physical roadway boundary, it is not a traversable lane-change route.
Step 5  Rule            right_boundary: The single solid white lane line discourages, but does not prohibit,
                        crossing into the adjacent lane with care. [US-3B.06-05-06] "Where crossing the lane
                        line markings with care is not discouraged or prohibited, the lane line markings shall
                        consist of a normal width broken white line. Wher"
Step 5  Rule            arrow:left: The left-only arrow permits a left turn and restricts movements not shown,
                        including straight, right, and U-turn movements. [US-3B.23-01] "Lane-use arrow
                        markings are used to indicate the mandatory or permissible movements in certain lanes
                        and in two-way left-turn lanes."
Step 5  Rule            symbol:bike: The bicycle pavement symbol provides guidance concerning bicycle traffic
                        and does not independently govern the seven requested actions. [US-3B.20-01] "Word,
                        symbol, and arrow markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. These pavement markings can be helpful to "
Step 5  Rule            text:only: ONLY supplements the arrow's exclusive left-turn designation. [US-3B.21-04]
                        "Where through lanes approaching an intersection become mandatory turn lanes, ONLY
                        word pavement markings should be used in addition to signs and the required la"
Step 5  Rule            line:stop_line: No supplied passage specifically covers this stop line, and under the
                        provided definitions it does not itself require stop_first.
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the crosswalk, and under the
                        provided definitions it does not decide the seven actions.
Step 6  change_left     prohibited (correct): The raised left curb is a physical edge, not a lane-change
                        route.
Step 6  change_right    allowed (contested, correct): US-3B.06-05-06 only discourages crossing the single
                        solid white lane line.
Step 6  go_straight     prohibited (correct): The left-only arrow does not show straight travel, so
                        US-3B.23-01 restricts it.
Step 6  turn_left       allowed (correct): The left arrow permits this movement under US-3B.23-01.
Step 6  turn_right      prohibited (correct): The left-only arrow does not show a right turn.
Step 6  u_turn          prohibited (contested, label allowed): The left-only arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a left turn; for another movement, change right only when safe and
                        verify the adjacent lane's permitted movements. Watch for cyclists and pedestrians,
                        obey the intersection signals, and stop before the visible stop line when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line', 'symbol:bike'], missed []), actions True, unsafe
                        [], citation None, contradictions []
Tokens                  in 7375, out 1372, 22.8 s

bdd100k_val__c3ecb3cb-5fb43d29 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban street has two lanes in this direction, with opposing traffic separated by a
                        narrow raised median with flexible posts. My car is in the left lane, approaching a
                        junction with a straight-only marking in its lane. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line follows a narrow raised median fitted with white-and-yellow
                        flexible posts; opposing traffic lies beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent same-direction lane
                        nearby, transitioning to short white segments and gaps farther ahead; there is no curb
                        along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): The white word ONLY is painted across my lane.; arrow:straight
                        (full): Beyond ONLY, a white arrow has a single head pointing straight ahead.
Step 4  Cross-check     position: Two same-direction lanes and ego position 1 agree with a median edge on the
                        left and a lane divider on the right. | roles: The yellow median-side edge and white
                        same-direction divider fit their assigned roles. | markings: ONLY agrees with the
                        single straight-ahead arrow; neither conflicts with the boundaries. | unseen: No
                        unseen stop line, waiting area, or additional arrow is inferred. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line identifies the left roadway edge, and the raised
                        median physically prevents a leftward lane change. [US-3B.09-03] "If used on the
                        roadways of divided highways or one-way streets, or on any ramp in the direction of
                        travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: Crossing the single solid white lane divider is discouraged rather
                        than prohibited, so a careful rightward lane change is permitted. [US-3B.06-05-06]
                        "Where crossing the lane line markings with care is not discouraged or prohibited, the
                        lane line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            text:only: ONLY supplements the arrow and identifies this lane as serving its single
                        indicated movement. [US-3B.21-04] "Where through lanes approaching an intersection
                        become mandatory turn lanes, ONLY word pavement markings should be used in addition to
                        signs and the required la"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight and excludes left
                        turns, right turns, and U-turns from this lane. [US-3B.23-01] "Lane-use arrow markings
                        are used to indicate the mandatory or permissible movements in certain lanes and in
                        two-way left-turn lanes."
Step 6  change_left     prohibited (correct): The raised median forms a physical left roadway edge that cannot
                        be crossed as a lane change.
Step 6  change_right    allowed (contested, correct): US-3B.06-05-06 discourages but does not prohibit
                        crossing the single solid white lane line.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement under US-3B.23-01.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane and do not cross the raised median. If you need a
                        different movement, select an appropriately marked lane safely in advance; crossing
                        the single white divider is discouraged but not prohibited, and the roadside no-U-turn
                        sign also warrants attention.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7375, out 1036, 16.24 s

bdd100k_val__c400a0e1-c137168b | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A divided urban highway passes beneath bridges and approaches a right-hand exit split.
                        My car is behind the yellow taxi in the leftmost of three visible same-direction
                        lanes. (lanes 3, mine 1, full)
Step 2  Left            A solid yellow line runs beside a concrete median barrier on the left, with opposing
                        traffic beyond the barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broad solid white line separates my lane from the lane to the right and leads toward
                        a striped separation area at the split.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with my lane being the leftmost of three. | roles: The solid yellow median edge and
                        solid white same-direction separator fit their assigned roles. | markings: No guidance
                        marking is readable within my lane; the striped separation area and pavement lettering
                        to the right are outside it. | unseen: The taxi hides some pavement ahead; no marking
                        has been inferred beneath it. | result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the left roadway edge; the concrete barrier
                        physically prevents leaving the lane to the left. [US-3B.09-03] "If used on the
                        roadways of divided highways or one-way streets, or on any ramp in the direction of
                        travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: The solid white lane line discourages crossing but does not prohibit a
                        careful change into the adjacent lane. [US-3B.06-05-06] "Where crossing the lane line
                        markings with care is not discouraged or prohibited, the lane line markings shall
                        consist of a normal width broken white line. Wher"
Step 6  change_left     prohibited (correct): The concrete median barrier prevents crossing the left roadway
                        edge.
Step 6  change_right    allowed (contested, correct): US-3B.06-05-06 discourages, but does not prohibit,
                        crossing the solid white lane line before the striped separation area.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing along my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue behind the taxi to remain on the left branch. If taking the right exit,
                        change lanes only when safe before the striped separation area; crossing the solid
                        white lane line is discouraged, and the median prevents any move left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6517, out 878, 15.67 s

bdd100k_val__c464c963-0279dcc0 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A two-way residential street continues ahead, with parked cars along both curbs. My
                        car is in the single through lane to the right of the double yellow center line; no
                        intersection is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            Two parallel solid yellow lines separate my lane from opposing traffic; no curb is
                        present at this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           No painted right boundary is visible; parked vehicles occupy the roadside, with
                        portions of a raised curb visible beyond them and much of the edge obscured.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with the center line on the left and
                        the parking-lined roadway edge on the right. | roles: The double solid yellow marking
                        fits a center line; the right edge is physical rather than painted. | markings: No
                        guidance markings are visible within my lane. | unseen: The right edge is partly
                        hidden by parked vehicles; no hidden paint or distant intersection markings are
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line prohibits crossing into opposing
                        traffic for passing. [US-3B.01-04] "The center line markings on two-lane, two-way
                        roadways shall be one of the following: A. Two-direction passing zone markings
                        consisting of a normal width broken"
Step 5  Rule            right_boundary: No supplied passage governs driving across this unpainted raised curb;
                        as a physical roadway boundary, it is not a permissible lane-change route.
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing for
                        passing under US-3B.01-04.
Step 6  change_right    prohibited (correct): The right side ends at a raised curb beyond parked vehicles, not
                        an adjacent travel lane.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow or other marking restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking in view governs this movement.
Step 6  turn_right      not_applicable: No marking in view governs this movement.
Step 6  u_turn          not_applicable: No marking in view governs this movement; the center line governs
                        boundary crossing, not intersection movements.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the existing lane without crossing the double yellow lines to pass. Slow
                        down and leave clearance for the person beside the parked minivan and for opening
                        vehicle doors; turn permissions at a later intersection are not established by this
                        view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6473, out 867, 15.61 s

bdd100k_val__c4b77809-63fd577c | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A wet, two-way urban street approaches a cross-street intersection. My car is in the
                        single through lane in its direction, with oncoming traffic to the left and parked
                        vehicles along the right curb. (lanes 1, mine 1, full)
Step 2  Left            Two solid yellow lines run along the left side of my lane, with opposing traffic
                        beyond and no curb at the lines.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           No painted right boundary is visible; parked vehicles obscure much of the roadside,
                        while a raised curb is visible farther ahead on the right.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        text:stop (full): A worn white STOP word is painted across my lane.; line:stop_line
                        (full): A transverse solid white stop line is visible ahead of the STOP word and
                        before the crosswalk.; line:crosswalk (full): White crosswalk bars cross my lane at
                        the intersection ahead.
Step 4  Cross-check     position: The center line on the left and curbside roadway edge on the right agree
                        with one lane in my direction and ego lane index 1. | roles: The double solid yellow
                        boundary separates opposing traffic; the unpainted curbside edge is not a lane
                        separator. | markings: The STOP word, stop line and crosswalk agree as an intersection
                        approach; no lane-use arrow or waiting area is visible. | unseen: The parked pickup
                        hides part of the right edge, so absence of paint beneath it cannot be confirmed. |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line prohibits crossing to the opposing
                        side for passing. [US-3B.01-04] "The center line markings on two-lane, two-way
                        roadways shall be one of the following: A. Two-direction passing zone markings
                        consisting of a normal width broken"
Step 5  Rule            right_boundary: No supplied passage authorizes crossing a raised curb; the physical
                        roadway edge is not a permitted lane-change route.
Step 5  Rule            text:stop: The STOP word supplies a regulatory message and, under the supplied action
                        definition, requires a full stop before an otherwise allowed movement. [US-3B.20-01]
                        "Word, symbol, and arrow markings on the pavement are used for the purpose of
                        regulating, warning, or guiding traffic. These pavement markings can be helpful to "
Step 5  Rule            line:stop_line: The solid white stop line identifies the point behind which the
                        required stop is to be made. [US-3B.19-01-02] "Stop lines may be used to indicate the
                        point behind which vehicles are required to stop in compliance with a STOP sign ... or
                        some other traffic control device "
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and this marking
                        does not determine any of the seven actions.
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing left for
                        passing under US-3B.01-04.
Step 6  change_right    prohibited (correct): The right side is a curbside roadway edge, not a traversable
                        adjacent lane; crossing the raised curb is prohibited.
Step 6  go_straight     stop_first (contested, label not_determined): No arrow restricts continuing straight,
                        but the STOP word requires a full stop first.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stop behind the white stop line before the crosswalk, consistent with the visible STOP
                        sign. Continue straight only after checking cross traffic and pedestrians; do not
                        cross the double yellow lines or move toward the curb and parked vehicles.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'text:stop'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 6628, out 1170, 18.37 s

bdd100k_val__c4d25f00-3b1d8669 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A broad urban street at night approaches a signal-controlled intersection with a
                        marked crosswalk. My car appears to be in the third of four same-direction lanes, with
                        another lane on the right; darkness makes the far-left roadway edge uncertain. (lanes
                        4, mine 3, partial)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb borders my lane here.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible separated segments, separates my lane from the lane
                        occupied by the sedan ahead-right; no curb borders my lane here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white transverse stop line crosses my lane before the
                        crosswalk.; line:crosswalk (full): Broad white crosswalk stripes extend across my lane
                        beyond the stop line.
Step 4  Cross-check     position: Same-direction lanes on both sides agree with an interior ego lane; the
                        apparent third-of-four position is less certain because the far-left edge is dark. |
                        roles: Both white broken boundaries fit ordinary same-direction lane separators. |
                        markings: The stop line and crosswalk agree with the intersection approach; no
                        directional arrow, STOP word, or waiting area is visible in my lane. | unseen: The
                        total lane count is an estimate because the far-left edge is poorly illuminated; no
                        hidden directional marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing to the left with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            right_boundary: The broken white lane line permits crossing to the right with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            line:stop_line: The white stop line identifies where to stop when the signal or
                        another applicable control requires stopping; it does not independently require every
                        movement to stop first. [US-3B.19-01-02] "Stop lines may be used to indicate the point
                        behind which vehicles are required to stop in compliance with a STOP sign ... or some
                        other traffic control device "
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalk markings; the
                        crosswalk identifies a pedestrian crossing and does not determine the seven requested
                        movement permissions.
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight;
                        the stop line only identifies a stopping position when stopping is required.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane if the signal and traffic permit; either dashed
                        boundary permits a careful lane change. If required to stop, stop behind the white
                        stop line and keep the crosswalk clear; these markings do not establish turn
                        permissions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6251, out 1234, 21.36 s

bdd100k_val__c4e92086-e1b8324f | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban divided roadway continues straight toward a distant signalized intersection.
                        My car is in the rightmost of three visible same-direction lanes, with parked vehicles
                        along the right curb. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; a dark pavement seam runs nearby.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A raised curb borders the right side, with parked vehicles beside it and a sidewalk
                        beyond; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right curb agree with my lane being the rightmost
                        of three same-direction lanes. | roles: The broken white line fits a same-direction
                        lane divider; the curb physically defines the roadway edge. | markings: No readable
                        arrows, words, symbols, or transverse markings are visible in my lane. | unseen: No
                        markings are inferred in the distant intersection, where fine details cannot be
                        resolved. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing into the adjacent lane with
                        care. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: No supplied passage governs crossing a physical curb; as a physical
                        roadway boundary, it prohibits moving right out of this lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    prohibited (contested, label allowed): The raised curb is a physical boundary, not a
                        traversable adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may continue straight or cross the broken white line to the left when safe; parked
                        vehicles may require moving left for clearance. Do not cross the right curb, and check
                        intersection signs, signals, and closer markings before making a turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6597, out 859, 15.78 s

bdd100k_val__c55da7df-facccafc | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signalized intersection, with a freeway direction
                        sign pointing right. My car is in the rightmost of three lanes traveling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A white broken line with short rectangular segments and intervening gaps separates my
                        lane from another same-direction lane on the left; there is no curb.
                        white dotted, curb no, lane_line, evidence full
Step 2  Right           A continuous white line curves right along my lane, with a paved roadside strip, a
                        parked vehicle, and a raised curb farther to its right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:only (full): The white word ONLY is clearly painted in my lane; no associated
                        directional arrow is readable in the visible pavement ahead.
Step 4  Cross-check     position: Three same-direction lanes, with my lane third from the left, agree with a
                        lane line on the left and a roadway edge line on the right. | roles: The white dotted
                        left boundary fits separation of same-direction lanes with a downstream lane-function
                        change; the solid white right boundary fits a roadway edge. | markings: ONLY suggests
                        an exclusive movement, but no arrow is visible to identify that movement; neither the
                        curving edge nor the roadside sign substitutes for an arrow in my lane. | unseen: No
                        directional arrow, stop line, crosswalk, or waiting area is reported where vehicles
                        and distance prevent reliable identification. | result: consistent
Step 5  Rule            left_boundary: The dotted lane line warns of a downstream lane-function change and
                        does not prohibit crossing into the adjacent ordinary lane. [US-3A.04-01-DE] "D. A
                        dotted lane line provides warning of a downstream change in lane function. E. A dotted
                        line used as a lane line or edge line extension guides vehicles thro"
Step 5  Rule            right_boundary: The solid white line identifies the roadway edge; this passage does
                        not prohibit crossing it. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 5  Rule            text:only: ONLY supplements an exclusive single-movement lane designation, but does
                        not identify the permitted direction without its associated arrow. [US-3B.21-04]
                        "Where through lanes approaching an intersection become mandatory turn lanes, ONLY
                        word pavement markings should be used in addition to signs and the required la"
Step 6  change_left     allowed (correct): The dotted white lane line warns of a lane-function change but does
                        not prohibit crossing.
Step 6  change_right    allowed (contested, label prohibited): The white edge line identifies the roadway
                        edge, and the specific edge-line passage does not prohibit crossing onto the paved
                        roadside strip.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight; ONLY
                        alone does not govern this action under the supplied definitions.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: ONLY and the roadside sign have not been used to invent an arrow
                        direction, and edge-line crossing permission is not a recommendation to drive on the
                        roadside.
Advice                  Check the lane-use arrows and intersection signs before proceeding: ONLY is visible,
                        but its associated movement is not identifiable here. A leftward lane change is not
                        prohibited by the dotted line; avoid the roadside strip and parked vehicle, and obey
                        the traffic signals.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 7164, out 1131, 24.38 s

bdd100k_val__c588eb5e-dfd59d8e | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street at dusk approaches a signalized intersection. My car is in the
                        leftmost of two lanes traveling in this direction, with opposing traffic to the left
                        and another travel lane and parked vehicles to the right. (lanes 2, mine 1, full)
Step 2  Left            Two parallel solid yellow lines separate my lane from oncoming traffic; no curb forms
                        this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A worn broken white line, with visible segments and gaps, separates my lane from the
                        adjacent same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and same-direction lane line on the right agree
                        with my lane being lane 1 of 2. | roles: Double solid yellow fits the opposing-traffic
                        center line, and broken white fits the same-direction lane divider. | markings: No
                        readable guidance markings appear within the visible portion of my lane. | unseen:
                        Vehicles and distance obscure the pavement near the intersection; no arrows, words,
                        stop line, or crosswalk are inferred there. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line separates opposing directions in a
                        no-passing zone, so crossing it to move left into opposing traffic is prohibited.
                        [US-3B.01-06] "Except where a reversible lane or a two-way left-turn lane is present,
                        the center line markings on undivided two-way roadways with four or more lanes for
                        moving"
Step 5  Rule            right_boundary: The broken white lane line permits changing right with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing left into
                        opposing traffic.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing right with care
                        under US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: Pavement near the intersection is obscured, so any lane-use arrow
                        governing a left turn cannot be determined.
Step 6  turn_right      not_determined: Pavement near the intersection is obscured, so any lane-use arrow
                        governing a right turn cannot be determined.
Step 6  u_turn          not_determined: Pavement near the intersection is obscured, so any marking governing a
                        U-turn cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary decisions follow their line types, straight travel has no visible
                        restriction, and obscured intersection markings are not treated as confirmed turn
                        permissions.
Advice                  Continue in this lane for straight travel; do not cross the double yellow lines, and
                        change right only after checking the vehicles alongside. Confirm turn-lane markings
                        and obey the intersection signals as they become clearly visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6484, out 845, 13.34 s

bdd100k_val__c59500f0-130d7415 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with parked vehicles along the curbs. My car
                        is in the left of two lanes traveling in this direction; no intersection or lane
                        ending is clearly visible ahead. (lanes 2, mine 1, full)
Step 2  Left            Two parallel solid yellow lines separate my lane from opposing traffic on the left; no
                        curb forms this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and a same-direction lane on the right agree
                        with my lane being lane 1 of 2. | roles: The double solid yellow center line and
                        broken white lane divider fit their observed roles. | markings: No arrows, words,
                        symbols, waiting areas, or transverse markings are visible in my lane. | unseen: No
                        markings or intersection details beyond the visible stretch have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line defines a two-direction no-passing
                        zone, prohibiting crossing it to pass opposing traffic. [US-3B.01-06] "Except where a
                        reversible lane or a two-way left-turn lane is present, the center line markings on
                        undivided two-way roadways with four or more lanes for moving"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane with care. [US-3B.06-05-06] "Where crossing the lane line markings with
                        care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 6  change_left     prohibited (correct): The double solid yellow center line marks a no-passing zone and
                        prohibits leaving this lane to the left for passing.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line only when
                        safe. Do not cross the double yellow center line to pass; no turn guidance or stopping
                        point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6484, out 811, 12.36 s

bdd100k_val__c5b2506d-07e406a6 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A multilane urban roadway runs beside a raised landscaped median, with a signalized
                        intersection ahead. My car is in the second lane from the left among four visible
                        lanes traveling in this direction. (lanes 4, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the same-
                        direction lane occupied by the white car on the right; no curb forms my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 4: one lane
                        lies to the left and two to the right. | roles: Both broken white boundaries fit
                        separation of same-direction traffic lanes. | markings: No readable guidance markings
                        or transverse lines appear in the visible portion of my lane. | unseen: The lead car
                        and distance obscure portions of the lane approaching the intersection; no markings
                        are inferred there. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        left lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The broken white lane line permits crossing with care into the
                        adjacent right lane. [US-3B.06-05-06] "Where crossing the lane line markings with care
                        is not discouraged or prohibited, the lane line markings shall consist of a normal
                        width broken white line. Wher"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible broken boundaries permit lane changes with care, and no unseen
                        intersection marking is used to authorize a turn.
Advice                  Continue in this lane for straight travel; either lane change is permitted by the
                        visible markings when traffic allows. Check the intersection's signs, signals and any
                        markings revealed ahead before selecting a turning lane or stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6096, out 866, 16.55 s

bdd100k_val__c74ee988-8f4b380d | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street with parked vehicles along both sides continues toward a
                        distant intersection. My car is in the single travel lane in its direction. (lanes 1,
                        mine 1, full)
Step 2  Left            Two solid yellow lines separate my lane from opposing traffic; there is no curb at
                        this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line separates my lane from the strip occupied by parked
                        vehicles; no curb forms the immediate lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and parking edge on the right agree with one
                        travel lane in my direction and ego lane index 1. | roles: The double yellow center
                        line separates opposing traffic, and the solid white edge line borders the parking
                        strip. | markings: No guidance markings are visible in my lane; the arrow and
                        lettering to the left are across the center line and do not govern my lane. | unseen:
                        No distant intersection markings or obscured pavement features have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow center line prohibits crossing to pass
                        opposing-direction traffic. [US-3B.01-04] "The center line markings on two-lane, two-
                        way roadways shall be one of the following: A. Two-direction passing zone markings
                        consisting of a normal width broken"
Step 5  Rule            right_boundary: The solid white edge line delineates the roadway edge and does not
                        itself prohibit crossing into the parking strip. [US-3B.09-01-02] "If used, edge line
                        pavement markings shall delineate the right or left edges of a roadway. ... Right edge
                        line pavement markings, if used, shall consist of a no"
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing for
                        passing under US-3B.01-04.
Step 6  change_right    allowed (contested, label prohibited): The white edge line identifies the parking edge
                        but does not prohibit crossing under US-3B.09-01-02.
Step 6  go_straight     allowed (contested, correct): No arrow in my lane restricts continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the current travel lane and do not cross the double yellow lines to
                        pass. The right-hand strip contains parked vehicles, not another travel lane; crossing
                        its white edge line is not a guarantee of safe or lawful space to drive.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6624, out 799, 11.11 s

bdd100k_val__c7c042ec-4986a853 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A three-lane urban roadway at night approaches a signalized intersection. My car is in
                        the middle lane; darkness limits visibility farther ahead. (lanes 3, mine 2, full)
Step 2  Left            A white line of short, closely spaced rectangular dashes separates my lane from the
                        lane on the left and becomes continuous farther ahead; no curb forms this boundary.
                        white dotted, curb no, lane_line, evidence full
Step 2  Right           A white line of short, closely spaced rectangular dashes separates my lane from the
                        lane on the right and becomes continuous farther ahead; no curb forms this boundary.
                        white dotted, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white bent arrow ahead has a head pointing left and a stem
                        extending back toward the car.
Step 4  Cross-check     position: A same-direction lane on each side agrees with three lanes and my position
                        as lane 2. | roles: White lane separators agree with same-direction traffic; the short
                        dashes warn of an approaching change in lane function. | markings: The left-turn arrow
                        governs my lane; the ONLY words in the adjacent lanes do not govern my lane. | unseen:
                        No stop line or waiting area can be identified in the dark intersection approach; none
                        is inferred. | result: consistent
Step 5  Rule            left_boundary: The dotted white lane line warns of a downstream lane-function change
                        and does not prohibit crossing it. [US-3A.04-01-DE] "D. A dotted lane line provides
                        warning of a downstream change in lane function. E. A dotted line used as a lane line
                        or edge line extension guides vehicles thro"
Step 5  Rule            right_boundary: The dotted white lane line warns of a downstream lane-function change
                        and does not prohibit crossing it. [US-3A.04-01-DE] "D. A dotted lane line provides
                        warning of a downstream change in lane function. E. A dotted line used as a lane line
                        or edge line extension guides vehicles thro"
Step 5  Rule            arrow:left: The left-turn lane-use arrow permits a left turn from my lane and
                        restricts movements not shown. [US-3B.23-01] "Lane-use arrow markings are used to
                        indicate the mandatory or permissible movements in certain lanes and in two-way left-
                        turn lanes."
Step 6  change_left     allowed (correct): The dotted white lane separator permits crossing with care; the
                        continuous white portion farther ahead discourages rather than prohibits crossing.
Step 6  change_right    allowed (correct): The dotted white lane separator permits crossing with care; the
                        continuous white portion farther ahead discourages rather than prohibits crossing.
Step 6  go_straight     prohibited (WRONG, label allowed): The left-turn arrow does not show a straight
                        movement.
Step 6  turn_left       allowed (WRONG, label not_determined): The left-turn arrow permits turning left.
Step 6  turn_right      prohibited (WRONG, label allowed): The left-turn arrow does not show a right turn.
Step 6  u_turn          prohibited (WRONG, label not_determined): The left-turn arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a left turn, following the applicable traffic signal and yielding as
                        required. For another movement, select an appropriately marked lane before the
                        intersection; check adjacent traffic before changing lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_right']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6715, out 1155, 22.51 s

bdd100k_val__c96ffe59-1cf2df11 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with opposing traffic to the left and
                        curbside parking to the right. My car is in the rightmost of two lanes traveling in
                        this direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with several visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white longitudinal line separates the travel lane from the curbside parking strip
                        ahead; its visible portion appears solid, but shadow obscures much of its nearer
                        continuation, and the sidewalk curb is beyond the parking strip.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 2 agree with a lane line on the
                        left and a parking-side roadway edge on the right. | roles: The broken white left line
                        fits separation of same-direction traffic; the visible solid white right line fits a
                        roadway edge adjoining parking. | markings: No readable guidance arrows, words,
                        symbols, or transverse markings are visible in my lane. | unseen: The right boundary's
                        near continuation is shadowed; no hidden markings or intersection movement
                        restrictions are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing with care into the adjacent
                        same-direction lane. [US-3B.06-05-06] "Where crossing the lane line markings with care
                        is not discouraged or prohibited, the lane line markings shall consist of a normal
                        width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white edge line delineates the roadway edge and does not
                        itself prohibit crossing into the adjoining parking strip. [US-3B.09-01-02] "If used,
                        edge line pavement markings shall delineate the right or left edges of a roadway. ...
                        Right edge line pavement markings, if used, shall consist of a no"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (WRONG, label prohibited): The visible white edge line delineates the parking-
                        side roadway edge under US-3B.09-01-02 without itself prohibiting crossing.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other in-lane marking restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary permissions concern crossing only, and no intersection turning
                        permissions are inferred from them.
Advice                  Continue straight in this lane; a left lane change is permitted when clear. The strip
                        to the right is for curbside parking rather than another through lane, so crossing its
                        edge marking is not permission to use it for passing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6597, out 996, 20.69 s

bdd100k_val__ca15f699-e51c14c0 | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A multilane urban road at night approaches a signalized intersection. My car is in the
                        middle of three visible lanes traveling in this direction; distant pavement details
                        are difficult to distinguish. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from the lane
                        containing the blue car on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another
                        traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One same-direction lane on each side agrees with three lanes and ego lane
                        index 2. | roles: Both white broken boundaries fit same-direction lane separators. |
                        markings: No guidance markings are readable within my lane, so none contradict the
                        boundaries. | unseen: No distant arrows, words, crosswalk, or stop line are inferred;
                        darkness and distance obscure the intersection approach. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits crossing to the left with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            right_boundary: The broken white lane line permits crossing to the right with care.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing with care under
                        US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant approach pavement is too dark and far away to determine
                        whether a lane-use marking governs a left turn.
Step 6  turn_right      not_determined: The distant approach pavement is too dark and far away to determine
                        whether a lane-use marking governs a right turn.
Step 6  u_turn          not_determined: The distant approach pavement is too dark and far away to determine
                        whether a movement marking governs a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may continue in this lane or cross either broken white boundary when safe; check
                        especially for the blue car on the left. Red signals are visible ahead: prepare to
                        stop and confirm the intersection's lane-use markings before attempting a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6096, out 897, 15.71 s

bdd100k_val__fe194677-e2d2ac8c | lane | Test R | gpt-6.1-sol
------------------------------------------------------------
Step 1  Scene           A congested airport-terminal roadway runs beneath elevated structures, with several
                        vehicles ahead. My car follows the black SUV beside a snow-covered strip on the left;
                        snow and traffic prevent a reliable lane count or lane-position assignment. (lanes
                        None, mine None, insufficient)
Step 2  Left            Snow covers most of the left boundary; a short yellow painted segment is visible near
                        the SUV ahead, with taxis beyond the snow, but its pattern and any underlying curb are
                        obscured.
                        yellow none, curb no, unknown, evidence partial
Step 2  Right           A short white painted segment is visible at the lower right, with vehicles beyond it,
                        but traffic and the hood hide enough of its continuation that a solid or broken
                        pattern cannot be established.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The right-side white marking and adjacent traffic suggest another same-
                        direction lane on the right, but the obscured left boundary and roadway width prevent
                        a reliable count or index. | roles: White fits a same-direction lane boundary; the
                        yellow fragment alone does not establish whether the left side is a roadway edge or
                        another boundary type. | markings: No arrows, words, symbols, waiting areas, or
                        transverse lines can be identified on the visible pavement in my lane. | unseen:
                        Neither boundary pattern is established. The curb values indicate no visible curb, not
                        confirmation that none exists beneath the snow; pattern values likewise do not
                        establish absence of paint. | result: consistent
Step 5  Rule            left_boundary: Yellow can delineate several different boundary types, so this partly
                        hidden fragment does not establish whether crossing left is permitted.
                        [US-3A.03-03-04] "When used, yellow markings for longitudinal lines shall delineate:
                        A. The separation of traffic traveling in opposite directions, B. The left-hand edge
                        of the r"
Step 5  Rule            right_boundary: Crossing a broken white lane line is permitted and crossing a single
                        solid white lane line is discouraged, but the incomplete view does not exclude a more
                        restrictive boundary. [US-3B.06-05-06] "Where crossing the lane line markings with
                        care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 6  change_left     not_determined (contested, correct): Snow hides the boundary configuration and any
                        physical edge that would decide whether crossing is permitted.
Step 6  change_right    not_determined (correct): The white boundary's complete configuration is hidden, so
                        the applicable crossing restriction cannot be determined.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane-ending marking
                        restricts continuing along my lane.
Step 6  turn_left       not_determined: Vehicles obscure the pavement farther ahead where any governing lane-
                        use marking would appear.
Step 6  turn_right      not_determined: Vehicles obscure the pavement farther ahead where any governing lane-
                        use marking would appear.
Step 6  u_turn          not_determined: Vehicles obscure the pavement farther ahead where any governing
                        movement marking would appear.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         consistent
Advice                  Continue cautiously behind the SUV and leave room for slowing traffic. Avoid crossing
                        either boundary until the snow-covered left edge and the right-side marking are clear;
                        no turn-lane assignment or stopping line can be confirmed.
Score                   lane False, boundaries {'left': None, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6694, out 985, 20.8 s
```
