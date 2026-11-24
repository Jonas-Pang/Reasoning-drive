# Reasoning of lane run 20261117_222453_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        right. My lane has no arrows.; no_turn:left (insufficient): Photo 1 shows a white
                        left-turn arrow in the lane to my right. My lane has no arrows.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on my left and a yellow solid
                        line on my right. | roles: The white dashed line on the left is a lane line, and the
                        yellow solid line on the right is an edge line. | markings: There are no markings in
                        my lane, and the lane to my right has a left-turn arrow. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving to the right onto the
                        sidewalk or shoulder.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Do not attempt to move to the
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 891, 7.4 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to continue
                        straight with a slight curve or intersection in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid yellow line clearly.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white dashed line is on my left (lane_line) and a
                        yellow solid line is on my right (edge_line). | roles: The white dashed line on the
                        left fits the role of a lane_line, and the yellow solid line on the right fits the
                        role of an edge_line. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving to the right onto the curb
                        or shoulder.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change to the left
                        lane if needed, but you are prohibited from turning left, right, or making a U-turn
                        from this lane. Do not move to the right onto the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 919, 7.69 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with a slight curve or intersection further ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a lane line on my left and an edge line on my right. | roles: The
                        white dashed line on the left is a lane line, and the solid white line on the right is
                        an edge line. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        sidewalk or shoulder.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if necessary, but you must not move to the right as it is bounded by a solid edge
                        line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 874, 7.76 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. My car is in a lane
                        bounded by a metal fence on the left and a white line on the right. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a metal fence and a concrete curb on the left. Photo 2 shows a solid
                        white line painted on the road next to the curb/fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is solid near the car and becomes dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a white curved line in the middle of my lane.
Step 4  Cross-check     close_up: The right boundary is solid near the car (Photo 2) and dashed further ahead
                        (Photo 1). Photo 2 decides the near line, Photo 1 decides the far line. Corrected
                        right_boundary pattern to dashed as it is the primary state for the lane. | position:
                        The lane count (3) and my position (1) agree with the left edge line (fence/curb) and
                        the right lane line. | roles: The white edge line on the left and white lane line on
                        the right fit the roles of edge_line and lane_line. | markings: The curved line is a
                        decorative or directional symbol and does not conflict with boundaries. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The edge line and curb prohibit moving to the left.
Step 5  Rule            right_boundary: The dashed lane line allows changing into the lane to the right.
Step 5  Rule            symbol:other: The curved line does not govern specific movements.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You can proceed straight or move into the lane to your
                        right. Do not attempt to move left as there is a physical barrier and edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 902, 8.26 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. The road ahead is
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is solid and white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is solid and white.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        markings are present, which is consistent with the straight road ahead. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 770, 6.63 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line marking the lane
                        boundaries.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with having a lane line on both the left and right. | roles:
                        The white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No specific arrows or words are visible in my lane to
                        contradict the boundary roles. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 799, 7.3 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median or barrier on the left and a sidewalk/fence on
                        the right. Ahead, there is a wide intersection or open area with multiple lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a dashed yellow line side by side on the right.
                        Photo 2 shows a solid yellow line and a dashed yellow line side by side next to my
                        car. Further ahead in Photo 1, the line appears to be a solid yellow line.
                        yellow solid_dashed (near line solid), curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
                        Photo 1 shows a white arrow pointing left in the lane to my left.; arrow:right (full):
                        Photo 2 shows a white arrow pointing right in the lane to my right. Photo 1 shows a
                        white arrow pointing right in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left lane line and the right edge line. | roles: The white
                        dashed line on the left is a lane line; the yellow solid-dashed line on the right is
                        an edge line. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits moving to the right onto the shoulder
                        or sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow near_line of the
                        right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change to the left lane if
                        needed, but you are prohibited from moving to the right. Use this lane to proceed
                        straight through the upcoming area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed []), actions True, unsafe [], citation None,
                        contradictions ['turn_right prohibited although an arrow shows it']
Tokens                  in 3797, out 993, 7.79 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure overhead. The road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to my right. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line further ahead in my
                        lane, possibly a lane-change indicator or just a continuation of the dashed line.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on my left and a white solid
                        line on my right. | roles: The white dashed line on the left correctly identifies a
                        lane-change possibility, and the white solid line on the right correctly identifies a
                        lane-change prohibition. | markings: No specific arrows or words are visible to
                        contradict the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for a lane change to the left.
Step 5  Rule            right_boundary: The white solid line prohibits a lane change to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes to the left. Changing lanes to the right is
                        prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3797, out 821, 7.66 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bridge or overpass ahead. The road is wide with clear
                        lane markings and a barrier on the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:two_way_left (partial): Photo 1 shows a left-turn arrow in the lane to the left
                        of my lane. Photo 1 shows a right-turn arrow in the lane to the right of my lane.;
                        arrow:merge_left (partial): Photo 1 shows a left-turn arrow in the lane to the left of
                        my lane.; arrow:merge_right (partial): Photo 1 shows a right-turn arrow in the lane to
                        the right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        arrows in adjacent lanes are consistent with the lane layout. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_left', 'arrow:merge_right', 'arrow:two_way_left'], missed []), actions
                        False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 903, 7.12 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be a dedicated bus lane or a lane with specific markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating my lane from the lane to my right. Photo
                        2 shows this solid yellow line clearly.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show large Chinese characters and a bus symbol
                        painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white line on the left and yellow line on the right. | roles:
                        The white line on the left and yellow line on the right correctly function as lane
                        boundaries. | markings: The bus markings indicate this is a dedicated lane, which is
                        consistent with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            text:bus: This lane is reserved for buses only.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  This is a bus-only lane. You should stay in your lane and proceed straight; lane
                        changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 833, 6.63 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the right. Ahead, there is
                        a crosswalk and a junction area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line next to
                        the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows a solid yellow line next
                        to the car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my
                        lane.; line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white line on the left separates me from another
                        lane, and a yellow line on the right separates me from a special lane/curb area. |
                        roles: The white line on the left is a lane line, and the yellow line on the right is
                        a lane line (separating from a special lane). | markings: The straight arrow in my
                        lane is consistent with the lane's purpose and the crosswalk ahead. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane on the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may proceed straight but
                        are prohibited from changing lanes or turning. Be prepared to stop for pedestrians at
                        the upcoming crosswalk.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3797, out 907, 7.7 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a metal
                        barrier on the right. Ahead, there is a gantry with overhead signs and a tunnel
                        entrance or underpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to its left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to its right. Photo
                        2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a yellow arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 840, 7.28 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be a center line or
                        edge line. Photo 2 shows a solid yellow line next to my lane. Further ahead in Photo
                        1, this line remains solid yellow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow in my lane pointing straight
                        ahead. Photo 1 shows the same arrow.; arrow:straight (full): Photo 2 shows a large
                        white arrow in the lane to my right pointing straight ahead. Photo 1 shows the same
                        arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a yellow solid
                        line on the right. | roles: The white dashed line on the left correctly identifies a
                        lane line, and the yellow solid line on the right correctly identifies a center line
                        separating my lane from the opposite direction or a restricted area. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but you are prohibited from changing lanes to the right due to the
                        solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 934, 8.1 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in a lane that
                        appears to lead toward a turn or straight movement at the intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating my lane from the lane to my right. Photo
                        2 shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 1 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 1 shows a white arrow pointing right in the lane to
                        my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white line on the left and yellow line on the right. | roles:
                        The white line on the left and yellow line on the right correctly function as lane
                        lines. | markings: The straight arrow in my lane is consistent with the lane's purpose
                        and the surrounding lane arrows. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed []), actions True, unsafe [],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 3797, out 911, 8.16 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass. There are three lanes of traffic
                        moving in the same direction ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to my right. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line is on my left and a white solid
                        line is on my right. | roles: The white dashed line on the left and white solid line
                        on the right fit the roles of lane lines. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose as a through lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow
