# Reasoning of lane run 20261118_001346_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is an intersection where traffic appears to be controlled by signals or markings.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2: A bicycle symbol is painted in the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating the middle lane of three lanes in this direction). | roles: the
                        color (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: the bicycle symbol is located within the lane and does not contradict the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            symbol:bike: This marking indicates the boundary of a mandatory cycle lane or a
                        division of a route into that part reserved for pedal cycles or pedestrians. [[UK-
                        TSRGD-Part6,item7]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and there is no
                        marking prohibiting a lane change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        and there is no marking prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes, which contains a bicycle symbol. You may
                        change lanes left or right, and you may proceed straight ahead. You should be aware of
                        the bicycle symbol indicating a cycle lane area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 14750, out 877, 7.54 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road leading towards a junction ahead. There are multiple lanes visible in
                        my direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to be a white dashed line continuing into the junction area. Photo 2 shows a white
                        dashed line next to my car, and further ahead, the line appears to be a white dashed
                        line continuing into the junction area.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to be a white dashed line continuing into the junction area. Photo 2 shows a white
                        dashed line next to my car, and further ahead, the line appears to be a white dashed
                        line continuing into the junction area.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white dashed lines forming a cross-hatching pattern
                        across the road ahead, indicating a junction area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles, as both boundaries are lane_lines, indicating my
                        lane is between two other lanes in the same direction. | roles: The white dashed lines
                        fit the role of lane_line. | markings: The area:grid marking is consistent with the
                        road layout shown in both photos. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            area:grid: A yellow criss-cross marking conveys the prohibition that a person must not
                        cause a vehicle to enter the box junction so that the vehicle has to stop within the
                        box junction due to the presence of stationary vehicles. [[UK-TSRGD-11(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left_boundary is a white
                        dashed line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right_boundary is a white
                        dashed line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right as the lane markings are
                        dashed. You may proceed straight ahead, but be aware of the grid marking ahead, which
                        prohibits stopping within the junction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14750, out 1175, 9.35 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, leading towards a junction or
                        intersection area. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to my car. Photo 2: A dashed white line
                        is visible next to my car. Further ahead, the line appears to be a dashed white line.
                        Photo 2 shows the line further ahead is also dashed white.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Photo 2: A solid white line is
                        visible next to my car. Further ahead, the line appears to be a solid white line.
                        Photo 2 shows the line further ahead is also solid white.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2: A bicycle symbol is painted in my lane, centered ahead.
                        Photo 2: Two white arrows pointing up and to the right are painted in my lane, ahead
                        of the bicycle symbol.; arrow:merge_right (full): Photo 2: Two white arrows pointing
                        up and to the right are painted in my lane, ahead of the bicycle symbol.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane index
                        is 2 (counting from the left). The left boundary is a lane line, indicating a lane to
                        the left. The right boundary is a lane line, indicating a lane to the right. This is
                        consistent. | roles: The left boundary is a dashed white lane line, and the right
                        boundary is a solid white lane line. This fits the role of lane_line. | markings: The
                        bicycle symbol is in my lane. The arrows indicate a merge right. These markings are
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            symbol:bike: This marking indicates the boundary of a mandatory cycle lane or a
                        division of a route into that part reserved for pedal cycles. [[UK-TSRGD-Part6,item7]]
Step 5  Rule            arrow:merge_right: This marking indicates the direction of possible traffic movements
                        at the end of an off side with-flow bus lane or other designated lane, or where there
                        is an intermediate discontinuation of the lane on the approach to a junction. [[UK-
                        TSRGD-Part6,item13]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed white
                        lane line, and while this line allows lane changes, the presence of the bicycle symbol
                        in my lane suggests this lane is designated for cycling/shared use, which may restrict
                        movement based on general guidance.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white lane line, and the
                        presence of the merge_right arrow indicates the intended movement is to the right.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: The arrow:merge_right marking indicates
                        that traffic must merge right, prohibiting straight travel.
Step 6  turn_left       prohibited (correct): prohibited: The arrow:merge_right marking indicates that traffic
                        must merge right, prohibiting left turns.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow:merge_right marking indicates
                        the direction of possible traffic movements at the end of an off side with-flow bus
                        lane or other designated lane, or where there is an intermediate discontinuation of
                        the lane on the approach to a junction, which allows movement to the right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow:merge_right marking indicates that traffic
                        must merge right, prohibiting U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: No markings for a waiting area were observed in my
                          lane or to its left.
Step 7  Reflect         consistent
Advice                  You must prepare to merge right into the adjacent lane, as indicated by the arrows. Do
                        not attempt to change left, go straight, or make a U-turn in this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['turn_right'], citation accepted, contradictions ['change_left prohibited
                        across a broken lane line', 'go_straight, turn_left, turn_right, u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 14750, out 1171, 9.6 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with buildings on the left and residential houses on the right. Ahead,
                        the road continues straight, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A double yellow line is visible further ahead. Photo 2: A double yellow line
                        is visible further ahead.
                        yellow double_solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 2: A solid yellow line is visible immediately ahead of
                        the car, separating the lanes.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line/center_line equivalent for the right side of the road). | roles: the color
                        and pattern of each boundary fit the role given to it. | markings: the markings (solid
                        yellow line) agree with the boundaries (right boundary is double yellow). | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: Double yellow lines mean no waiting at any time, unless there are
                        signs that specifically indicate seasonal restrictions. [[UK-HC_MARKINGS-p2-2]]
Step 5  Rule            line:stop_yield: You must give way to traffic from the right at a mini-roundabout
                        (though this marking is used here as a stop/yield indication). [[UK-HC_MARKINGS-p1-5]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        line, which prohibits lane changes unless necessary to enter adjoining premises or a
                        side road, but the rule for a solid line is not explicitly cited for prohibiting a
                        change here, and the line is a lane_line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a double yellow
                        line, and [UK-HC_MARKINGS-p2-2] mandates no waiting at any time, which implies
                        restrictions on movement into that area.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You should remain in the left lane to proceed straight ahead. Do not attempt to change
                        lanes to the right, as the double yellow line prohibits waiting there. You must give
                        way to traffic from the right before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 14750, out 947, 7.62 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a paved urban road with buildings on both sides. Ahead, there is a pedestrian
                        crossing area and what appears to be a junction or crossing point. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car, and further ahead, the line
                        continues as a white dashed line. Photo 2: The line next to the car is a white dashed
                        line, and the line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car, and further ahead, the line
                        continues as a white dashed line. Photo 2: The line next to the car is a white dashed
                        line, and the line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2: A white dashed line marking is visible across the
                        lane, indicating a pedestrian crossing area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in this direction) | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line | markings: the crosswalk marking is consistent
                        with the lane boundaries and does not contradict them | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:crosswalk: This line indicates a stop line for pedestrians at a level crossing.
                        [[UK-HC_MARKINGS-p1-3]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a dashed white
                        lane_line, and there is no marking allowing a lane change.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a dashed white
                        lane_line, and there is no marking allowing a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Be aware of the
                        pedestrian crossing area ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left', 'change_left prohibited across a broken
                        lane line', 'change_right prohibited across a broken lane line']
Tokens                  in 14750, out 902, 7.35 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction or intersection where
                        the road continues and other lanes are present. There are three lanes visible in my
                        direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and further ahead, it is also a
                        dashed white line. Photo 2 shows a dashed white line next to my car, and further
                        ahead, it is also a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it is also a solid
                        white line. Photo 2 shows a solid white line next to my car, and further ahead, it is
                        also a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a solid white line marking the right boundary,
                        and further ahead, there are no arrows or words visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles: the left boundary is a lane line (separating from
                        lane 1), and the right boundary is a lane line (separating from lane 3). | roles: The
                        left boundary is a dashed white line, consistent with a lane_line. The right boundary
                        is a solid white line, consistent with a lane_line. | markings: The stop line is
                        visible in Photo 2, and it is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicular traffic must stop at signals or a
                        'Stop' sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, and
                        [UK-Rule131] recommends keeping between lane dividers, which allows for a lane change
                        if safe.
Step 6  change_right    allowed (correct): The right boundary is a solid white line, and [UK-Rule131]
                        recommends keeping between lane dividers, but the solid line suggests a restriction,
                        though no specific prohibition is given for changing onto the next lane.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibited-movement markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so it is not applicable.
Step 6  turn_right      not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so it is not applicable.
Step 6  u_turn          not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so it is not applicable.
Step 6  enter_waiting_areanot_applicable: There is no marked waiting area or two-way left-turn lane present,
                          so it is not applicable.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a rule from step 5.
Advice                  You are in the middle lane, and you may proceed straight or change lanes left or right
                        if safe. You must stop at the solid white line ahead if there is a stop sign or
                        signal.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14750, out 1227, 9.59 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with traffic lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows a broken white line continuing, and
                        Photo 2 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane line, indicating
                        a lane to the left, and the right boundary is a lane line, indicating a lane to the
                        right. This is consistent. | roles: The left boundary is a solid white lane line, and
                        the right boundary is a dashed white lane line. This fits the role of lane_line. |
                        markings: The white arrow in my lane indicates a permitted movement, and this is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane line, and
                        [UK-Rule131] suggests keeping between lane dividers.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, and [UK-Rule131]
                        suggests keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): The lane marking shows a white arrow pointing straight
                        ahead, and [UK-Rule128-2] indicates this direction is permitted.
Step 6  turn_left       prohibited: The lane marking does not show an arrow for turning left, and since there
                        is no specific prohibition, it is not explicitly prohibited by the arrow, but the
                        arrow only permits straight ahead.
Step 6  turn_right      prohibited: The lane marking does not show an arrow for turning right, and since there
                        is no specific prohibition, it is not explicitly prohibited by the arrow, but the
                        arrow only permits straight ahead.
Step 6  u_turn          prohibited: The lane marking does not show an arrow for U-turning, and since there is
                        no specific prohibition, it is not explicitly prohibited by the arrow, but the arrow
                        only permits straight ahead.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a waiting area in my lane, so this
                          action is not applicable.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a rule from step 5.
Advice                  You should stay in the middle lane for straight travel, as indicated by the arrow. You
                        may change right if necessary, but turning left, turning right, or U-turning is
                        prohibited by the lane arrow.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14750, out 1189, 9.38 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is a visible '20' speed limit marking on the
                        road surface. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car. Further ahead, the dashed white line continues. Further
                        ahead, there is a solid white line marking the boundary of the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car. Further ahead, the dashed white line continues. Further
                        ahead, there is a solid white line marking the boundary of the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible on the road surface
                        ahead of the car.; line:stop_line (partial): Photo 2: A white dashed line is visible
                        on the road surface ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of both boundaries (white dashed) fit the
                        role of lane_line. | markings: the two instances of line:stop_line are consistent with
                        the road markings visible in Photo 2. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white line, which
                        permits crossing if safe, as per [UK-Rule128].
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white line, which
                        permits crossing if safe, as per [UK-Rule128].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane indicating a
                        permitted U-turn or prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or a two-way left-turn lane ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right if it is safe to do so.
                        You may proceed straight ahead, but you must stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14750, out 977, 8.31 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a pedestrian
                        crossing and what appears to be an intersection or junction area. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to the car, and Photo 2 shows a solid white line
                        next to the car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to the car, and Photo 2 shows a dashed white
                        line next to the car. Further ahead, Photo 1 shows a dashed white line continuing, and
                        Photo 2 shows a dashed white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the edge of the lane,
                        and Photo 2 shows a white dashed line marking the edge of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the line:stop_line marking is consistent with the boundaries and the
                        general road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicles must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white line on the left
                        boundary and [UK-Rule131].
Step 6  change_right    allowed (contested, label prohibited): allowed as the right boundary is a dashed white
                        line and [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows or prohibited-movement
                        markings in the lane and boundaries do not restrict it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane, and while you can change right, you must stay in your lane
                        to go straight. You must stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1101, 7.69 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction/crossing area. There
                        are two lanes visible in my direction near the bottom of the photo. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1: A dashed white line is visible next to my car. Further ahead, the dashed
                        white line continues. Photo 2: A dashed white line is visible next to my car. Further
                        ahead, the dashed white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible next to my car. Further ahead, the dashed
                        white line continues. Photo 2: A dashed white line is visible next to my car. Further
                        ahead, the dashed white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1: A dashed white line with a bicycle symbol is visible on
                        the left side of the road ahead. Photo 2: A dashed white line with a bicycle symbol is
                        visible on the left side of the road ahead.; symbol:bike (full): Photo 1: A dashed
                        white line with a bicycle symbol is visible on the left side of the road ahead. Photo
                        2: A dashed white line with a bicycle symbol is visible on the left side of the road
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction) | roles: the color and pattern of
                        both boundaries fit the role of a lane_line | markings: the bicycle symbols are
                        consistent with the lane markings and do not contradict the boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            symbol:bike: This marking indicates the boundary of a mandatory cycle lane or division
                        of a route into that part reserved for pedal cycles or pedestrians. [[UK-TSRGD-
                        Part6,item7]]
Step 5  Rule            symbol:bike: This marking indicates a cycle lane, track, route, or a way that would be
                        a cycle track but for it being accessible, under a temporary statutory provision, by
                        electric scooters being used in a trial. [[UK-TSRGD-S11P4-item28]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, which is marked as a cycle lane area on
                        the left. You may change lanes left or right, and you may proceed straight ahead. Be
                        aware of the bicycle markings on the left side of the road.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1093, 7.51 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining the left side. Ahead, the road
                        continues into the distance, and there is a white arrow indicating a straight
                        movement. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Photo 2: A
                        solid white line is visible immediately to the left of my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken white line is visible to the right of my car. Photo 2: A broken
                        white line is visible to the right of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is painted in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The solid white line on the left and the dashed white line on the right both
                        fit the role of a lane_line. | markings: The straight arrow in my lane is consistent
                        with the lane boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a solid white
                        line, and while no specific rule prohibits changing left, the solid line generally
                        restricts lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the line nearer to you is broken if
                        it is safe.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a white arrow pointing straight
                        ahead, and [UK-Rule128-2] indicates this direction is permitted.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The lane marking only shows an arrow
                        for straight ahead, and an arrow that does not show a turn prohibits that movement.
Step 6  turn_right      prohibited (correct): prohibited: The lane marking only shows an arrow for straight
                        ahead, and an arrow that does not show a turn prohibits that movement.
Step 6  u_turn          prohibited (correct): prohibited: The lane marking only shows an arrow for straight
                        ahead, and an arrow that does not show a U-turn prohibits that movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is restricted to straight movement. You may change
                        right if safe, but you must not change left. You are permitted to go straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1112, 13.16 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction or intersection where
                        the road continues straight and curves slightly to the right. My car is in the lane
                        closest to the left side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to my car, and further ahead, this
                        solid white line continues. Photo 2 shows a solid white line immediately next to my
                        car, and further ahead, this solid white line continues.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line further ahead, and near my car, there is no painted
                        line visible immediately to the right. Photo 2 shows a broken white line further
                        ahead, and near my car, there is no painted line visible immediately to the right.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line on the left, dashed white line on the right). | markings: the arrow
                        in my lane agrees with the boundaries (it indicates movement within the lane defined
                        by the boundaries). | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white line on the left
                        boundary, as this line indicates the boundary of the lane.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white line, which
                        permits crossing if safe.
Step 6  go_straight     allowed (contested, correct): allowed because the lane marking shows an arrow pointing
                        straight ahead, and no other marking prohibits it.
Step 6  turn_left       prohibited: prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  turn_right      prohibited: prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  u_turn          prohibited: prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must stay in your lane or change right if necessary, as the solid white line on
                        the left prohibits changing left. You are permitted to go straight or change right,
                        but turning left, right, or making a U-turn is prohibited by the lane arrow.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1073, 9.48 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic lanes are marked for specific movements. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, this line transitions into a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, this line transitions into a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:left (full): Photo 2; arrow:right (full): Photo
                        2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles, as there are lane lines on both the left and right,
                        indicating my lane is in the middle. | roles: The white dashed lines on both sides fit
                        the role of lane_line. | markings: The arrows in Photo 2 are consistent with the lane
                        boundaries, showing allowed movements within the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            arrow:straight: The white direction arrow indicates that you need to get back onto
                        your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:left: Vehicular traffic must turn left. [[UK-TSRGD-Part6,item19]]
Step 5  Rule            arrow:right: Vehicular traffic must turn right. [[UK-TSRGD-Part6,item21]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed line, and the
                        arrow for turning left is present, which allows the change.
Step 6  change_right    allowed (correct): The right boundary is a dashed line, and the arrow for turning
                        right is present, which allows the change.
Step 6  go_straight     allowed (correct): The lane marking includes an arrow for straight movement, which is
                        allowed by the rule for direction arrows.
Step 6  turn_left       allowed (correct): The lane marking includes an arrow for turning left, which is
                        mandatory for that movement.
Step 6  turn_right      allowed (WRONG, label prohibited): The lane marking includes an arrow for turning
                        right, which is mandatory for that movement.
Step 6  u_turn          prohibited (correct): No marking governs this action, and since the lane has arrows,
                        it is prohibited unless an arrow shows a turn toward the opposite traffic.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The boundaries and markings were settled in the close-up check, no action is allowed
                        although a rule prohibits it, no action was decided without a feature that decides it,
                        each reason leads to its action, and the decision is consistent.
Advice                  You are in the middle lane, which allows you to go straight, turn left, or turn right.
                        You may change lanes to the left or right as the lane markings permit.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['arrow:straight_left']),
                        actions False, unsafe ['turn_right'], citation accepted, contradictions []
Tokens                  in 14750, out 1190, 9.77 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a street scene in a built-up area, and ahead there is an intersection where
                        the road appears to continue or change direction. My car is in the lane closest to the
                        left side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to the car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line immediately next to the car, and further ahead, this
                        line continues as a dashed white line. Photo 2 shows a dashed white line immediately
                        next to the car, and further ahead, this line continues as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the edge of the
                        lane, which is the right boundary.; line:stop_line (partial): Photo 2 shows a white
                        dashed line marking the edge of the lane, which is the right boundary.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is edge_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (line:stop_line) are consistent with the boundaries (right
                        boundary is a lane_line) | unseen: no | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction or
                        the start of a traffic lane. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where a vehicle must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is an
                        edge_line and no rule prohibits changing into the adjacent area.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a
                        lane_line and no rule prohibits changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that permit turning left.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that permit turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that permit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You should be
                        aware of the stop line ahead, which indicates where you must stop if required by a
                        signal or sign.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14750, out 964, 8.96 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection visible in the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, and further ahead, it is also a
                        white dashed line. Photo 2 shows a white dashed line next to the car, and further
                        ahead, it is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, and further ahead, it is also a
                        white dashed line. Photo 2 shows a white dashed line next to the car, and further
                        ahead, it is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the lane
                        next to the car. Photo 2 also shows a white arrow pointing straight ahead in the lane
                        to the right of the car.; arrow:straight (full): Photo 2 shows a white arrow pointing
                        straight ahead in the lane to the left of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (dashed lines indicate lane division between lanes
                        of the same direction). | roles: the dashed white lines fit the role of lane_line. |
                        markings: the arrows in the lane agree with the boundaries (they indicate movement
                        within the lane structure). | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a dashed white line,
                        but the lane marking (arrow:straight) in my lane does not permit a change left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the lane
                        marking (arrow:straight) in my lane permits movement within the lane structure.
Step 6  go_straight     allowed (correct): allowed: The lane marking (arrow:straight) in my lane permits
                        proceeding straight ahead.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The lane marking (arrow:straight) in my
                        lane does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane marking (arrow:straight) in my lane does
                        not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane marking (arrow:straight) in my lane does
                        not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should remain in the middle lane to proceed straight ahead, as indicated by the
                        lane markings. While the lane markings permit staying in the lane, the dashed lines
                        allow for lane changes if necessary, but the current markings restrict turning
                        movements.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 14750, out 982, 8.64 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a wet urban road, and ahead there is a pedestrian crossing and a junction
                        area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, the
                        solid white line continues. Photo 2 shows a solid white line immediately next to the
                        car, and further ahead, the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line immediately next to the car, and further ahead, the
                        dashed white line continues. Photo 2 shows a dashed white line immediately next to the
                        car, and further ahead, the dashed white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white dashed line marking the pedestrian
                        crossing area ahead.; line:yield_line (full): Photo 1 shows white dashed lines
                        indicating the stop/give way area ahead of the junction.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line, indicating two lanes in the direction of travel) | roles: the color and
                        pattern of each boundary fit the role given to it | markings: the line:crosswalk and
                        line:yield_line are consistent with the boundaries and each other | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:crosswalk: This line indicates the stopping point for pedestrians at a level
                        crossing. [[UK-HC_MARKINGS-p1-3]]
Step 5  Rule            line:yield_line: Vehicular traffic must give way in accordance with the requirements
                        in paragraph 7 of Part 7 when approaching a junction indicated by this marking. [[UK-
                        TSRGD-Part6,item3]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and while no explicit rule prohibits a lane change, the solid line generally restricts
                        it, and the lane markings do not permit it.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which permits crossing if safe, as per [UK-Rule128].
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the lane
                        that restrict proceeding straight ahead.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in the lane that
                        govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in the lane that
                        govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in the lane that
                        govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is bordered by a solid white line, restricting lane
                        changes to the left. You may change right if it is safe, as the right boundary is
                        dashed. You must give way to pedestrians at the crossing and at the junction ahead,
                        and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1005, 9.17 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with multiple lanes ahead, and it appears to be approaching a junction
                        or area where lane usage is defined. There are at least three lanes visible in my
                        direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and further ahead, this line
                        continues as a dashed white line. Photo 2 shows a dashed white line next to my car,
                        and further ahead, this line continues as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, this line
                        continues as a solid white line. Photo 2 shows a solid white line next to my car, and
                        further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows the text 'BUS LANE' painted on the road in my lane.
                        Photo 2 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the text 'BUS LANE' in my lane is consistent with the boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [[UK-Rule141]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        white line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed because the right boundary is a solid white line, and [UK-
                        Rule131] permits keeping between lane dividers (though the solid line suggests
                        caution).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane, and no specific rule prohibits it.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you should only drive in this lane if permitted by signage.
                        You may change lanes left or right, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14750, out 917, 8.17 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance with traffic moving in both directions. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the bus. Photo 2: A solid white line is
                        visible next to the bus.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible ahead, separating
                        the lanes.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (a dashed line ahead) agree with the boundaries (lane lines) |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and while no specific rule prohibits changing left, the solid line generally restricts
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which permits
                        crossing if safe, as per [UK-Rule128].
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You may change right if it is safe, and you may proceed straight ahead. You should
                        keep within the lane boundaries, especially noting the solid line on your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 855, 6.91 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is a junction or intersection where traffic flow is managed by lane markings. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: The white dashed line on the left and the white solid line on the
                        right fit the role of lane_line. | markings: The white arrow pointing straight ahead
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a lane_line, and
                        the arrow in the lane does not permit a change left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a lane_line, and
                        the arrow in the lane does not permit a change right.
Step 6  go_straight     allowed (correct): allowed: The arrow in the lane permits proceeding ahead, and no
                        boundary prohibits it.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in the lane does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The arrow in the lane does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in the lane does not show a U-turn, and no
                        exception applies for turning toward opposite traffic.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of this lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the observed markings and rules.
Advice                  You must stay in your current lane to proceed straight ahead, as indicated by the lane
                        arrow. Lane changes and turns are prohibited by the lane markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 14750, out 862, 7.45 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is an intersection where traffic
                        appears to be moving through or approaching a junction. My car is in the lane closest
                        to the center of the road, based on the lane markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_left (full): Photo 2 shows a white arrow pointing left, in the lane to my
                        left. Photo 2 shows a white arrow pointing straight ahead, in my lane. Photo 2 shows a
                        white arrow pointing right, in the lane to my right.; arrow:straight (full): Photo 2
                        shows a white arrow pointing straight ahead, in my lane.; arrow:merge_right (full):
                        Photo 2 shows a white arrow pointing right, in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line. | markings: the arrows in Photo 2 are consistent
                        with the lane structure: the left arrow is in the left lane, the straight arrow is in
                        the middle lane, and the right arrow is in the right lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:merge_left: White direction arrows on the road indicate that you need to get
                        back onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:merge_right: White direction arrows on the road indicate that you need to get
                        back onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed lane_line, and the arrow in the
                        left lane indicates a merge_left, which is allowed by [UK-Rule128-2].
Step 6  change_right    allowed (correct): The right boundary is a white dashed lane_line, and the arrow in
                        the right lane indicates a merge_right, which is allowed by [UK-Rule128-2].
Step 6  go_straight     allowed (correct): The arrow in my lane indicates straight movement, which is allowed
                        by [UK-Rule128-2].
Step 6  turn_left       allowed (WRONG, label prohibited): The arrow in the left lane indicates a merge_left,
                        which implies a left turn is possible, and this is allowed by [UK-Rule128-2].
Step 6  turn_right      allowed (WRONG, label prohibited): The arrow in the right lane indicates a
                        merge_right, which implies a right turn is possible, and this is allowed by [UK-
                        Rule128-2].
Step 6  u_turn          allowed (WRONG, label prohibited): No specific marking governs a U-turn, but the lane
                        markings suggest general movement is allowed, and no prohibition is visible.
Step 6  enter_waiting_areanot_applicable: No marking governs entering a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight. You may change left or right
                        to utilize the adjacent lanes for turning or merging, and you may turn left or right
                        at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_left', 'arrow:merge_right'], missed ['line:stop_line']), actions False,
                        unsafe ['turn_left', 'turn_right', 'u_turn'], citation accepted, contradictions
                        ['turn_left allowed although no arrow shows it', 'turn_right allowed although no arrow
                        shows it']
Tokens                  in 14750, out 1189, 9.01 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection or ramp. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line, indicating my lane is the leftmost of the three lanes). | roles: the color
                        and pattern of both boundaries (white dashed) fit the role of a lane_line. | markings:
                        there are no markings in my lane to check against boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and there is no rule prohibiting a lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and there is no
                        rule prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of three. You may change left or right, and you may
                        proceed straight ahead. No specific lane is required for turning movements as there
                        are no markings governing them.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 14750, out 810, 6.93 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street in a built-up area, and ahead there is a continuation of the road
                        with traffic moving in both directions. My car is in the lane closest to the left side
                        of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to my car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to my car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line immediately next to my car, and further ahead, this
                        line continues as a broken white line. Photo 2 shows a broken white line immediately
                        next to my car, and further ahead, this line continues as a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is an edge line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: no markings were reported, so they agree with each other and with the
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates a stop line at signals or police control. [[UK-
                        HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white edge
                        line, and there are no markings allowing a lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white lane line, and there
                        are no markings prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You may change right if safe, and you may proceed straight ahead. You should keep
                        within your lane, as the left boundary is a solid edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14750, out 918, 7.41 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is a junction or intersection visible in the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the edge of the
                        lane near my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction) | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line | markings: the line:stop_line in Photo 2 is
                        consistent with the lane markings observed | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited because the left boundary is a dashed
                        white line, and there is no indication allowing a lane change in the visible stretch.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a dashed
                        white line, and there is no indication allowing a lane change in the visible stretch.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. No lane changes or
                        turns are explicitly permitted or prohibited by the visible markings, other than the
                        stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_left prohibited across a broken lane line', 'change_right prohibited across a
                        broken lane line']
Tokens                  in 14750, out 875, 7.63 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban street with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or lane end
                        visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car, continuing
                        ahead. Photo 2: A solid white line is visible immediately to the left of my car,
                        continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible immediately to the right of my car, continuing
                        ahead. Photo 2: A solid yellow line is visible immediately to the right of my car,
                        continuing ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: no markings were reported, so they agree with each other and with the
                        boundaries | unseen: no attributes were reported that were not actually seen | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The boundary of the carriageway at a road junction or a lay-by, or at
                        an exit from a private drive onto a public road, is indicated by this marking. [[UK-
                        TSRGD-S11P4-item10]]
Step 5  Rule            line:stop_line: This line indicates a stop line at signals or police control. [[UK-
                        HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The solid white line on my left indicates
                        a lane boundary, and there is no rule allowing a lane change into the adjacent lane.
Step 6  change_right    prohibited: prohibited: The solid yellow line on my right indicates the edge of the
                        carriageway, and there is no rule allowing a lane change into the adjacent area.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid lines. No specific stopping location is marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 921, 7.94 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection or crossing
                        area. There are two lanes visible in my direction near the bottom of the photo. (lanes
                        2, mine 1, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2; text:bus (full): Photo 2; text:bus (full): Photo 2; text:bus
                        (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (dashed white line is a lane_line, solid white line is a lane_line). | markings: the
                        markings (text:bus) are consistent with the boundaries and each other. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: Bus lanes are shown by road markings and signs that indicate which (if any)
                        other vehicles are permitted to use the bus lane. [[UK-Rule141]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and [UK-Rule131] implies keeping between lane dividers, and a solid line
                        generally restricts lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is marked as a bus lane. You may proceed straight
                        ahead, but changing right is prohibited by the solid white line. You should use this
                        lane for straight travel or changing left if necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1170, 9.82 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a paved urban road with buildings on both sides, and there is an
                        intersection/junction ahead where the road appears to widen or change direction. My
                        car is in the lane closest to the left side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows a large white 'BUS' marking painted on the road ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction) | roles: the color and pattern of
                        both boundaries (white dashed) fit the role of a lane_line | markings: the text:bus
                        marking is in my lane and is consistent with the boundaries | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [[UK-Rule141]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a lane_line, and
                        while no specific prohibition is given for changing left, the general rule suggests
                        keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane_line, and there is no marking
                        prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight ahead.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the bus lane, so you should not drive in it unless permitted by signs. You
                        may change right, and you may proceed straight ahead, but turning left, right, or
                        performing a U-turn is not indicated as permitted by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['area:grid']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_left prohibited across a broken lane line']
Tokens                  in 14750, out 946, 12.5 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is a red bus visible in the distance. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to the car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line immediately next to the car, and further ahead, this
                        line continues as a dashed white line. Photo 2 shows a dashed white line immediately
                        next to the car, and further ahead, this line continues as a dashed white line.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a center_line, meaning my lane is the leftmost lane of my direction. |
                        roles: the color and pattern of each boundary fit the role given to it. | markings:
                        the symbol:bike in my lane is consistent with the boundaries and does not contradict
                        any rules. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: A broken white line marks the centre of the road, and when it
                        lengthens and the gaps shorten, it means that there is a hazard ahead; do not cross it
                        unless you can see the road is clear and wish to overtake or turn off. [[UK-Rule127]]
Step 5  Rule            symbol:bike: This marking indicates the boundary of a mandatory cycle lane or a
                        division of a route into that part reserved for pedal cycles. [[UK-TSRGD-Part6,item7]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a
                        lane_line, and [UK-Rule131] recommends keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed because the right boundary is a center_line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if it is
                        safe.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is designated for cycling. You may proceed
                        straight or change lanes, but you should be aware of the cycle lane marking and
                        exercise caution when changing lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1164, 9.26 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is a junction where the road appears
                        to continue straight and potentially turn. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, this line appears to transition into a solid white
                        line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, this line appears to transition into a solid white
                        line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:yield_line (full): Photo 2 shows white dashed lines forming a 'give way' triangle
                        marking on the road surface ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles, as both boundaries are lane_lines, indicating my
                        lane is between two lanes of my direction. | roles: The color (white) and pattern
                        (dashed) of both boundaries fit the role of lane_lines. | markings: The yield line
                        marking is present in Photo 2 and is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:yield_line: Vehicular traffic must give way in accordance with the requirements
                        in paragraph 7 of Part 7. [[UK-TSRGD-Part6,item3]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a dashed
                        white line, and there is no indication that a lane change is permitted or required.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a dashed
                        white line, and there is no indication that a lane change is permitted or required.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that permit turning left.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that permit turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that permit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane, but you must give way to
                        traffic approaching from the right at the junction ahead, as indicated by the yield
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_left prohibited across a broken lane line', 'change_right prohibited across a
                        broken lane line']
Tokens                  in 14750, out 1083, 8.25 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a continuation of the road with
                        buildings on both sides. There are three lanes visible in my direction near the bottom
                        of the photo. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating my lane is between two lanes of my direction). | roles: the
                        color and pattern of both boundaries (white dashed lines) fit the role of lane_line. |
                        markings: there are no arrows, words, or areas painted in my lane, so they agree with
                        each other and with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and there is no marking prohibiting a lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and there is no
                        marking prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of three. You may change left or right, and you may
                        proceed straight ahead. You should use the lane appropriate for your intended
                        movement, as there are no specific lane markings directing you.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 14750, out 841, 6.65 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction. My car is in the
                        lane closest to the left curb. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the curb. Photo 2 shows a solid white line
                        next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the lane. Photo 2 shows a broken white line
                        next to the lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2; arrow:left (full): Photo
                        2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is edge_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrows in my lane agree with each other and with the boundaries (they
                        indicate allowed movements from this lane) | unseen: no | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: This marking indicates that proceeding straight ahead is a possible
                        movement for my car. [null]
Step 5  Rule            arrow:right: This marking indicates that turning right is a possible movement for my
                        car. [null]
Step 5  Rule            arrow:left: This marking indicates that turning left is a possible movement for my
                        car. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: The right boundary is a lane_line, and
                        there is no marking governing a change to the left.
Step 6  change_right    allowed (contested, correct): allowed: The right boundary is a lane_line, and the
                        markings allow movement into the adjacent lane.
Step 6  go_straight     allowed (correct): allowed: The lane markings include an arrow showing straight ahead,
                        and no rule prohibits this movement.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed: The lane markings include an arrow showing
                        a left turn, and no rule prohibits this movement.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane markings include an arrow showing
                        a right turn, and no rule prohibits this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane that governs a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight, turn left, or turn right from your lane. You may also change
                        right into the adjacent lane. You should use the lane indicated by the arrows for your
                        intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['line:stop_line', 'symbol:bike']), actions
                        False, unsafe ['turn_left', 'turn_right'], citation unlisted, contradictions []
Tokens                  in 14750, out 947, 7.71 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road appears to continue or change direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to my car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to my car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line immediately next to my car, and further ahead, this
                        line continues as a broken white line. Photo 2 shows a broken white line immediately
                        next to my car, and further ahead, this line continues as a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a solid line
                        (lane_line), indicating a lane to the left, and the right boundary is a dashed line
                        (lane_line), indicating a lane to the right. This is consistent with my lane being the
                        middle lane. | roles: The left boundary is a solid white lane_line, and the right
                        boundary is a dashed white lane_line. This is consistent. | markings: The stop line is
                        located in my lane, which is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane_line, and
                        [UK-Rule131] suggests keeping between lane dividers, which implies a lane change is
                        restricted or requires caution.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane_line, and [UK-Rule131]
                        suggests keeping between lane dividers, which implies a lane change is permitted if
                        safe.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibited-movement markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       allowed: There are no arrows or prohibited-movement markings in my lane, and the
                        boundaries do not prohibit turning left.
Step 6  turn_right      allowed: There are no arrows or prohibited-movement markings in my lane, and the
                        boundaries do not prohibit turning right.
Step 6  u_turn          allowed: There are no arrows or prohibited-movement markings in my lane, and the
                        boundaries do not prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a waiting area in my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed that is prohibited by a rule from step 5.
Advice                  You are in the middle lane, and while you can proceed straight, turn left, or turn
                        right, you should not change lanes to the left due to the solid white line. You may
                        change right if it is safe to do so, and you must stop at the stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 14750, out 1176, 9.36 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        appears to continue straight, possibly leading into a junction or area where lane
                        configuration changes. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues as a solid white line. Photo 2 shows a solid white line
                        immediately to the left of my car, and further ahead, this line continues as a solid
                        white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line immediately to the right of my car, and further
                        ahead, this line continues as a broken white line. Photo 2 shows a broken white line
                        immediately to the right of my car, and further ahead, this line continues as a broken
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line for lane line, dashed white line for lane line). | markings: the
                        stop line marking is consistent with the lane configuration. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicles must stop at signals or police
                        control. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, the left boundary is a solid white
                        line, and there is no rule passage that permits crossing a solid white line for lane
                        change.
Step 6  change_right    allowed (correct): allowed, the right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the line nearer to you is broken if
                        it is safe.
Step 6  go_straight     allowed (contested, correct): allowed, there are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable, there are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  turn_right      not_applicable: not_applicable, there are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  u_turn          not_applicable: not_applicable, there are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, there are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane if it is safe, and you may proceed
                        straight ahead. You must stop at the solid white line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1079, 8.8 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a standard road section rather than an
                        immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane division
                        ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The color and pattern of
                        both boundaries (white dashed lines) fit the role of lane_line. | markings: The lane
                        marking (stop_line) is consistent with the boundaries and general road context. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [UK-Rule131]
                        permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes and can change left or right if safe. You
                        may proceed straight ahead, but you must stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14750, out 1047, 8.55 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is a junction where traffic appears
                        to be merging or continuing through. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        near my car.; line:stop_line (partial): Photo 1 shows a white dashed line marking the
                        lane boundary further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line, indicating my lane is between two lanes of my direction). | roles: the
                        color and pattern of both boundaries (white dashed) fit the role of a lane_line. |
                        markings: the markings (line:stop_line) are consistent with the lane boundaries and do
                        not contradict the lane roles. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a white
                        dashed lane_line, and there is no rule prohibiting a lane change.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed lane_line, and
                        there is no rule prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict turning left.
Step 6  turn_right      allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict turning right.
Step 6  u_turn          allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or a two-way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes, and all movements (straight, left, right,
                        U-turn) are permitted. You should observe the stop line ahead and follow the general
                        guidance of the road markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 14750, out 947, 7.53 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street in a built-up area, and the road continues ahead into the distance.
                        There are two lanes of traffic visible in my direction near the bottom of the photo.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane lines, indicating two
                        lanes in my direction) | roles: the color and pattern of each boundary fit the role
                        given to it (both are white dashed lines, consistent with lane dividers) | markings:
                        there are no markings in my lane to check against the boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and no rule prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and no rule
                        prohibits changing right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane indicating a
                          waiting area.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and since the lane markings are dashed,
                        you may change lanes if it is safe to do so. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 14750, out 768, 5.8 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch of road. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating my lane is the leftmost of the three lanes). | roles: the color
                        and pattern of both boundaries (white dashed lines) fit the role of lane_line. |
                        markings: the stop line in my lane agrees with the boundaries as it is located within
                        the lane defined by the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or a 'Stop' sign.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a dashed white line,
                        which permits lane changes if safe, but the stop line ahead governs the immediate
                        action.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which permits
                        lane changes if safe, and no immediate restriction is present.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane in view.
Step 7  Reflect         consistent
Advice                  You may change right if safe, and you may proceed straight ahead. You must stop at the
                        stop line visible ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left prohibited
                        across a broken lane line']
Tokens                  in 14750, out 892, 7.36 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is a continuation of the road with
                        traffic moving in both directions. My car is in the lane closest to the left side of
                        the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Further ahead, Photo 1 shows a dashed white line continuing, and
                        Photo 2 shows a dashed white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows the text 'BUS LANE' painted on the road in my lane, and
                        Photo 2 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line for lane line, dashed white line for lane line). | markings: the
                        text 'BUS LANE' in my lane agrees with the boundaries (it is in the lane defined by
                        the boundaries). | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: These markings indicate which (if any) other vehicles are permitted to use
                        the bus lane. [[UK-Rule141]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and while no specific rule prohibits changing left from a solid line, the solid line
                        generally restricts lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule128] permits crossing double white lines where the line nearer to you is broken if
                        it is safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you should only use this lane if permitted by signage. You
                        may change right if safe, but changing left is prohibited by the solid white line. You
                        may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1143, 8.62 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road in a built-up area, and ahead there is a junction where the
                        road continues and appears to curve slightly to the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows the solid white line continuing, and
                        Photo 2 shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows the broken white line continuing,
                        and Photo 2 shows the broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line on the left, dashed white line on the right). | markings: the
                        channelizing markings are consistent with the lane boundaries and do not contradict
                        the lane structure. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            area:channelizing: These diagonal stripes are used to separate traffic lanes or to
                        protect traffic turning right. [[UK-Rule130]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a lane
                        line and no rule prohibits changing left.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a lane
                        line and no rule prohibits changing right.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you are permitted to go straight or
                        change lanes left or right. You should keep within the lane dividers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1009, 12.22 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes traveling in the same direction. Ahead,
                        there is a junction where traffic appears to be moving through or approaching a
                        crossing area. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A dashed white line is visible next to my car. Photo 2: A dashed white line
                        is visible next to my car. Further ahead, the dashed white line continues. Photo 2
                        shows the line further ahead continuing as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Photo 2: A solid white line is
                        visible next to my car. Further ahead, the solid white line continues. Photo 2 shows
                        the line further ahead continuing as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.; arrow:right (full): Photo 2: A white arrow pointing right is visible in my
                        lane, further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 1 (leftmost). The left boundary is a lane line, and the right boundary is a lane
                        line, which is consistent with my lane being the leftmost lane of my direction. |
                        roles: The left boundary is a dashed white lane line, and the right boundary is a
                        solid white lane line, which fits the role of lane_line. | markings: The arrows
                        (straight and right) are within my lane and are consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 5  Rule            arrow:right: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed white
                        lane line, and while this line allows lane changes, the presence of the right arrow
                        suggests a primary movement constraint.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        lane line, and the presence of the right arrow allows movement into the adjacent lane.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The white arrow pointing straight ahead in
                        my lane allows this movement, and no other marking prohibits it.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking in my lane that allows a left
                        turn.
Step 6  turn_right      allowed (correct): allowed: The white arrow pointing right in my lane allows this
                        movement.
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: There is no marking in my lane that
                        allows a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which allows you to go straight or turn right. You may
                        change right into the adjacent lane, but you cannot change left. You should proceed
                        with caution as you approach the junction.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation
                        accepted, contradictions ['leftmost lane, but a lane line on the left', 'change_left
                        prohibited across a broken lane line']
Tokens                  in 14750, out 1015, 8.59 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible immediately to the right of my car. Further
                        ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1: The text 'BUS LANE' is painted on the road in my lane near
                        the bottom.; text:bus (full): Photo 2: The text 'BUS LANE' is painted on the road in
                        my lane near the bottom.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (solid white lines on both sides indicate lane
                        dividers, and being the leftmost lane in the visible stretch confirms index 1). |
                        roles: the solid white lines on both sides fit the role of lane_line. | markings: the
                        text 'BUS LANE' is consistent across both photos and is located within my lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            text:bus: This marking indicates that the lane is designated for buses and other
                        permitted vehicles, and you should not drive in it unless permitted by signs. [[UK-
                        Rule141]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and the rule for lane dividers suggests keeping between them.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and the rule for lane dividers suggests keeping between them.
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
Advice                  You must remain in this lane as lane changes are prohibited by the solid white lines.
                        You may proceed straight ahead, but be aware that this lane is designated as a bus
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 880, 7.07 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and there is a street continuing ahead. There are
                        three lanes visible in my direction near the bottom of the photo. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in my lane near the bottom.;
                        line:stop_line (partial): Photo 2 shows a dashed white line marking the boundary of
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating I am in the middle lane of three lanes in my direction). |
                        roles: the color and pattern of both boundaries (white dashed lines) fit the role of a
                        lane_line. | markings: the text:bus marking is in my lane, and the line:stop_line is
                        visible ahead, which is consistent with the lane boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [[UK-Rule141]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or police control.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a white dashed
                        lane_line, and while this line permits lane changes, the presence of the text:bus
                        marking in my lane suggests this lane is reserved, which restricts movement.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and this
                        line permits lane changes if safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you should not drive in it unless permitted by signs; you
                        may change right if safe, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line', 'text:bus'], missed ['text:other']), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions ['change_left prohibited across a broken
                        lane line']
Tokens                  in 14750, out 993, 8.51 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a continuation of the road with
                        buildings on both sides. My car is in one of the lanes near the bottom of the photo.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: no markings
                        were reported, so there is no agreement to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates a stopping point at signals or a police control.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        white line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit it, and boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right as long as it is safe, and you may proceed straight ahead.
                        No specific stopping or turning restrictions are visible in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14750, out 905, 6.82 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to lead towards a junction or a continuation of
                        the street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and a dashed white line further
                        ahead. Photo 2 shows a dashed white line next to my car, and a dashed white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line for lane line, dashed white line for lane line). | markings: the
                        text 'BUS LANE' in my lane is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: These markings indicate which (if any) other vehicles are permitted to use
                        the bus lane. [[UK-Rule141]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a lane line, and
                        no rule prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane line, and no rule prohibits
                        changing right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you should only use this lane if you are permitted to do so
                        by local regulations. You may change lanes left or right, and you may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14750, out 1051, 7.32 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, appearing to be a standard road section rather than an
                        immediate intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, this
                        solid white line continues. Photo 2 shows a solid white line immediately next to the
                        car, and further ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line immediately next to the car, and further ahead,
                        this broken yellow line continues. Photo 2 shows a broken yellow line immediately next
                        to the car, and further ahead, this broken yellow line continues.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a center_line, indicating my lane is the leftmost of the two lanes in my
                        direction. | roles: The left boundary is a solid white lane_line, and the right
                        boundary is a dashed yellow center_line, which fits the roles assigned. | markings:
                        The stop line is located within my lane and is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You may cross the double white lines to overtake if it is safe,
                        provided you can complete the manoeuvre before reaching a solid white line on your
                        side. [[UK-Rule128]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a
                        lane_line, and [UK-Rule131] recommends keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed because the right boundary is a center_line, and [UK-
                        Rule128] permits crossing double white lines if safe.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and should stop at the stop line ahead. You may proceed
                        straight or change lanes if safe, but turning left, right, or performing a U-turn is
                        not governed by any visible markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14750, out 1147, 8.75 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, it remains a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car, and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane line (separating from
                        lane 1), and the right boundary is a lane line (separating from lane 3). | roles: The
                        left boundary is a dashed white line (lane_line), and the right boundary is a solid
                        white line (lane_line). This is consistent. | markings: The stop line is located ahead
                        of the lane, consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where vehicular traffic must stop at signals or a
                        'Stop' sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, and
                        [UK-Rule131] recommends keeping between lane dividers, which permits a lane change if
                        safe.
Step 6  change_right    allowed (correct): The right boundary is a solid white line, and [UK-Rule131]
                        recommends keeping between lane dividers, but the solid line suggests a restriction,
                        though no specific prohibition is cited for changing across a solid line in this
                        context.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibited-movement markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so this action is not governed by a
                        marking.
Step 6  turn_right      not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so this action is not governed by a
                        marking.
Step 6  u_turn          not_applicable: There are no arrows or prohibited-movement markings in my lane, and no
                        waiting area or two-way left-turn lane is present, so this action is not governed by a
                        marking.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane
                          present, so this action is not applicable.
Step 7  Reflect         The boundaries and markings were settled in the close-up check, no action is allowed
                        although a rule prohibits it, no action was decided without a feature that decides it,
                        each reason leads to its action, and the reasoning is consistent.
Advice                  You are in the middle lane, and you may change left or right if safe, but you must
                        stop before the solid white line marked as a stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14750, out 1196, 9.48 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues straight, and there is a marked area indicating a speed limit. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2: A circular marking with '20' inside is visible in the
                        lane.; symbol:other (full): Photo 2: A circular marking with '20' inside is visible in
                        the lane.; symbol:other (full): Photo 2: A circular marking with '20' inside is
                        visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (dashed lines indicate lane division between lanes
                        of the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: the symbols (speed limit) are
                        present in all three lanes and do not contradict the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            symbol:other: No specific traffic rule passage was found that dictates the action
                        based on the speed limit symbol. [null]
Step 6  change_left     allowed (contested, correct): allowed: The left boundary is a dashed white line, and
                        no marking prohibits a lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and no marking
                        prohibits a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane that restrict proceeding straight ahead.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that permit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that permit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that permit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of the lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane dividers are dashed, and you are
                        permitted to go straight ahead. Be aware of the 20 mph speed limit indicated by the
                        circular markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 14750, out 928, 7.22 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street in a built-up area, and ahead there is a junction where the road
                        continues straight and curves slightly to the right. My car is in the lane closest to
                        the right side of the road among the lanes traveling in the same direction. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to my car. Further ahead, this dashed
                        white line continues. Photo 2: A dashed white line is visible next to my car. Further
                        ahead, this dashed white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        this solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A series of white arrows pointing straight ahead are
                        visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrow in my lane agrees with the boundaries (it governs movement within
                        the lane defined by the boundaries) | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The line indicates the edge of the carriageway at a road junction or a
                        lay-by, or at an exit from a private drive onto a public road. [[UK-
                        TSRGD-S11P4-item10]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a lane_line, and
                        while no specific prohibition is given for changing left, the lane_line suggests a
                        boundary to another lane.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is an edge_line,
                        and no rule prohibits changing into the area beyond it.
Step 6  go_straight     allowed (contested, correct): allowed: The lane has a white arrow pointing straight
                        ahead, and no rule prohibits going straight.
Step 6  turn_left       prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a left turn.
Step 6  turn_right      prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a right turn.
Step 6  u_turn          prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as indicated by the
                        arrow. You may change right if safe, but turning left, turning right, or making a
                        U-turn is prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line']
Tokens                  in 14750, out 955, 8.22 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and the road continues ahead without an
                        immediate intersection or end visible in the frame. My car is in one of the lanes near
                        the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car. Further ahead, the dashed white line continues. Photo 2
                        shows the line further ahead continuing as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Photo 2 shows
                        the line further ahead continuing as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and there is no
                        rule prohibiting a lane change across a dashed line.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        line, but since there is no explicit rule prohibiting crossing a solid line in this
                        context (e.g., double solid), and the line is a lane divider, a lane change is
                        permitted if safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern U-turns or turning in the opposite direction.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes in view.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change lanes
                        to the left or right if the road conditions are safe, as the boundaries permit lane
                        changes across dashed and solid lines respectively. No specific stopping points are
                        marked in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14750, out 873, 7.23 s
```
