# Reasoning of lane run 20261117_124025_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction ahead. My car is in a lane heading towards a
                        set of traffic lights and a pedestrian crossing. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane dividers. | markings: The straight arrow is consistent with the
                        lane's role and the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right (UK-Rule131)
Step 6  go_straight     allowed (contested, correct): allowed by the straight ahead arrow (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       prohibited: prohibited by the straight ahead arrow (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited: prohibited by the straight ahead arrow (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited: prohibited by the straight ahead arrow (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line', 'symbol:bike']), actions False, unsafe
                        [], citation accepted, contradictions []
Tokens                  in 13891, out 874, 7.54 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane that appears to be part of a multi-lane flow. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which is adjacent to
                        a sidewalk and a brick building.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): A white dashed line extends across the lane ahead, forming a V-shape
                        or hatching to indicate a pedestrian crossing or junction area.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white dashed lines on both sides. | roles: The white dashed lines correctly function
                        as lane dividers and an edge line near a curb. | markings: The grid/hatching ahead is
                        consistent with a pedestrian crossing or junction area. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: I may cross the broken white line to overtake or turn off if it is safe
                        to do so. [UK-Rule127] "A broken white line. This marks the centre of the road. When
                        this line lengthens and the gaps shorten, it means that there is a hazard ahead. Do
                        not cross it un"
Step 5  Rule            right_boundary: I should keep between the broken white lines that divide the lanes.
                        [UK-Rule131] "Lane dividers. These are short, broken white lines which are used on
                        wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            area:grid: These markings separate traffic lanes or protect traffic turning right; I
                        should not enter the area unless necessary and safe. [UK-Rule130] "Areas of white
                        diagonal stripes or chevrons painted on the road. These are to separate traffic lanes
                        or to protect traffic turning right."
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line (UK-Rule127).
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken white line (UK-Rule131)
                        and the lack of a solid line, though a curb is present.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no u-turn arrow is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right if it is safe to
                        do so. Proceed straight through the junction area, being mindful of the pedestrian
                        crossing markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_right allowed across a curb']
Tokens                  in 13891, out 746, 6.06 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching a junction or pedestrianized
                        area. There are several lanes of traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a cycle lane on the right, which is bounded
                        by a curb and a metal railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.; symbol:bike (full): A white bicycle symbol is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the solid white line/curb on my right. | roles: The white dashed
                        line correctly acts as a lane divider, and the solid white line/curb correctly acts as
                        an edge line for the cycle lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose, and the bicycle symbol correctly identifies the
                        adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe to do so. [UK-Rule127] "A broken white line. This marks the centre of the road.
                        When this line lengthens and the gaps shorten, it means that there is a hazard ahead.
                        Do not cross it un"
Step 5  Rule            right_boundary: You should not cross or straddle the line separating the carriageway
                        from the cycle lane. [UK-TSRGD-S11P4-item3] "Diagram 1004.1 Vehicular traffic should
                        not cross or straddle the line unless it is safe to do so and when the line is used to
                        indicate a cycle lane, motor vehi"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): Allowed by the broken white line (UK-Rule127).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line and cycle lane
                        rules (UK-TSRGD-S11P4-item3).
Step 6  go_straight     allowed (correct): Allowed by the straight arrow (UK-TSRGD-Part6,item20).
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no left-turn
                        arrow.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no right-turn
                        arrow.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no u-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. You can change to the left
                        lane if it is safe to do so, but you must not move into the cycle lane on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 834, 7.22 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on the left and residential buildings on the right.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line is on the left, separating my lane from a cycle lane or pavement
                        area.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line is on the right, separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow edge line on the left and a white dashed lane line on the right. | roles: The
                        yellow solid line correctly identifies the left edge of the carriageway, and the white
                        dashed line correctly identifies a lane divider. | markings: No markings are present
                        to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Yellow lines indicate waiting restrictions, but do not prohibit lane
                        movement. [UK-HC_MARKINGS-p2] "Waiting restrictions indicated by yellow lines apply to
                        the carriageway, pavement and verge. You may stop to load or unload (unless there are
                        also loading restr"
Step 5  Rule            right_boundary: A broken white line marks the centre of the road and may be crossed to
                        overtake or change lanes if safe. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can proceed straight ahead or change into the right
                        lane. Changing into the left lane is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 779, 7.34 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a city street approaching a junction with a pedestrian crossing. My
                        car is positioned in a lane that leads directly toward the crossing. (lanes 2, mine 1,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        one-way or restricted lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:yield_line (full): A white dashed line forms a V-shape pointing forward,
                        indicating a lane split or junction approach.; line:crosswalk (full): A pedestrian
                        crossing (zebra crossing) is visible ahead.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        the solid white line on my left and the solid white line on my right. | roles: The
                        solid white lines correctly function as lane dividers. | markings: The V-shaped dashed
                        lines and the crosswalk are consistent with a junction approach. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            line:yield_line: I must give way to traffic on the major road ahead. [UK-
                        HC_MARKINGS-p1-4] "Give way to traffic on major road (can also be used at mini
                        roundabouts)"
Step 6  change_left     prohibited (contested, correct): prohibited by solid white line
Step 6  change_right    prohibited (contested, correct): prohibited by solid white line
Step 6  go_straight     stop_first (contested, label allowed): allowed as no arrow prohibits it, but must give
                        way at the yield line
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane. You must give way to traffic at the junction ahead before
                        proceeding straight. Do not attempt to change lanes as the boundaries are solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13891, out 736, 6.45 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with houses on the left and a sidewalk/trees on the right. The
                        road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A double red line is visible on the left, separating the lane from a
                        sidewalk/pavement.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:merge_left (insufficient): No markings are
                        visible in my lane.; arrow:merge_right (insufficient): No markings are visible in my
                        lane.; arrow:two_way_left (insufficient): No markings are visible in my lane.;
                        no_turn:left (insufficient): No markings are visible in my lane.; no_turn:right
                        (insufficient): No markings are visible in my lane.; text:only (insufficient): No
                        markings are visible in my lane.; text:bus (insufficient): No markings are visible in
                        my lane.; text:hov (insufficient): No markings are visible in my lane.; text:stop
                        (insufficient): No markings are visible in my lane.; text:keep_clear (insufficient):
                        No markings are visible in my lane.; text:speed_limit (insufficient): No markings are
                        visible in my lane.; symbol:hov_diamond (insufficient): No markings are visible in my
                        lane.; symbol:bike (insufficient): No markings are visible in my lane.; symbol:other
                        (insufficient): No markings are visible in my lane.; area:left_turn_waiting
                        (insufficient): No markings are visible in my lane.; area:two_way_left_turn_lane
                        (insufficient): No markings are visible in my lane.; area:grid (insufficient): No
                        markings are visible in my lane.; area:channelizing (insufficient): No markings are
                        visible in my lane.; line:crosswalk (insufficient): No markings are visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the left edge
                        line and right lane line. | roles: The double red line correctly identifies the left
                        edge, and the white dashed line correctly identifies the right lane divider. |
                        markings: No markings were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double red line indicates a prohibition on stopping or parking.
                        [UK-Rule127] "A broken white line. This marks the centre of the road. When this line
                        lengthens and the gaps shorten, it means that there is a hazard ahead. Do not cross it
                        un"
Step 5  Rule            right_boundary: The broken white line indicates a lane divider where I should keep
                        between the lines. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 6  change_left     prohibited (contested, correct): prohibited by the double red line (UK-Rule127)
Step 6  change_right    allowed (correct): allowed by the broken white line (UK-Rule131)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the right lane. Changing into the left
                        lane is prohibited by the red lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'no_turn:left', 'no_turn:right', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions True, unsafe [],
                        citation accepted, contradictions ['go_straight allowed without the stop that the STOP
                        or 停 marking in my lane requires']
Tokens                  in 13891, out 1221, 10.42 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a park-like area with trees on
                        the left. The road continues straight ahead. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which appears to be a
                        cycle lane or a dedicated lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the middle
                        of my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2nd from left) are consistent with the
                        boundaries: a solid line on my left and a dashed line on my right. | roles: The white
                        lines are consistent with standard UK lane dividers. | markings: The straight arrow is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: None |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You may cross the broken white line to overtake if it is safe and you
                        wish to. [UK-Rule127] "A broken white line. This marks the centre of the road. When
                        this line lengthens and the gaps shorten, it means that there is a hazard ahead. Do
                        not cross it un"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    allowed (correct): allowed by the broken white line on the right (UK-Rule127)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. You may change into the
                        lane on your right if it is safe to do so, but you should not cross the solid white
                        line into the lane on your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 876, 8.96 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and parked cars on the right.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a cycle lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left separates me from the cycle lane, and a white line on the right
                        separates me from the parking area. | roles: The solid white lines correctly function
                        as a lane divider on the left and an edge line on the right. | markings: The straight
                        arrow in my lane is consistent with the straight road ahead and the surrounding
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: The line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        (UK-TSRGD-S11P4-item11)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight ahead in your current lane. Do not attempt to change lanes to the
                        left or right as the solid white lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 721, 8.17 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing ahead. My car is in a lane
                        approaching a junction or crossing. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible across the lane before the
                        pedestrian crossing.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers. | markings: The stop line is consistent with the approach to a
                        pedestrian crossing. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            line:stop_line: I must not proceed beyond the line when required to stop. [UK-TSRGD-
                        Part6,item1] "Vehicular traffic must not proceed beyond the line when required to stop
                        by the stop sign"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right (UK-
                        Rule131)
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line (UK-TSRGD-
                        Part6,item1)
Step 6  turn_left       stop_first: stop_first due to the stop line (UK-TSRGD-Part6,item1)
Step 6  turn_right      stop_first: stop_first due to the stop line (UK-TSRGD-Part6,item1)
Step 6  u_turn          stop_first: stop_first due to the stop line (UK-TSRGD-Part6,item1)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before the pedestrian crossing. Do
                        not change lanes as the solid white lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 13891, out 881, 9.18 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a cycle lane on the left. The
                        road continues straight ahead past a junction area. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which contains a cycle
                        symbol.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A bicycle symbol is painted in the lane to my left.;
                        line:stop_yield (insufficient): A white line separates the cycle lane from the main
                        carriageway.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lines
                        on both sides. | roles: The white solid lines correctly function as lane dividers. |
                        markings: The cycle symbol is in the adjacent lane, not my lane. No markings are in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but since this is
                        solid, it indicates a more formal division. [UK-Rule131] "Lane dividers. These are
                        short, broken white lines which are used on wide carriageways to divide them into
                        lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the white lines. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid white lines on both sides prohibit lane
                        changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield', 'symbol:bike'], missed ['text:speed_limit']), actions False,
                        unsafe [], citation in_pack_not_accepted, contradictions ['go_straight allowed without
                        the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13891, out 785, 7.69 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on the left and a park/trees on the right. An
                        intersection or junction is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly function as lane
                        dividers. | markings: The straight arrow is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white line on the left
                        (UK-Rule131)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        (UK-Rule131)
Step 6  go_straight     allowed (correct): allowed by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow (UK-TSRGD-
                        Part6,item20)
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Do not attempt to change lanes
                        or turn left/right as the markings and solid lines prohibit these actions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13891, out 712, 14.18 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and a bus lane or dedicated lane
                        on the right. The road continues straight ahead. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left (which appears to be a
                        cycle lane).
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from a lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the boundaries: a
                        solid line on my left and a dashed line on my right. | roles: The solid white line on
                        the left and dashed white line on the right are consistent with standard UK lane
                        markings. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines, but since this
                        is a solid line, it generally prohibits crossing unless for specific reasons. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You may cross the broken white line to overtake if it is safe and you
                        can complete the manoeuvre. [UK-Rule127] "A broken white line. This marks the centre
                        of the road. When this line lengthens and the gaps shorten, it means that there is a
                        hazard ahead. Do not cross it un"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    allowed (correct): allowed by the broken white line on the right (UK-Rule127)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change into the lane
                        on your right if it is safe to do so, but you should not cross the solid white line
                        into the cycle lane on your left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 734, 7.1 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or intersection ahead. The car is positioned
                        in one of the central lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid red line on the left, with a sidewalk and a low wall beyond it.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line on the right, separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        red edge line on the left and a white dashed lane line on the right. | roles: The red
                        line acts as an edge line and the white dashed line as a lane divider, which is
                        consistent with UK road layouts. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The red line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider,
                        allowing for a lane change if safe. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead in this lane. [UK-TSRGD-
                        Part6,item20] "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid red edge line
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change into the right
                        lane if it is safe to do so, but you must not move to the left across the red line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 695, 6.51 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street with a junction ahead. My car is in a lane that appears to be part of a
                        multi-lane road approaching a complex intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        cycle lane or a restricted area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly function as
                        lane dividers. | markings: The straight arrow is consistent with the lane's path. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right (UK-
                        Rule131)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_left       prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 721, 7.5 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane dividers. | markings: The straight arrow is consistent with the
                        straight road ahead and the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it generally prohibits lane changes unless safe and necessary. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it generally prohibits lane changes unless safe and necessary. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to proceed straight ahead as indicated
                        by the arrow. Lane changes to the left or right are restricted by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13891, out 678, 6.87 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching a junction in a built-up urban area. A pedestrian crossing is
                        directly ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk/building area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another lane or area on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible before the pedestrian crossing.;
                        line:yield_line (full): A white 'Give Way' triangle is painted on the road surface.
Step 4  Cross-check     position: The lane count and position are consistent with the boundaries (edge line on
                        left, lane line on right). | roles: The white solid lines correctly function as edge
                        and lane dividers. | markings: The stop line and yield line are consistent with a
                        junction approach. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            right_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            line:stop_line: Vehicular traffic must not proceed beyond the line when required to
                        stop. [UK-TSRGD-Part6,item1] "Vehicular traffic must not proceed beyond the line when
                        required to stop by the stop sign"
Step 5  Rule            line:yield_line: No vehicle is to cross the transverse line nearer to the major road
                        at the side of which that line is placed, or if that line is not clearly visible,
                        enter that major road, so as to be likely to endanger any person. [UK-TSRGD-3]
                        "Subject to paragraph 4, the requirements conveyed to vehicular traffic on roads by a
                        give way sign are that no vehicle is to cross the transverse line nearer to"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line and yield
                        marking
Step 6  turn_left       stop_first: stop_first due to the stop line and yield marking
Step 6  turn_right      stop_first: stop_first due to the stop line and yield marking
Step 6  u_turn          stop_first: stop_first due to the stop line and yield marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before the junction. You are
                        prohibited from changing lanes due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line', 'line:yield_line'], missed ['line:crosswalk']), actions None,
                        unsafe [], citation in_pack_not_accepted, contradictions ['rightmost lane, but a lane
                        line on the right', 'turn_left, turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 13891, out 781, 7.99 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the left. Ahead, there is a clear
                        stretch of road with a bus in the adjacent lane. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The words 'BUS LANE' are painted in white on the road to the left of
                        my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lines
                        on both sides. | roles: The white solid lines correctly identify the boundaries of my
                        lane. | markings: The 'BUS LANE' text is correctly identified as being in the lane to
                        my left, not in my lane. | unseen: None | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it indicates a more restrictive boundary. [UK-Rule131] "Lane dividers. These are
                        short, broken white lines which are used on wide carriageways to divide them into
                        lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            text:bus: The lane to my left is a bus lane, and I should not enter it unless
                        permitted. [UK-Rule141] "Bus lanes. These are shown by road markings and signs that
                        indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Do not attempt to change lanes to the left into the bus
                        lane or to the right, as both boundaries are marked with solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 13891, out 674, 7.76 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a cycle lane in the middle.
                        The car is in a lane to the right of the cycle lane. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from a cycle lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my
                        right.; line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white line on my left separates me from the cycle lane, and a white line/curb on my
                        right marks the edge. | roles: The white solid lines correctly function as lane
                        dividers and edge lines. | markings: No markings are present in my lane to contradict
                        the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines, but as this is a
                        solid line, it indicates a more permanent division. [UK-Rule131] "Lane dividers. These
                        are short, broken white lines which are used on wide carriageways to divide them into
                        lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the main carriageway. You may proceed straight ahead
                        but are prohibited from changing lanes to the left or right due to the solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 13891, out 699, 7.74 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or intersection ahead. My car is in one of the
                        central lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers. | markings: The straight arrow is consistent with the lane's role
                        and the surrounding lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid white lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 643, 6.98 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a junction or intersection. The road is lined with
                        buildings and trees. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        function as lane dividers. | markings: The straight arrow in my lane is consistent
                        with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe to do so. [UK-Rule127] "A broken white line. This marks the centre of the road.
                        When this line lengthens and the gaps shorten, it means that there is a hazard ahead.
                        Do not cross it un"
Step 5  Rule            right_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe to do so. [UK-Rule127] "A broken white line. This marks the centre of the road.
                        When this line lengthens and the gaps shorten, it means that there is a hazard ahead.
                        Do not cross it un"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): Allowed by the broken white line on the left (UK-Rule127).
Step 6  change_right    allowed (correct): Allowed by the broken white line on the right (UK-Rule127).
Step 6  go_straight     allowed (correct): Allowed by the straight arrow in my lane (UK-TSRGD-Part6,item20).
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no left-turn
                        arrow in my lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no right-turn
                        arrow in my lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no u-turn arrow
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right if it is safe to do so, as the lane dividers are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 725, 8.0 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; arrow:merge_left (full): No markings are visible in my lane.;
                        arrow:merge_right (full): No markings are visible in my lane.; arrow:two_way_left
                        (full): No markings are visible in my lane.; text:only (full): No markings are visible
                        in my lane.; text:bus (full): No markings are visible in my lane.; text:hov (full): No
                        markings are visible in my lane.; text:stop (full): No markings are visible in my
                        lane.; text:keep_clear (full): No markings are visible in my lane.; text:speed_limit
                        (full): No markings are visible in my lane.; symbol:hov_diamond (full): No markings
                        are visible in my lane.; symbol:bike (full): No markings are visible in my lane.;
                        symbol:other (full): No markings are visible in my lane.; area:left_turn_waiting
                        (full): No markings are visible in my lane.; area:two_way_left_turn_lane (full): No
                        markings are visible in my lane.; area:grid (full): No markings are visible in my
                        lane.; area:channelizing (full): No markings are visible in my lane.; line:crosswalk
                        (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers. | markings: No markings were observed in the lane, which is
                        consistent with the lack of specific movement instructions. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line indicates a division of traffic lanes where I
                        should stay in my lane. [UK-TSRGD-S11P4-item4] "Diagram 1005 Division of carriageway
                        into traffic lanes on part of the carriageway where vehicles normally proceed in the
                        same direction other than at places wh"
Step 5  Rule            right_boundary: The solid white line indicates a division of traffic lanes where I
                        should stay in my lane. [UK-TSRGD-S11P4-item4] "Diagram 1005 Division of carriageway
                        into traffic lanes on part of the carriageway where vehicles normally proceed in the
                        same direction other than at places wh"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left or right due to the solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13891, out 1164, 12.2 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus lane on the left and a pedestrian crossing ahead.
                        My car is in the middle lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries
                        (solid line on left, dashed on right). | roles: The solid white line on the left
                        correctly identifies a special lane (bus lane) boundary, and the dashed line on the
                        right is a standard lane divider. | markings: The straight arrow is consistent with
                        the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: I must stay in my lane and not enter the bus lane on the left. [UK-
                        Rule136] "Where a single carriageway has four or more lanes, use only the lanes that
                        signs or markings indicate."
Step 5  Rule            right_boundary: I may cross the broken white line to change lanes if it is safe to do
                        so. [UK-Rule127] "A broken white line. This marks the centre of the road. When this
                        line lengthens and the gaps shorten, it means that there is a hazard ahead. Do not
                        cross it un"
Step 5  Rule            arrow:straight: I must only proceed straight ahead in this lane. [UK-TSRGD-
                        Part6,item20] "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line and bus lane rules
Step 6  change_right    allowed (correct): allowed by the broken white line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow
Step 6  turn_left       prohibited: prohibited by the straight arrow
Step 6  turn_right      prohibited: prohibited by the straight arrow
Step 6  u_turn          prohibited: prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change into the right
                        lane if safe, but you must not move into the bus lane on your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 682, 7.38 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which contains a
                        parked van.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:yield_line (full): A white dashed line and a white solid line form a V-shape or
                        'ghost island' marking ahead of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and a lane line on my right. | roles: The white dashed line on the
                        left and solid line on the right are consistent with lane dividers. | markings: The
                        yield-style markings ahead are consistent with a junction or crossing area. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road; I may cross it to
                        overtake or turn off if the road is clear. [UK-Rule127] "A broken white line. This
                        marks the centre of the road. When this line lengthens and the gaps shorten, it means
                        that there is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: Short, broken white lines are used to divide lanes; I should keep
                        between them, but here the line is solid, which generally prohibits crossing. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            line:yield_line: The marking indicates I must give way to traffic on the major road.
                        [UK-HC_MARKINGS-p1-4] "Give way to traffic on major road (can also be used at mini
                        roundabouts)"
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line on the left
                        (UK-Rule127).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white line on the right (UK-
                        Rule131).
Step 6  go_straight     stop_first (contested, label allowed): Allowed as no markings prohibit it, but I must
                        give way at the yield line.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn marking is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if it is safe to do so.
                        You must give way to traffic ahead before proceeding straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 762, 7.93 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk on the left and a junction or open area ahead.
                        My car is in a lane with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is next to a
                        sidewalk and curb.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly function as lane
                        dividers. | markings: The straight arrow is consistent with the lane's role and the
                        surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I should keep between the white lane lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the white lane lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white line on the right
                        (UK-Rule131)
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking (UK-TSRGD-Part6,item20)
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel only. Do not attempt to change
                        lanes or turn left or right, as the solid white lines and the road marking arrow
                        prohibit these actions.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 899, 8.78 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and shops on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the road surface
                        ahead of my lane, marking the division between lanes.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        dashed line on my left and the solid white line/curb on my right. | roles: The white
                        dashed line on the left correctly identifies a lane divider, and the solid white line
                        on the right correctly identifies the edge of the carriageway. | markings: No specific
                        arrows or words are visible in my lane; the dashed lines are lane dividers. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road; you may cross it to
                        overtake if it is safe to do so. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 6  change_left     allowed (correct): Allowed by the broken white line on the left (UK-Rule127).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line and curb on the
                        right (UK-TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or marking is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or marking is present.
Step 6  u_turn          not_applicable: Not applicable as no u-turn arrow or marking is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if it is safe to do so. You must stay within your
                        lane and not move to the right towards the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 13891, out 736, 7.92 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide pedestrianized area or sidewalk to the right.
                        Ahead, there is a junction or a continuation of the road with multiple lanes. (lanes
                        3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left correctly identifies a lane divider, and the solid white line on the right
                        correctly identifies an edge line. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road; I may cross it to
                        overtake or turn off if the road is clear. [UK-Rule127] "A broken white line. This
                        marks the centre of the road. When this line lengthens and the gaps shorten, it means
                        that there is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): Allowed by the broken white line (UK-Rule127).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line and curb (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow (UK-TSRGD-Part6,item20).
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no u-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change to the left lane
                        if safe. Do not move to the right as it is the edge of the carriageway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 769, 6.69 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates the lanes in the middle
                        of the road.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lines on both sides. | roles: The white solid lines correctly function as a
                        lane divider on the left and an edge line on the right. | markings: No specific arrows
                        or words are visible in my lane; the dashed lines are between lanes, not across mine.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but since this is
                        solid, it generally prohibits lane changes unless safe and necessary. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        you should not change lanes to the left or right as the boundaries are solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 13891, out 661, 14.53 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a cycle lane on the right. The
                        car is in a central lane heading straight. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): A white 'BUS LANE' marking is visible in the lane to my left.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the boundaries (lane line on left, lane line on right). | roles: The solid white line
                        on the left and dashed white line on the right are consistent with standard UK lane
                        divisions. | markings: The 'BUS LANE' text is in the lane to the left, which is
                        consistent with the solid white line separating it from my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line indicates a lane divider where I should keep
                        between the lines. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider,
                        allowing me to cross it to overtake if safe. [UK-Rule127] "A broken white line. This
                        marks the centre of the road. When this line lengthens and the gaps shorten, it means
                        that there is a hazard ahead. Do not cross it un"
Step 5  Rule            text:bus: The lane to my left is a bus lane, which I should not enter unless
                        permitted. [UK-Rule141] "Bus lanes. These are shown by road markings and signs that
                        indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    allowed (correct): allowed by the broken white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead in your current lane. You may change into the lane on
                        your right if it is safe to do so, but you must not change into the bus lane on your
                        left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 13891, out 707, 6.85 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide pedestrian area and parked cars on the left.
                        Ahead, the road continues straight with a clear view of the street layout. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane with parked cars on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a pedestrian area/sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): A white line with a zig-zag pattern is painted in the middle of
                        my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left separates me from a lane, and a white line/curb on the right
                        marks the edge. | roles: The white solid lines correctly function as a lane divider
                        and an edge line. | markings: The zig-zag marking is centered in the lane and does not
                        contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: The line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            symbol:other: The zig-zag markings are used to separate traffic lanes or protect
                        turning areas. [UK-Rule130] "Areas of white diagonal stripes or chevrons painted on
                        the road. These are to separate traffic lanes or to protect traffic turning right."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line and curb on the
                        right (UK-TSRGD-S11P4-item11)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 13891, out 719, 14.94 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a junction or intersection. The road is wide with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from a pedestrian area/sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead and slightly to the
                        left.; arrow:left (full): A white arrow pointing to the left in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line on my right. | roles: The white dashed line on
                        the left correctly identifies a lane divider, and the solid white line with a curb on
                        the right correctly identifies an edge line. | markings: The straight-ahead arrow in
                        my lane is consistent with the lane's purpose, and the left-turn arrow in the adjacent
                        lane is consistent with its role. | unseen: None | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe to do so. [UK-Rule127] "A broken white line. This marks the centre of the road.
                        When this line lengthens and the gaps shorten, it means that there is a hazard ahead.
                        Do not cross it un"
Step 5  Rule            right_boundary: The solid white line and curb mark the edge of the carriageway
                        available for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead in this lane. [UK-TSRGD-
                        Part6,item20] "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): Allowed by the broken white line (UK-Rule127).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white line and curb (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the straight-ahead arrow (UK-TSRGD-
                        Part6,item20).
Step 6  turn_left       prohibited (correct): Not indicated by the arrow in my lane (UK-TSRGD-Part6,item20).
Step 6  turn_right      prohibited (WRONG, label allowed): Not indicated by the arrow in my lane (UK-TSRGD-
                        Part6,item20).
Step 6  u_turn          prohibited: Not indicated by the arrow in my lane (UK-TSRGD-Part6,item20).
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change to the left lane
                        if safe. You are prohibited from turning left or right from this lane and must not
                        move onto the pavement to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:right']), actions False, unsafe
                        ['go_straight'], citation in_pack_not_accepted, contradictions ['turn_left prohibited
                        although an arrow shows it']
Tokens                  in 13891, out 862, 8.56 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus lane on the left and parking/traffic lanes on the
                        right. The car is positioned in a lane with a bus lane to its left. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or another lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Large white text 'BUS LANE' is painted in the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lines
                        on both sides. | roles: The white solid lines correctly act as lane dividers. |
                        markings: The 'BUS LANE' text is in the lane to the left, which is consistent with the
                        lane divider. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [UK-Rule141-2] "Unless otherwise indicated, you should not drive
                        in a bus lane during its period of operation."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line and the bus lane
                        designation
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not move into the lane on the left
                        as it is a designated bus lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 13891, out 666, 6.52 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is in the middle of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The solid white lines correctly
                        function as lane dividers. | markings: The dashed line in the center of the lane is
                        not a stop or yield line but a lane divider for the lane to the right; however, it is
                        within my lane's boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is solid,
                        it implies a stricter separation. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines, but as this is solid,
                        it implies a stricter separation. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            line:stop_yield: No specific rule provided for a dashed line in the middle of a lane,
                        but it typically indicates a lane division.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 13891, out 683, 7.31 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a wide pedestrian area on the left and parked cars on
                        the right. The road ahead appears to be a straight continuation of the current street.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which has a 'BUS'
                        marking.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to the right where cars are parked.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in the lane to my left.; arrow:straight
                        (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both the left and right. | roles: The solid white lines
                        correctly function as lane dividers between lanes of the same direction. | markings:
                        The 'BUS' marking is in the adjacent lane, and the straight arrow is in my lane, which
                        is consistent. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it generally prohibits lane changes unless safe. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the lines, and the solid line prohibits a lane
                        change to the right. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            text:bus: The lane to my left is a bus lane and should not be entered by my car. [UK-
                        Rule141] "Bus lanes. These are shown by road markings and signs that indicate which
                        (if any) other vehicles are permitted to use the bus lane."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead in this lane. [UK-TSRGD-
                        Part6,item20] "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line and the bus lane
                        marking
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You should proceed straight ahead as indicated by the
                        arrow. Do not move into the lane on your left as it is marked for buses only.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'text:bus'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 13891, out 778, 8.73 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A wide urban street with multiple lanes of traffic moving in the same direction. There
                        is a clear lane ahead of the car, with a pedestrianized or parking area to the left
                        and a parking area to the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on my left indicates another lane of my direction, and a white line on my right
                        indicates the edge of the carriageway. | roles: The white solid lines correctly fit
                        the roles of lane divider and edge line. | markings: No markings are present in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 764, 8.14 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A '20' speed limit circle is painted in the center of my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers. | markings: The '20' speed limit marking is centered in my lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it indicates a firmer division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines, but as this is a solid
                        line, it indicates a firmer division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            text:speed_limit: You should follow the road markings and get into the lane as
                        directed. [UK-Rule134] "You should follow the signs and road markings and get into the
                        lane as directed."
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        you should not change lanes to the left or right as the solid white lines prohibit it.
                        Observe the 20 mph speed limit indicated on the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 688, 7.61 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line with a slight curve/zigzag pattern
                        is visible in the middle of the road, but no specific arrows or words are in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white dashed lines correctly
                        function as lane dividers. | markings: No specific arrows or words are clearly visible
                        in my lane; the zigzag/curved lines are part of the lane structure. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road; I may cross it to
                        overtake or turn off if it is safe to do so. [UK-Rule127] "A broken white line. This
                        marks the centre of the road. When this line lengthens and the gaps shorten, it means
                        that there is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: A broken white line marks the centre of the road; I may cross it to
                        overtake or turn off if it is safe to do so. [UK-Rule127] "A broken white line. This
                        marks the centre of the road. When this line lengthens and the gaps shorten, it means
                        that there is a hazard ahead. Do not cross it un"
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line on the left
                        (UK-Rule127).
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken white line on the right
                        (UK-Rule127).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no u-turn arrow is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right if it is safe to
                        do so. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 13891, out 700, 7.9 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on the right. A red double-decker bus
                        is in the lane to the left, and a silver van is in the lane to the right. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane with the bus.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane with the van, and a curb is further
                        to the right.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        function as lane dividers. | markings: The straight arrow is consistent with the
                        lane's position and the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left (UK-
                        Rule131)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right (UK-
                        Rule131)
Step 6  go_straight     allowed (contested, correct): allowed by the straight ahead arrow (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 854, 8.22 s
```