Step 6  turn_left       prohibited: prohibited by the straight arrow
Step 6  turn_right      prohibited: prohibited by the straight arrow
Step 6  u_turn          prohibited: prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change to the left lane if
                        needed, but changing to the right is prohibited by the solid line. Do not attempt to
                        turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 875, 8.06 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in a lane heading
                        straight toward the intersection. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which then transitions into a solid
                        white line bordering a curb/median. Photo 2 shows a solid white line next to my car.
                        Further ahead in Photo 1, the line remains solid white before the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows the arrow clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with a white dashed line on the left and a solid white line/curb on the
                        right. | roles: The white dashed line on the left correctly functions as a lane line,
                        and the solid white line on the right correctly functions as an edge line. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose and the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if necessary, but you are prohibited from turning left, right, or making a U-turn
                        from this lane. Do not move to the right as there is a solid line and curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 930, 8.66 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows the
                        solid white line and the curb clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a dashed line on my left separates me from another lane,
                        and a solid line/curb on my right marks the edge of the roadway. | roles: The white
                        dashed line on the left is a lane line, and the white solid line with a curb on the
                        right is an edge line. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the shoulder
                        or sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right_boundary and curb
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change to the left
                        lane if needed, but you must stay within your lane and cannot turn left, right, or
                        make a U-turn from this position.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3797, out 901, 8.15 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane heading
                        straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight movement.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        through the intersection and avoid changing lanes, as the solid white lines on both
                        sides prohibit lane changes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 816, 7.41 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. There is a metal fence on the left
                        and a sidewalk with trees on the right. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (2) agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The straight arrow indicates that this lane is intended for going
                        straight ahead.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right as needed, but you should not attempt to turn left, turn right, or make
                        a U-turn from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 856, 6.63 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the left lane. Photo 2 shows a
                        white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the right lane. Photo 2 shows a
                        white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that this lane is for going straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to go straight ahead. Lane changes to the left or right are permitted as
                        the boundaries are dashed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3797, out 832, 7.76 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in a lane that
                        appears to be a dedicated turn lane or a lane leading to a turn. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white solid line separating my lane from the lane to the left. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to the right. Photo
                        2 shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles; I am in the middle of three lanes. | roles: The white
                        solid lines correctly define the boundaries of my lane. | markings: The left-turn
                        arrow in my lane is consistent with the lane's purpose and the surrounding markings. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:left: The arrow allows turning left and prohibits going straight, turning right,
                        or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to turn left at the upcoming intersection. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight']), actions False, unsafe ['turn_left'],
                        citation None, contradictions []
Tokens                  in 3797, out 826, 7.54 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with specific
                        directional markings. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line separating my lane from a sidewalk/fence area on the
                        left. Photo 2 shows a white solid line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to the right. Photo
                        2 shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a large white arrow in my lane pointing
                        straight ahead and slightly to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (edge line on left, lane line on right). | roles: The
                        white solid lines correctly define the edge and the adjacent lane. | markings: The
                        straight-left arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid edge line prohibits moving to the left onto the
                        sidewalk/fence area.
Step 5  Rule            right_boundary: The solid lane line prohibits changing into the lane on the right.
Step 5  Rule            arrow:straight_left: The arrow allows going straight or turning left, and prohibits
                        turning right or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. Lane changes to the
                        left or right are prohibited by the solid lines. Follow the arrow's guidance for your
                        intended movement at the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 838, 7.88 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight toward the intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a sidewalk/fence area. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across the lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left edge line, right lane line). | roles: The white
                        solid lines correctly define the edge and the adjacent lane. | markings: The stop line
                        is consistent with the intersection ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white edge line prohibits moving to the left onto the
                        sidewalk/fence area.
Step 5  Rule            right_boundary: The solid white lane line prohibits changing into the lane to the
                        right.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        entering the intersection.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of your direction. You must come to a full stop at the white
                        line before proceeding straight or turning at the intersection. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3797, out 837, 7.94 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching an intersection or a junction under a bridge. There are
                        multiple lanes of traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a divider before a sidewalk/curb. Photo 2 shows this solid white line
                        clearly next to a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large yellow arrow pointing straight ahead and
                        slightly to the right in my lane.; arrow:left (full): Photo 2 shows a large yellow
                        arrow pointing left in the lane to my left.; arrow:right (full): Photo 2 shows a large
                        yellow arrow pointing right in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left separates me from the
                        left lane, and a white line/curb on the right defines the edge. | roles: The white
                        solid lines correctly function as a lane line and an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. The left and right
                        arrows in adjacent lanes are consistent with their respective boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the left lane.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Do not attempt to change lanes
                        or turn left or right, as these actions are prohibited by the solid lines and the lane
                        markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe ['go_straight'],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 3797, out 959, 8.23 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk on the right.
                        The road continues straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the solid
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Proceed straight ahead as indicated by
                        the lane arrow.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 832, 7.42 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose and the
                        dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left or right as needed, but you should only proceed straight through the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3797, out 899, 7.8 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane that appears to
                        go straight through the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and white near the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white near the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the surrounding
                        lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight only. Do not attempt to change lanes
                        or turn at the upcoming intersection; proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 868, 7.85 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a large intersection ahead. My car is in a lane that
                        appears to be part of a complex intersection layout with yellow markings. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating my lane from the lane to my right. Photo
                        2 shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a large yellow grid/box pattern across the
                        intersection ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles; I am in a middle lane bounded by yellow lines on both
                        sides. | roles: The yellow solid lines correctly function as lane lines separating my
                        lane from adjacent lanes. | markings: The grid area is consistent with a 'no-blocking'
                        zone at an intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            area:grid: The grid area indicates a zone where vehicles should not stop.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes to the left or right are prohibited by the
                        solid yellow lines. Proceed straight through the intersection, ensuring you do not
                        stop within the yellow grid area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 843, 7.62 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide roadway and trees lining the sides. Ahead, the
                        road continues straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 shows a white diamond symbol in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white lane line is
                        on my right. | roles: The yellow solid line correctly identifies a center line, and
                        the white solid line correctly identifies a lane line. | markings: The diamond symbol
                        is a neutral marking and does not conflict with the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits changing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white lane line prohibits changing into the lane to the
                        right.
Step 5  Rule            symbol:other: The diamond symbol indicates a neutral zone and does not govern specific
                        movements.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a middle lane. You may proceed straight ahead, but lane changes to the left
                        or right are prohibited by the solid lines. No turn markings are present in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 844, 7.28 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street with an intersection ahead. There is a bus lane
                        or special lane to the left and a sidewalk to the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is solid and white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, and Photo 2 shows it is a solid white line.
                        Beyond that is a raised curb and sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large white left-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (3) agree with the boundaries: a white line on the left separates me from the middle
                        lane, and a white line/curb on the right defines the edge. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line. | markings: The left-turn arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:left: The arrow indicates that the lane is for turning left.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     prohibited (correct): prohibited
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to turn left at the upcoming intersection. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        None, contradictions []
Tokens                  in 3797, out 849, 8.24 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a concrete barrier on the left. Ahead, there is a truck
                        in the same direction and a white car in the adjacent lane to the right. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier on the left. Photo 2 shows a solid white line painted
                        on the road next to the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow painted in the lane to my
                        right.; arrow:right (full): Photo 1 shows a white right-turn arrow painted in the lane
                        to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a concrete barrier/edge line on the left and a lane
                        line on the right. | roles: The white solid lines correctly define the edge and the
                        lane divider. | markings: The arrows in the right lane indicate its specific
                        movements, while my lane has no specific arrow, implying straight movement. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The concrete barrier and solid line prohibit moving to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may proceed straight ahead, but lane
                        changes to the right are prohibited by the solid white line. The lane to your right is
                        designated for turns.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it', 'turn_right not_applicable although an
                        arrow shows it']
