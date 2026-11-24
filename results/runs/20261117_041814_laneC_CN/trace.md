# Reasoning of lane run 20261117_041814_laneC_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch leading toward a distant intersection or continuation. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which is an edge lane
                        or a lane adjacent to a curb/sidewalk.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white lane line is on my left and a yellow edge line is on my right. | roles: The
                        white lane line on the left and yellow edge line on the right are consistent with
                        standard markings for a right-hand traffic system. | markings: The straight arrow in
                        my lane is consistent with the straight road ahead. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white/yellow line delineates the edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are discouraged/prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 853, 7.55 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees lining both sides. The road ahead appears to be a
                        straight stretch with a potential intersection or turn-off in the distance. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, adjacent to a sidewalk and
                        greenery.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in my
                        lane.; arrow:left (full): A white arrow pointing left is painted in the lane to my
                        left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on my left separates me from another lane, and a white line on my right
                        marks the edge. | roles: The yellow line on the left and white line on the right are
                        consistent with standard lane/edge roles. | markings: The straight arrow in my lane is
                        consistent with the straight-ahead path. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is designated for straight-ahead
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        and avoid changing lanes, as the solid lines on both sides discourage or prohibit lane
                        changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left not_applicable although an arrow
                        shows it']
Tokens                  in 8628, out 895, 7.81 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with buildings on both sides. Ahead, there is
                        a clear roadway with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left correctly identifies a lane-line, and the white solid line on the
                        right correctly identifies an edge-line. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking (US-3B.23-01)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to continue straight ahead. Lane changes
                        to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 741, 7.35 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure on the right. The road ahead
                        appears to be a straight stretch of highway or a large boulevard. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is bounded by a
                        metal fence and a sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow is consistent with the lane's role and
                        the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 843, 7.97 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure on the right. The road ahead
                        appears to be a straight stretch with multiple lanes of traffic. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is adjacent to a
                        sidewalk and a fence.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, where another vehicle
                        is traveling.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        the separation of same-direction traffic lanes. | markings: No markings are present in
                        my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 784, 7.44 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        lines are consistent with lane separation and edge delineation. | markings: The
                        straight arrow is consistent with the straight road ahead. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking in the lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 681, 5.48 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with buildings and trees on both sides. An intersection or
                        junction is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a lane line on my
                        left and an edge line on my right. | roles: The yellow line on the left and white line
                        on the right correctly identify the lane's position in a right-hand traffic system. |
                        markings: The straight arrow is consistent with the lane's forward path. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that moving straight ahead is a permissible
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow lane line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [US-3B.23-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 706, 6.81 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure overhead. The road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left indicates another lane of the same direction, and a white line
                        on the right indicates the edge of the roadway. | roles: The white solid lines
                        correctly represent lane separation and the right edge of the roadway. | markings: No
                        markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 782, 6.9 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a city skyline in the distance. The road appears to be
                        a large boulevard or a bridge approach. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow is consistent with the lane's role as a
                        through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead as indicated by
                        the pavement arrow. Lane changes to the left or right are prohibited by the solid
                        white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 835, 7.51 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or turn area ahead. The car is in a lane
                        that appears to be a turn lane or a lane approaching a turn. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): A large white arrow pointing left is painted in my lane.; text:only
                        (full): The word 'ONLY' is painted in my lane next to the arrow.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a center line on
                        the left and an edge line on the right. | roles: The yellow center line and white edge
                        line fit the roles of separating opposite traffic and the roadway edge. | markings:
                        The left arrow and 'ONLY' text are consistent with a mandatory left-turn lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a yellow center line in this context, but
                        it generally separates opposite traffic flows. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates the lane is designated for the exclusive use of a
                        left-turning movement. [US-3B.23-03]
Step 5  Rule            text:only: The 'ONLY' marking reinforces that the lane is for the exclusive use of the
                        movement shown by the arrow. [US-3B.21-04]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a mandatory left-turn lane. You must turn left at the upcoming intersection
                        and are prohibited from changing lanes or going straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'text:only'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8628, out 744, 6.53 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus stop or transit area on the left. An intersection
                        or pedestrian crossing is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bus lane or special lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        function. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['turn_left not_applicable although an arrow shows it']
Tokens                  in 8628, out 870, 7.71 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a concrete barrier on the left and a curb/barrier on
                        the right. Ahead is a clear stretch of road with a traffic signal overhead. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right, which is bounded by a
                        curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): A solid yellow line is painted in the middle of my lane,
                        appearing to delineate a space or area.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a white
                        line on my left and a white line on my right. | roles: The white lines correctly
                        delineate same-direction traffic and the right edge. | markings: The yellow marking is
                        a distinct feature in the lane but does not contradict the boundaries. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            symbol:other: No specific rule provided for this yellow marking; it does not
                        explicitly govern movements.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 843, 7.8 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a pedestrian overpass ahead. The road appears to be a
                        one-way street or a divided highway with multiple lanes moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is in the lane to my
                        left.; arrow:straight (full): A white arrow pointing straight ahead is in the lane to
                        my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly delineate same-direction
                        traffic and the right edge. | markings: The straight arrows in all lanes are
                        consistent with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 735, 6.82 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. The car is positioned in a
                        lane heading straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        two-way left-turn lane or a median area.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane.;
                        line:yield_line (insufficient): No markings are visible within my lane.;
                        area:two_way_left_turn_lane (full): No markings are visible within my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left and a yellow line on the right. | roles: The white line on the
                        left correctly identifies a same-direction lane, and the yellow line on the right
                        correctly identifies a center line/separation from opposite flow. | markings: No
                        markings are in my lane, which is consistent with the clear path ahead. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but here it serves as a boundary for a special lane (two-way left-turn lane).
                        [US-3B.01-05]
Step 5  Rule            area:two_way_left_turn_lane: The area to my right is a two-way left-turn lane.
                        [US-3B.05-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'line:stop_line', 'line:yield_line'], missed []),
                        actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 788, 7.78 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an overpass and overhead signs. The road ahead appears to be
                        a continuous through-way. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is bounded by a
                        curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-line, and the white solid line on
                        the right correctly identifies an edge-line. | markings: The straight arrow in my lane
                        is consistent with the 'Through Lane' designation on the overhead signs. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white solid line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the white dashed lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the white solid edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow [US-3B.23-01].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn marking.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight or change into the left lane.
                        Changing into the right lane is prohibited as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 755, 7.43 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in a lane
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area with a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        correctly identifies a lane-line, and the white solid line correctly identifies an
                        edge-line. | markings: The straight arrow is consistent with the lane's role as a
                        through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and curb
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow marking [US-3B.23-01].
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or area is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the left lane. Do not attempt to move to
                        the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 905, 8.48 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge of the roadway.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is painted in the lane to my right.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        delineate lanes of the same direction. | markings: The straight arrow in my lane is
                        consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['line:stop_line']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left not_applicable although an arrow
                        shows it']
Tokens                  in 8628, out 882, 7.49 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow in my lane is consistent with the
                        lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left not_applicable although an arrow
                        shows it']
