# Reasoning of lane run 20261117_154504_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is a bus visible in the distance. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lines marking the boundaries of my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line marking is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed line, and [UK-Rule131]
                        permits keeping between lane dividers.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed line, and
                        [UK-Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane dividers are broken, and you may
                        proceed straight ahead. You should use the lane appropriate for your intended
                        movement, as no specific lane markings dictate otherwise.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['symbol:bike']), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 13887, out 1008, 65.52 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with multiple lanes ahead, leading towards what appears to be a
                        junction or intersection in the distance. My car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lines marking the boundaries of the lanes.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line marking is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where a vehicle must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed line,
                        and [UK-Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane dividers are broken, and you may
                        proceed straight ahead. You should observe the stop line ahead, as it indicates where
                        you must stop if there is a signal or stop sign.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13887, out 1014, 31.27 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides, and traffic is
                        moving forward towards a junction or area ahead. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right,
                        which appears to be the edge of the carriageway or another lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead in the center of my
                        lane.; arrow:straight (full): A white arrow pointing straight ahead in the center of
                        my lane, further ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: The arrows in my
                        lane indicate straight movement, which is consistent with the lane markings and
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        line, and while no specific rule prohibits changing left from a solid line, the
                        general guidance suggests keeping between lane dividers.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and while no specific rule prohibits changing right from a solid line, the
                        general guidance suggests keeping between lane dividers.
Step 6  go_straight     allowed (correct): allowed: The lane markings show an arrow pointing straight ahead,
                        and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as indicated by the
                        lane markings. Lane changes are prohibited by the solid white lines bordering your
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1085, 81.04 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with buildings lining the left side and residential buildings on the
                        right side. Ahead, the road continues into the distance, and there is no immediate
                        intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is defined by a solid white line separating my lane from the
                        adjacent area where the buildings are located.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           The right boundary is defined by a broken yellow line separating my lane from the
                        adjacent lane.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): A single solid yellow line runs down the center of the road,
                        separating the two lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is solid white, fitting
                        the role of an edge_line. The right boundary is dashed yellow, fitting the role of a
                        lane_line. | markings: The single solid yellow line is interpreted as a stop/yield
                        line, which is consistent with the general markings observed. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The boundary indicates the edge of the carriageway, which is the
                        boundary between the main carriageway and an adjacent area. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: The lane divider should be kept between, as it divides the carriageway
                        into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_yield: Vehicular traffic must give way to traffic on the major road when
                        approaching a junction indicated by this marking. [[UK-HC_MARKINGS-p1-4]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is an edge_line, and
                        no rule prohibits changing into the adjacent area.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed yellow lane_line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if safe.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must give
                        way to traffic on the major road when approaching the junction indicated by the solid
                        yellow line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 13887, out 1063, 67.28 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides, and ahead there is a junction
                        where the road continues and other traffic is present. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, adjacent to a
                        pavement.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line marking the division between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A white dashed line marking the division between lanes.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is a solid white edge
                        line, and the right boundary is a dashed white lane line, which fits their roles. |
                        markings: The dashed line observed in the lane is interpreted as a stop/yield line,
                        which is consistent with the lane markings. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_yield: Vehicular traffic must give way to traffic on a major road when
                        approaching a junction indicated by this marking. [[UK-HC_MARKINGS-p1-4]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a dashed lane
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a dashed lane line,
                        and [UK-Rule131] permits keeping between lane dividers, but the presence of the
                        stop/yield line suggests a controlled movement ahead.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in the left lane for straight travel, as the right boundary is a lane
                        divider. You must give way to traffic when approaching the junction indicated by the
                        stop/yield line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left allowed across a curb',
                        'change_right prohibited across a broken lane line', 'go_straight allowed without the
                        stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13887, out 1053, 65.05 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction where traffic appears
                        to be merging or diverging. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the lane boundary is visible
                        ahead.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, and the right boundary is dashed white, which fits the
                        roles of lane lines. | markings: The stop line is visible ahead, which is consistent
                        with the lane markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicular traffic must stop at signals or a
                        'Stop' sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line and [UK-Rule129] states you MUST NOT cross or straddle a solid white line
                        unless necessary to enter adjoining premises or a side road.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line and [UK-
                        Rule128] states you may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change right if it is safe, but you must not change left. You may proceed
                        straight ahead, and you must stop at the visible stop line before proceeding into the
                        junction.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1061, 83.66 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban area, and the road continues ahead into the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the boundary between lanes.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (left boundary is a lane_line, right boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The stop line marking is present in the lane and is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line and [UK-Rule129] states you MUST NOT cross or straddle a solid white line
                        unless necessary to enter adjoining premises or a side road.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white line and [UK-Rule129] states you MUST NOT cross or straddle a solid white line
                        unless necessary to enter adjoining premises or a side road.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane to govern turning movements.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane to govern turning movements.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane to govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight ahead, but you must stop before the visible
                        stop line if required by a signal or sign.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13887, out 1029, 67.27 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with commercial buildings lining the sides. Ahead, the
                        road continues into the distance, and there is no immediate intersection or ramp
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the
                        adjacent lane to the right.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, and the right boundary is dashed white, which fits the
                        roles of lane_line. | markings: The arrow in my lane shows straight ahead, which is
                        consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white line and [UK-Rule129] states you MUST NOT cross or straddle a solid white line
                        unless necessary to enter adjoining premises or a side road.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line and [UK-
                        Rule128] states you may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side.
Step 6  go_straight     allowed (contested, correct): allowed, because the arrow in my lane shows straight
                        ahead and [UK-Rule128-2] indicates the direction of possible traffic movements.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is restricted from changing left due to the solid
                        white line. You may change right if it is safe, and you are permitted to go straight
                        ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1166, 26.85 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a pedestrian
                        crossing area leading into what appears to be a junction or crossing. (lanes 2, mine
                        1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent area.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A series of white dashed lines forming a pedestrian crossing.;
                        line:yield_line (full): A white dashed line indicating the boundary of the lane ahead
                        of the pedestrian crossing.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: The crosswalk and
                        yield line markings are consistent with the lane boundaries and the general road
                        layout. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:crosswalk: This line indicates a stop line for pedestrians at a level crossing.
                        [[UK-HC_MARKINGS-p1-3]]
Step 5  Rule            line:yield_line: You must give way to traffic on the major road when approaching a
                        crossing indicated by this marking. [[UK-HC_MARKINGS-p1-4]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line, and the rules for solid lines prohibit crossing unless necessary to enter
                        adjoining premises or a side road, which is not indicated.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a solid
                        white line, and the rules for solid lines prohibit crossing unless necessary to enter
                        adjoining premises or a side road, which is not indicated.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Be prepared to stop
                        for pedestrians at the marked crossing area ahead, as you must give way to them.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1137, 68.79 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection where traffic
                        appears to be moving through or approaching a junction. (lanes 2, mine 1, full)
Step 2  Left            There is a dashed white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a dashed white line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A dashed white line marking the boundary of the lane.;
                        line:stop_line (partial): A dashed white line marking the boundary of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane_lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop lines are located at
                        the end of the visible lane stretch, consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where a vehicle must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed white
                        line, and [UK-Rule128] permits crossing double white lines where the nearer line is
                        broken if safe.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if safe.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes left or right if it is safe to do so, and you may proceed
                        straight ahead. You should observe the intersection ahead for any required maneuvers.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1101, 67.18 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining the left side and trees lining
                        the right side. Ahead, the road continues into the distance, appearing to be a
                        standard road section rather than an immediate intersection or ramp. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, adjacent to a
                        pavement/sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from an adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead, located in the center of
                        the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: The single straight arrow in my lane is consistent with the
                        boundaries and does not contradict any other markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The boundary indicates the edge of the carriageway, which is consistent
                        with the role of an edge_line. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: The broken white line serves as a lane divider, and you should keep
                        between these lines. [[UK-Rule131]]
Step 5  Rule            arrow:straight: The white direction arrow indicates that you need to get back onto
                        your side of the road, which in this context means proceeding straight ahead. [[UK-
                        Rule128-2]]
Step 6  change_left     prohibited (contested, label allowed): prohibited, because the right boundary is a
                        lane_line and the left boundary is an edge_line, and there is no marking allowing a
                        change left.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed lane_line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if safe.
Step 6  go_straight     allowed (correct): allowed, because the arrow:straight in my lane indicates that
                        proceeding straight ahead is permitted, and nothing restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no waiting area is
                        visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no waiting area is
                        visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no waiting area is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and are permitted to proceed straight ahead. You may
                        change right into the adjacent lane, but changing left is not permitted. No specific
                        stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13887, out 1099, 60.93 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction where the road
                        continues straight and appears to curve slightly to the right. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, and the right boundary is dashed white, which fits the
                        roles of lane lines. | markings: The straight arrow in my lane agrees with the lane
                        boundaries, indicating movement within the lane. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        line, and the rule for lane dividers suggests keeping between them.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the rule
                        for double white lines where the nearer line is broken suggests you may cross to
                        overtake if safe.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a white arrow pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a turn left.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a turn right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your lane to go straight, but you may change right if it is safe to
                        do so. No specific stopping or turning instructions are visible in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 993, 67.04 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction where
                        the road continues and other lanes diverge. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead in the left lane.;
                        arrow:straight (full): A white arrow pointing straight ahead in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead in the right lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        color and pattern of the boundaries fit their roles: the left boundary is a solid lane
                        line, and the right boundary is a dashed lane line. | markings: The arrows in my lane
                        (straight ahead) agree with the boundaries (lane lines allow lane changes if permitted
                        by the line type). | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): Allowed because the left boundary is a solid white
                        line, and the rule [UK-Rule131] suggests keeping between lane dividers, but the solid
                        line implies a restriction on crossing.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if safe.
Step 6  go_straight     allowed (correct): Allowed because the marking in my lane is an arrow pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The action for change_left is potentially prohibited by the solid line, but the rule
                        cited is only a recommendation, which is a contradiction in application.
Advice                  You should stay in your lane to go straight, but you may change right into the
                        adjacent lane if it is safe. Do not attempt to change left as the solid white line
                        prohibits it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13887, out 1105, 81.91 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a street in a built-up area, and ahead there is an intersection where the road
                        continues and other lanes are visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, next to a
                        pavement/sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line marking the division between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the division between lanes.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is a solid white edge
                        line, and the right boundary is a dashed white lane line, which fits their roles. |
                        markings: The stop line is located across my lane, which is consistent with the lane
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction or
                        the start of a traffic lane. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicular traffic must stop at signals or a
                        'Stop' sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a dashed lane
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): prohibited: The right boundary is a dashed lane
                        line, and [UK-Rule131] suggests keeping between lane dividers, but no specific rule
                        prohibits changing right here.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of two. You may proceed straight or change left, but you
                        should be aware of the stop line ahead, which indicates you must stop if there is a
                        signal or stop sign.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left allowed across a curb']
Tokens                  in 13887, out 1067, 82.18 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane_line, right boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The arrow in my lane (straight ahead) is consistent with the lane markings and
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between lane dividers, which are short, broken white
                        lines used on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between lane dividers, which are short, broken white
                        lines used on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line and the rule for lane dividers suggests keeping between them.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white line and the rule for lane dividers suggests keeping between them.
Step 6  go_straight     allowed (correct): allowed, because the arrow in my lane points straight ahead and
                        nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in the middle lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines. No specific stopping or turning maneuvers are
                        indicated by the markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13887, out 1001, 67.29 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is a pedestrian crossing and a
                        junction area. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A pedestrian crossing marked by white stripes is ahead.;
                        text:speed_limit (full): A speed limit of 20 is visible.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is a solid white lane line, and the right boundary is a dashed white
                        lane line, which fits the role of lane dividers. | markings: The pedestrian crossing
                        and speed limit sign are consistent with the lane markings observed. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:crosswalk: This line indicates a stop line for pedestrians at a level crossing.
                        [[UK-HC_MARKINGS-p1-3]]
Step 5  Rule            text:speed_limit: No specific rule passage was found that dictates the action based on
                        a speed limit sign. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane line, and
                        [UK-Rule131] suggests keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed white lane line,
                        and [UK-Rule131] suggests keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no prohibited
                        action is allowed.
Advice                  You should stay in the left lane unless you need to change right, as the left boundary
                        is a solid line. Be prepared to stop for pedestrians at the crossing ahead, and
                        observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1113, 66.11 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with multiple lanes ahead, and it appears to be approaching a junction
                        or area where lane configuration might change. (lanes 3, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, consistent with a lane line, and the right boundary is
                        dashed white, consistent with a lane line. | markings: The straight arrow in my lane
                        is consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and while no specific rule prohibits changing left from a solid line, the solid line
                        generally restricts lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if it is
                        safe.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a white arrow pointing
                        straight ahead, and [UK-Rule128-2] indicates this direction is permitted.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, noting that the solid left
                        boundary restricts lane changes, while the dashed right boundary permits them.
Advice                  You are in the leftmost lane, which is restricted from changing further left by a
                        solid line. You may change right if safe, and you are permitted to go straight ahead
                        in this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1039, 79.98 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction where
                        the road continues and other lanes diverge. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        the left boundary is a lane_line and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The stop line is consistent with the lane boundaries and does not contradict
                        any other markings. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line, and UK-Rule129 mandates that you MUST NOT cross or straddle a solid white
                        line unless necessary to enter adjoining premises or a side road.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white line, and UK-Rule129 mandates that you MUST NOT cross or straddle a solid white
                        line unless necessary to enter adjoining premises or a side road.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight ahead until you reach the stop line, where you must
                        stop if required by a signal or sign.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1073, 62.21 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues, and there is no immediate intersection or ramp visible. (lanes 3, mine
                        2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        my left.; arrow:straight (full): A white arrow pointing straight ahead is visible in
                        the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane lines on both sides). | roles: The white dashed lines on both sides fit the role
                        of lane_line. | markings: The arrows in my lane (straight) agree with the boundaries
                        (dashed lines allow lane changes if safe, but the arrow dictates straight movement). |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed line, and the arrow
                        in my lane allows straight movement, which is consistent with lane change permissions
                        when safe.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed line, and the arrow
                        in my lane allows straight movement, which is consistent with lane change permissions
                        when safe.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane shows straight ahead, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not_applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not_applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not_applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations, as the dashed boundaries permit lane
                        changes and the straight arrow permits going straight, while the lack of other
                        markings dictates the other actions as not applicable.
Advice                  You are in the middle lane, and all lanes are marked to proceed straight ahead. You
                        may change lanes left or right if it is safe to do so, but you should proceed straight
                        in your current lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13887, out 1247, 80.18 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:e4b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction where the road
                        continues straight and appears to have other lanes or traffic flow. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead.; arrow:straight (full): A white arrow pointing
                        straight ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line, indicating I
                        am in the middle lane of three. | roles: The left boundary is solid white, and the
                        right boundary is dashed white, which fits the roles of lane lines. | markings: The
                        three visible arrows in my lane all point straight ahead, which is consistent with the
                        lane markings. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white line and the rule for solid lines prohibits crossing unless necessary to enter
                        adjoining premises or a side road.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line and the
                        rule for double white lines where the line nearer to you is broken means you may cross
                        the lines to overtake if it is safe.
Step 6  go_straight     allowed (correct): allowed, because the lane markings include a white arrow pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change right if it is safe, but changing
                        left is prohibited by the solid white line. You are permitted to go straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13887, out 1098, 67.95 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with traffic moving in both directions. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries, as it is located within the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane dividers are dashed, and you may
                        proceed straight ahead. You should stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1018, 81.2 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road with multiple lanes ahead, and it appears to be approaching an
                        intersection or a point where traffic flow changes. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, and the right boundary is dashed white, which fits the
                        roles of lane lines. | markings: The straight arrow in my lane is consistent with the
                        lane markings and boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and while no specific rule prohibits changing left from a solid line, the solid line
                        generally restricts lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the line nearer to you is broken if
                        it is safe.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a white arrow pointing
                        straight ahead, and [UK-Rule128-2] indicates this direction is permitted.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane ahead of my lane.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action is
                        decided without the governing feature.
Advice                  You are currently in the left lane, which is marked to proceed straight ahead. You may
                        change right into the adjacent lane if it is safe, but changing left is prohibited by
                        the solid white line. You should proceed straight ahead unless you intend to turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1050, 26.25 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, there is an
                        intersection marked by road markings. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): White dashed lines forming a cross-hatching pattern at the
                        intersection.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The area:grid marking is
                        consistent with the lane boundaries and the intersection ahead. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            area:grid: You must not cause a vehicle to enter the box junction so that the vehicle
                        has to stop within the box junction due to the presence of stationary vehicles. [[UK-
                        TSRGD-11(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed line,
                        and [UK-Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you are allowed to go straight ahead. You
                        should be aware of the box junction ahead, as you must not enter it if it forces you
                        to stop due to stationary vehicles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1039, 83.26 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction where the road
                        continues and other traffic is present. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, adjacent to a
                        pavement.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from an adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead, located in the adjacent lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which is consistent
                        with the roles assigned. | markings: The white arrow in my lane shows straight ahead,
                        and the arrow in the adjacent lane also shows straight ahead, which is consistent with
                        the lane markings. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: This marking indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between lane dividers, which are short, broken white
                        lines used on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the right boundary is a dashed
                        lane_line and the arrow in my lane only permits straight ahead.
Step 6  change_right    allowed (contested, correct): allowed, because the right boundary is a dashed
                        lane_line and the arrow in my lane only permits straight ahead.
Step 6  go_straight     allowed (correct): allowed, because the arrow in my lane shows straight ahead and no
                        other marking prohibits it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your lane to go straight, but you may change right if necessary. No
                        specific stopping or turning instructions are visible for your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 13887, out 1137, 85.13 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction where
                        the road continues and appears to curve slightly to the right. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across my lane from the bottom to the end of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        color and pattern of the boundaries fit their roles: the left boundary is a solid lane
                        line, and the right boundary is a dashed lane line. | markings: The lane markings list
                        is empty, which is consistent with the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a solid white line, and there is no
                        specific rule prohibiting a lane change into the adjacent lane on the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and according
                        to [UK-Rule128], you may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific markings for turning, you should proceed with caution at the
                        junction ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 987, 61.8 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is a circular junction visible further down the
                        road. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries, indicating the end of the current travel area. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed lane_line, and [UK-Rule131]
                        permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [UK-Rule131]
                        permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the dashed lane lines
                        permit lane changes, and the absence of specific markings allows straight travel.
Advice                  You are in the left lane of a two-lane road, and you may change lanes left or right as
                        the dashed lines permit. You may proceed straight ahead, but you must stop before the
                        visible stop line if approaching a controlled junction.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1059, 65.24 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch of road. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible across my lane from the bottom
                        to the end of the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line (indicating a lane to the left), and the right boundary
                        is a lane_line (indicating a lane to the right). | roles: The left boundary is a
                        dashed lane_line, and the right boundary is a solid lane_line, which fits the roles. |
                        markings: There are no arrows, words, or areas in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            no_turn:right: No specific rule passage applies to this marking as it was not seen.
                        [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [UK-Rule131] recommends keeping between lane dividers.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid
                        lane_line and [UK-Rule131] recommends keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or waiting areas in my lane to
                        govern this action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You are in the middle lane, and you may change left if safe, but you must not change
                        right. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 13887, out 1017, 59.95 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area with buildings on the left and trees on the right.
                        Ahead, the road continues into the distance, and there is no immediate intersection or
                        lane end visible. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it is a curb.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a solid white line, and beyond it is the edge of the
                        carriageway/roadside.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the road.; arrow:straight (full): A
                        white arrow pointing straight ahead is painted on the road.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        solid white line on the left fits the role of a lane_line, and the solid white line on
                        the right fits the role of an edge_line. | markings: The text 'BUS LANE' and the
                        straight arrow are consistent with the lane boundaries and each other. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: This marking indicates the edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by or emergency refuge area. [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            text:bus: Bus lanes are shown by road markings and signs that indicate which (if any)
                        other vehicles are permitted to use the bus lane. [[UK-Rule141]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white line, and the rules for solid lines prohibit crossing unless necessary to enter
                        adjoining premises or a side road, which is not indicated.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white line, and the rules for solid lines prohibit crossing unless necessary to enter
                        adjoining premises or a side road, which is not indicated.
Step 6  go_straight     allowed (contested, correct): allowed, because the arrow:straight marking indicates
                        that proceeding straight ahead is required/allowed, and no other marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in this lane as it is marked as a bus lane, and you are directed to
                        proceed straight ahead. Lane changes are prohibited by the solid white lines on both
                        sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:bus'], missed []), actions False, unsafe [], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1194, 81.36 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a typical urban road with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, followed by a
                        pavement/sidewalk area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line marking the division between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A white dashed line marking the division between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is solid white and
                        functions as an edge_line, and the right boundary is dashed white and functions as a
                        lane_line, which is consistent. | markings: The dashed line marking is consistent with
                        the right boundary role (lane_line), although it is listed as a marking, it primarily
                        defines the boundary. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_yield: You must give way to traffic on a major road when approaching a give
                        way marking. [[UK-HC_MARKINGS-p1-4]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a lane_line, and
                        there is no marking prohibiting a lane change to the left.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a lane_line, and
                        there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you must give way to traffic on a
                        major road ahead. You may change lanes left or right, and you may proceed straight,
                        but turning movements are not explicitly governed by markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left allowed across a curb',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13887, out 1069, 60.59 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, the
                        road continues into a built-up area, and there is a pedestrian crossing visible
                        further down the road. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane to the right,
                        and beyond that, there is a pavement/sidewalk.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted on the road.;
                        arrow:right (full): A white arrow pointing right is painted on the road.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        white dashed line on the left fits the role of a lane_line, and the white dashed line
                        on the right fits the role of an edge_line. | markings: The arrows (straight and
                        right) are painted within my lane and are consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The boundary indicates the edge of the carriageway, or the boundary to
                        a shoulder, a bicycle or non-motorized lane, or parking. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:right: Vehicular traffic must turn right. [[UK-TSRGD-Part6,item21]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a lane_line, and
                        [UK-Rule131] suggests keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is an edge_line,
                        and [UK-TSRGD-S11P4-item10] describes the boundary of the carriageway.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane marking 'arrow:straight' is
                        present, and [UK-Rule128-2] indicates the direction of travel.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no marking in my
                        lane that permits a left turn.
Step 6  turn_right      allowed (correct): allowed: The lane marking 'arrow:right' is present, and [UK-TSRGD-
                        Part6,item21] mandates turning right.
Step 6  u_turn          not_applicable: not_applicable: There is no marking in my lane that permits a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or a two-
                          way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, and while you can proceed straight or turn right, changing
                        left is prohibited. You may change right if necessary, but you should use the lane
                        markings to guide your movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left', 'change_left
                        prohibited across a broken lane line', 'change_right allowed across a curb']
Tokens                  in 13887, out 1173, 26.59 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 3, mine 1, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it, there is a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line, and beyond it, there is no
                        visible curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the road.
Step 4  Cross-check     position: The lane count (3) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the three lanes. | roles: The solid white line on the left
                        fits the role of an edge line, and the dashed white line on the right fits the role of
                        a lane line. | markings: The 'BUS LANE' text is present in my lane and does not
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The boundary indicates the edge of the carriageway, which may be the
                        boundary between the main carriageway and a diverging or merging traffic lane at a
                        road junction, or the start of a traffic lane. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: This marking indicates that the lane is a bus lane, and other vehicles may
                        or may not be permitted to use it depending on accompanying signs. [[UK-Rule141]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a lane line, and
                        there is no marking prohibiting a lane change to the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a dashed lane
                        line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no left-turn waiting areas or two-way
                          left-turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so be aware of restrictions on other vehicles using this lane.
                        You may proceed straight, and you may change left, but you are prohibited from
                        changing right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        ['change_left allowed across a curb', 'change_right prohibited across a broken lane
                        line']
Tokens                  in 13887, out 1061, 62.3 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area with shops on both sides, and it appears to be a
                        multi-lane road ahead, possibly leading into a junction or continuing through the
                        town. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the edge of my lane towards the
                        right.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane_lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries, indicating the end of the current travel area. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicular traffic must stop when required by
                        a stop sign or traffic signals. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you may change lanes left or right,
                        or proceed straight ahead. You must stop at the visible stop line if required by a
                        signal or sign.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1049, 62.57 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the boundary of the lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the boundary of the lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the road.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The 'BUS LANE' text is present in
                        the lane and does not contradict the boundaries. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: This marking indicates that the lane is a bus lane, and unless otherwise
                        indicated, you should not drive in it during its period of operation. [[UK-Rule141]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a solid white lane line,
                        and [UK-Rule131] suggests keeping between lane dividers, but no specific rule
                        prohibits changing left.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, and [UK-Rule128]
                        permits crossing double white lines where the nearer line is broken if it is safe.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibited-movement markings in
                        the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: There are no arrows or prohibited-movement markings in the lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: There are no arrows or prohibited-movement markings in the lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: There are no arrows or prohibited-movement markings in the lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane visible
                          ahead of the lane.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed while a rule prohibits it.
Advice                  You are in a bus lane, so you should be aware of its operating times; you may change
                        lanes left or right if safe, and you are permitted to go straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1061, 62.66 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance without an immediate intersection visible. (lanes 2, mine
                        1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A solid white line marking the edge of the road on the
                        far left.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating two
                        lanes in my direction. | roles: The left boundary is solid white, and the right
                        boundary is dashed white, which fits the roles of lane_line. | markings: The only
                        marking observed is a solid white line on the far left, which is interpreted as a
                        stop/yield line, but its placement relative to the lane boundaries is unclear for
                        governing actions. | unseen: No contradictions were found in the observations. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_yield: This marking indicates that you must give way to traffic from the
                        right at a mini-roundabout. [[UK-HC_MARKINGS-p1-5]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        line, and [UK-Rule131] recommends keeping between lane dividers, but no specific rule
                        prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if it is
                        safe.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed while a rule prohibits it.
Advice                  You are in the left lane of a two-lane road. You may change left or right if safe, and
                        you may proceed straight. Be aware of the solid white line on the far left, which may
                        indicate a give way requirement if this is a mini-roundabout.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left', 'go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13887, out 1081, 62.61 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is a speed limit marking visible. (lanes 3,
                        mine 2, full)
Step 2  Left            The left boundary is marked by a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A circular speed limit sign showing 20 mph.; text:speed_limit
                        (full): A circular speed limit sign showing 30 mph.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The white dashed lines fit the role of
                        lane_line. | markings: The speed limit markings are placed across the lane and do not
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:speed_limit: No specific rule passage was found that dictates the action based on
                        the presence of a speed limit marking. [null]
Step 5  Rule            text:speed_limit: No specific rule passage was found that dictates the action based on
                        the presence of a speed limit marking. [null]
Step 6  change_left     allowed (contested, correct): Allowed, as the left boundary is a dashed line and [UK-
                        Rule128] permits crossing if safe.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed line and [UK-Rule128]
                        permits crossing if safe.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the dashed lines permit
                        lane changes and the absence of directional markings allows straight travel.
Advice                  You are in the middle lane, and you may change left or right if it is safe to do so.
                        You may proceed straight ahead, but be mindful of the 20 mph and 30 mph speed limits
                        indicated on the road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 13887, out 1129, 79.44 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a street scene in a built-up area, and ahead there is a continuation of the
                        road with buildings on both sides. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Two white dashed arrows pointing forward in my lane.;
                        arrow:straight (full): Two white dashed arrows pointing forward in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles (a
                        lane line on both sides indicates two lanes in my direction). | roles: The color and
                        pattern of both boundaries (white dashed lines) fit the role of a lane_line. |
                        markings: The arrows in my lane (straight) agree with the boundaries (dashed lines
                        allow lane changes if safe, but the arrows dictate movement). | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a dashed
                        white line, and the arrows indicate straight movement, which does not prohibit lane
                        changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed because the right boundary is a dashed
                        white line, and the arrows indicate straight movement, which does not prohibit lane
                        changes.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane markings show arrows pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: Not_applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: Not_applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you are permitted to go straight or
                        change lanes left or right, provided it is safe. No specific stopping or turning
                        instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1011, 79.06 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides, and the road continues ahead
                        without an immediate intersection visible in the frame. My car is in one of the lanes
                        near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the carriageway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across my lane from the bottom to the end of the lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, and the right boundary is a solid white
                        edge line, which fits their roles. | markings: There are no markings in my lane to
                        check against the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The solid white line indicates the edge of the carriageway, which is a
                        boundary for traffic lanes. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            no_turn:right: No specific rule passage applies to the absence of a marking in this
                        context. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed white lane line, and [UK-
                        Rule131] recommends keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a solid white
                        edge line, and no rule prohibits changing right.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead. Since
                        there are no specific markings for turning, you should proceed with caution regarding
                        the surrounding traffic.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13887, out 1071, 67.04 s
```