Tokens                  in 3797, out 862, 7.75 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a white
                        arrow pointing straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with long dashes and clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line with long dashes and clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right as needed, but you should only proceed straight through the
                        intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 851, 6.48 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the left lane. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the right lane. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the surrounding
                        lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the left lane.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the right lane.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel only. You may proceed straight
                        through the intersection but are prohibited from changing lanes or turning left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 818, 7.08 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        ahead appears to continue straight with no immediate intersection or ramp visible.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a white solid line next to the car. Further ahead in Photo 1,
                        the line remains solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a lane line on the left and an edge line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane line,
                        and the white solid line on the right correctly identifies an edge line. | markings:
                        No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving to the right onto the shoulder or
                        sidewalk.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you are
                        prohibited from moving to the right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 834, 7.83 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and parked cars on both sides. The road ahead
                        appears to be a straight stretch with a clear view of the horizon. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the lane to the left. Photo
                        2 shows the same double yellow line clearly, with the inner line being solid and the
                        outer line also solid.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this white line as a
                        solid line near the car, which remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a double yellow center line is on my left, and a white
                        lane line is on my right. | roles: The double yellow center line correctly identifies
                        the boundary with oncoming traffic, and the white line identifies the boundary with
                        the adjacent lane. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You are prohibited from
                        changing lanes to the left or right due to the solid markings. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 868, 7.75 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and power lines. The road ahead appears to be a
                        wide thoroughfare with multiple lanes in both directions. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows the same double yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to my right. Photo 2 shows a white dashed line
                        clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the double yellow center line on my left and a white dashed lane
                        line on my right. | roles: The double yellow center line correctly identifies the
                        boundary with oncoming traffic, and the white dashed line correctly identifies the
                        boundary with the adjacent lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change to the right
                        lane if needed, but you are prohibited from turning left, turning right, or making a
                        U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation None,
                        contradictions []
Tokens                  in 3797, out 841, 7.41 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left. The road ahead continues
                        straight with several lanes of traffic. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to my right. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white left-turn arrow in the lane to my left.
                        Photo 1 shows a white straight arrow in my lane. Photo 1 shows a white right-turn
                        arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (3) agree with the boundaries: a white dashed line on my left and a white solid line
                        on my right. | roles: The white dashed line on the left and white solid line on the
                        right fit the roles of lane lines. | markings: The straight arrow in my lane is
                        consistent with the lane boundaries and the surrounding lane arrows. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows for going straight ahead.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow in my lane
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow in my lane
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if needed, but lane changes to the right are prohibited by the solid line. Do not
                        attempt to turn left or right from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 906, 8.22 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left. The road ahead leads toward a
                        city area with buildings and a pedestrian area to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a straight arrow in my lane further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with the white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane boundaries and the
                        road layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 824, 7.5 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection or complex junction ahead. My car is
                        in one of the middle lanes. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway or a barrier. Photo 2 shows a white solid line and a raised curb/planter area
                        to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows white dashed lines separating the lanes
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a lane line on my left and an edge line on my right. |
                        roles: The white dashed line on the left is a lane line; the white solid line with a
                        curb on the right is an edge line. | markings: No specific arrows or words are visible
                        in my lane; the dashed lines ahead indicate lane separation. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the
                        sidewalk/planter.
Step 6  change_left     allowed (correct): left_boundary allows it
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Do not attempt to move to the
                        right as there is a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 833, 8.16 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with short dashes and gaps near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.;
                        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, right, or
                        making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right as needed, but you must proceed straight ahead at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions ['turn_left prohibited although an
                        arrow shows it']
Tokens                  in 3797, out 894, 7.0 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road approaching a large intersection with a
                        crosswalk. There are several vehicles and a motorcycle ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white crosswalk and a white stop line across
                        the lanes.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left and solid line on the
                        right fit the roles of lane lines. | markings: The stop line is consistent with the
                        intersection ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for a lane change to the left.
Step 5  Rule            right_boundary: The solid line prohibits a lane change to the right.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        entering the intersection.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line
Step 6  turn_left       stop_first: stop_first due to the stop line
Step 6  turn_right      stop_first: stop_first due to the stop line
Step 6  u_turn          stop_first: stop_first due to the stop line
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but changing to
                        the right is prohibited. You must come to a full stop at the white line before
                        proceeding through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3797, out 878, 7.65 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane heading towards
                        the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to my right. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left and white solid line on
                        the right are consistent with lane-line roles. | markings: The left-turn arrow in my
                        lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white solid line prohibits lane changes to the right.
Step 5  Rule            arrow:left: The arrow allows for a left turn and prohibits other movements.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid right boundary
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow
Step 6  turn_left       allowed: allowed by the left-turn arrow
Step 6  turn_right      prohibited: prohibited by the left-turn arrow
Step 6  u_turn          prohibited: prohibited by the left-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn at the upcoming intersection. Lane changes to the
                        left are permitted, but changing to the right is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 858, 7.34 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to my right, followed by a concrete barrier. Photo 2
                        shows the solid white line and the concrete barrier clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a lane line on my left and an edge line on my right. | roles: The
                        white dashed line on the left is a lane line, and the solid white line with a barrier
                        on the right is an edge line. | markings: The straight arrow in my lane is consistent
                        with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and barrier prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can continue straight or change to the left lane if
                        needed. Do not attempt to move to the right as there is a solid line and a barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 834, 6.45 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median on the left and a tree-lined shoulder on the
                        right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose and the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane and can proceed straight ahead. Lane changes to the left or
                        right are permitted as the boundaries are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 857, 6.83 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. Ahead, there is a lane with Chinese
                        characters and arrows. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to the left. Photo
                        2 shows the same yellow dashed line clearly.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be a bus lane
                        boundary. Photo 2 shows a solid yellow line and a white line side by side. Further
                        ahead in Photo 1, the line remains solid yellow.
                        yellow solid_dashed (near line solid), curb yes, special_lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 show a left-turn arrow in my lane.; text:bus
                        (full): Photo 1 and Photo 2 show Chinese characters in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow dashed line on the left and a solid yellow
                        line on the right. | roles: The yellow dashed line on the left is a lane line; the
                        solid yellow line on the right is a special lane line (bus lane). | markings: The
                        left-turn arrow and 'bus' characters are consistent with a bus-only lane or a lane
                        with specific turn restrictions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits changing into the lane on the right.
Step 5  Rule            arrow:left: The arrow allows for a left turn and prohibits going straight, turning
                        right, or making a U-turn.
Step 5  Rule            text:bus: The lane is reserved for buses only.
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     prohibited (contested, correct): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  This lane is marked for buses only and is designated for left turns. You should only
                        use this lane if you are a bus and intend to turn left; otherwise, stay in the general
                        traffic lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 965, 7.98 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a concrete barrier on the right and a wall on the left.
                        Ahead, there is a gantry with signs and a merging area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, followed by a metal guardrail. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a yellow solid line
                        on the right. | roles: The white dashed line on the left is a lane line, and the
                        yellow solid line on the right is an edge line. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line and guardrail prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the left lane.
                        Changing to the right is prohibited by the solid yellow line and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 877, 7.98 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete wall on the left and a guardrail on
                        the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to a yellow line. Further ahead in
                        Photo 1, the white line remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in either photo.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left lane line and right edge line. | roles: The white dashed
                        line on the left is a lane line; the solid white line on the right is an edge line. |
                        markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving to the right onto the shoulder or
                        beyond.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but do not move
                        to the right as the edge is solid. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 814, 6.76 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a barrier on the right and a guardrail on the left. The road
                        ahead appears to be a continuous highway with no immediate intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a guardrail. Photo 2 shows
                        a solid white line next to my car. Further ahead in Photo 1, the line remains solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a white dashed line on the left and a solid white
                        line/guardrail on the right. | roles: The white dashed line on the left correctly
                        identifies a lane line, and the solid white line on the right correctly identifies an
                        edge line. | markings: No markings are present in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and guardrail prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you are
                        prohibited from moving to the right. Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 828, 7.32 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or overpass with a concrete barrier on the left and a
                        curb/barrier on the right. The road ahead continues straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as a lane line on the left and an edge line on the right. |
                        markings: No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 767, 7.38 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with trees on both sides. The road ahead appears to be a
                        continuous stretch of highway with no immediate intersection or ramp visible. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with a dashed line on the left and a solid line on the right. |
                        roles: The white dashed line on the left correctly identifies a lane-change
                        possibility, and the white solid line on the right correctly identifies the edge of
                        the roadway. | markings: No markings are present in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving to the right beyond the roadway.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the left lane.
                        Changing to the right is prohibited as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 808, 7.92 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a guardrail on the right. The road ahead is
                        straight with no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead. A metal
                        guardrail is visible beyond the line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a dashed line on my left and a solid line/guardrail on my
                        right. | roles: The white dashed line on the left fits a lane_line role, and the solid
                        white line/guardrail on the right fits an edge_line role. | markings: No markings are
                        present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and guardrail prohibit moving to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Changing to the right is
                        prohibited by the solid line and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 827, 7.77 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a raised
                        embankment with a guardrail on the right. The road ahead curves slightly to the right.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a concrete barrier/curb on the right. Photo 2
                        shows a solid white line next to my car, and a concrete barrier further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a red-painted area in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from the left
                        lane, and a white line/curb on my right marks the edge. | roles: The white solid line
                        on the left is a lane line, and the white solid line with a curb on the right is an
                        edge line. | markings: The red grid area is centered in my lane and does not conflict
                        with the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 5  Rule            area:grid: The red grid area indicates a restricted zone, typically for keeping clear.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines and the curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 871, 7.43 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming intersection or exit area. My car
                        is in a lane that appears to be a through lane or a right-turn lane. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows the solid white line and the guardrail clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows the arrow clearly.; arrow:right (full): Photo 1 shows a white arrow
                        pointing right in the lane to my left. Photo 2 shows it clearly.; arrow:left (full):
                        Photo 1 shows a white arrow pointing left in the lane to the left of that one. Photo 2
                        shows it clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a dashed line on the left separates me from another lane,
                        and a solid line/guardrail on the right marks the edge. | roles: The white dashed line
                        on the left is a lane line, and the solid white line with a guardrail on the right is
                        an edge line. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and guardrail prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow allows for going straight ahead.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary and
                        guardrail
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       prohibited: prohibited by the straight arrow in my lane
Step 6  turn_right      prohibited: prohibited by the straight arrow in my lane
Step 6  u_turn          prohibited: prohibited by the straight arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but you are prohibited from moving to the right or making turns
                        from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed []), actions False, unsafe [],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 3797, out 1016, 9.12 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a green overhead sign. My car is in one of the middle lanes
                        traveling forward. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and my position as
                        2nd from the left are consistent with the white dashed lines on both sides. | roles:
                        The white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No markings are present to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left or right as the lane markings
                        are dashed. No specific turn markings are present in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 783, 7.08 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on both sides. The road ahead
                        appears to continue straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings are present, which is consistent with a standard highway lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you can proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 798, 7.23 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a sound barrier on the right. The road ahead is straight
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail and a
                        sound barrier. Photo 2 shows the solid white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left lane line and right edge line. | roles: The white dashed
                        line on the left is a lane line; the solid white line on the right is an edge line. |
                        markings: The straight arrow in my lane is consistent with the straight road ahead. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and guardrail prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change to the left lane.
                        Changing to the right is prohibited by the edge line and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 845, 6.96 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a curve ahead. My car is in a lane bounded by a concrete
                        barrier on the left and a painted line on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier and a metal railing on the left. Photo 2 shows a
                        concrete barrier with a metal railing and a white line painted on the concrete.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line with a dashed
                        pattern (broken line) next to it, but the line immediately to the right of my lane is
                        a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the
                        center of my lane.