Tokens                  in 8628, out 843, 7.24 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in one of
                        the middle lanes. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3rd from left) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with a
                        through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 813, 7.07 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection ahead. The car is positioned in one of the
                        central lanes. (lanes 4, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to its right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        same-direction traffic flows. | markings: The straight arrow is consistent with the
                        lane's position and the surrounding turn lanes. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 659, 6.6 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a median separating opposing traffic. Ahead is a clear
                        stretch of road with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        lane's role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 663, 5.76 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane that appears to be a dedicated turn lane or a lane with specific directional
                        markings. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow pointing left is painted in my lane.; arrow:straight
                        (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate lanes in the same
                        direction of travel. | markings: The left and straight arrows are consistent with a
                        multi-movement lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [US-3B.23-01]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement from
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       allowed (correct): allowed by the left arrow marking
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 732, 7.08 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which appears to be a
                        parking or shoulder area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; arrow:straight (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate same-direction
                        traffic and the right edge. | markings: No markings were observed in the lane. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane', 'arrow:straight', 'line:stop_line',
                        'line:yield_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read']
Tokens                  in 8628, out 705, 7.69 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway passing under a bridge (Dashan Bridge). There is
                        a pedestrian area and a sidewalk to the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk and a pedestrian area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in my
                        lane.; arrow:left (full): A large white arrow pointing left is painted in the lane to
                        my left.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with a
                        white lane line on my left and a white edge line/curb on my right. | roles: The white
                        solid line on the left is a standard lane line, and the white solid line on the right
                        is a standard edge line. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose, and the left arrow in the adjacent lane is consistent with its
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited: prohibited by the solid white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited: prohibited by the solid white edge line and curb [US-3B.09-01-02]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may proceed straight
                        ahead, but lane changes to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:right']), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['turn_left not_applicable although an
                        arrow shows it']
Tokens                  in 8628, out 780, 6.73 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a white fence on the left and trees on the right. The
                        road continues straight ahead toward a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        having a lane line on both the left and right. | roles: The white solid lines
                        correctly delineate lanes in the same direction of travel. | markings: The straight
                        arrow is consistent with the lane's forward path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that moving straight ahead is a permitted
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead as indicated by the arrow.
                        Lane changes to the left or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 669, 6.75 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in a lane
                        heading straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow is consistent with the lane's role and
                        the surrounding boundaries. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may proceed straight
                        ahead but are prohibited from changing lanes to the left or right due to the solid
                        white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 830, 5.78 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in a lane
                        with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may proceed straight
                        but are prohibited from changing lanes to the left or right due to the solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 655, 6.12 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a wide intersection ahead. The road is lined with trees
                        and buildings. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bike lane or sidewalk area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): A large yellow box with a grid pattern is painted across the
                        intersection ahead.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        delineate lanes in the same direction of travel. | markings: The grid area is
                        consistent with a 'Do Not Block' or 'Keep Clear' zone at an intersection. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:grid: The grid area indicates a 'Do Not Block Intersection' zone where vehicles
                        must not stop. [US-3B.26-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight through the intersection. Do not change lanes to the left or
                        right, and do not stop within the yellow grid area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 688, 6.22 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides and trees lining the sidewalk.
                        The road ahead appears to be a straight continuation of the current street. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white diamond symbol is painted in the center of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white lane line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (opposite traffic) and the white
                        solid line identifies a same-direction lane line. | markings: The diamond symbol is a
                        neutral marking and does not contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but in this context (right-hand traffic), it delineates the
                        separation of opposite traffic. [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 5  Rule            symbol:other: No specific rule governs the diamond symbol for movement.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 858, 7.78 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or pedestrian area ahead. The car is in a
                        lane moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the edge line on my right. | roles: The white solid line on the
                        left is a standard lane line; the white solid line on the right is a standard edge
                        line. | markings: The straight arrow is consistent with the lane's forward direction.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited: prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited: prohibited by the solid white edge line and curb on the right.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow marking in my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid lines and curb prohibit these movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 852, 6.15 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway in an urban area with buildings and trees in the
                        background. The road ahead appears to be a straight stretch of highway or a large
                        boulevard. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is adjacent to a
                        concrete barrier.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, where a white car is
                        currently positioned.
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
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        the separation of traffic flows in the same direction. | markings: No markings were
                        observed, which is consistent with the lack of specific movement restrictions in the
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white line on the
                        left.
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 8628, out 1186, 10.78 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in a lane
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left indicates another lane of the same direction, and a white line
                        on the right indicates the edge of the roadway. | roles: The white solid lines
                        correctly represent lane separation and the right edge of the roadway. | markings: The
                        straight arrow is consistent with the lane's function and the surrounding boundaries.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        (US-3B.09-01-02).
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking (US-3B.23-01).
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 902, 6.97 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway approaching an intersection. There are
                        several lanes of traffic moving in the same direction. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A straight arrow pointing forward is painted in the center of
                        my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        lane-to-lane boundaries for same-direction traffic. | markings: The straight arrow in
                        my lane is consistent with a through-lane configuration. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The straight arrow indicates that moving straight ahead is a
                        permissible movement for this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 667, 5.92 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        ahead appears to be a straight stretch with multiple lanes of traffic. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        delineate lanes in the same direction of travel. | markings: No markings were
                        observed, which is consistent with the clear lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are discouraged or prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 636, 6.4 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the left and a parking area on the right.
                        The road ahead appears to be a straight continuation of the current roadway. (lanes 3,
                        mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        center line is on my left and an edge line is on my right. | roles: The yellow double
                        solid line correctly identifies a center line (opposite traffic), and the white solid
                        line correctly identifies an edge line. | markings: The straight arrow is consistent
                        with the lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left are prohibited by the double solid yellow line, and
                        the right side is bounded by a solid white line and a curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 853, 8.25 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection or large junction ahead. The car is
                        positioned in a lane moving forward. (lanes 4, mine 3, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        double yellow center line is to my left, and a white lane line is to my right. |
                        roles: The double yellow line correctly identifies a center line (opposite traffic),
                        and the white line correctly identifies a same-direction lane line. | markings: The
                        straight arrow is consistent with the lane's purpose and the surrounding markings. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the markings prohibit these maneuvers.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 888, 7.68 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure on the left and buildings on the
                        right. The road ahead appears to be a straight continuation of the current street.
                        (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        dedicated turn lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        straight roadway ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 676, 6.72 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway under an overpass. The road continues straight ahead
                        towards a city area. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white lane line on my left and a white edge line on my right. | roles: The white
                        solid lines correctly represent a lane line and a right edge line. | markings: No
                        markings were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may proceed straight ahead, but lane
                        changes to the left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 625, 6.6 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in one of
                        the center lanes. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
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
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify as lane lines between same-direction traffic. | markings: No markings were
                        observed in my lane, which is consistent with the lack of specific movement
                        restrictions. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): Allowed by the white dashed left boundary line.
Step 6  change_right    allowed (correct): Allowed by the white dashed right boundary line.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or boundaries govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings or boundaries govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings or boundaries govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right as the lane markings are dashed. Proceed
                        straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 8628, out 1142, 11.96 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in a lane
                        with a straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        same-direction traffic flows. | markings: The straight arrow is consistent with the
                        lane's role and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. Lane changes to the left or
                        right are prohibited by the solid white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 663, 6.91 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The car is positioned in a lane
                        heading forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        delineate lanes of the same direction. | markings: The straight arrow is consistent
                        with the lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 654, 6.21 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. The car is
                        positioned in a lane heading towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to my right, which appears to be a
                        bike lane or a separate travel lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 664, 6.5 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass ahead. The road is wide and
                        appears to be a high-speed thoroughfare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a standard lane line, and the white solid line on the right is a
                        standard edge line. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking in my lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to continue straight ahead. Lane changes
                        to the left or right are discouraged/prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 701, 5.88 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a median on the left and a curb/barrier on the right.
                        An intersection or lane ending is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.; text:only
                        (full): A white word 'ONLY' is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white lane line
                        on my left and a white edge line on my right. | roles: The white solid lines correctly
                        function as a lane line and an edge line. | markings: The straight arrow and 'ONLY'
                        text are consistent with a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 5  Rule            text:only: The 'ONLY' marking indicates that the lane is designated for the exclusive
                        use of the movement shown by the arrow. [US-3B.21-04]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow and 'ONLY' marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated exclusively for straight-through traffic. Do not attempt
                        to change lanes to the left or right as the solid lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:only'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 752, 6.78 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and trees on the right. The road ahead appears
                        to be a straight stretch with an intersection or junction further ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which is an edge
                        lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.; arrow:straight
                        (full): A white straight-ahead arrow is painted in my lane.; text:only (full): A white
                        'ONLY' word marking is visible near the left turn arrow.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the yellow
                        boundaries on both sides. | roles: The yellow lines correctly delineate the separation
                        of traffic flows and the left-hand edge of the roadway in a right-hand traffic system.
                        | markings: The left-turn and straight arrows in my lane are consistent with the
                        lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow line separates my lane from the lane to my left.
                        [US-3A.03-03-04]
Step 5  Rule            right_boundary: The yellow line delineates the left-hand edge of the roadway (in this
                        right-hand traffic context). [US-3A.03-03-04]
Step 5  Rule            arrow:left: The arrow indicates a permissible left turn. [US-3B.23-01]
Step 5  Rule            arrow:straight: The arrow indicates a permissible straight movement. [US-3B.23-01]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid yellow line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line
Step 6  go_straight     allowed (contested, label prohibited): allowed by the straight arrow
Step 6  turn_left       allowed: allowed by the left turn arrow
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left as indicated by the pavement markings. Lane
                        changes to the left or right are prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight', 'text:only'], missed ['text:bus']), actions None,
                        unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 782, 7.04 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right and a
                        wall/barrier on the left. Ahead, there is a gantry and a merging area. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway, which is
                        bordered by a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        lines correctly represent a lane line and an edge line for right-hand traffic. |
                        markings: No markings were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): The solid white lane line on the left prohibits
                        crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line and concrete barrier
                        prohibit crossing.
Step 6  go_straight     allowed (contested, correct): No markings in the lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in the lane allow or prohibit a left turn.
Step 6  turn_right      not_applicable: No markings in the lane allow or prohibit a right turn.
Step 6  u_turn          not_applicable: No markings in the lane allow or prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is visible or marked.
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid markings and the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 668, 6.61 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a guardrail
                        on the right. An overhead gantry with signs is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line is visible on the right side of my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        delineate lanes of the same direction. | markings: No specific arrows or words are
                        visible in my lane to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as lane changes to the left or right are
                        discouraged/prohibited by the solid white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 793, 7.58 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The sun is high in the
                        sky, creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; arrow:straight (full): No
                        markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line, which is consistent with the right-hand traffic flow. | markings: No markings
                        were reported in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: No marking governs this action. [null]
Step 6  change_left     prohibited (WRONG, label allowed): The solid white line on the left discourages or
                        prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white line on the right delineates the
                        edge of the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead.
                        Lane changes to the left or right are discouraged or prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8628, out 718, 7.32 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway on a bridge or elevated structure. Ahead, there is a clear path
                        with multiple lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly delineate same-direction
                        traffic and the right edge. | markings: No markings are present, which is consistent
                        with the clear lane path. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged or prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 790, 7.61 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with trees on both sides. The road ahead appears to be a straight
                        stretch of highway. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail and trees
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as the 3rd lane (rightmost) are
                        consistent with a white lane line on my left and a white edge line on my right. |
                        roles: The white solid line on the left is a standard lane line, and the white solid
                        line on the right is a standard edge line. | markings: No markings were observed in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        my left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        guardrail on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead, but lane changes to the
                        left are discouraged or prohibited by the solid white line. Do not attempt to move to
                        the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 663, 6.94 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a guardrail on the right. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line/guardrail on the right. | roles: The white
                        dashed line correctly identifies a lane-to-lane separation, and the white solid line
                        correctly identifies the right edge. | markings: No markings are present, which is
                        consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and guardrail
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings or arrows are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings or arrows are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings or arrows are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you must stay within the roadway and
                        not move right toward the guardrail. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 856, 8.02 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. The road ahead is straight with a clear
                        view of the lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line, which is consistent with the right-hand traffic flow. | markings: No markings
                        were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right
                        (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged or prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 681, 6.74 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with a clear sky. The road ahead appears to be a straight
                        stretch of highway with a median on the left and a guardrail on the right. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left correctly identifies a lane-to-lane separation, and the white solid
                        line on the right correctly identifies the edge of the roadway. | markings: The
                        straight arrow in my lane is consistent with the straight path of the highway. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        guardrail on the right (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking (US-3B.23-01)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You are permitted to continue
                        straight ahead, but lane changes to the left or right are discouraged or prohibited by
                        the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 756, 7.38 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a clear sky. The road ahead appears to be a straight stretch
                        of highway with no immediate intersection or ramp visible. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white line on my left and a white line on my right. | roles: The white solid lines
                        correctly function as a lane line and an edge line for a right-hand traffic system. |
                        markings: No markings are present, which is consistent with a standard through-lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and it is a through
                        lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 806, 6.87 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a
                        wall/barrier on the right. The road ahead appears to be a straight stretch of highway.
                        (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        wall.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white dashed line on the left indicates another lane of the same direction, and a
                        white solid line on the right indicates the edge of the roadway. | roles: The white
                        dashed line on the left and white solid line on the right are consistent with standard
                        lane markings for same-direction traffic. | markings: No markings are present in the
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the dashed white line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the dashed white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or arrows govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings or arrows govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings or arrows govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane as it is marked with a dashed line. Do not attempt
                        to move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 861, 8.23 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on the right. The road ahead
                        is straight with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        bordered by a metal guardrail and a sound barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left and solid white line on the right correctly identify a lane-line and an edge-line
                        for a right-hand traffic system. | markings: The straight arrow is consistent with the
                        straight road ahead and the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the dashed white line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (correct): Allowed by the dashed white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow marking [US-3B.23-01].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or waiting area.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or waiting area.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the left lane. Do not attempt to move to
                        the right beyond the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 769, 6.59 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with buildings and construction equipment ahead. The road
                        appears to be a divided highway or a large multi-lane street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white lines
                        correctly represent a lane line and an edge line for a right-hand traffic system. |
                        markings: The straight arrow is consistent with the lane's role as a through lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 838, 7.85 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a bridge or elevated structure. A bus is directly ahead in
                        the adjacent lane. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail delineate the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on my left and a white line/guardrail on my right. | roles: The white lines
                        and guardrail correctly identify the lane-line and edge-line roles. | markings: No
                        markings are present, which is consistent with the lack of specific movement
                        instructions. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
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
Score                   lane False, boundaries {'left': True, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8628, out 758, 7.27 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or bridge with overhead lane-use signs. The road ahead is
                        straight. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        'Through Lane' signs above. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 651, 6.62 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation or a wide intersection area. (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb and a small planter area with bushes separate my lane from the
                        sidewalk/pedestrian area on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (1) are consistent with the left curb and
                        right lane line. | roles: The left curb acts as an edge line and the white line acts
                        as a lane line. | markings: No markings are present to contradict the boundaries. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a curb as an edge line, but it serves as
                        a physical boundary. [null]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the adjacent lane.
                        [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the physical curb/edge
                        boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): Discouraged by the solid white lane line.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is the default
                        allowed movement.
Step 6  turn_left       not_applicable: No marking governs this action, but the left boundary is a curb.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in your lane. Lane changes to the right are discouraged by the solid
                        white line, and the left side is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8628, out 794, 7.58 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. Ahead, there is a
                        clear roadway with several lanes of traffic moving in the same direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A concrete median wall separates my lane from the opposing traffic.
                        none none, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        a center median on the left and a lane line on the right. | roles: The concrete median
                        correctly serves as a center line, and the solid white line correctly serves as a lane
                        line. | markings: No markings were observed in my lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The concrete median acts as a physical barrier separating opposing
                        traffic flows. [null]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): Prohibited by the concrete median (center_line).
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white lane line
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight ahead, but
                        lane changes to the right are discouraged or prohibited by the solid white line. Do
                        not attempt to cross the median to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8628, out 666, 6.66 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a pedestrian bridge overpass on the right. The road
                        ahead appears to be a straight stretch with a sidewalk and a pedestrian area on the
                        right. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        yellow line on my left and a white line on my right. | roles: The yellow line on the
                        left and white line on the right are consistent with standard lane/edge markings. |
                        markings: The straight arrow is consistent with the straight roadway ahead. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        left lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow line on the
                        left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white line and the
                        curb on the right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid markings and the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 693, 6.51 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear view ahead. The road appears to be a divided
                        highway or a large boulevard with a median on the left. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white lines
                        correctly delineate same-direction traffic and the right edge of the roadway. |
                        markings: No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 798, 14.54 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a pedestrian overpass on the right. The road ahead
                        appears to be a straight continuation or a large intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with a white
                        lane line on the left and a white edge line on the right. | roles: The white solid
                        line on the left correctly identifies a lane-line, and the white solid line on the
                        right correctly identifies an edge-line. | markings: The straight arrow is consistent
                        with the lane's forward path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 684, 5.15 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; area:left_turn_waiting (insufficient): No
                        markings are visible in my lane.; area:two_way_left_turn_lane (insufficient): No
                        markings are visible in my lane.; area:grid (insufficient): No markings are visible in
                        my lane.; area:channelizing (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line, which is consistent with the road layout. | markings: No markings were observed
                        in my lane. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): The solid white lane line on the left prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line on the right prohibits
                        crossing.
Step 6  go_straight     allowed (contested, correct): No markings govern this action, and the lane continues
                        straight.
Step 6  turn_left       not_applicable: No markings govern this action, and no arrow is present.
Step 6  turn_right      not_applicable: No markings govern this action, and no arrow is present.
Step 6  u_turn          not_applicable: No markings govern this action, and no arrow is present.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8628, out 868, 8.27 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear sky. Ahead, there is a wide intersection or
                        open area with a bike lane and a motorcycle to the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bike lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate the separation of
                        same-direction traffic lanes. | markings: No markings are present to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the bike
                        lane on the right. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 762, 7.04 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overpass to the left and a park-like area with
                        trees to the right. The road ahead appears to be a straight continuation of the
                        current roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left indicates another lane of the same direction, and a white line
                        on the right indicates the edge of the roadway. | roles: The white solid lines
                        correctly represent lane separation and the right edge of the roadway. | markings: The
                        straight arrow is consistent with the straight roadway ahead. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead as indicated by the lane
                        arrow. Lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 855, 8.06 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with a dedicated bicycle lane and a motor vehicle lane. The car is
                        positioned in a lane that appears to be a bicycle lane or a shared lane, with a large
                        white arrow pointing straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead in the center of my
                        lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 2 (rightmost) are consistent
                        with a white lane line on my left and a white edge line/curb on my right. | roles: The
                        white solid line on the left correctly identifies a lane-line, and the white solid
                        line on the right correctly identifies an edge-line. | markings: The straight arrow is
                        consistent with the lane's forward direction. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 716, 5.92 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings and trees on both sides. The road ahead
                        appears to be a continuous street with multiple lanes of traffic. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:merge_left (insufficient): No markings are
                        visible in my lane.; arrow:merge_right (insufficient): No markings are visible in my
                        lane.; arrow:two_way_left (insufficient): No markings are visible in my lane.;
                        text:only (insufficient): No markings are visible in my lane.; text:bus
                        (insufficient): No markings are visible in my lane.; text:hov (insufficient): No
                        markings are visible in my lane.; text:stop (insufficient): No markings are visible in
                        my lane.; text:keep_clear (insufficient): No markings are visible in my lane.;
                        text:speed_limit (insufficient): No markings are visible in my lane.;
                        symbol:hov_diamond (insufficient): No markings are visible in my lane.; symbol:bike
                        (insufficient): No markings are visible in my lane.; symbol:other (insufficient): No
                        markings are visible in my lane.; area:left_turn_waiting (insufficient): No markings
                        are visible in my lane.; area:two_way_left_turn_lane (insufficient): No markings are
                        visible in my lane.; area:grid (insufficient): No markings are visible in my lane.;
                        area:channelizing (insufficient): No markings are visible in my lane.; line:crosswalk
                        (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) are consistent with the
                        boundaries: a yellow line on my left and a white edge line on my right. | roles: The
                        yellow line on the left and white line on the right fit the roles of a lane line and
                        edge line respectively. | markings: No markings were observed in my lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow line on the left (US-3B.06-05-06)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line on the right
                        (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 8628, out 1201, 10.57 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the left. Ahead, there is a
                        clear roadway with several lanes of traffic moving in the same direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk/median area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on the left with a curb indicates an edge line, and a white line on the right
                        indicates a lane line. | roles: The white solid lines correctly fit the roles of edge
                        line and lane line for a right-hand traffic system. | markings: No markings are
                        present to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the roadway. You may proceed straight ahead, but lane
                        changes to the right are prohibited by the solid white line. No left turn or right
                        turn markings are present.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 789, 6.57 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a median and a sidewalk on the right. Ahead, there is
                        a clear roadway with multiple lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with a
                        yellow line on the left and a white line/curb on the right. | roles: The yellow line
                        on the left correctly identifies a lane separation, and the white line on the right
                        correctly identifies the edge of the roadway. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose and the surrounding boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that moving straight ahead is a permissible
                        movement in this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow line on the
                        left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to continue straight ahead. Lane changes
                        to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 706, 5.94 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk/building area on
                        the right. Ahead, there is a clear roadway with several lanes of traffic. (lanes 3,
                        mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the rightmost lane/shoulder area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        delineate lanes in the same direction of travel. | markings: No markings were observed
                        in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 631, 6.55 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings and trees on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid yellow line is visible in the center of the
                        road, but it is not inside my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (opposite traffic) and the white
                        solid line identifies the right edge. | markings: No markings are inside my lane; the
                        yellow line is a boundary. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but in this context (right-hand traffic), it delineates the
                        separation of opposite traffic. [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 810, 7.45 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a mix of vehicles, including a bus and a scooter. The
                        road continues straight ahead with trees and buildings lining both sides. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bicycle/scooter lane or sidewalk area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line is visible on the right, and a solid
                        white line is on the left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on the left and a white edge line on the right. | roles: The white
                        lines correctly represent same-direction lane separation and the right edge of the
                        roadway. | markings: No specific arrows or words are visible in my lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 796, 7.69 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with trees and buildings on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        yellow line on the left and a white line on the right. | roles: The yellow line on the
                        left correctly identifies a separation from another lane, and the white line on the
                        right correctly identifies the edge of the roadway. | markings: The straight arrow is
                        consistent with the straight road ahead and the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a solid yellow lane line between same-
                        direction lanes in this context, but generally discourages crossing. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that moving straight ahead is a permissible
                        movement in this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): The solid yellow line discourages or prohibits
                        crossing.
Step 6  change_right    prohibited (correct): The solid white edge line and curb prohibit moving onto the
                        sidewalk.
Step 6  go_straight     allowed (contested, correct): The straight arrow indicates this movement is permitted.
Step 6  turn_left       not_applicable: No arrow or marking allows for a left turn.
Step 6  turn_right      not_applicable: No arrow or marking allows for a right turn.
Step 6  u_turn          not_applicable: No arrow or marking allows for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead as indicated by the
                        pavement arrow. Lane changes to the left are discouraged/prohibited by the solid
                        yellow line, and moving to the right is prohibited by the edge line and curb.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8628, out 742, 8.52 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with buildings and trees on both sides. The road ahead
                        appears to be a straight continuation or a large intersection. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white line on my left and a white line/curb on my right. | roles: The white lines
                        correctly delineate lanes in the same direction of travel. | markings: No markings are
                        present to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
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
Tokens                  in 8628, out 785, 5.69 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The road is wet, and there are
                        pedestrians and cyclists visible. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight and to the right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries
                        (lane line on left, edge line on right). | roles: The white solid lines correctly
                        represent a lane line and an edge line in a right-hand traffic system. | markings: The
                        straight-right arrow is consistent with the lane's position and the surrounding
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is used for straight or right-
                        turn movements. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 818, 7.19 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a tunnel or underpass ahead. The road is bounded by
                        concrete walls on both sides. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the rightmost lane, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-line, and the white solid line on
                        the right correctly identifies an edge-line. | markings: The straight arrow is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is discouraged but not prohibited.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (correct): The white dashed line on the left discourages but does not prohibit
                        a lane change.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white line and curb on the right
                        prohibit moving onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): The straight arrow indicates that going straight is a
                        permissible movement.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. A lane change to the left is
                        discouraged but permitted, while moving to the right is prohibited by the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 715, 5.8 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway with a concrete barrier on the right and a
                        wall on the left. An overpass is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a concrete barrier/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane appears clear of specific arrows or words.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line/curb on the right. | roles: The white dashed
                        line correctly identifies a lane-line, and the white solid line correctly identifies
                        an edge-line. | markings: No markings are clearly visible in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane as it is marked with a dashed line. Do not attempt
                        to move to the right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 850, 8.41 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide roadway and a sidewalk/parking area on the right.
                        The road continues straight ahead. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane itself has no arrows or words.; area:two_way_left_turn_lane (full): No
                        markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a solid white line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-line, and the solid white line on
                        the right correctly identifies an edge-line. | markings: No markings were found in my
                        lane, which is consistent with the lack of specific movement indicators. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is discouraged but not prohibited.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:two_way_left_turn_lane: No rule applies as no two-way left-turn lane was
                        identified.
Step 6  change_left     allowed (correct): The white dashed line on the left discourages but does not prohibit
                        crossing.
Step 6  change_right    prohibited (correct): The solid white line and curb on the right prohibit moving onto
                        the sidewalk.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane allow or prohibit a left turn.
Step 6  turn_right      not_applicable: No markings in my lane allow or prohibit a right turn.
Step 6  u_turn          not_applicable: No markings in my lane allow or prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: No two-way left-turn lane or waiting area was identified.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Lane changes to the left are discouraged
                        but permitted, while moving to the right onto the sidewalk is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'line:stop_line'], missed []), actions True, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 789, 6.64 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an overpass ahead. My car is in a lane that appears to be a
                        one-way street or a ramp, with a wall on the right and a hedge/barrier on the left.
                        (lanes 1, mine 1, full)
Step 2  Left            A dense hedge and a low concrete barrier form the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid red wall and a concrete curb form the right side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in the lane.
Step 4  Cross-check     position: The lane count and position are consistent with the physical boundaries
                        (curbs/walls) on both sides. | roles: The physical boundaries correctly serve as edge
                        lines. | markings: No markings are present to contradict the lane's purpose. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: No specific rule for a hedge/barrier, but it acts as a physical edge.
                        [null]
Step 5  Rule            right_boundary: No specific rule for a wall/curb, but it acts as a physical edge.
                        [null]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited due to the physical boundaries (hedge and wall).
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8628, out 742, 7.69 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway approaching a large intersection. The sun is high, creating
                        significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal railing/fence form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in the center of my lane.;
                        line:stop_line (full): A solid white stop line is visible across the lane before the
                        intersection.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white lane line
                        on my left and a white edge line/curb on my right. | roles: The white lines and curb
                        correctly identify the lane boundaries. | markings: The left-turn arrow and stop line
                        are consistent with an approach to an intersection. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement in this
                        lane. [US-3B.23-01]
Step 5  Rule            line:stop_line: The stop line indicates the point behind which the vehicle must stop.
                        [US-3B.19-01-02]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     prohibited (correct): prohibited
Step 6  turn_left       stop_first (WRONG, label prohibited): stop_first
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Your lane is designated for a left turn only. You must come to a complete stop at the
                        white stop line before making your turn. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 937, 8.55 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway under an overpass. The road ahead appears to be a straight
                        stretch of highway or a large boulevard. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line separates the lane to my left from
                        the lane further left.; line:stop_line (insufficient): Nothing is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        same-direction traffic flows. | markings: No markings are visible in my lane to
                        contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 826, 5.53 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        divided highway with a guardrail on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        bordered by a guardrail.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): A blue circle with a white '60' inside is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        lines correctly serve as a lane line and an edge line for a right-hand traffic system.
                        | markings: The '60' speed limit marking is consistent with the highway environment. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            text:other: The '60' marking provides a guidance message for the speed limit.
                        [US-3B.20-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and it is the default
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight, but lane
                        changes to the left or right are discouraged/prohibited by the solid lines. Observe
                        the 60 speed limit indicated on the pavement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:other'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 725, 6.4 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a bus and other vehicles ahead. The road appears to be
                        a divided highway or a wide boulevard. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify the
                        boundaries between lanes of the same direction. | markings: No markings are present,
                        which is consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 772, 6.24 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a clear sky and trees on both sides. The road ahead appears
                        to be a straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; arrow:merge_left (full): No markings are visible in my lane.;
                        arrow:merge_right (full): No markings are visible in my lane.; arrow:two_way_left
                        (full): No markings are visible in my lane.; no_turn:left (full): No markings are
                        visible in my lane.; no_turn:right (full): No markings are visible in my lane.;
                        text:only (full): No markings are visible in my lane.; text:bus (full): No markings
                        are visible in my lane.; text:hov (full): No markings are visible in my lane.;
                        text:stop (full): No markings are visible in my lane.; text:keep_clear (full): No
                        markings are visible in my lane.; text:speed_limit (full): No markings are visible in
                        my lane.; symbol:hov_diamond (full): No markings are visible in my lane.; symbol:bike
                        (full): No markings are visible in my lane.; symbol:other (full): No markings are
                        visible in my lane.; area:left_turn_waiting (full): No markings are visible in my
                        lane.; area:two_way_left_turn_lane (full): No markings are visible in my lane.;
                        area:grid (full): No markings are visible in my lane.; area:channelizing (full): No
                        markings are visible in my lane.; line:crosswalk (full): No markings are visible in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly delineate lanes
                        of the same direction. | markings: No markings were observed, which is consistent with
                        a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The dashed white line on the left allows for a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white line on the right prohibits a lane
                        change.
Step 6  go_straight     allowed (contested, correct): No markings govern this action, and it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action, and it is not applicable.
Step 6  turn_right      not_applicable: No marking governs this action, and it is not applicable.
Step 6  u_turn          not_applicable: No marking governs this action, and it is not applicable.
Step 6  enter_waiting_areanot_applicable: No marking governs this action, and it is not applicable.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change into the left lane
                        as it is marked with a dashed line, but you should not change into the right lane as
                        it is marked with a solid line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'no_turn:left', 'no_turn:right', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight allowed without the stop
                        that the STOP or 停 marking in my lane requires']
Tokens                  in 8628, out 1264, 11.32 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with a median separating opposing traffic. The road ahead
                        is straight with several lanes of traffic moving in the same direction. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be
                        the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left indicates another lane of my direction, and a white line on the
                        right indicates the edge of the roadway. | roles: The white solid lines correctly
                        represent lane separation and the right edge of the roadway. | markings: No markings
                        are present, which is consistent with the clear lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged or prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 792, 7.12 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky and bright sunlight. The road
                        ahead appears to be a straight stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        adjacent to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white line on my left and a white line/barrier on my right. | roles: The white solid
                        lines correctly delineate same-direction traffic and the right edge of the roadway. |
                        markings: No markings are present, which is consistent with a standard through-lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the concrete barrier
                        on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through-lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid line markings and the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 809, 7.1 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway under an overpass. The road ahead appears to be a straight
                        stretch or a wide intersection area. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on the left and a white line on the right. | roles: The yellow line on the
                        left and white line on the right are consistent with standard lane delineations for
                        same-direction traffic. | markings: The straight arrow is consistent with the lane's
                        forward path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left boundary line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead as indicated by
                        the pavement arrow. Lane changes to the left or right are prohibited by the solid lane
                        markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 839, 7.07 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a divided median. The sun is low in the sky, creating a hazy
                        atmosphere. There is a gantry with signs ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify
                        lane-to-lane boundaries for same-direction traffic. | markings: No markings are
                        present, which is consistent with a standard highway lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may proceed straight, but lane
                        changes to the left or right are discouraged or prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 786, 7.75 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead power lines and a concrete barrier on
                        the right. The road ahead appears to be a straight stretch of highway. (lanes 3, mine
                        2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        bordered by a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white dashed line is on my left and a white solid line/curb is on my right. | roles:
                        The white dashed line correctly identifies a lane-line (same direction), and the white
                        solid line correctly identifies an edge-line. | markings: No markings are present,
                        which is consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or area.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or area.
Step 6  u_turn          not_applicable: Not applicable as there is no u-turn arrow or area.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move to the
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 879, 7.64 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a median on the left and a shoulder/barrier on the right.
                        The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand shoulder/edge.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white lane line is visible to the left of my lane.;
                        line:stop_line (insufficient): A white lane line is visible to the right of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        lines correctly represent a lane line and an edge line for a right-hand traffic
                        system. | markings: No markings were clearly identified within my lane; the lines
                        observed are boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 675, 6.56 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with overhead signs. The road ahead is a straight stretch of
                        highway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        delineate lanes of the same direction. | markings: The straight arrow is consistent
                        with the straight road ahead and the lane boundaries. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 802, 7.39 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. The road ahead is clear, and
                        the car is traveling in a lane with several others nearby. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an emergency
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow is consistent with the 'Through Lane'
                        overhead sign for my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        emergency lane to the right. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is designated for through traffic.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 838, 5.93 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with buildings and trees on both sides. The road ahead
                        appears to be a straight stretch with multiple lanes of traffic. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        lane lines on both sides. | roles: The white solid lines correctly delineate lanes of
                        traffic moving in the same direction. | markings: No markings were observed in the
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
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
Tokens                  in 8628, out 609, 6.18 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming interchange or exit. The road is
                        straight ahead with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be an
                        exit or shoulder area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is visible in the lane to my right.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['text:speed_limit']), actions
                        False, unsafe [], citation in_pack_not_accepted, contradictions ['turn_left
                        not_applicable although an arrow shows it', 'turn_right not_applicable although an
                        arrow shows it']
Tokens                  in 8628, out 917, 8.37 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overhead gantry containing traffic signals and
                        signs. The road ahead appears to be a large intersection or a major junction. (lanes
                        3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white lane line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (opposite traffic) and the white
                        solid line identifies a same-direction lane divider. | markings: The straight arrow is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: A double yellow line or a specific configuration is required for no-
                        passing; however, a single solid yellow line is generally used to separate opposite
                        traffic. [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white line discourages or prohibits crossing into the adjacent
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 850, 7.77 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear view ahead. The road appears to be a divided
                        highway or a large boulevard with a median on the right. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a green-painted median/curb area on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on the left and a solid white line/curb on the right. | roles: The
                        white dashed line on the left correctly identifies a same-direction lane line, and the
                        white solid line on the right correctly identifies an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the surrounding
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight ahead is a permissible
                        movement for this lane. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): The dashed white line on the left allows for a lane
                        change.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white line and curb on the right prohibit
                        moving to the right.
Step 6  go_straight     allowed (contested, correct): The straight arrow in my lane allows for going straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane as it is marked with a
                        dashed line. You are permitted to proceed straight ahead. Do not attempt to move to
                        the right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 745, 7.88 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with overhead wires for trams or trolleybuses. Ahead is a
                        continuation of the roadway with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from a tram/bus lane on the right.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the yellow
                        boundaries on both sides. | roles: The yellow lines correctly delineate the separation
                        of traffic flows and special lanes. | markings: The straight arrow is consistent with
                        the lane's purpose. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line discourages or prohibits crossing into the left
                        lane. [US-3A.04-01]
Step 5  Rule            right_boundary: The yellow line separates my lane from the special lane (tram/bus) to
                        the right. [US-3A.03-03-04]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 826, 7.92 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear sky. Ahead, the road continues straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow is consistent with the lane's role as a
                        through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 829, 6.51 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a subway station on the right. The road ahead appears
                        to be a straight continuation or a large intersection area. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from a lane to my right, which appears to be a
                        transit or special lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.
Step 4  Cross-check     position: The lane count and my position as the middle lane are consistent with the
                        yellow lines on both sides. | roles: Yellow lines are used for separation of traffic
                        flows or special lanes, which fits the urban context. | markings: The straight arrow
                        aligns with the lane's purpose and the surrounding boundaries. | unseen: None |
                        result: consistent
Step 5  Rule            left_boundary: The solid line discourages or prohibits crossing to the left.
                        [US-3A.04-01]
Step 5  Rule            right_boundary: The solid line discourages or prohibits crossing to the right.
                        [US-3A.04-01]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. Do not attempt to change
                        lanes to the left or right as the solid yellow lines prohibit such maneuvers. Proceed
                        straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 818, 7.87 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the left and a median/curb
                        on the right. Ahead is a clear stretch of road with several lanes of traffic. (lanes
                        3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a lane to the left (likely a bus lane).
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb/median area are on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large yellow arrow pointing straight ahead is painted in my
                        lane.; area:channelizing (full): A yellow-colored pavement area with diagonal lines is
                        visible to the right of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a yellow line on
                        the left and a yellow line/curb on the right. | roles: The yellow lines correctly
                        delineate the separation of traffic flows and the edge of the roadway. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line discourages or prohibits crossing into the lane
                        to the left. [US-3A.04-01]
Step 5  Rule            right_boundary: The solid white/yellow line delineates the right-hand edge of the
                        roadway. [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid yellow lines and curb prohibit such maneuvers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 894, 7.72 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The sun is low in the sky,
                        creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bus lane or a dedicated lane for a bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left_boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary line.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 834, 7.17 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center. The road appears to be a one-way or
                        multi-lane street with overhead wires for public transit. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: White solid lines are appropriate for separating lanes
                        of the same direction. | markings: No markings are present to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        per US-3B.06-05-06.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        per US-3B.06-05-06.
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 796, 14.56 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road in China, where traffic keeps to the right.
                        Ahead, there is an intersection with several lanes of traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes for traffic moving in the same direction. | markings: The straight arrow in my
                        lane is consistent with the lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead but are
                        prohibited from changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 686, 6.64 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban intersection with multiple lanes of traffic. The sun is creating a
                        significant glare on the left side of the photo. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible across the lane at the
                        intersection.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on my left and a white solid line on my right. | roles: The white dashed line
                        correctly identifies a lane-line, and the white solid line correctly identifies an
                        edge-line. | markings: The stop line is consistent with the approach to an
                        intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:stop_line: Vehicles are required to stop behind the white line. [US-3B.19-01-02]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the white dashed lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     stop_first (contested, label not_determined): Stop first due to the stop line
                        [US-3B.19-01-02].
Step 6  turn_left       stop_first: Stop first due to the stop line [US-3B.19-01-02].
Step 6  turn_right      stop_first: Stop first due to the stop line [US-3B.19-01-02].
Step 6  u_turn          stop_first: Stop first due to the stop line [US-3B.19-01-02].
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before proceeding through the
                        intersection. You are permitted to change into the left lane, but you cannot move to
                        the right of the edge line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8628, out 945, 15.42 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a subway station ahead. The car is in a lane moving
                        forward toward the station. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-colored lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on the left and a white line on the right. | roles: The yellow line on the
                        left and white line on the right are consistent with standard lane delineations. |
                        markings: The straight arrow is consistent with the lane's forward path. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line discourages or prohibits crossing to the left.
                        [US-3A.04-01]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing to the right.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid lines prohibit this movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 827, 6.8 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear view ahead. The road appears to be a divided
                        thoroughfare with a median or separation on the left. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which has a yellow-
                        colored pavement area.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A yellow arrow pointing straight ahead is visible in my lane.;
                        area:channelizing (full): A yellow-colored pavement area with diagonal lines is to the
                        right of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        yellow lane lines on both sides. | roles: The yellow lines correctly delineate the
                        separation of traffic flows in the same direction (right-hand traffic context). |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. The
                        channelizing area to the right is consistent with the right boundary. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white (or yellow in this context) line discourages or
                        prohibits crossing. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid yellow line discourages or prohibits crossing.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates the mandatory or permissible movement of going
                        straight. [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead as indicated by
                        the pavement arrow. Lane changes to the left or right are prohibited by the solid
                        yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 895, 8.5 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with overhead wires, likely for a tram or trolleybus. The
                        road ahead is straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete curb/barrier form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Two parallel solid yellow lines are painted in the
                        center of the roadway.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on my left separates me from another lane, and a white line/curb on my
                        right marks the edge. | roles: The yellow line on the left correctly identifies a lane
                        separation, and the white line on the right correctly identifies the edge. | markings:
                        The double yellow lines indicate a two-way left-turn lane to the left, which is
                        consistent with the yellow lane line on my left. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:two_way_left_turn_lane: The markings delineate a lane that can be used by traffic
                        in either direction as part of a left-turn maneuver. [US-3B.05-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 886, 9.04 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the right and a wide intersection or open
                        area ahead. The car is in a central lane. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bus lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow is consistent with the lane's role and
                        the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the bus
                        lane on the right. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 836, 7.76 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection with an overpass. The road is
                        wide with multiple lanes of traffic moving in the same direction. (lanes 4, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.; arrow:left (full): A white arrow pointing left is in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is in the lane to my right.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow in my lane is consistent with the
                        lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left not_applicable although an arrow
                        shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 8628, out 917, 9.07 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in one of
                        the center lanes. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: White dashed lines correctly identify
                        lane-to-lane separation for same-direction traffic. | markings: The straight arrow is
                        consistent with the lane's role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a white dashed line, which
                        allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a white dashed line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): The straight arrow in my lane permits going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight or change lanes to the left or
                        right as needed. No specific turn markings are present for your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 665, 6.44 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus and other vehicles ahead. The road appears to be
                        a one-way street or a multi-lane roadway with a median or curb on the left. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        delineate lanes of traffic moving in the same direction. | markings: The straight
                        arrow is consistent with the lane's function and the surrounding boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 857, 7.9 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban street approaching an intersection with a
                        crosswalk. My car is positioned in one of the center lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white crosswalk is visible ahead across the lanes.
Step 4  Cross-check     position: The lane count of 4 and my position as lane 2 are consistent with the white
                        lane lines on both sides. | roles: The white solid lines correctly delineate same-
                        direction traffic flows. | markings: The crosswalk is consistent with an approaching
                        intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: No specific rule provided for crosswalks in the list, but they
                        indicate a pedestrian crossing area.
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the solid white lane line on
                        the left.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white lane line on
                        the right.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it and it is the default
                        movement.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or marking is present in my lane.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or marking is present in my
                        lane.
Step 6  u_turn          not_applicable: Not applicable as no u-turn arrow or marking is present in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may proceed straight through the intersection. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 694, 7.01 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a wide intersection ahead. The road has overhead wires
                        for trams or trolleybuses. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which contains a large
                        truck.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is visible in the lane to my right.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (correct): allowed by the dashed white line (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (US-3B.23-01)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change into the left
                        lane. Changing into the right lane is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed []), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['turn_left not_applicable although an
                        arrow shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 8628, out 948, 8.17 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or junction ahead. The road appears to be
                        a one-way or multi-lane one-way street given the markings. (lanes 3, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from the sidewalk/pedestrian
                        area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): A white character '直' (straight) is painted in my lane.; text:other
                        (full): A white character '左' (left) is painted in the lane to my left.; text:other
                        (full): A white character '右' (right) is painted in the lane to the far left.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        dashed line is on my left and a solid line/curb is on my right. | roles: The white
                        dashed line correctly identifies a lane-line for same-direction traffic, and the white
                        solid line/curb correctly identifies the right edge. | markings: The 'straight'
                        character in my lane is consistent with the lane's role as a through lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line and curb delineate the right edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            text:other: The 'straight' character guides the driver to continue forward in this
                        lane. [US-3B.20-01]
Step 6  change_left     allowed (contested, correct): allowed by the dashed white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the 'straight' character and lack of
                        restrictive markings [US-3B.20-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. You are permitted to
                        change into the lane to your left, but you cannot move further to the right as it is
                        the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 1031, 10.22 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow is consistent with the lane's purpose
                        and the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that moving straight ahead is a permissible
                        movement in this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid white lines prohibit it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 823, 6.32 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. Ahead, there is a
                        wide intersection or open area with a white vehicle in the lane directly ahead. (lanes
                        2, mine 1, full)
Step 2  Left            A raised concrete curb and a solid white line separate my lane from the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A large white rectangle is painted in the center of my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (left edge
                        line/curb and right lane line). | roles: The white solid lines and curb correctly
                        define the boundaries for a right-hand traffic system. | markings: The rectangle
                        marking is centered in the lane and does not contradict the boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line and curb delineate the left-hand edge of the
                        roadway. [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            symbol:other: The pavement marking is used for regulating, warning, or guiding
                        traffic. [US-3B.20-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white line and curb (left_boundary).
Step 6  change_right    prohibited (correct): prohibited by the solid white line (right_boundary).
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 853, 8.13 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings and trees on both sides. The road ahead
                        appears to be a continuous stretch of city street. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (opposite traffic) and the white
                        solid line identifies the right edge. | markings: The straight arrow is consistent
                        with the lane's role and the surrounding boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but in this context (right-hand traffic), it delineates the separation of
                        opposite traffic. [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates the mandatory or permissible movement of going
                        straight. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid boundary lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 857, 7.82 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. The car is positioned in a lane
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a center line on
                        the left and an edge line on the right. | roles: The yellow center line and white edge
                        line match the standard roles for a right-hand traffic system. | markings: No markings
                        are present to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but in this context, it delineates the separation of opposite traffic.
                        [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 766, 7.35 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway approaching a large intersection with a
                        pedestrian crosswalk. The road appears to be a divided highway or a wide urban
                        boulevard. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with a white
                        line on my left and a white line/curb on my right. | roles: The white solid lines
                        correctly delineate same-direction traffic and the right edge. | markings: The
                        straight arrow is consistent with the lane's path toward the intersection. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        the curb on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking in my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight movement. You may proceed straight through
                        the intersection but are prohibited from changing lanes to the left or right due to
                        the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 691, 6.76 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. A bus is directly
                        ahead in the lane to the left. (lanes 3, mine 3, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with a center line on
                        my left and an edge line on my right. | roles: The yellow center line and white edge
                        line match the expected roles for a right-hand traffic system. | markings: No markings
                        were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but here it separates lanes of the same direction (right-hand traffic).
                        [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. Lane changes to the
                        left are prohibited by the solid yellow line, and moving further right is restricted
                        by the edge of the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 644, 6.17 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway, possibly a ramp or a dedicated transit corridor,
                        with a large building on the right and a covered structure on the left. The road ahead
                        appears to be a straight path leading toward a distant area. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A metal railing and a concrete curb form the right edge of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        a yellow lane line on my left and a curb/railing on my right. | roles: The yellow
                        solid line on the left correctly identifies a lane separation, and the curb on the
                        right correctly identifies the edge of the roadway. | markings: No markings were
                        observed, which is consistent with the clear pavement. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white (or yellow in this context) line discourages or
                        prohibits crossing into the adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The right edge line delineates the edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow line on the left
Step 6  change_right    prohibited (correct): prohibited by the curb and railing on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of this section. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left due to the solid yellow line and to the
                        right due to the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8628, out 686, 6.94 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a wide boulevard layout. Ahead, the road continues
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-colored bike lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane to my right, not in
                        my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        lane lines on both sides. | roles: The white solid lines correctly delineate lanes of
                        the same direction. | markings: The bike symbol is correctly identified as being in
                        the adjacent lane, not my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the bike lane on the
                        right. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): The solid white line on the left discourages this
                        action.
Step 6  change_right    prohibited (correct): The solid white line on the right discourages this action.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_applicable: No markings govern this action.
Step 6  turn_right      not_applicable: No markings govern this action.
Step 6  u_turn          not_applicable: No markings govern this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left or right are
                        discouraged by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 627, 5.7 s
```
