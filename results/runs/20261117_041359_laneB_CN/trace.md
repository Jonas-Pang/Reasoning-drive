# Reasoning of lane run 20261117_041359_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with an intersection or signalized area in the distance. (lanes 3,
                        mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which is an edge lane
                        or a boundary to a different flow.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a solid yellow line on the right. | roles: The white dashed line
                        on the left correctly identifies a crossable lane line, and the solid yellow line on
                        the right correctly identifies a no-crossing edge/boundary. | markings: The straight
                        arrow in my lane is consistent with the lane's role as a through lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid yellow line prohibits me from crossing into the area to my
                        right. [[CN-6.1.4]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid yellow line [CN-6.1.4].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the lane on your left, but you are prohibited from moving to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 748, 6.68 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight stretch with a slight curve or intersection in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which is an edge lane
                        or a boundary to a different flow.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white line on
                        the left and a yellow line on the right. | roles: The white line on the left is a lane
                        line, and the yellow line on the right is an edge line, which is consistent with
                        Chinese traffic rules. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow edge line marks the boundary of the roadway and prohibits
                        crossing to the right. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 775, 7.09 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with buildings on both sides. Ahead, there is
                        a clear roadway with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be an
                        edge lane or a lane next to a sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; area:left_turn_waiting (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.; area:grid (insufficient): No markings are visible in
                        my lane.; area:channelizing (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: No markings were
                        observed, which is consistent with the clear view of the lane surface. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 832, 8.83 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. The road ahead
                        appears to be a straight stretch with multiple lanes of traffic. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        is consistent with the straight road ahead and the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 672, 5.85 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated highway structure on the right. The road
                        ahead is straight with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; area:left_turn_waiting (insufficient): No markings
                        visible in my lane.; area:two_way_left_turn_lane (insufficient): No markings visible
                        in my lane.; area:grid (insufficient): No markings visible in my lane.;
                        area:channelizing (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed in the lane, which is consistent with the visual evidence. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side to the left lane.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side to the right
                        lane. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 803, 7.07 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and shops on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is a parking or
                        slow-moving lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: The straight arrow is
                        consistent with the straight road ahead and the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to continue straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 687, 6.43 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        the left and yellow line on the right. | roles: The white line on the left and yellow
                        line on the right are consistent with standard lane markings for a multi-lane road in
                        China. | markings: The straight arrow is consistent with the lane's forward direction.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line (CN-6.2.1)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line (CN-6.2.1)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 833, 8.87 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the left and a bus stop on the
                        right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; area:left_turn_waiting (insufficient): No markings
                        visible in my lane.; area:two_way_left_turn_lane (insufficient): No markings visible
                        in my lane.; area:grid (insufficient): No markings visible in my lane.;
                        area:channelizing (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: No markings were observed, which
                        is consistent with the lack of specific movement indicators. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (CN-6.2.1).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right (CN-6.2.1).
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and the lane
                        continues straight.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 803, 7.65 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a city skyline in the distance. The road appears to be a
                        wide boulevard with a median or separation on the left. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white line on
                        my left and a white line on my right. | roles: The white solid lines correctly
                        represent a lane line and a right-hand edge line in a right-hand traffic system. |
                        markings: The straight arrow is consistent with the lane's role and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 755, 8.94 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or junction ahead. My car is in a lane
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my right.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: The straight arrow in
                        my lane is consistent with the lane's role. The left arrow in the right lane is
                        consistent with its role. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line on the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 7595, out 781, 12.83 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or pedestrian crossing ahead. The sun is
                        low in the sky, creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or non-motorized area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        identify lane-to-lane and lane-to-edge boundaries. | markings: The straight arrow is
                        consistent with the lane's role and boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid lines prohibit it.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 761, 7.49 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an overpass or bridge structure ahead.
                        The car is positioned in a lane heading towards an intersection or a merge point.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A yellow arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        the left and yellow line on the right. | roles: The white line on the left and yellow
                        line on the right are consistent with lane markings for same-direction traffic. |
                        markings: The straight arrow is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the lane on the right.
                        [[CN-6.1.4]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line (CN-6.2.1)
Step 6  change_right    prohibited (correct): prohibited by the solid yellow line (CN-6.1.4)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. Lane changes to the left or right
                        are prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 675, 6.76 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass ahead. The road continues straight
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is bounded by a
                        fence/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        on the left is a crossable lane line, and the white solid line on the right is an edge
                        line. | markings: The straight arrow in my lane is consistent with the lane's purpose.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the left lane, but you cannot move to the right beyond the solid edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 717, 6.98 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight towards a signalized intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        parking or stopping area.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        a white line on my left and a yellow line on my right. | roles: The white line on the
                        left correctly identifies a same-direction lane, and the yellow line on the right
                        correctly identifies a boundary with a different flow or area. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the area to my right.
                        [[CN-6.1.4] [mandatory] GB 5768.3-2025, section 6.1.4, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow lane line
                        [CN-6.1.4]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You are prohibited from changing
                        lanes to the left or right due to the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 793, 7.83 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass and overhead signs. The road ahead appears to
                        be a continuous stretch of lanes. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is bounded by a
                        curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on the left and a white solid line on the right. | roles: The white
                        dashed line on the left correctly identifies a crossable lane line, and the white
                        solid line on the right correctly identifies an edge line. | markings: The straight
                        arrow in my lane is consistent with the lane's function as a through lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change into the left
                        lane. Changing into the right lane is prohibited by the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 704, 132.0 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        on the left correctly identifies a crossable lane line, and the white solid line on
                        the right correctly identifies an edge line. | markings: The straight arrow in my lane
                        is consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the left lane if necessary, but you must not move to the right beyond the solid edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 701, 7.08 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection. The road is wide with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or a lane-change area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly identify lane
                        boundaries for same-direction traffic. | markings: The straight arrow is consistent
                        with the lane's role and the white lane lines. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane on my
                        right. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the left lane. Changing into the right
                        lane is prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 677, 6.97 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane moving forward towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight ahead arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 667, 11.34 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in one of
                        the middle lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight
                        arrows in my lane are consistent with the lane's role and the surrounding lane
                        markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 757, 5.98 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with an intersection ahead. The car is positioned in one of the
                        middle lanes. (lanes 4, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        separating traffic in the same direction. | markings: The straight arrow in my lane is
                        consistent with the lane's role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 664, 6.71 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or junction ahead. The road is wide with
                        clear lane markings. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 639, 5.91 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to have a turn option. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and slightly to the
                        left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: The straight-left
                        arrow is consistent with the lane's position and the surrounding lane markings. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight_left: The arrow indicates that the lane allows for traveling straight
                        ahead or turning left. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (CN-6.2.1).
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right (CN-6.2.1).
Step 6  go_straight     allowed (correct): allowed by the straight-left arrow (CN-5.13.1).
Step 6  turn_left       allowed (correct): allowed by the straight-left arrow (CN-5.13.1).
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 696, 8.25 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed, which is consistent with the lack of specific movement restrictions in the
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to my right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable: not_applicable as no right-turn arrow or area is present.
Step 6  u_turn          not_applicable: not_applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:stop'], missed []),
                        actions True, unsafe [], citation in_pack_not_accepted, contradictions ['go_straight
                        decided from an arrow that cannot be read', 'go_straight allowed without the stop that
                        the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 818, 8.04 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road passing under a bridge (Dashan Bridge). Ahead, there
                        is an intersection or a junction area with several vehicles and a pedestrian/cyclist
                        on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from a sidewalk/pedestrian area on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is in the lane to my
                        left.; arrow:left (full): A white arrow pointing left is in the lane to my left.;
                        arrow:left (full): A white arrow pointing left is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on my left and a white line/curb on my right. | roles: The white solid
                        lines correctly function as a lane line and an edge line. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose. The arrows in adjacent lanes
                        are also consistent with their respective boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway and prohibits
                        crossing onto the sidewalk. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3,
                        page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited: prohibited by the solid white lane line on the left
Step 6  change_right    prohibited: prohibited by the solid white edge line and curb on the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking in my lane
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:right']), actions False, unsafe [],
                        citation unlisted, contradictions ['turn_left not_applicable although an arrow shows
                        it']
Tokens                  in 7595, out 884, 8.32 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and trees on the right. The
                        road ahead appears to be a straight stretch leading towards a distant intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        lane lines on both sides. | roles: The white solid lines correctly identify as lane
                        lines separating traffic in the same direction. | markings: No markings were observed,
                        which is consistent with the lack of specific movement instructions. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left (CN-6.2.1)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right (CN-6.2.1)
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line', 'text:stop'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions ['go_straight decided from an arrow
                        that cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking
                        in my lane requires']
Tokens                  in 7595, out 815, 47.24 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is wet, and there are
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        identify as lane lines separating traffic in the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's function and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to my right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 675, 6.33 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in a lane
                        that continues straight through the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left that appears to turn
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to the right that appears to turn
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: The straight arrow is
                        consistent with the lane's function and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the left lane. [[CN-6.2.1]
                        [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the right lane.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a straight-through lane. You should proceed straight ahead and avoid
                        changing lanes, as the solid white lines on both sides prohibit lane changes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 757, 7.46 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is lined with trees and
                        buildings. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A white grid pattern is visible on the pavement ahead in the
                        intersection area.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2] [mandatory] GB 5768.3-2025, section 6.8.1, 6.8.2, page 53]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 691, 6.02 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide boulevard layout. Ahead, the road continues
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which contains a car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white diamond shape is painted in the center of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The diamond symbol
                        is a neutral marking and does not contradict the lane boundaries. | unseen: None |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            symbol:other: No specific rule governs the diamond symbol for movement.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 641, 10.72 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. There is a bus
                        lane on the left and a sidewalk/curb on the right. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left is a lane line, and the white solid line on the right is an edge line, which
                        is consistent with the road layout. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule for a white solid lane line is provided in the text,
                        but it generally prohibits crossing. [null]
Step 5  Rule            right_boundary: No specific rule for a white solid edge line is provided in the text,
                        but it marks the edge of the roadway. [null]
Step 5  Rule            arrow:straight: The straight arrow indicates that the lane is intended for straight-
                        ahead travel. [null]
Step 6  change_left     prohibited: prohibited by the solid white lane line on the left
Step 6  change_right    prohibited: prohibited by the solid white edge line and curb on the right
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may proceed straight but
                        are prohibited from changing lanes to the left or right due to the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation unlisted, contradictions []
Tokens                  in 7595, out 693, 10.89 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a concrete barrier on the left and a white car in the
                        adjacent lane to the right. Ahead, there is a truck and a clear roadway. (lanes 2,
                        mine 1, full)
Step 2  Left            A concrete barrier with a yellow and black striped post at the end.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:straight (insufficient): none; arrow:left
                        (insufficient): none; arrow:right (insufficient): none; text:stop (insufficient):
                        none; text:keep_clear (insufficient): none; area:left_turn_waiting (insufficient):
                        none; area:two_way_left_turn_lane (insufficient): none; area:grid (insufficient):
                        none; area:channelizing (insufficient): none
Step 4  Cross-check     position: The lane count (2) and my lane position (1) are consistent with the left
                        edge (barrier) and right lane line. | roles: The white solid line on the right
                        correctly identifies a lane-line separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is marked by a yellow line, but a physical
                        barrier serves the same purpose here. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: No arrow is present, but the default is straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label not_determined): no marking governs this action
Step 6  change_right    prohibited (correct): prohibited by the solid white line per [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the right are
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:left', 'arrow:right', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:keep_clear',
                        'text:stop'], missed []), actions False, unsafe [], citation accepted, contradictions
                        ['change_left allowed across a curb', 'go_straight decided from an arrow that cannot
                        be read', 'go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 7595, out 907, 9.43 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in one
                        of the lanes of the main roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        in my lane is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to my right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 655, 7.59 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection. There is a bridge structure on
                        the right and a traffic light system ahead. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding lane markings. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 666, 5.67 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        ahead appears to be a straight stretch or a wide intersection approach. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify the lane-line
                        on the left and the edge-line on the right. | markings: No markings are present, which
                        is consistent with the clear lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line (CN-5.4.3)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 784, 7.31 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the left and a parking area on the right.
                        The road ahead appears to be a straight stretch with an intersection or signalized
                        area in the distance. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        double solid yellow line on the left indicates a center line (separating opposing
                        traffic), and a white line on the right indicates a lane line. | roles: The yellow
                        double solid line correctly identifies a center line, and the white solid line
                        correctly identifies a lane line. | markings: The straight arrow is consistent with
                        the lane's role as a through lane. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The guide arrow indicates that the lane allows for straight
                        ahead or U-turn movements. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the straight or U-turn arrow marking [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn as indicated by the lane markings.
                        Lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 913, 15.61 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or large junction ahead. The road is wide
                        with several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        double solid yellow line on the left indicates a center line separating opposing
                        traffic, and a white line on the right separates lanes in the same direction. | roles:
                        The double solid yellow line correctly identifies a no-crossing center line, and the
                        white line correctly identifies a lane-separation line. | markings: The straight arrow
                        in my lane is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the direction of travel for this lane
                        is straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but you are prohibited from
                        changing lanes to the left or right due to the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation
                        accepted, contradictions []
Tokens                  in 7595, out 717, 10.52 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a large building and a subway entrance on
                        the right. The road continues straight ahead into a city area. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        dedicated lane or area near a subway entrance.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: No markings were
                        observed in my lane, which is consistent with the lack of specific movement
                        instructions. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
                        [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line', 'text:stop'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions ['go_straight decided from an arrow
                        that cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking
                        in my lane requires']
Tokens                  in 7595, out 824, 8.19 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road passing under an overpass. Ahead, the road
                        continues straight towards a city area. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        sidewalk or parking area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; area:left_turn_waiting (insufficient): No markings are visible in
                        my lane.; area:two_way_left_turn_lane (insufficient): No markings are visible in my
                        lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lines
                        on both sides. | roles: The white lines correctly identify a lane-line on the left and
                        an edge-line on the right. | markings: No markings were observed, which is consistent
                        with the clear pavement. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the lane to
                        the left. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: no marking governs this action [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line'], missed []), actions True,
                        unsafe [], citation unlisted, contradictions ['go_straight decided from an arrow that
                        cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking in
                        my lane requires']
Tokens                  in 7595, out 802, 9.85 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is wide with several
                        lanes of traffic moving in the same direction. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and a landscaped
                        area beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the lane to your left, but you must not move to the right beyond the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 632, 33.2 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the central
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        in my lane is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 739, 5.88 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection. The road ahead has several lanes
                        of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly identify lane boundaries for
                        traffic in the same direction. | markings: The straight-ahead arrow is consistent with
                        the lane's role. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from crossing into the lane on my
                        right. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is intended for straight ahead
                        or right turn movements. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the arrow [CN-5.13.1]
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. You are permitted to
                        change into the left lane, but you are prohibited from changing into the right lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 848, 15.3 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection. My car is in a
                        lane heading straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bicycle lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        is consistent with the lane's role and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to my right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 656, 5.06 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass ahead. The road is wide and clear.
                        (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left and solid white line on the right are consistent with lane and edge line roles. |
                        markings: The straight arrow is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the left lane, but you are prohibited from moving into the area to the right of the
                        solid white line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 686, 13.81 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median on the left and a sidewalk/curb on the right. An
                        intersection or junction is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.; area:grid (full): A white 'KEEP CLEAR' style grid is visible in the lane to my
                        right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white lines
                        correctly identify lane separation and the right-hand edge of the roadway. | markings:
                        The straight arrow in my lane is consistent with the lane's role. The grid is in the
                        adjacent lane, not mine. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line (CN-5.4.3)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       prohibited: prohibited by the lack of a left-turn arrow and the solid white line
                        (CN-6.2.1)
Step 6  turn_right      allowed: allowed by the straight or right arrow (CN-5.13.1)
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'arrow:straight_right'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7595, out 942, 15.91 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight stretch with a potential intersection or lane configuration change further
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        special lane.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.; text:bus
                        (full): White text '公交' (BUS) is painted in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        my left and the yellow line on my right. | roles: The white line on the left is a
                        standard lane line; the yellow line on the right marks a special lane (bus lane). |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. The
                        '公交' text correctly identifies the lane to the right as a bus lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The bus lane line prohibits vehicles other than buses from entering
                        the lane to the right. [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1, page 54]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow bus lane line
Step 6  go_straight     allowed (contested, label prohibited): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 815, 7.17 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a large overhead gantry ahead. The road
                        appears to be a divided highway with a physical barrier on the right. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        physical barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the edge line/barrier on my right. | roles: The white solid line
                        on the left is a lane line, and the white solid line on the right is an edge line,
                        which is consistent with the right-hand traffic rule. | markings: The straight arrow
                        is consistent with the lane's role as a through lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane allows for straight ahead or
                        U-turn movements. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page
                        27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        physical barrier on the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the straight or U-turn arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or perform a U-turn if permitted by local signs. Lane
                        changes to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 804, 7.63 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a metal
                        guardrail on the right. The road ahead appears to be a straight stretch of highway.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        is consistent with the lane's role as a through lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the left lane. [[CN-6.2.1]
                        [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the right lane.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['turn_right not_applicable although an arrow shows it']
Tokens                  in 7595, out 762, 5.89 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The sun is high in the
                        sky, creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; arrow:straight (full): No markings are visible in my lane.; text:stop
                        (full): No markings are visible in my lane.; text:keep_clear (full): No markings are
                        visible in my lane.; area:left_turn_waiting (full): No markings are visible in my
                        lane.; area:two_way_left_turn_lane (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white dashed lines on both sides. | roles: The white dashed lines correctly identify
                        as lane lines between lanes of the same direction. | markings: No markings were
                        observed, which is consistent with a standard highway lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you are permitted to continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:keep_clear',
                        'text:stop'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 7595, out 842, 6.51 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or elevated road with an upcoming split or exit. My car is in one
                        of the middle lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings are
                        present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by solid white lines, which prohibit lane changes to the
                        left or right. You should continue straight in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 816, 10.81 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with trees lining both sides. The road ahead
                        appears to be a straight stretch of highway. (lanes 3, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail and trees
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white dashed line is on my left (lane 2) and a white solid line is on my right (edge).
                        | roles: The white dashed line correctly identifies a crossable lane line, and the
                        white solid line correctly identifies a right-hand edge line. | markings: No markings
                        are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move to the
                        right beyond the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 798, 13.78 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky and power lines visible in the
                        distance. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway, next to a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the white solid line on my right. | roles: The white dashed line
                        on the left correctly identifies a lane-change possibility, and the white solid line
                        on the right correctly identifies the road edge. | markings: No markings were observed
                        in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no turn markings or arrows are present.
Step 6  turn_right      not_applicable: Not applicable as no turn markings or arrows are present.
Step 6  u_turn          not_applicable: Not applicable as no turn markings or arrows are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. Do not move to the right of the white
                        edge line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 661, 8.59 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a raised
                        embankment/barrier on the right. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (insufficient): none; no_turn:left (insufficient): none; text:only
                        (insufficient): none; text:bus (insufficient): none; text:hov (insufficient): none;
                        text:stop (insufficient): none; text:keep_clear (insufficient): none; text:speed_limit
                        (insufficient): none; symbol:hov_diamond (insufficient): none; symbol:bike
                        (insufficient): none; symbol:other (insufficient): none; area:left_turn_waiting
                        (insufficient): none; area:two_way_left_turn_lane (insufficient): none; area:grid
                        (insufficient): none; area:channelizing (insufficient): none; line:stop_line
                        (insufficient): none; line:yield_line (insufficient): none; line:stop_yield
                        (insufficient): none; line:crosswalk (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:straight', 'line:crosswalk', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line', 'no_turn:left', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation unlisted, contradictions ['go_straight decided from an arrow that cannot be
                        read', 'go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 7595, out 1032, 45.24 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or major road with a clear sky. The road ahead appears to be a
                        straight stretch with multiple lanes of traffic. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, followed by a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with a white dashed
                        line on my left and a white solid line on my right. | roles: The white dashed line on
                        the left correctly identifies a crossable lane line, and the white solid line on the
                        right correctly identifies the edge of the roadway. | markings: The straight arrow in
                        my lane is consistent with the lane's role as a through lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the lane to your left, but you must not move to the right beyond the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 737, 6.01 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        straight stretch with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) are consistent with the white
                        dashed line on my left and the white solid line on my right. | roles: The white dashed
                        line on the left correctly identifies a lane-change possibility, and the white solid
                        line on the right correctly identifies the road edge. | markings: No markings were
                        observed in my lane, which is consistent with a standard highway lane. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: No rule applies as no stop line is present.
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which marks the road's end [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. You should stay within the lane and not
                        move past the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 700, 7.14 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road is bounded by
                        barriers on both sides. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; arrow:straight (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: No markings
                        are present, which is consistent with a standard highway lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The absence of a specific turn arrow implies that going straight is
                        the primary allowed movement. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane is a
                        standard through-lane.
Step 6  turn_left       not_applicable: No markings or arrows in my lane indicate a left turn is allowed.
Step 6  turn_right      not_applicable: No markings or arrows in my lane indicate a right turn is allowed.
Step 6  u_turn          not_applicable: No markings or arrows in my lane indicate a U-turn is allowed.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible to my left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you are permitted to continue straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_line', 'line:stop_yield', 'line:yield_line'], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 796, 7.67 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on the right. The road ahead
                        is straight with no immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a physical barrier/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        on the left correctly identifies a crossable lane line, and the white solid line on
                        the right correctly identifies an edge line. | markings: No markings are present,
                        which is consistent with a standard highway lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway and prohibits
                        crossing onto the shoulder/curb. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it and the lane
                        continues straight.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not move to the right as it
                        is bounded by a solid edge line and a physical barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 817, 7.45 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a construction area or barrier on the left. The road
                        ahead appears to be a straight stretch with a construction crane visible in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        shoulder or a lane ending near a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A white arrow pointing straight ahead is visible in the
                        center of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly identify lane separation and
                        the right-hand edge of the travel direction. | markings: The straight arrow is
                        consistent with the lane's forward path. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane allows for traveling straight
                        ahead or making a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-5.4.3)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the straight or U-turn arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn as indicated by the lane markings.
                        Lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 888, 8.88 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with a bridge or elevated structure ahead. The road is bounded by
                        metal guardrails on both sides. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify lane boundaries
                        for traffic in the same direction. | markings: No markings are present, which is
                        consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): prohibited by the solid white line on the left (CN-6.2.1)
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right (CN-6.2.1)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 774, 7.22 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. The road ahead is straight.
                        (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the 'Through Lane' signs above and the solid lane lines. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for travel straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should continue straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 896, 14.62 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a clear view ahead. There is a sidewalk
                        and a row of trees on the right, and a landscaped area with a low wall on the left.
                        (lanes 2, mine 1, full)
Step 2  Left            A low concrete wall and a landscaped area are to the left of my lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        a left edge (wall) and a right lane line. | roles: The white solid line on the right
                        correctly identifies a lane-line separating traffic in the same direction. | markings:
                        No markings were observed, which is consistent with the clear lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: No marking governs this action. [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     allowed (WRONG, label not_determined): no marking governs this action
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line per
                        CN-6.2.1
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Changing to the right is
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 7595, out 615, 5.13 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a central median. Ahead, there is a clear path for the
                        vehicle, with other cars and a motorcycle visible. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left, which is separated
                        from the median by a concrete barrier.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, adjacent to a sidewalk and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:straight (insufficient): none; arrow:left
                        (insufficient): none; arrow:right (insufficient): none; text:stop (insufficient):
                        none; text:keep_clear (insufficient): none; area:left_turn_waiting (insufficient):
                        none; area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (separating opposing traffic or a
                        median-adjacent lane), and the white solid line correctly identifies an edge line. |
                        markings: No markings were observed in the lane, which is consistent with the general
                        layout. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines and the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:left', 'arrow:right',
                        'arrow:straight', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'text:keep_clear', 'text:stop'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read', 'go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 7595, out 874, 7.55 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. The road ahead
                        appears to be a straight stretch with a clear path forward. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a sidewalk and a
                        pedestrian overpass.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; area:left_turn_waiting (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.; area:grid (insufficient): No markings are visible in
                        my lane.; area:channelizing (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line on the left correctly identifies a center line separating opposing
                        traffic, and the white solid line on the right correctly identifies the edge line. |
                        markings: No markings were observed in the lane, which is consistent with the lack of
                        specific movement instructions. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the lane to the
                        left. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 5  Rule            line:yield_line: no marking governs this action
Step 5  Rule            line:stop_yield: no marking governs this action
Step 5  Rule            area:left_turn_waiting: no marking governs this action
Step 5  Rule            area:two_way_left_turn_lane: no marking governs this action
Step 5  Rule            area:grid: no marking governs this action
Step 5  Rule            area:channelizing: no marking governs this action
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid boundary lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 1023, 133.8 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a straight
                        stretch with a median on the left and a sidewalk/curb on the right. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a sidewalk and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left is a lane line, and the white solid line on the right is an edge line, which
                        is consistent with the road layout. | markings: No markings were observed in my lane.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 700, 14.95 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a pedestrian overpass on the right. The
                        road ahead appears to be a straight stretch with an intersection or signalized area
                        further ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left is a lane line, and the white solid line on the right is an edge line, which
                        is consistent with the road layout. | markings: The straight-ahead arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight-ahead component of the lane
                        arrow
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the right-turn component of the lane arrow
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 805, 7.69 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with buildings and trees on both sides. The
                        road ahead appears to be a straight stretch with no immediate intersection or ramp
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: No markings were
                        observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 634, 6.56 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a clear sky. Ahead, there is a wide
                        intersection or open area with several lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 603, 6.48 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an overpass to the left and a tree-lined
                        sidewalk to the right. Ahead, the road continues straight with several lanes visible.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk and trees.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        a white lane line on my left and a white edge line on my right. | roles: The white
                        solid line on the left is a standard lane line, and the white solid line on the right
                        is a standard edge line. | markings: The straight arrow is consistent with the lane's
                        forward path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb on
                        the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may proceed straight ahead but
                        are prohibited from changing lanes to the left or right due to the solid boundary
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 780, 6.69 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a city street with a dedicated bicycle/non-motorized lane and a motor
                        vehicle lane. My car is positioned in a lane that appears to be a bicycle lane or a
                        shared lane, with a clear path ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A large white arrow pointing straight ahead is painted
                        in the center of my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        the white lane line on my left and the edge line/curb on my right. | roles: The white
                        solid line on the left correctly identifies a lane-line, and the white solid line on
                        the right correctly identifies an edge-line. | markings: The straight arrow is
                        consistent with the lane's forward direction. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway and prohibits
                        crossing onto the sidewalk. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3,
                        page 5]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may proceed straight ahead but
                        are prohibited from changing lanes to the left or right due to the solid boundary
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe [],
                        citation unlisted, contradictions ['leftmost lane, but a lane line on the left',
                        'u_turn not_applicable although an arrow shows it']
Tokens                  in 7595, out 810, 6.71 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with buildings and trees on both sides. Ahead,
                        there is a clear roadway with several lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line is on my right, and beyond it is a sidewalk with a curb and parked
                        vehicles.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; area:left_turn_waiting (full): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (full): No markings are visible in my lane.;
                        arrow:straight (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line, which is consistent with the rules. | markings: No markings were observed in my
                        lane, which is consistent with the lack of specific movement instructions. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: A straight arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and no arrow
                        restricts it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation unlisted, contradictions ['go_straight
                        allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 931, 9.33 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a clear view ahead. My car is in a lane
                        that appears to be the leftmost lane of a two-way road or a one-way road with a wide
                        sidewalk/curb on the left. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk/curb area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; arrow:left (insufficient): No markings are visible in my lane.;
                        arrow:right (insufficient): No markings are visible in my lane.; text:stop
                        (insufficient): No markings are visible in my lane.; text:keep_clear (insufficient):
                        No markings are visible in my lane.; area:left_turn_waiting (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. The left
                        boundary is an edge line (white line next to a curb), and the right boundary is a lane
                        line (white line separating lanes). | roles: The white solid lines correctly represent
                        an edge line on the left and a lane line on the right in a right-hand traffic system.
                        | markings: No markings were observed, which is consistent with the clear road
                        surface. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from the side of the
                        solid line (my side). [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 5  Rule            arrow:straight: No arrow is present, but the default is straight ahead. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and the lane
                        continues forward.
Step 6  turn_left       not_applicable: not_applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable: not_applicable as no right-turn arrow or area is present.
Step 6  u_turn          not_applicable: not_applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions ['go_straight
                        decided from an arrow that cannot be read', 'go_straight allowed without the stop that
                        the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 1018, 10.64 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        clear roadway with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the yellow center
                        line on my left and white edge line on my right. | roles: The yellow center line
                        correctly separates opposing traffic (or a median), and the white edge line marks the
                        right boundary. | markings: The straight arrow is consistent with the lane's purpose.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
                        [CN-6.1.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 679, 6.95 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; area:left_turn_waiting (insufficient): No markings
                        visible in my lane.; area:two_way_left_turn_lane (insufficient): No markings visible
                        in my lane.; area:grid (insufficient): No markings visible in my lane.;
                        area:channelizing (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        boundary [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right boundary
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 734, 11.95 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight stretch with a car directly in front. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, with a sidewalk and trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): A yellow line is visible on the pavement
                        in the lane to my left, but my lane itself has no markings.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (separating opposing traffic) and
                        the white solid line identifies the right edge. | markings: No markings are visible in
                        my lane; the yellow line to the left belongs to the adjacent lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the motor vehicle
                        lane. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines and the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7595, out 714, 10.62 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a dedicated lane for non-motorized
                        vehicles on the right. Ahead, the road continues straight with trees and buildings
                        lining the sides. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a non-motorized vehicle lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white solid lines
                        correctly identify lane boundaries for traffic in the same direction. | markings: No
                        markings were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the non-motorized lane to
                        the right. [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 619, 4.9 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tram line in the center. Ahead is a clear stretch of
                        road with buildings and trees on both sides. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white line marks the right edge of the roadway, with a sidewalk and trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (separating opposing traffic or a
                        special lane), and the white line correctly identifies the right edge. | markings: The
                        straight arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may proceed straight ahead. Lane changes to the
                        left are prohibited by the solid yellow line, and moving to the right is restricted by
                        the road edge.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 774, 13.26 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or large junction ahead. The car is
                        positioned in one of the middle lanes. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white broken
                        lines on both sides, indicating I am in a middle lane. | roles: The white broken lines
                        correctly identify as crossable lane lines between lanes of the same direction. |
                        markings: The straight arrow is consistent with the lane's role as a through lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white line on the left [CN-5.2.1-2].
Step 6  change_right    allowed (correct): Allowed by the broken white line on the right [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow marking [CN-5.13.1].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or marking.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change lanes to the left
                        or right as the lane markings are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 890, 7.03 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be a dedicated turn lane or a lane with specific guidance markings. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the sidewalk/curb area on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A large white arrow pointing straight and to the left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left and a yellow edge line on the right. | roles: The white lane
                        line and yellow edge line fit the roles of a lane line and a right-hand edge line
                        respectively. | markings: The straight-left arrow is consistent with the lane's
                        position and the surrounding markings. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_left: The arrow indicates that the lane allows for both straight ahead
                        and left turn movements. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1,
                        表1, page 27]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe ['turn_left'], citation unlisted, contradictions []
Tokens                  in 7595, out 916, 44.56 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bridge overhead in the distance. The car is positioned
                        in one of the middle lanes of a multi-lane roadway. (lanes 4, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: White dashed lines correctly identify
                        as crossable lane lines between lanes of the same direction. | markings: The straight
                        arrow is consistent with the lane's role and the dashed boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white line on the left [CN-5.2.1-2]
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white line on the right
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You are permitted to change
                        lanes to the left or right as needed, as both boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 856, 7.35 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road or highway with a bridge ahead. The road is bounded by
                        concrete walls on both sides. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway, next to a concrete
                        barrier/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane appears clear of specific arrows or text.; area:two_way_left_turn_lane
                        (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white dashed
                        line on my left and the white solid edge line on my right. | roles: The white dashed
                        line on the left correctly identifies a lane-change possibility, and the white solid
                        line on the right correctly identifies the road edge. | markings: No markings were
                        observed in my lane, which is consistent with the lack of specific movement
                        restrictions. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: No rule applies as no crosswalk was identified.
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and
                        physical curb.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or area is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane to your left. Do not move to the
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'line:crosswalk'], missed []), actions False, unsafe
                        [], citation accepted, contradictions []
Tokens                  in 7595, out 760, 7.5 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or large crossing ahead. My car is in one
                        of the middle lanes. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane itself appears clear of specific arrows or text.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        identify lane-to-lane boundaries in a same-direction flow. | markings: No specific
                        markings are clearly visible in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane on my
                        right. [[CN-6.2.1]]
Step 6  change_left     allowed (correct): allowed by the broken white line on the left [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane to your left. Changing into the lane
                        to your right is prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 811, 9.8 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a narrow paved path or lane, possibly a service road or a pedestrian-
                        adjacent path, passing under a large overpass. A white van is ahead in the same lane.
                        (lanes 1, mine 1, full)
Step 2  Left            The left side of the lane is bounded by a low hedge and a dirt/grass area with no
                        painted line.
                        none none, curb no, edge_line, evidence full
Step 2  Right           The right side of the lane is bounded by a solid red wall and a concrete curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count and position are consistent with the boundaries (no lines,
                        just physical edges). | roles: The boundaries are correctly identified as edges of the
                        roadway. | markings: No markings were observed in the lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: No marking governs this action.
Step 5  Rule            right_boundary: No marking governs this action.
Step 6  change_left     not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  change_right    not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Proceed straight ahead in your current lane. No lane changes or turns are indicated by
                        markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation none, contradictions []
Tokens                  in 7595, out 542, 9.34 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection. The sun is high, creating
                        significant glare. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line and a metal fence/railing separate my lane from the
                        sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the white solid line/fence on my right. | roles: The white dashed
                        line correctly identifies a crossable lane line, and the white solid line/fence
                        correctly identifies the right edge of the roadway. | markings: The straight arrow is
                        consistent with the lane's path toward the intersection. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and physical fence
                        [CN-5.4.3]
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the left lane if necessary, but you must not move to the right as it is bounded by a
                        solid line and a physical barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'go_straight'], citation accepted, contradictions []
Tokens                  in 7595, out 884, 7.53 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, passing under an overpass. The road
                        ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and a lane line on my right. | roles: The white dashed line on the
                        left and white solid line on the right are consistent with lane-line roles. |
                        markings: No markings were observed, which is consistent with the clear lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the right lane.
                        [[CN-6.2.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which is
                        a no-crossing lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): No markings govern this action, and the lane is not a
                        special lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change into the left lane as it is marked with a broken white line. You are
                        prohibited from changing into the right lane due to the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 666, 4.34 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear blue sky. The road ahead is straight,
                        and there is a green overhead sign in the distance. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle with the number 60 inside is painted in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the white solid line on my right. | roles: The white dashed line
                        on the left is a crossable lane line, and the white solid line on the right is a road
                        edge line. | markings: The speed limit marking is consistent with the lane's purpose.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 5  Rule            text:speed_limit: The marking indicates a maximum speed limit of 60 for this lane.
                        [[CN-5.14.2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line, which is an edge line.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken, but you should not move to the
                        right as it is the edge of the roadway. Maintain a speed of 60 or below as indicated
                        by the pavement marking.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 725, 7.23 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus and a van in the adjacent lanes. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white solid lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 608, 6.48 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear blue sky. The road ahead is straight
                        with several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; area:left_turn_waiting (full): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (full): No markings are visible in my lane.; area:grid
                        (full): No markings are visible in my lane.; area:channelizing (full): No markings are
                        visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white broken lines on both sides. | roles: The white broken lines correctly
                        identify as lane lines between lanes of the same direction. | markings: No markings
                        were observed, which is consistent with a standard highway lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane to my right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You are permitted to change lanes to
                        the left or right as needed, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 7595, out 824, 11.28 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or arterial road with a clear view ahead. The road continues
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        on the left correctly identifies a lane-change possibility, and the white solid line
                        on the right correctly identifies the road edge. | markings: No markings were observed
                        in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change into the lane on the
                        left. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which marks the road's end [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. You should stay within the roadway and
                        not move past the right edge line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 651, 14.98 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky and bright sunlight. The road
                        ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        identify lane-to-lane and lane-to-edge boundaries. | markings: No markings were
                        observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 628, 6.95 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway under an overpass. Ahead, the road
                        continues straight with multiple lanes visible. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white lane line is on my right. | roles: The
                        yellow solid line on the left correctly identifies a center line (separating opposing
                        traffic), and the white solid line on the right identifies a lane line. | markings: No
                        markings were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 674, 6.74 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The sun is low in the sky,
                        creating a hazy atmosphere. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: No markings are
                        present, which is consistent with a standard highway lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line (CN-6.2.1).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        (CN-6.2.1).
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 787, 40.63 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead power lines and a railway line to the
                        left. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line on the left correctly identifies a crossable lane line, and the white
                        solid line on the right correctly identifies a road edge line. | markings: No markings
                        were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: No rule applies as no stop line is present.
Step 6  change_left     allowed (correct): The broken white line on the left allows a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line on the right prohibits
                        moving onto the shoulder or beyond.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_applicable: No markings govern this action.
Step 6  turn_right      not_applicable: No markings govern this action.
Step 6  u_turn          not_applicable: No markings govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary. You should stay within the lane and
                        not move toward the right edge.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 656, 10.79 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a barrier on the left and a wide shoulder/curb
                        area on the right. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        shoulder or exit area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): A white dashed line is visible between the lane to my
                        right and the lane further right.; area:grid (full): A white grid pattern is visible
                        on the far right edge of the roadway.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane/shoulder. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            area:grid: Stopping in the grid area is prohibited. [[CN-6.8.1-2] [mandatory] GB
                        5768.3-2025, section 6.8.1, 6.8.2, page 53]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid', 'line:crosswalk'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7595, out 745, 6.89 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a gantry overhead. The road ahead is straight.
                        (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A white arrow pointing straight ahead is in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white dashed lines correctly
                        identify as crossable lane lines between lanes of the same direction. | markings: The
                        straight arrow is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane allows for straight ahead
                        travel or a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white line on the left
                        [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white line on the right [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in the lane [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the arrow in the lane [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane that allows for straight travel or a U-turn. You may change
                        lanes to the left or right as needed, as both boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 7595, out 869, 7.53 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. The road ahead is a straight
                        stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly identify lane-
                        to-lane boundaries. | markings: No markings were observed in the lane. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane to my
                        right. [[CN-6.2.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): The right boundary is a solid white line, which is a no-crossing
                        lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may change into the lane to your left,
                        but you are prohibited from changing into the lane to your right. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 645, 5.23 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on both sides. The road ahead appears
                        to be a straight stretch with no immediate intersection visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly identify lane
                        boundaries for traffic in the same direction. | markings: No markings were observed in
                        the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the right lane.
                        [[CN-6.2.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which is
                        a no-crossing lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action.
Step 6  turn_right      not_applicable: No markings in my lane govern this action.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is visible or marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary, but you are prohibited from changing
                        into the right lane. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 652, 5.94 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with an upcoming intersection or
                        exit. My car is in a lane that appears to be a through lane or a lane leading to a
                        turn. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:left (full): A white arrow pointing left is in the lane to my left.; arrow:right
                        (full): A white arrow pointing right is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify lane boundaries
                        and the right edge. | markings: The straight arrow in my lane is consistent with the
                        lane's role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['text:speed_limit']), actions
                        False, unsafe [], citation in_pack_not_accepted, contradictions ['turn_left
                        not_applicable although an arrow shows it', 'turn_right not_applicable although an
                        arrow shows it']
Tokens                  in 7595, out 741, 19.12 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. There are overhead traffic signals
                        and several vehicles in the vicinity. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line on the left and a white lane line on the right. | roles: The yellow
                        double solid line correctly identifies a center line (opposing traffic), and the white
                        solid line correctly identifies a lane line (same direction). | markings: The straight
                        arrow is consistent with the lane's role and boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: The guide arrow indicates the direction of travel is straight
                        ahead or to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
                        [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the single solid white lane line
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the straight or right arrow [CN-5.13.1]
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 877, 8.11 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a main
                        thoroughfare with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a green-painted
                        curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the white solid line on my right. | roles: The white dashed line
                        on the left correctly identifies a lane-change possibility, and the white solid line
                        on the right correctly identifies the edge of the roadway. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose and the surrounding boundaries.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the lane to your left, but you must not move to the right beyond the solid white edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 714, 43.41 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a tram system. Ahead, there is a clear
                        roadway with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the tram lane on the right.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        my left and the yellow line on my right. | roles: The white line on the left correctly
                        identifies a lane-line, and the yellow line on the right correctly identifies a
                        special lane boundary (tram lane). | markings: The straight arrow is consistent with
                        the lane's role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid yellow line and tram context prohibit entering the tram lane
                        on the right. [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1, page 54]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow special lane line
                        [CN-6.9.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 785, 6.16 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear sky. The road ahead appears to be a straight
                        stretch with an intersection or junction further ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        one-way or restricted lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        my left and yellow line on my right. | roles: The white line on the left and yellow
                        line on the right are consistent with standard lane markings for a multi-lane road in
                        China. | markings: No markings were observed in my lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing from my side into the right
                        lane. [[CN-6.1.4] [mandatory] GB 5768.3-2025, section 6.1.4, page 44]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:stop'], missed []),
                        actions False, unsafe [], citation unlisted, contradictions ['go_straight decided from
                        an arrow that cannot be read', 'go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 7595, out 868, 10.68 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection or a transit hub.
                        There is a subway station structure on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        transit or special lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on the left and a yellow line on the right. | roles: The white line on the
                        left correctly identifies a lane-line, and the yellow line on the right correctly
                        identifies a boundary with a special lane or opposing flow (though here it's a special
                        lane). | markings: The straight arrow is consistent with the lane's role and the
                        surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow line indicates a special lane (likely a bus lane) that I am
                        prohibited from entering. [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1, page
                        54]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the yellow line marking a special lane
                        [CN-6.9.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 811, 6.23 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the left and a
                        sidewalk/curb on the right. Ahead is a clear stretch of road with several lanes of
                        traffic. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the right edge of the roadway, next to a sidewalk and trees.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with a white lane line
                        on my left and a yellow edge line on my right. | roles: The white lane line on the
                        left and yellow edge line on the right are consistent with standard Chinese road
                        markings. | markings: The straight arrow in my lane is consistent with the lane's role
                        as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The yellow edge line marks the boundary of the roadway and prohibits
                        crossing to the right. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the yellow edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the straight or right arrow [CN-5.13.1]
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 717, 10.89 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The sun is low in the sky,
                        creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; arrow:straight
                        (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: no marking governs this action [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['go_straight decided from an arrow that cannot be read']
Tokens                  in 7595, out 622, 5.53 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center. The road appears to be a straight
                        stretch with an intersection or crossing ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed, which is consistent with the lack of specific movement restrictions in the
                        current view. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line', 'text:stop'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions ['go_straight decided from an arrow
                        that cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking
                        in my lane requires']
Tokens                  in 7595, out 801, 15.48 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane heading straight towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 737, 8.4 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban intersection with a crosswalk. My car is
                        approaching the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible at the intersection.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The stop line is
                        consistent with an intersection approach. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right
Step 6  go_straight     allowed (contested, label not_determined): allowed as no markings prohibit it and it
                        is the default for a lane without specific turn arrows
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight through the intersection. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 749, 15.27 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road in China, approaching a large intersection
                        with a prominent overhead sign. My car is in a lane heading straight toward the
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        dedicated bus lane or a special lane.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        my left and the yellow line on my right. | roles: The white line on the left is a
                        standard lane line; the yellow line on the right indicates a special lane (bus lane).
                        | markings: The straight arrow is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The bus lane line prohibits vehicles other than buses from entering
                        the lane on the right. [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1, page 54]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the bus lane line [CN-6.9.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left are
                        prohibited by the solid white line, and the lane to your right is a reserved bus lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 802, 7.03 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or junction ahead. The road is lined
                        with buildings on the left and trees on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on the left and a yellow line on the right. | roles: The white line on the
                        left and yellow line on the right are consistent with lane markings for a multi-lane
                        road in China. | markings: The straight arrow is consistent with the lane's role. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the lane to the right.
                        [[CN-6.1.4]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        (CN-6.2.1)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line on the right
                        (CN-6.1.4)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to go straight ahead, but lane changes
                        to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 686, 6.7 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway with overhead wires, likely a BRT or light rail
                        corridor. Ahead, the road continues straight with several lanes visible. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Two parallel solid yellow lines are painted in the
                        center of the road, separating the lanes.; line:stop_yield (insufficient): No arrows,
                        words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the yellow lines on both sides. | roles: The yellow lines correctly indicate
                        separation of traffic flows in the same direction (as per the context of a multi-lane
                        corridor). | markings: The markings in the center are actually lane dividers, not
                        stop-yield lines; I will treat them as lane lines. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white/yellow line prohibits crossing from the side of the
                        solid line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white/yellow line prohibits crossing from the side of the
                        solid line. [[CN-6.2.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow left boundary line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 684, 6.58 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 662, 10.07 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection with an overpass.
                        My car is in a lane that appears to be one of several lanes heading straight through
                        the intersection. (lanes 4, mine 3, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        in my lane is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 749, 7.01 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in one of
                        the central lanes. (lanes 4, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white broken lines on both sides. | roles: The white broken lines correctly
                        identify as lane lines between lanes of the same direction. | markings: The straight
                        arrow is consistent with the lane's role and the surrounding markings. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        allows lane changes [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows lane changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): The lane contains a straight arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You are permitted to change
                        lanes to the left or right as needed, as both boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 700, 7.12 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a bus on the right and a fence on the
                        left. Ahead, there is a wide intersection or open area with several lanes of traffic.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify lane boundaries
                        for traffic in the same direction. | markings: The straight arrow is consistent with
                        the lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the straight or right arrow marking
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 930, 13.93 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching a large intersection with a
                        pedestrian crossing. My car is in one of the central lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible ahead of my lane at the
                        intersection.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The stop line is
                        consistent with the approach to an intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it, but must
                        stop at the stop line
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that prohibits lane changes to the left or right due to the solid
                        white lines. You must come to a complete stop at the white stop line before proceeding
                        through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7595, out 776, 14.56 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the central
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead is visible in my
                        lane.; arrow:straight_left (full): A white arrow pointing straight ahead is visible in
                        the lane to my left.; arrow:straight_right (full): A white arrow pointing straight
                        ahead is visible in the lane to my right.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white dashed
                        lines on both sides. | roles: White dashed lines correctly identify lane-to-lane
                        boundaries for same-direction traffic. | markings: The straight-ahead arrows in my
                        lane are consistent with the dashed boundaries allowing lane changes. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_left: The arrow indicates that my lane allows for both straight ahead
                        and left turn movements. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white line on the left [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white line on the right [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed by the straight-left arrow [CN-5.13.1]
Step 6  turn_left       allowed: allowed by the straight-left arrow [CN-5.13.1]
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn left from your current lane. Lane changes to
                        the left or right are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_left', 'arrow:straight_right'], missed []), actions True, unsafe [],
                        citation accepted, contradictions ['turn_right not_applicable although an arrow shows
                        it']
Tokens                  in 7595, out 957, 8.13 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is wide with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/pedestrian area on
                        the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and left.;
                        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway and prohibits
                        crossing onto the sidewalk. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_left: The arrow indicates that my lane allows for both straight ahead
                        and left turn movements. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane allows for straight ahead movement.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): The broken white lane line allows for a lane change
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): The solid white edge line and curb prohibit moving onto the
                        sidewalk [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): The guide arrows in my lane allow for straight ahead
                        movement [CN-5.13.1].
Step 6  turn_left       allowed: The guide arrow in my lane allows for a left turn [CN-5.13.1].
Step 6  turn_right      not_applicable: No marking governs this action, and no arrow allows it.
Step 6  u_turn          not_applicable: No marking governs this action, and no arrow allows it.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible to the left of
                          my lane.
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn left from your current lane. A lane change to the
                        left is permitted as the line is broken, but you must not move to the right onto the
                        sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'arrow:straight_left'], missed ['text:other']), actions True,
                        unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 796, 11.28 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly identify lane-
                        to-lane boundaries in the same direction. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the right lane.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the left lane. Changing into the right
                        lane is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 669, 9.55 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a median and a sidewalk on the right.
                        Ahead, there is a clear lane for motor vehicles and a separate lane for
                        bicycles/pedestrians. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a median strip on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a bicycle/pedestrian lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles; the left
                        boundary is a median edge and the right is a lane edge. | roles: The white solid lines
                        correctly function as edge lines for the motor vehicle lane. | markings: The straight
                        arrow is consistent with the lane's purpose and the surrounding boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: No specific rule for this white solid edge line is provided, but it
                        marks the boundary of the motor lane. [null]
Step 5  Rule            right_boundary: No specific rule for this white solid edge line is provided, but it
                        marks the boundary of the motor lane. [null]
Step 5  Rule            arrow:straight: The straight arrow indicates that the lane is intended for straight-
                        ahead travel. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white line and the median.
Step 6  change_right    prohibited (correct): prohibited by the solid white line.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white edge lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 664, 6.64 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides and trees lining the sidewalk. The road
                        ahead appears to be a straight continuation of the current street. (lanes 2, mine 2,
                        full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white line marks the right edge of my lane, next to a sidewalk and trees.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with a yellow center
                        line on my left and a white edge line on my right. | roles: The yellow solid line
                        correctly identifies a center line separating opposing traffic, and the white line
                        correctly identifies the right edge. | markings: The straight arrow is consistent with
                        the straight road ahead and the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the opposite lane.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the direction of
                        travel. [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the curb and edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow and lack of prohibiting
                        markings
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of the roadway. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left due to the solid yellow center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 765, 10.23 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the opposing traffic flow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; area:left_turn_waiting (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.; area:grid (insufficient): No markings are visible in
                        my lane.; area:channelizing (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white lane line is on my left and a yellow center line is on my right. | roles: The
                        white line on the left is a lane line and the yellow line on the right is a center
                        line, which is consistent with Chinese traffic rules. | markings: No markings were
                        observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The single solid yellow line prohibits crossing into the opposing
                        traffic flow. [[CN-6.1.4] [mandatory] GB 5768.3-2025, section 6.1.4, page 44]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_yield', 'line:yield_line'], missed []),
                        actions False, unsafe [], citation unlisted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 848, 7.4 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection with a pedestrian crossing.
                        The road is wide and appears to be a main thoroughfare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the opposing traffic flow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.; line:stop_line (full): A white stop line is visible at the end of my lane
                        before the intersection.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white lane line
                        on the left and a yellow center line on the right. | roles: The white line on the left
                        correctly identifies a same-direction lane, and the yellow line on the right correctly
                        identifies a center line. | markings: The straight arrow and stop line are consistent
                        with a through-lane configuration. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the opposing traffic
                        flow. [[CN-6.1.4]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where the vehicle must stop before entering the
                        intersection. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  go_straight     stop_first (WRONG, label allowed): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through-lane. You may proceed straight ahead but must come to a complete
                        stop at the white stop line before entering the intersection. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 783, 7.57 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. A bus is ahead in the
                        center lane. (lanes 3, mine 3, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white line marks the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count is 3. My lane is the rightmost (3). The left boundary is a
                        yellow line (center line) and the right is a white line (edge line), which is
                        consistent. | roles: The yellow line correctly identifies a center line separating
                        opposing traffic (or a left-turn lane), and the white line correctly identifies the
                        right edge. | markings: No markings were observed in my lane. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [CN-6.1.1] "The no-crossing centre line has three forms: double solid yellow, broken-
                        solid yellow and single solid yellow. It separates opposing traffic flows and
                        prohibits"
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 624, 130.84 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane elevated roadway or bridge with buildings visible on both
                        sides. Ahead, the road continues straight. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A metal railing and a concrete curb form the right edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        a white lane line on my left and a curb/railing on my right. | roles: The white solid
                        line correctly identifies a lane-line, and the curb/railing correctly identifies an
                        edge line. | markings: No markings are present, which is consistent with the clear
                        path ahead. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The edge line marks the boundary of the roadway. [CN-5.4.3] "An edge
                        line on the right side of the direction of travel shall be white, and an edge line on
                        the left side of the direction of travel shall be yellow; a motor/"
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line (CN-6.2.1)
Step 6  change_right    prohibited (correct): prohibited by the curb/edge line (CN-5.4.3)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left are
                        prohibited by the solid white line, and the right side is bounded by a physical
                        barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7595, out 792, 10.28 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide boulevard layout. Ahead is a long stretch of road
                        with a bike lane on the right and a grassy area on the left. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-painted bike lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the red area to the right of
                        my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white solid lines
                        correctly identify lane boundaries for traffic in the same direction. | markings: The
                        bike symbol is in the adjacent lane, not my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the bike lane on the
                        right. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            symbol:bike: The bike symbol indicates the adjacent lane is for bicycles. [no marking
                        governs this action]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 723, 6.88 s
```