Step 4  Cross-check     close_up: The right boundary is a solid white line next to my car (Photo 2), while a
                        dashed line is visible further to the right (Photo 1). Photo 2 decides the immediate
                        boundary. | position: The lane count and position are consistent. The left boundary is
                        an edge line (barrier), and the right boundary is a lane line separating me from the
                        lane to my right. | roles: The white solid line on the right correctly acts as a lane
                        line, and the barrier on the left acts as an edge line. | markings: The straight arrow
                        in my lane is consistent with the lane's purpose. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The concrete barrier prohibits moving to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight movement.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are blocked by a
                        barrier, and lane changes to the right are prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 893, 8.4 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road on a bridge or overpass with a bus directly ahead. The road is
                        bounded by metal guardrails on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with white lane lines on both sides. | roles: The white solid
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings are present, which is consistent with a standard through-lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 775, 7.21 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with overhead signs. My car is in one of the middle lanes
                        traveling forward. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose as a 'Through Lane' as indicated by the overhead signs. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-through
                        traffic.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change lanes to the left or
                        right as needed. Turning maneuvers are prohibited in this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 856, 7.71 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a median on the left and a sidewalk/parking area on the
                        right. Ahead, there is a slight curve or intersection area with a bridge structure
                        visible in the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised concrete curb/median on the left. Photo 2 shows the same raised
                        concrete curb/median.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a curb on the left and a dashed line on the right. |
                        roles: The curb acts as an edge line and the dashed line acts as a lane line. |
                        markings: No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The curb prohibits moving to the left.
Step 5  Rule            right_boundary: The dashed line allows changing into the lane on the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (WRONG, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight in your lane or change to the right lane if needed. Do not
                        attempt to move left as there is a physical curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3797, out 778, 6.99 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. Ahead, there is a
                        continuous stretch of road with a motorcycle and a car in the same direction. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a concrete median/barrier on the left. Photo 2 shows the concrete median
                        clearly.
                        other solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white painted line on the right. Photo 2 shows a solid white line on
                        the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white line dividing the two lanes on
                        the right side of the median.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a center line (median) is on my left and an edge line
                        is on my right. | roles: The center line (median) and edge line (solid white) fit the
                        roles correctly. | markings: No specific arrows or words are visible in my lane to
                        contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The concrete median prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white edge line prohibits moving onto the shoulder or
                        sidewalk to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are blocked by a
                        median, and the solid white line on your right prohibits moving onto the shoulder.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 792, 6.93 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. My car is in a lane
                        heading straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a yellow line on the left. Photo 2 shows a yellow
                        solid line next to a raised curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line with a dashed pattern. Further ahead in Photo 1, the line appears
                        to be a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: The right boundary is dashed in Photo 2 but appears solid further ahead in
                        Photo 1; Photo 2 decides the pattern next to the car (dashed), and Photo 1 shows it
                        becomes solid ahead. | position: The lane count (2) and my position (1) agree with the
                        left edge line and right lane line. | roles: The yellow solid line on the left is an
                        edge line; the white line on the right is a lane line. | markings: The straight arrow
                        in my lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow solid line and curb prohibit moving to the left.
Step 5  Rule            right_boundary: The white dashed line allows changing into the lane on the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane. You can proceed straight ahead or change into the right
                        lane. Changing to the left is prohibited by the curb and solid yellow line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 873, 7.8 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. My car is in a lane with a white line
                        on its right and a physical barrier/curb on its left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a metal fence on the left. Photo 2 shows a raised curb
                        and a metal fence on the left.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree: a
                        curb on the left and a white line on the right indicate the leftmost lane of the
                        direction. | roles: The white line on the right is a lane line, and the curb on the
                        left is an edge line. | markings: No markings are present to contradict the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The curb prohibits moving to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the curb and the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 772, 23.09 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. My car is in a lane
                        heading straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows a solid
                        white line and a raised curb next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:yield_line (full): Photo 2 shows a white dashed line in the middle of my lane,
                        and Photo 1 shows a white dashed line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from another
                        lane, and a white line/curb on the right marks the edge. | roles: The white solid line
                        on the left is a lane line, and the white solid line with a curb on the right is an
                        edge line. | markings: The dashed line in the middle of the lane is consistent with a
                        yield line or a lane-splitting marking in a specific context, but no arrows are
                        present. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            line:yield_line: The dashed line in the lane indicates a specific area or movement,
                        but does not restrict straight movement.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines and the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 888, 8.25 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. The road ahead
                        appears to be a straight stretch with a clear lane for my car. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to my car. There is a sidewalk and
                        trees beyond this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from another lane,
                        and a white line on my right marks the edge of the road. | roles: The white solid line
                        on the left is a lane line, and the white solid line on the right is an edge line. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may proceed straight, but
                        lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 866, 7.66 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        clear roadway with a car and a pedestrian visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, and a sidewalk/curb further right.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from another
                        lane, and a white line/curb on the right marks the edge. | roles: The white solid line
                        on the left is a lane line, and the white solid line on the right is an edge line. |
                        markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk or
                        area to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 807, 7.8 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bridge structure on the left and a tree-lined sidewalk
                        on the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to its left. Photo
                        2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to the car. Further ahead, it remains
                        solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with a dashed line on the left and a solid edge line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane line,
                        and the solid white line on the right correctly identifies an edge line. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose and the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       prohibited: prohibited by the straight arrow in my lane
Step 6  turn_right      prohibited: prohibited by the straight arrow in my lane
Step 6  u_turn          prohibited: prohibited by the straight arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change to the left lane.
                        Do not attempt to turn left, turn right, or move onto the sidewalk to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 899, 7.87 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a dedicated bicycle and scooter lane on a city street. Ahead, the lane
                        continues straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a large white arrow pointing straight ahead in
                        the center of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left lane-line, right edge-line). | roles: The white
                        solid lines and the curb correctly define the lane boundaries. | markings: The
                        straight arrow is consistent with the lane's purpose and boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in this lane. Lane changes to the left or right are prohibited
                        by the solid lines and the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3797, out 781, 6.31 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. Ahead, there is a
                        continuous flow of traffic and a clear roadway. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid yellow line next to my car on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in either photo.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The yellow line on my left separates me from another
                        lane, and the yellow line on my right marks the edge of the road. | roles: The yellow
                        color and solid pattern fit the roles of a lane line and an edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving onto the sidewalk or
                        shoulder to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 791, 7.39 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and trees on the left. Ahead, there is a clear
                        roadway with parked cars on the right and a bicycle/scooter lane or sidewalk area on
                        the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a lane to the left. Photo 2
                        shows a solid white line next to my car and a raised curb further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a lane to the right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The left boundary is an edge line (curb/solid white) and the right is a
                        lane line (solid white). | roles: The white solid lines correctly define the lane
                        boundaries. | markings: No markings are present in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white edge line prohibits changing into the area to the left.
Step 5  Rule            right_boundary: The solid white lane line prohibits changing into the lane to the
                        right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of the roadway. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3797, out 806, 7.78 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        large blue overhead sign with lane guidance and a speed limit sign. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a raised curb/barrier on the right. Photo 2
                        shows a solid yellow line next to a raised yellow curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line in the middle of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a white dashed line on my left and a yellow solid line/curb
                        on my right. | roles: The white dashed line on the left is a lane line; the yellow
                        solid line/curb on the right is an edge line. | markings: The white dashed line in the
                        center of my lane is a lane divider, not a stop/yield line. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may proceed straight or change to the left lane.
                        Do not attempt to move to the right as it is bounded by a solid yellow line and a
                        curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3797, out 845, 8.24 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a dashed line on the left and a solid line on the
                        right. | roles: The white dashed line on the left and solid line on the right are
                        consistent with lane-line roles. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow
Step 6  turn_left       prohibited: prohibited by the straight arrow
Step 6  turn_right      prohibited: prohibited by the straight arrow
Step 6  u_turn          prohibited: prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but changing to the right is prohibited by the solid line. Do not attempt
                        to turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 874, 6.93 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line and a raised curb/barrier on the right. Photo 2 shows a
                        white line and a raised curb/barrier next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white edge
                        line is on my right. | roles: The yellow solid line correctly identifies a center
                        line, and the white line with a curb correctly identifies an edge line. | markings: No
                        markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The white edge line and curb prohibit moving to the right onto the
                        sidewalk/curb.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left or moving onto the curb to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 809, 7.68 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a bus lane and a bicycle lane on the right. The road
                        continues straight ahead with some buildings and trees on the sides. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bus lane on the right.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white line with a bicycle symbol and a solid white
                        line to its right, indicating a bicycle lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from the leftmost
                        lane, and a white line on the right separates me from the bus/bike lane. | roles: The
                        white solid lines correctly function as lane lines between lanes of the same
                        direction. | markings: The bike symbol is in the lane to the right, which is
                        consistent with the lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bus/bike lane to the
                        right.
Step 5  Rule            symbol:bike: Indicates a lane reserved for bicycles.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a standard travel lane. You may proceed straight ahead, but lane changes to
                        the left or right are prohibited by the solid white lines. The lane to your right is
                        reserved for bicycles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 873, 7.39 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with trees and buildings on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed line with yellow paint.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a sidewalk on the right. Photo 2 shows a solid yellow
                        line next to the curb, and the curb itself is clearly visible.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow dashed line is on my left (lane_line) and a
                        yellow solid line/curb is on my right (edge_line). | roles: The yellow dashed line on
                        the left fits the role of a lane_line, and the yellow solid line/curb on the right
                        fits the role of an edge_line. | markings: No markings are present in my lane to
                        contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed yellow line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        sidewalk.
Step 6  change_left     allowed (correct): allowed by the dashed yellow lane_line
Step 6  change_right    prohibited (correct): prohibited by the solid yellow edge_line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight or change into the left lane. Do not attempt to move to the
                        right as it is bounded by a curb and a solid line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 850, 8.16 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and white near the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white near the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and my position as
                        3rd from the left are consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for going straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Continue straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 823, 6.21 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide sidewalk and a pedestrian area on the right.
                        Ahead, there is a large intersection with several lanes and a pedestrian crossing.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is solid and white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the sidewalk/pedestrian area. Photo
                        2 shows this line is solid and white, with a yellow line further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow in my lane pointing
                        straight and to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) are consistent with the boundaries: a white lane line is on my left and a white
                        edge line is on my right. | roles: The white solid line on the left is a lane line,
                        and the white solid line on the right is an edge line. | markings: The straight-right
                        arrow in my lane is consistent with the lane's purpose and the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk.
Step 5  Rule            arrow:straight_right: The arrow allows going straight or turning right, and prohibits
                        turning left or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. Lane changes to the
                        left or right are prohibited by the solid lines. Do not attempt to turn left from this
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 873, 8.0 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tunnel or underpass ahead. My car is in one of the
                        middle lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows white dashed lane markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) agree with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No specific arrows or words are visible in my lane to contradict the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary allows it
Step 6  change_right    allowed (correct): right_boundary allows it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a middle lane with dashed lines on both sides, allowing you to change lanes
                        if necessary. Proceed straight through the underpass.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 785, 7.04 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or underpass in an urban area. Ahead, there is a tunnel or
                        underpass structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this white solid line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Photo 1 shows a white dashed line and a white
                        solid line forming a left-turn waiting area or turn lane to the left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a dashed line on my left indicates another lane of my
                        direction, and a solid line on my right indicates the edge of the roadway. | roles:
                        The white dashed line on the left fits the role of a lane line, and the white solid
                        line on the right fits the role of an edge line. | markings: The two-way left-turn
                        lane to the left is consistent with the markings seen in Photo 1. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        shoulder or sidewalk.
Step 5  Rule            area:two_way_left_turn_lane: The area to the left is a designated zone for two-way
                        left turns.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areaallowed: allowed by the two_way_left_turn_lane to the left
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move to the
                        right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 925, 8.26 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with a wide roadway and a sidewalk on the right. The
                        road continues straight ahead towards a distant intersection or commercial area.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid white line clearly next to my car, with a sidewalk
                        and some debris/objects beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line in the middle of my
                        lane, but no arrows or words are visible in the lane itself.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a dashed line on the left separates me from
                        another lane, and a solid line on the right marks the edge of the road. | roles: The
                        white dashed line on the left correctly functions as a lane line, and the solid white
                        line on the right correctly functions as an edge line. | markings: No specific arrows
                        or words are present to contradict the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        sidewalk.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right edge line and curb
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight or change to the left lane. Do not attempt to move to the
                        right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 873, 8.49 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with an overpass ahead. My car is in a lane bounded by a curb on the
                        right and a low wall/hedge on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a low hedge and a small curb/wall on the left. Photo 2 shows a concrete
                        curb and a low wall/hedge on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a red wall on the right. Photo 2 shows a solid
                        white line and a red wall on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane is the only lane of my
                        direction, bounded by an edge line on the left and a solid line/curb on the right. |
                        roles: The white solid line and curb on the right correctly identify the edge of the
                        roadway. | markings: No markings are present to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The curb/wall on the left marks the edge of the roadway.
Step 5  Rule            right_boundary: The solid white line and curb on the right mark the edge of the
                        roadway and prohibit crossing into the sidewalk/wall area.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the roadway boundaries.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 797, 7.53 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road approaching a large intersection with a pedestrian crossing and
                        a metal fence on the right. The sun is high, creating a bright glare. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a metal fence on the right. Photo 2 shows a solid
                        white line immediately adjacent to the metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large white left-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with a white dashed line on the left and a solid white line/fence on
                        the right. | roles: The white dashed line on the left correctly identifies a lane-
                        line, and the solid white line with a fence correctly identifies an edge-line. |
                        markings: The left-turn arrow in my lane is consistent with the lane's purpose as a
                        dedicated turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and fence prohibit moving to the right.
Step 5  Rule            arrow:left: The arrow permits turning left and prohibits going straight, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right_boundary and curb
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the left-turn arrow
Step 6  u_turn          prohibited (correct): prohibited by the left-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to turn left at the upcoming intersection. Lane changes to
                        the left are permitted, but you must not proceed straight or turn right from this
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'turn_left'], citation None, contradictions []
Tokens                  in 3797, out 895, 7.17 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway under an overpass. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a yellow lane-use arrow in my lane further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line is on both my left and right. |
                        roles: The white dashed lines correctly function as lane lines between lanes of the
                        same direction. | markings: The straight arrow in my lane is consistent with the lane
                        boundaries and the straight road ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to continue straight. You may change lanes to the
                        left or right as needed, as the boundaries are dashed. Do not attempt to turn left,
                        right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 889, 5.53 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear blue sky. The road ahead is straight
                        with several lanes moving in the same direction. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a guardrail. Photo 2 shows
                        a solid white line very close to the car's right side, then a gap, then another solid
                        white line before the guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a large circular marking with '60' inside it in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with the left lane line and right edge line. | roles: The white dashed
                        line on the left is a lane line; the solid white line on the right is an edge line. |
                        markings: The speed limit marking is centered in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and guardrail prohibit moving to the right.
Step 5  Rule            text:speed_limit: The speed limit is 60 km/h.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane. Do
                        not attempt to move to the right as there is a solid edge line and a guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 876, 7.73 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus and a van in adjacent lanes. The road ahead appears
                        to be a straight stretch with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No markings are present in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 790, 7.27 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a clear sky. The road ahead is straight with several lanes
                        of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line next
                        to my car. Further ahead in Photo 1, it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line is on my left and a white solid line is
                        on my right. | roles: The white dashed line on the left correctly functions as a lane
                        line, and the white solid line on the right functions as an edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white solid line prohibits moving to the right beyond the edge of
                        the roadway.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change to the left lane if
                        needed, but you are prohibited from moving to the right beyond the solid white line.
                        Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 832, 7.3 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a median and a barrier on the right. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        the middle lane (2) are consistent with the white dashed lines on both sides. | roles:
                        The white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No markings are present in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change lanes to the left
                        or right as needed, and you are clear to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 799, 7.07 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        divided highway with a concrete barrier on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car and a concrete barrier further ahead.
                        Photo 2 shows a solid white line next to my car. The line further ahead is a concrete
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a solid white
                        line/barrier on the right. | roles: The white dashed line on the left correctly
                        identifies a lane line, and the solid white line/barrier on the right correctly
                        identifies an edge line. | markings: No markings are present in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and barrier prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change to the left lane if
                        needed, but you are prohibited from moving to the right due to the solid line and
                        concrete barrier. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 837, 7.93 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway under an overpass. Ahead, the road
                        continues straight with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be an edge line or a
                        divider. Photo 2 shows a solid yellow line very close to the car's right side.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a yellow edge line on the right.
                        | roles: The white line is a lane line and the yellow line is an edge line, which fits
                        the layout. | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving to the right beyond the
                        roadway.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid white line, and moving to the right is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 800, 6.62 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a barrier on the left and a shoulder/curb on the right. The
                        road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on the left and a white line on the right
                        define my lane. | roles: The white solid lines correctly function as lane lines
                        between lanes of the same direction. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the solid boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel only. Lane changes to the left or
                        right are prohibited by the solid white lines. Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 837, 7.52 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with overhead power lines and a railway structure to the left.
                        The road ahead is straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier/curb.
                        Photo 2 shows a solid white line next to the car and a concrete barrier further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left correctly identifies a lane line, and the
                        solid white line with a curb on the right correctly identifies an edge line. |
                        markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you are
                        prohibited from moving to the right due to the solid line and curb. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 826, 7.42 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a guardrail on the left and a barrier on the right. The road
                        ahead appears to be a straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with a dashed line on the left and a solid line on the right.
                        | roles: The white dashed line on the left and solid line on the right are consistent
                        with lane-line roles. | markings: No markings are present, which is consistent with
                        the highway environment. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but changing to
                        the right lane is prohibited by the solid line. Continue straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3797, out 804, 6.67 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with overhead signs. My car is in a lane with a white arrow
                        pointing straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left or right as needed, but you should stay in this lane to continue straight.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3797, out 849, 7.73 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. My car is in a lane heading
                        straight ahead. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to my right, which is the edge of the roadway. Photo
                        2 shows this solid white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows overhead signs for my lane indicating 'Through
                        Lane' with a straight arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a dashed line on my left and a solid line/curb on my
                        right. | roles: The white dashed line on the left correctly identifies a lane-line,
                        and the solid white line on the right correctly identifies an edge-line. | markings:
                        The 'Through Lane' arrow in the overhead sign matches the straight-ahead movement
                        allowed by the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        shoulder or beyond.
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for through traffic.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change to the left if needed.
                        Do not move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 869, 6.91 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on both sides. The road ahead appears
                        to be a straight stretch with multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose and the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as needed, but
                        you should continue straight ahead as indicated by the lane markings. Do not attempt
                        to turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 887, 7.01 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a large truck to the left. Ahead, there is a
                        complex area of lane markings and a possible interchange or merging point. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to the right. Photo
                        2 shows this white solid line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 1 shows a large white arrow pointing left in the lane
                        to my left.; arrow:right (full): Photo 1 shows a large white arrow pointing right in
                        the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left allows lane changes, and
                        the white solid line on the right prohibits them, which is consistent with standard
                        lane markings. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. The left and right arrows in adjacent lanes are consistent with their
                        respective lane purposes. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows changing into the left lane.
Step 5  Rule            right_boundary: The white solid line prohibits changing into the right lane.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the white solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       prohibited: prohibited by the straight arrow in my lane
Step 6  turn_right      prohibited: prohibited by the straight arrow in my lane
Step 6  u_turn          prohibited: prohibited by the straight arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change into the left
                        lane if needed, but changing into the right lane is prohibited. Do not attempt to turn
                        left, right, or perform a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['text:speed_limit']), actions
                        True, unsafe [], citation None, contradictions ['turn_left prohibited although an
                        arrow shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 3797, out 1007, 8.9 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving forward
                        towards a set of traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the lane to my left. Photo
                        2 shows the same double yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left and
                        white line on the right correctly identify my lane as the middle lane of three lanes
                        in my direction. | roles: The double yellow line correctly functions as a center line,
                        and the white line functions as an edge line. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line marks the edge of the roadway and prohibits
                        crossing onto the shoulder.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may proceed straight
                        through the intersection but are prohibited from changing lanes or turning. Obey the
                        traffic lights ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 831, 7.51 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        clear roadway with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, which becomes a solid white line
                        further ahead. Photo 2 shows a solid white line. To the right of that line is a raised
                        curb and a green barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on my left and a solid white
                        line/curb on my right. | roles: The white dashed line on the left correctly functions
                        as a lane line, and the solid white line with a curb on the right correctly functions
                        as an edge line. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the sidewalk
                        or shoulder.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (contested, correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       prohibited: prohibited by the straight arrow in my lane
Step 6  turn_right      prohibited: prohibited by the straight arrow in my lane
Step 6  u_turn          prohibited: prohibited by the straight arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if necessary, but you must not move to the right as it is bounded by a solid line
                        and a curb. Do not attempt to turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 940, 8.21 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tram line on the right. My car is in a lane heading
                        straight ahead towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow double-solid line separating my lane from the lane to my left.
                        Photo 2 shows the same yellow double-solid line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the tram/bus lane on the
                        right. Photo 2 shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow double-solid line is on my left (center line) and
                        a white line is on my right (lane line). | roles: The yellow double-solid line
                        correctly identifies the center line, and the white line correctly identifies the lane
                        boundary. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double-solid yellow line prohibits lane changes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel only. Lane changes to the left
                        or right are prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 852, 6.49 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the right. The road
                        continues straight ahead with some vehicles in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to my left. Photo
                        2 shows a yellow dashed line next to my car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a lane on the right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow dashed line on the left and a white solid line
                        on the right. | roles: The yellow dashed line on the left fits a lane-line role, and
                        the white solid line on the right fits a lane-line role. | markings: The straight
                        arrow in my lane is consistent with the lane boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The yellow dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the yellow dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited: prohibited by the straight arrow marking
Step 6  turn_right      prohibited: prohibited by the straight arrow marking
Step 6  u_turn          prohibited: prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. You may change lanes to
                        the left if necessary, but changing to the right is prohibited by the solid line. Do
                        not attempt to turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3797, out 896, 8.09 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a subway station entrance on the right. The road ahead has
                        multiple lanes and an intersection or transit area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a sidewalk/fence on the right. Photo 2 shows a
                        solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a large white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 1 shows a white arrow pointing left in the lane to my
                        left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow line on the left separates me from another lane,
                        and a yellow line/curb on the right marks the edge. | roles: The yellow solid lines
                        correctly function as a lane line and an edge line. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement for this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Do not attempt to change lanes to the
                        left or right, as both boundaries are solid yellow lines. Use this lane to proceed
                        straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left prohibited although an arrow shows it']
Tokens                  in 3797, out 892, 7.95 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the right. My car is in a lane that appears
                        to be a dedicated bus lane or a lane with specific markings, heading straight toward a
                        distant area. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to its left. Photo
                        2 shows the same yellow dashed line clearly.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which then transitions into a solid
                        yellow line bordering a sidewalk/curb area. Photo 2 shows a solid yellow line next to
                        my car. Further ahead in Photo 1, there is a solid yellow line and a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 shows a large yellow Chinese character '专'
                        (special/dedicated) and a bus symbol in my lane. Photo 2 shows the character '专'
                        clearly.; symbol:other (full): Photo 1 shows a bus symbol in my lane. Photo 2 shows
                        the bus symbol clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3. My lane is the
                        rightmost (index 3). The left boundary is a lane line, and the right boundary is an
                        edge line, which is consistent. | roles: The yellow dashed line on the left is a lane
                        line, and the solid yellow line on the right is an edge line, which fits the roles. |
                        markings: The '专' (dedicated) text and bus symbol indicate this is a bus lane, which
                        is consistent with the lane's position and the solid edge line on the right. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right.
Step 5  Rule            text:other: The '专' character indicates this is a dedicated lane, typically for buses.
Step 5  Rule            symbol:other: The bus symbol indicates this lane is reserved for buses.
Step 6  change_left     allowed (contested, correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  This is a dedicated bus lane as indicated by the '专' character and bus symbol. You may
                        proceed straight or change to the left, but you should avoid using this lane unless
                        you are a bus.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other', 'text:other'], missed []), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 1050, 8.45 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving forward
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left. Photo 2 shows the same double
                        solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right. Photo 2 shows the same solid white line
                        clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a double yellow center line is on my left, and a white edge
                        line is on my right. | roles: The double yellow center line and white edge line
                        correctly define the lane boundaries. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits lane changes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving onto the shoulder or area to the
                        right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, right, or
                        making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may proceed straight
                        ahead but are prohibited from changing lanes or turning at the upcoming intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 818, 7.31 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center. The road ahead appears to be a
                        straight stretch with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line very
                        close to the car's right side.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with a lane line on the left and a lane line on the right. |
                        roles: The white dashed line on the left and solid line on the right correctly
                        identify the boundaries of my lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can proceed straight ahead or change to the left lane.
                        Changing to the right lane is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 854, 23.44 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane moving forward.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and yellow near my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white near my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane ahead.;
                        arrow:straight (full): Photo 1 shows a white straight-ahead arrow in my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the yellow line on my left and white line on my right. | roles:
                        The yellow line on the left and white line on the right correctly identify the
                        boundaries of my lane. | markings: The left-turn and straight arrows in my lane are
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to my left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to my right.
Step 5  Rule            arrow:left: The arrow allows turning left from my lane.
Step 5  Rule            arrow:straight: The arrow allows going straight from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 896, 7.22 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane approaching a
                        crosswalk and a set of traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The crosswalk is consistent with an intersection ahead. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            line:crosswalk: The crosswalk indicates a pedestrian crossing area where the vehicle
                        should be prepared to stop.
Step 6  change_left     allowed: allowed by the dashed left_boundary
Step 6  change_right    allowed: allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as needed. Be
                        prepared to stop for pedestrians at the upcoming crosswalk.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 844, 23.51 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the right. Ahead, there is a
                        large overhead gantry with electronic signs and a wide intersection or transit hub
                        area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the lane to the left. Photo
                        2 shows the double yellow line clearly, with the inner line being solid and the outer
                        line being solid as well.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-painted bus lane. Photo
                        2 shows this solid white line clearly.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the double yellow center line on the left and the white line on
                        the right. | roles: The double yellow line correctly identifies a center line, and the
                        white line separates my lane from a special lane (bus lane). | markings: The straight
                        arrow is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the bus lane to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right, as both boundaries are solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 860, 7.25 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane configuration. Ahead, the road
                        continues straight with several lanes visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this line is a dashed yellow line near my car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows a solid yellow line and
                        a thick yellow painted area with a character (likely 'BUS' or similar) on the right.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a yellow arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 1 shows a yellow arrow pointing left in the lane to my
                        left.; text:bus (full): Photo 2 shows a large yellow character/symbol on the right
                        side of my lane, indicating a bus lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        (middle) agree with the boundaries: a dashed line on the left and a solid line on the
                        right. | roles: The yellow dashed line on the left is a lane line; the solid yellow
                        line on the right marks a special lane (bus lane). | markings: The straight arrow in
                        my lane aligns with the lane's purpose. The bus marking on the right explains the
                        solid boundary. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed yellow line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the bus lane on the
                        right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 5  Rule            text:bus: The lane to the right is reserved for buses.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may change to the left lane if
                        needed, but you must not move into the bus lane on your right. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight', 'text:bus'], missed []), actions None, unsafe [],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 3797, out 1029, 9.64 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a green surface. Ahead, the road continues straight
                        with several vehicles in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the lane to my left. Photo
                        2 shows the same double yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a raised concrete barrier/curb on the right. Photo 2 shows the same
                        raised concrete barrier/curb.
                        none solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 1 shows no arrows or words in my lane.; no_turn:right
                        (full): Photo 1 shows no arrows or words in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a center line is on my left and an edge line/curb is on my
                        right. | roles: The yellow double solid line correctly identifies a center line, and
                        the curb correctly identifies an edge line. | markings: No markings are present in my
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The raised curb prohibits crossing to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        double solid yellow line, and the right side is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right'], missed []), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3797, out 822, 7.19 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the right and a wide intersection ahead. My
                        car is in a central lane. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a yellow double-dashed line separating my lane from the lane to my left.
                        Photo 2 shows the same yellow double-dashed line clearly.
                        yellow double_dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 shows
                        this solid white line clearly.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the boundaries: a yellow double-dashed line on the left and a
                        white solid line on the right. | roles: The yellow double-dashed line correctly
                        identifies a lane-change boundary, and the white solid line correctly identifies a
                        special lane (bus lane) boundary. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The yellow double-dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bus lane on the
                        right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow double-dashed left
                        boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if needed, but you must not move into the bus lane on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 870, 8.34 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane that leads
                        toward a signalized intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right as needed, but you should not turn left, right, or perform a U-turn from
                        this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left prohibited although an arrow shows it']
Tokens                  in 3797, out 905, 7.89 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in one of the center
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight arrow in my lane pointing
                        forward.; arrow:straight (full): Photo 1 shows a white straight arrow in the lane to
                        my right.; arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my
                        left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose and the
                        dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right as needed, but you should stay in this lane to proceed straight through the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['line:stop_line']), actions False, unsafe
                        ['change_left', 'change_right'], citation None, contradictions ['turn_left prohibited
                        although an arrow shows it']
Tokens                  in 3797, out 937, 8.15 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the right. The road ahead appears to be a
                        straight stretch with a pedestrian area or sidewalk on the left. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating my lane from a bus lane on the right.
                        Photo 2 shows a solid yellow line.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a yellow solid line
                        on the right. | roles: The white dashed line on the left correctly identifies a lane
                        line, and the yellow solid line on the right correctly identifies a special lane
                        boundary (bus lane). | markings: The left-turn arrow in my lane is consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the bus lane on the
                        right.
Step 5  Rule            arrow:left: The arrow allows for a left turn and prohibits going straight, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow right_boundary
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow
Step 6  turn_left       allowed: allowed by the left-turn arrow
Step 6  turn_right      prohibited: prohibited by the left-turn arrow
Step 6  u_turn          prohibited: prohibited by the left-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn. Do not attempt to move into the bus lane on your
                        right or proceed straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 887, 7.93 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane approaching a
                        crosswalk and a set of traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is dashed (broken) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is dashed (broken) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white crosswalk ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        crosswalk is consistent with an intersection ahead. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 5  Rule            line:crosswalk: The crosswalk indicates a pedestrian crossing area where the vehicle
                        should be prepared to stop.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed white left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight through the intersection, being mindful of the
                        crosswalk and traffic signals.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3797, out 843, 7.38 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a white
                        car to its left and a red car and a truck to its right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines. | markings: The left-turn arrow in my lane is
                        consistent with the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:left: The arrow indicates that my lane is designated for turning left.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the arrow:left marking
Step 6  turn_left       allowed: allowed by the arrow:left marking
Step 6  turn_right      prohibited: prohibited by the arrow:left marking
Step 6  u_turn          prohibited: prohibited by the arrow:left marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to turn left at the upcoming intersection. Lane changes to the left or
                        right are permitted as the boundaries are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 842, 7.89 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in the rightmost lane of
                        a multi-lane roadway. (lanes 4, mine 4, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to its left. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb on the right. Photo 2 shows a
                        white solid line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows a large white character '直' (straight) in my lane.;
                        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The white dashed line on my left separates me from
                        another lane of my direction, and the white solid line/curb on my right marks the edge
                        of the roadway. | roles: The white dashed line fits the role of a lane line, and the
                        white solid line with a curb fits the role of an edge line. | markings: The 'straight'
                        character and the straight arrow in my lane are consistent with each other and the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white solid line and curb prohibit moving to the right onto the
                        sidewalk/shoulder.
Step 5  Rule            text:other: The 'straight' character indicates the lane is intended for straight
                        movement.
Step 5  Rule            arrow:straight: The arrow allows for straight movement and prohibits turning left,
                        right, or making a U-turn.
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the white solid right_boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight and text:other
Step 6  turn_left       prohibited: prohibited by the arrow:straight
Step 6  turn_right      prohibited: prohibited by the arrow:straight
Step 6  u_turn          prohibited: prohibited by the arrow:straight
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may change to the left
                        if needed, but you are prohibited from turning left, right, or making a U-turn from
                        this lane. Do not move to the right onto the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 1017, 8.88 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a dashed line on the left and a solid line on the right. |
                        roles: The white dashed line on the left and solid line on the right fit the roles of
                        lane lines. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but lane changes to the right are prohibited. Do not attempt to
                        turn left, right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3797, out 870, 7.49 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a dedicated lane for straight-ahead
                        traffic. There is a sidewalk and a bicycle parking area to the right. (lanes 2, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in
                        the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The left boundary is a lane line and the right is an
                        edge line. | roles: The white solid lines fit the roles of a lane line and an edge
                        line. | markings: The straight arrow in my lane is consistent with the lane's purpose
                        and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight ahead. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 835, 7.88 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead is a multi-lane
                        street with a center line and a sidewalk on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a sidewalk. Photo 2 shows a
                        solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 1 shows a white dashed line in the middle of my lane
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white edge
                        line is on my right. | roles: The yellow solid line fits the role of a center line,
                        and the white solid line fits the role of an edge line. | markings: The dashed line in
                        the middle of the lane is consistent with a lane divider or a specific lane marking,
                        though its specific meaning is unclear without more context. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white edge line and curb prohibit moving onto the sidewalk
                        to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Lane changes to the left or right are prohibited by the
                        solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3797, out 825, 7.57 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and trees on the right. Ahead, there is a
                        signalized intersection with a red light. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows the same solid yellow line clearly.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows a solid
                        white line next to a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with the boundaries: a yellow line on my left and a white line/curb on
                        my right. | roles: The yellow solid line correctly identifies a lane divider, and the
                        white line/curb correctly identifies the edge of the roadway. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose and the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You are permitted to go straight ahead but are
                        prohibited from changing lanes or turning. Stop at the red light ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 3797, out 846, 6.87 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in a lane that
                        appears to have a dedicated turn or straight-ahead path. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb/sidewalk on the right. Photo 2
                        shows a solid white line next to my car and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a lane line on the left and an edge line on the right. | roles:
                        The white solid line on the left is a lane line; the white solid line with a curb on
                        the right is an edge line. | markings: The straight arrow in my lane is consistent
                        with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Your lane is designated for straight-ahead travel. You are prohibited from changing
                        lanes to the left or right. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 842, 7.75 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. A bus is directly
                        ahead in the lane to the left of my car. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white edge
                        line is on my right. | roles: The yellow solid line fits the role of a center line,
                        and the white solid line fits the role of an edge line. | markings: No markings are
                        present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits changing into the lane on the
                        left.
Step 5  Rule            right_boundary: The solid white edge line prohibits moving onto the sidewalk or
                        shoulder on the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 782, 7.0 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane roadway, possibly a ramp or a dedicated transit
                        corridor, with a large building on the right and a covered structure on the left. The
                        road ahead appears to continue straight. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a metal railing/barrier on the right. Photo 2
                        shows a solid white line very close to the right edge, followed by a concrete curb and
                        a metal railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        the rightmost lane (index 2) are consistent with a white lane line on my left and an
                        edge line/curb on my right. | roles: The white solid line on the left acts as a lane
                        divider, and the white line with a curb on the right acts as an edge line. | markings:
                        No markings are present to contradict the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The edge line and curb prohibit moving to the right off the roadway.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid white line, and the right side is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3797, out 832, 7.38 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bike lane on the right. The road continues
                        straight ahead into a city area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-painted bike lane.
                        Photo 2 shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): Photo 1 shows a white bicycle symbol on the red lane to the
                        right, but no markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with a white dashed line on the left and a solid white line on
                        the right. | roles: The white dashed line on the left correctly identifies a lane-
                        change possibility, and the solid white line on the right correctly identifies a
                        boundary with a special area (bike lane). | markings: No markings are in my lane,
                        which is consistent with the lane's role as a standard through-lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bike lane on the
                        right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change to the left lane. Do not move into the red bike
                        lane on your right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 831, 7.11 s
```
