# Reasoning of lane run 20261117_230334_laneC_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current roadway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line to the right of my lane. Photo 2 shows a solid
                        yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; arrow:straight
                        (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line on the left separates me from another
                        lane, and a yellow line on the right marks the edge of the roadway. | roles: The white
                        dashed line correctly functions as a lane line, and the yellow line correctly
                        functions as an edge line. | markings: The left-turn and straight-ahead arrows are
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is discouraged but not prohibited.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line (or yellow edge line) delineates the edge of the
                        roadway. [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement in this
                        lane. [US-3B.23-01]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     allowed (correct): The white dashed line on the left discourages but does not prohibit
                        a lane change.
Step 6  change_right    prohibited (contested, correct): The yellow edge line on the right delineates the
                        roadway boundary.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow indicates this movement is
                        permissible.
Step 6  turn_left       allowed: The left-turn arrow indicates this movement is permissible.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. A lane change to the
                        left is discouraged but permitted, while moving to the right is prohibited as it is
                        the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 842, 9.05 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. Ahead, there is a clear roadway with
                        multiple lanes and a potential intersection or continuation of the road. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid yellow line clearly visible next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. No
                        markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line on the left indicates another lane of
                        my direction, and a yellow line on the right indicates the edge of the roadway. |
                        roles: The white dashed line fits the role of a lane line, and the yellow line fits
                        the role of an edge line. | markings: No markings are in my lane, and the left-turn
                        arrow is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line (or yellow edge line) delineates the edge of the
                        roadway. [US-3B.09-01-02]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you must stay within the roadway and
                        cannot move to the right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 906, 8.99 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The car is traveling straight
                        ahead in a lane with a vehicle directly in front. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line as a solid line next
                        to the car. Further ahead in Photo 1, the line appears to remain solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a white edge line on the right.
                        | roles: The white color and solid pattern are consistent with lane and edge line
                        roles. | markings: The straight arrow is consistent with the lane's purpose and
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        discouraged/prohibited by the solid markings, and the lane-use arrow indicates that
                        only straight movement is permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 877, 8.42 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overpass to the right and a fenced-off area to the
                        left. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a white curved line in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        curved symbol is centered in the lane and does not conflict with the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            symbol:other: The symbol is used for regulating, warning, or guiding traffic.
                        [US-3B.20-01]
Step 6  change_left     prohibited (correct): prohibited
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
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 883, 8.21 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure on the right. The car is
                        traveling in a lane bounded by a fence/curb on the left and a white line on the right.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line and a physical fence/curb on the left. Photo 2 shows a
                        solid white line next to the car and a physical fence/curb further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line next to the
                        car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in the lane ahead pointing
                        straight.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (1) agree with the left edge line and right lane line. | roles: The white solid lines
                        and curb correctly identify the left edge and right lane boundary. | markings: The
                        straight arrow in the lane matches the straight-ahead movement. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You should continue straight ahead as indicated by the
                        lane-use arrow. Lane changes to the right are discouraged/prohibited by the solid
                        white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 879, 9.44 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight stretch with a median on the left and a sidewalk/parking area on the
                        right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line and a raised curb/median with plants. Photo 2 shows a
                        solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line. Photo 2 shows a solid white line next to the car and
                        a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries. The left boundary is an edge line (curb/median) and the
                        right boundary is an edge line (sidewalk/parking). | roles: The white solid lines
                        correctly function as edge lines for the roadway. | markings: The straight arrow in my
                        lane is consistent with the straight road ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-lane roadway. You are permitted to proceed
                        straight ahead as indicated by the pavement arrow. Lane changes to the left or right
                        are prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 903, 8.78 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a central divider and a sidewalk/fence on the right.
                        Ahead, there is a wide intersection or open area with multiple lanes of traffic.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a solid white line side by side on the right.
                        Photo 2 shows a solid yellow line and a solid white line side by side next to my car.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. Photo
                        2 shows a white right-turn arrow in the lane to my right.; arrow:right (full): Photo 2
                        shows a white right-turn arrow in the lane to my right.; arrow:right (full): Photo 2
                        shows a white right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        match the boundaries: a white dashed line on the left and a yellow/white solid-dashed
                        line on the right. | roles: The white dashed line correctly identifies a lane-line,
                        and the yellow/white solid-dashed line correctly identifies a center-line (separating
                        my lane from the right-hand side traffic/turn lane). | markings: The arrows in
                        adjacent lanes are consistent with the lane layout. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for crossing into the left lane with care.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the right-hand lane for
                        passing. [US-3B.01-04]
Step 5  Rule            arrow:left: The arrow in the left lane indicates a mandatory or permissible left turn.
                        [US-3B.23-01]
Step 5  Rule            arrow:right: The arrow in the right lane indicates a mandatory or permissible right
                        turn. [US-3B.23-01]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid yellow center line
                        [US-3B.01-04].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings in my lane prohibit it.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the left lane. Changing into the right lane is
                        prohibited by the solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_left not_applicable although an arrow shows it', 'turn_right not_applicable
                        although an arrow shows it']
Tokens                  in 9491, out 943, 8.69 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure overhead. The road ahead appears
                        to be a straight stretch with multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.; no_turn:u_turn (insufficient): No markings are visible in my lane in Photo 1
                        or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        per [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        per [US-3B.06-05-06]
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
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 793, 8.48 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a skyline in the distance. The car is traveling in a
                        lane that appears to be part of a multi-lane flow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car's left side.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line very close to the car's right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to the
                        left of my lane. No markings are visible in my lane.; no_turn:right (insufficient):
                        Photo 1 shows a white left-turn arrow in the lane to the left of my lane. No markings
                        are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow solid line correctly identifies a center line
                        (separation of opposite flows) and the white solid line identifies an edge line. |
                        markings: No markings are in my lane, which is consistent with the lane's role as a
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but here it delineates the separation of opposite traffic flows.
                        [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            no_turn:left: no marking governs this action
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 786, 7.68 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the right. My car is in a through
                        lane, and an intersection or turn area is ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left. Photo 2 shows a solid white line to the
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line to the right. Photo 2 shows a solid yellow line to
                        the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows a large white bus symbol and the word 'BUS' in the lane
                        to the right.; arrow:right (full): Photo 1 shows a white arrow in the lane to the
                        right indicating a turn.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on the left and a yellow line on the right. |
                        roles: The white line on the left separates lanes in the same direction; the yellow
                        line on the right separates my lane from the bus lane. | markings: The bus markings
                        and arrow are in the lane to the right, not in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid yellow line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 5  Rule            text:bus: The lane to the right is a preferential bus lane. [US-3E.03-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings in my lane prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right', 'text:bus'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 9491, out 766, 7.12 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the right. My car is in a
                        lane next to a bus lane. There is an intersection or lane change area ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bus lane on the right.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows a bus lane marking on the right. Photo 2 shows a bus
                        lane marking on the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line on the left and a solid white line on
                        the right. | roles: The white dashed line on the left and solid white line on the
                        right fit the roles of lane lines. | markings: The bus marking on the right is
                        consistent with the solid white line separating my lane from a special lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the solid white line is discouraged or prohibited.
                        [US-3B.06-05-06]
Step 5  Rule            text:bus: The lane to the right is reserved for buses. [US-3E.03-02]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed line (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane, but you are prohibited from moving into the bus
                        lane on your right. Proceed straight ahead.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 926, 7.77 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a concrete barrier on the left and a metal barrier on
                        the right. Ahead, there is an overpass and a signalized intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line and a concrete barrier on the left. Photo 2 shows a
                        solid white line and a concrete barrier on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows two solid yellow lines in the center of the lane,
                        forming a large 'X' or cross shape.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white edge line on the left and a white lane line on
                        the right. | roles: The white solid lines correctly function as an edge line and a
                        lane line. | markings: The yellow cross-hatching is centered in the lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the adjacent lane.
                        [US-3B.06-05-06]
Step 5  Rule            symbol:other: The yellow markings are used to discourage travel on certain paved
                        areas. [US-3B.25-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 870, 8.43 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass. The road ahead appears to be a
                        straight stretch with multiple lanes of traffic moving in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right. Photo 2 shows this yellow line as a solid
                        line near my car. Further ahead in Photo 1, the line appears to remain solid yellow.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow in my lane pointing straight
                        ahead. Photo 1 shows the same arrow.; text:other (full): Photo 2 shows white
                        characters (Chinese) in my lane. Photo 1 shows these characters as well.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane) agree with the boundaries: a white lane line is on my left and a yellow
                        edge line is on my right. | roles: The white dashed line correctly functions as a lane
                        line, and the solid yellow line correctly functions as a right edge line. | markings:
                        The straight arrow and text are consistent with a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line (though yellow here, the rule for edge lines
                        applies) delineates the right-hand edge of the roadway. [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [US-3B.23-01]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change into the left
                        lane. Changing into the right lane or making any turns is prohibited by the markings
                        and boundaries.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'text:other'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 967, 10.11 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a large intersection ahead. My car is in
                        a lane that appears to be a through lane or a turn lane approaching a junction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow center line on the left and a white edge line on the
                        right. | roles: The yellow solid line correctly identifies a center line (separating
                        opposite traffic) and the white solid line identifies the right edge. | markings: The
                        straight arrow is consistent with the lane's role as a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line separates my lane from traffic in the opposite
                        direction. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes or making turns. Follow the straight arrow and stay between the yellow
                        and white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9491, out 689, 6.06 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an overpass and overhead signs. My car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose as a through lane.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-through traffic.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 858, 9.03 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane traveling
                        straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this line clearly as a solid white line next to a raised
                        curb/median area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a white edge line on the right.
                        | roles: The white solid line on the left correctly functions as a lane line, and the
                        white solid line on the right correctly functions as an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-through
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You should continue
                        straight and avoid changing lanes, as the solid white lines on both sides discourage
                        or prohibit lane changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 726, 6.32 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane that appears to be the rightmost lane of the main roadway, adjacent to a sidewalk
                        and a curb. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white lane line separating my lane from the lane to my left. Photo 2
                        shows this same white line clearly as a solid line near my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a sidewalk on the right. Photo 2 shows a solid white
                        line painted on the pavement next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with the left lane line and right edge line. | roles: The white solid
                        line on the left is a lane line; the white solid line and curb on the right are an
                        edge line. | markings: The straight arrow in my lane is consistent with the lane's
                        role and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You may proceed straight
                        ahead, but lane changes to the left or right are discouraged/prohibited by the solid
                        markings. No turns are permitted from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 732, 7.88 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
                        Photo 1 shows the same arrow.; area:channelizing (full): Photo 2 shows white diagonal
                        lines (hatching) to the right of my lane, separating it from the rightmost lane. Photo
                        1 shows the same.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose. The channelizing
                        lines correctly delineate the rightmost lane's boundary. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the mandatory or
                        permissible movement for this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines, and the lane-use arrow indicates that only
                        straight movement is permitted.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 935, 8.4 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a central lane.
                        (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a straight arrow in my lane.; arrow:left (full):
                        Photo 2 shows a left-turn arrow in the lane to my left.; arrow:right (full): Photo 2
                        shows a right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly identify the boundaries of my lane. | markings: The straight arrow in
                        my lane is consistent with the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The dashed white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The straight arrow indicates that going straight is a permitted
                        movement in this lane. [US-3B.23-01]
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows a lane
                        change.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows a lane
                        change.
Step 6  go_straight     allowed (correct): The straight arrow in my lane indicates that going straight is
                        permitted.
Step 6  turn_left       prohibited (correct): No arrow in my lane allows a left turn, and the lane to my left
                        is designated for left turns.
Step 6  turn_right      prohibited (correct): No arrow in my lane allows a right turn, and the lane to my
                        right is designated for right turns.
Step 6  u_turn          prohibited (correct): No arrow in my lane allows a U-turn.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight or change lanes. To turn left or
                        right, you should move into the designated turn lanes to your left or right
                        respectively.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left prohibited although an arrow shows
                        it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 9491, out 816, 8.95 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the left lane. Photo 2 shows a
                        solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the right lane. Photo 2 shows a
                        solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines between same-direction traffic. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not change lanes or attempt
                        to turn left or right, as the solid white lines and lane-use arrow prohibit these
                        actions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 694, 6.24 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white solid line to the left of my lane. Photo 2 shows a white solid
                        line to the left of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my lane. Photo 2 shows a white solid
                        line to the right of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white forward-pointing arrow in the center of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white solid lines on both sides. | roles: The white solid lines
                        correctly delineate the lane boundaries. | markings: The straight arrow is consistent
                        with the lane's forward direction. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines. No turns are permitted from
                        this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 708, 7.41 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and buildings on the right.
                        Ahead, there is an intersection with a white vehicle in the lane directly ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white fence and a curb on the left. Photo 2 shows a solid white line
                        and a curb on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 2 shows a white left-turn arrow and a white straight-
                        ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white edge line on the left and a white lane line on
                        the right. | roles: The white solid lines correctly serve as an edge line and a lane
                        line. | markings: The arrows in my lane (left and straight) are consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white solid line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            arrow:left_right: The arrows indicate that both left turns and straight movements are
                        permissible from this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight allowed although no arrow
                        shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 9491, out 879, 8.68 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane moving forward towards the intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left, which is a lane line separating my lane from
                        the lane to my left. Photo 2 shows this same white line clearly as a solid line next
                        to my car. Further ahead in Photo 1, the line appears to continue as a solid line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which is a lane line separating my lane from
                        the lane to my right. Photo 2 shows this same white line clearly as a solid line next
                        to my car. Further ahead in Photo 1, the line continues as a solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. A white line on my left and a white line on my right
                        indicate I am in a lane between two other lanes of the same direction. | roles: The
                        white solid lines correctly function as lane lines separating traffic flows in the
                        same direction. | markings: No markings were observed, which is consistent with the
                        lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 9491, out 723, 6.98 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road passing under a bridge (Dayan Bridge). There
                        is an intersection or a junction ahead with several vehicles and a pedestrian with a
                        scooter. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my car. Photo 2 shows a solid white
                        line to the left of my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car. Photo 2 shows a solid white
                        line to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large yellow left-turn arrow in my lane.;
                        arrow:straight (full): Photo 2 shows a large yellow straight-ahead arrow in my lane.;
                        arrow:right (full): Photo 2 shows a large yellow right-turn arrow in the lane to my
                        right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on the left and the white edge line/curb on
                        the right. | roles: The white solid line on the left correctly acts as a lane line,
                        and the white solid line on the right acts as an edge line. | markings: The yellow
                        arrows in my lane (left and straight) are consistent with the lane's function. The
                        right-turn arrow is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement in this
                        lane. [US-3B.23-01]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line (US-3B.06-05-06)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (US-3B.09-01-02)
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight-ahead arrow (US-3B.23-01)
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow (US-3B.23-01)
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the lack of a right-turn arrow in my
                        lane (US-3B.23-01)
Step 6  u_turn          prohibited (correct): prohibited by the lack of a U-turn arrow in my lane
                        (US-3B.23-01)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe ['go_straight',
                        'turn_left'], citation in_pack_not_accepted, contradictions ['turn_right prohibited
                        although an arrow shows it']
Tokens                  in 9491, out 958, 9.39 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk/curb on the
                        right. The road continues straight ahead toward an intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from a fence/pedestrian area. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a broken white line next to the car and a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (1)
                        agree with the boundaries: a white edge line is on my left and a white lane line is on
                        my right. | roles: The white solid line on the left acts as an edge line, and the
                        white dashed line on the right acts as a lane line. | markings: No markings are
                        present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white solid line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change into the lane to your
                        right. Changing to the left is prohibited by the solid edge line and the physical
                        barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 847, 7.75 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane that appears to be a dedicated through-lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to its left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to its right. Photo 2
                        shows this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the lane's role as a through-lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated through-lane. You are permitted to go straight ahead, but lane
                        changes and turns are prohibited by the lane markings and solid boundary lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 811, 8.0 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is
                        positioned in a lane that leads straight through the intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this same white line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a large white arrow pointing to the right in
                        the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The white lines on both sides indicate lanes of the
                        same direction. | roles: The white solid lines correctly function as lane lines
                        separating traffic in the same direction. | markings: The straight arrow in my lane
                        matches the straight-ahead movement, and the right arrow in the adjacent lane matches
                        its function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        through the intersection and avoid changing lanes, as the solid white lines on both
                        sides prohibit lane changes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed ['line:crosswalk', 'line:stop_line']), actions True, unsafe
                        [], citation in_pack_not_accepted, contradictions ['turn_right prohibited although an
                        arrow shows it']
Tokens                  in 9491, out 852, 9.21 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a wide intersection ahead. The road is lined with trees
                        and buildings, and there is a large yellow-painted grid area in the middle of the
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows the same solid yellow line clearly.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line and a
                        raised curb/sidewalk area further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a large yellow grid pattern (cross-
                        hatching) across the intersection ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the boundaries: a yellow line on my left and a white line/curb on
                        my right. | roles: The yellow line correctly identifies a separation from a lane to
                        the left, and the white line/curb identifies the right edge. | markings: The grid area
                        is consistent with an intersection area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:grid: The grid marking is used to discourage travel on certain paved areas like
                        neutral areas. [US-3B.25-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight through the intersection. Do not attempt to change lanes as the
                        solid lines prohibit it. Avoid driving into the yellow grid area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 898, 9.2 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide roadway and a dedicated lane for a vehicle on the
                        right. There is a clear intersection or continuation of the road ahead. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): A white diamond symbol is visible in the center of my lane in
                        Photo 1 and Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line on the left and a white edge line
                        on the right. | roles: The yellow solid line correctly identifies a center line
                        (opposite traffic), and the white solid line correctly identifies an edge line. |
                        markings: The diamond symbol is centered in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but in this context, it delineates the separation of opposite traffic flows.
                        [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            symbol:other: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 704, 8.34 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane that appears to be a dedicated turn lane or a lane ending at an intersection.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line clearly as a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows this as a solid white line next to a sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large white left-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The white line on the left separates me from the lane with the straight
                        arrow, and the white line on the right is the edge of the road. | roles: The white
                        solid line on the left is a lane line, and the white solid line on the right is an
                        edge line, which is consistent with the layout. | markings: The left-turn arrow in my
                        lane is consistent with the lane's position as a turn lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The left-turn arrow indicates the mandatory or permissible movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     prohibited (correct): prohibited
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane exclusively for making a left turn at the upcoming intersection. Do not
                        attempt to go straight or change lanes, as the lane is marked for left turns only.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 918, 7.38 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway in an urban area with a concrete barrier on the
                        left. A large truck is directly ahead in my lane, and a white car is in the lane to my
                        right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier on the left. Photo 2 shows a solid white line painted
                        on the pavement next to the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 2 shows a white left-turn arrow in the lane to my right.
                        There are no markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a concrete barrier/edge line on the left and a lane
                        line on the right. | roles: The white solid line on the left acts as an edge line
                        (next to a barrier), and the white solid line on the right acts as a lane line. |
                        markings: The left-turn arrow is in the adjacent lane, not my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white solid line delineates the left-hand edge of the roadway.
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
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 849, 7.32 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The dashed white line indicates that crossing into the right lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [[US-3B.23-01]]
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows a lane
                        change.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows a lane
                        change.
Step 6  go_straight     allowed (correct): The straight arrow in my lane allows going straight.
Step 6  turn_left       prohibited (correct): No arrow or marking allows a left turn.
Step 6  turn_right      prohibited (correct): No arrow or marking allows a right turn.
Step 6  u_turn          prohibited (correct): No arrow or marking allows a U-turn.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may go straight or change lanes to the left or right.
                        Left turns, right turns, and U-turns are not permitted from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 727, 5.9 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection with traffic
                        lights. My car is in a central lane. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines separating same-direction traffic. |
                        markings: The straight arrow in my lane is consistent with the lane's role as a
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-through movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes or turning left or right due to the solid white lane markings and the
                        straight-ahead arrow.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 686, 7.75 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        ahead appears to be a straight stretch with multiple lanes of traffic moving in the
                        same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows this line as a solid white line next to my car, with a curb/barrier area
                        further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on my left and the white edge line on my
                        right. | roles: The white solid line on the left correctly functions as a lane line,
                        and the white solid line on the right functions as an edge line. | markings: No
                        markings were observed, which is consistent with the clear lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are discouraged or prohibited by the solid white
                        markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 753, 7.38 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with buildings and parked cars on both sides. The road
                        ahead appears to be a straight stretch with a bridge in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a white line that is
                        solid near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. Photo
                        1 shows a white left-turn arrow in the lane to my left.; arrow:left (full): Photo 1
                        shows a white left-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left
                        indicates a center line separating opposite traffic, and the white line on the right
                        separates lanes in the same direction. This is consistent with my lane being the
                        middle of three lanes in my direction. | roles: The yellow double solid line correctly
                        identifies a center line. The white solid_dashed line correctly identifies a lane
                        line. | markings: The arrows in adjacent lanes are consistent with the lane
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid portion of the white line discourages crossing into the
                        right lane. [[US-3B.06-05-06]]
Step 5  Rule            arrow:left: The arrow in the left lane indicates a mandatory or permissible left turn
                        for that lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): discouraged
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight ahead. Changing to the left is
                        prohibited by the double solid yellow center line. Changing to the right is
                        discouraged by the solid white line near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions ['change_right allowed with the solid line of a solid-and-broken pair
                        nearer my lane', 'go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it']
Tokens                  in 9491, out 788, 8.64 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a double yellow center line is on my left, and a
                        white lane line is on my right. | roles: The double yellow line correctly identifies a
                        center line (opposite traffic), and the white line correctly identifies a lane line
                        (same direction traffic). | markings: The straight arrow in my lane is consistent with
                        the lane's purpose and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 870, 8.18 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure on the left and a sidewalk/bike
                        lane on the right. The road ahead appears to be a straight continuation of the current
                        roadway. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight arrow in my lane.;
                        arrow:straight (full): Photo 1 shows a white straight arrow in the lane to my right.;
                        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with the white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines separating traffic in the same direction.
                        | markings: The straight arrow in my lane is consistent with the lane's role as a
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should continue straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 9491, out 967, 9.37 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway under an overpass. Ahead, the road
                        continues straight toward a city area with buildings and a pedestrian/bicycle zone to
                        the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my car. Photo 2 shows a solid white
                        line very close to the car's left side.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car. Photo 2 shows a solid white
                        line very close to the car's right side.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly delineate the boundaries of my lane from adjacent lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose and the surrounding markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You should continue
                        straight and avoid changing lanes or turning, as the solid white lines and lane
                        markings prohibit these actions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 924, 9.2 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in one of the center
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and my position as
                        lane 2 are consistent with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings were observed in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white dashed line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action.
Step 6  turn_right      not_applicable: No markings in my lane govern this action.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right as the lane markings are dashed. Proceed
                        straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line', 'line:stop_yield', 'line:yield_line'], missed []), actions True,
                        unsafe [], citation in_pack_not_accepted, contradictions ['go_straight allowed without
                        the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 747, 7.83 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows a white line with
                        short dashes (dotted) next to my car.
                        white dotted, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a white line with
                        short dashes (dotted) next to my car.
                        white dotted, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dotted
                        lines correctly delineate lanes in the same direction of travel. | markings: The
                        straight arrow in my lane is consistent with the lane's function. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white lane line allows for crossing with care. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white lane line allows for crossing with care. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     allowed (WRONG, label prohibited): The white dotted left boundary allows for crossing
                        with care.
Step 6  change_right    allowed (WRONG, label prohibited): The white dotted right boundary allows for crossing
                        with care.
Step 6  go_straight     allowed (correct): The straight arrow in my lane indicates that going straight is a
                        permitted movement.
Step 6  turn_left       prohibited (correct): The straight arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): The straight arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): The straight arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left or right with care, but you should proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 723, 7.57 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection. My car is in a
                        lane that appears to be part of a multi-lane roadway with a median or curb on the
                        left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle lane of three lanes moving in the
                        same direction. | roles: The white solid lines correctly delineate the boundaries of
                        my lane. | markings: The straight arrow in my lane is consistent with the lane's
                        function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        my left. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to my right. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited: prohibited by the straight arrow marking
Step 6  turn_right      prohibited: prohibited by the straight arrow marking
Step 6  u_turn          prohibited: prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines. You should not attempt to turn
                        left, turn right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 756, 7.12 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a solid white line next to my car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a solid white line next to my car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white lane lines
                        correctly delineate the separation of same-direction traffic flows. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the right lane.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to go straight ahead. Lane changes to the
                        left or right are discouraged by the solid white lines near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 853, 7.12 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with an overpass ahead. My car is in a lane moving forward.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a broken line (dashed) next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this same solid white line next to my car. Further ahead in
                        Photo 1, there is a concrete barrier/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2 shows white diagonal lines (hatching) across the
                        lane, indicating a lane drop or area restriction.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line/curb on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        white solid line correctly functions as an edge line. | markings: The channelizing
                        markings (hatching) are consistent with a lane drop or narrowing ahead. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            area:channelizing: Channelizing lines are used to form neutral areas where traffic is
                        not permitted to travel. [[US-3B.08-01-03]]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane as the boundary is a dashed line. Do not move to the
                        right as it is the edge of the roadway. Be aware of the lane narrowing indicated by
                        the hatching ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 929, 9.35 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a median on the left and a landscaped area on the
                        right. There is an intersection or transition area ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a dashed line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a dashed line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows the arrow clearly.; text:only (full): Photo 1 shows the word 'ONLY' in
                        white text in the lane to my right. Photo 2 shows this clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The dashed white line indicates that crossing into the right lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the dashed white left boundary line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change lanes to the left
                        or right as the dashed lines permit. The lane to your right is designated for a
                        specific movement (ONLY).
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'text:only'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 990, 9.95 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with trees and a low wall on the left. Ahead,
                        there is a clear roadway with multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows Chinese characters painted in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a yellow solid
                        line/curb on the right. | roles: The white dashed line correctly functions as a lane
                        line, and the yellow solid line correctly functions as an edge line. | markings: The
                        Chinese characters are centered in the lane and do not contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white/yellow line delineates the right-hand edge of the
                        roadway. [US-3B.09-01-02]
Step 5  Rule            text:other: The pavement markings provide guidance or regulation for the lane.
                        [US-3B.20-01]
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left boundary
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, label prohibited): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right. Proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 767, 8.46 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        right and a wall/barrier on the left. Ahead, there is a gantry with signs and a
                        merging area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway or a separation from a shoulder. Photo 2 shows a solid yellow line clearly
                        visible next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_left (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_right (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:two_way_left (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:only (full): No markings are visible in my lane in Photo 1 or Photo 2.; text:bus
                        (full): No markings are visible in my lane in Photo 1 or Photo 2.; text:hov (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; text:stop (full): No markings
                        are visible in my lane in Photo 1 or Photo 2.; text:keep_clear (full): No markings are
                        visible in my lane in Photo 1 or Photo 2.; text:speed_limit (full): No markings are
                        visible in my lane in Photo 1 or Photo 2.; symbol:hov_diamond (full): No markings are
                        visible in my lane in Photo 1 or Photo 2.; symbol:bike (full): No markings are visible
                        in my lane in Photo 1 or Photo 2.; symbol:other (full): No markings are visible in my
                        lane in Photo 1 or Photo 2.; area:left_turn_waiting (full): No markings are visible in
                        my lane in Photo 1 or Photo 2.; area:two_way_left_turn_lane (full): No markings are
                        visible in my lane in Photo 1 or Photo 2.; area:grid (full): No markings are visible
                        in my lane in Photo 1 or Photo 2.; area:channelizing (full): No markings are visible
                        in my lane in Photo 1 or Photo 2.; line:crosswalk (full): No markings are visible in
                        my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a yellow solid line
                        on the right. | roles: The white dashed line on the left fits the role of a lane line,
                        and the yellow solid line on the right fits the role of an edge line. | markings: No
                        markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line (or yellow in this context) delineates the edge
                        of the roadway. [US-3B.09-01-02]
Step 5  Rule            area:two_way_left_turn_lane: No two-way left-turn lane is present in my lane.
                        [US-3B.05-01]
Step 6  change_left     allowed (correct): The white dashed line on the left allows for a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): The solid yellow edge line and physical barrier
                        prohibit moving to the right.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action.
Step 6  turn_right      not_applicable: No markings in my lane govern this action.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in my lane.
Step 7  Reflect         consistent
Advice                  You may change to the left lane if needed. Do not attempt to move to the right as it
                        is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 9491, out 1481, 13.72 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete wall on the left and a guardrail on
                        the right. The road ahead appears to be a straight stretch of highway. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line clearly as a broken line near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this white line clearly as a broken line near the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines separating traffic in the same
                        direction. | markings: No markings are present, which is consistent with a standard
                        highway lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary (US-3B.06-05-06)
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change lanes to the left
                        or right as the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 857, 7.81 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a median on the left and a guardrail on the right. The road
                        ahead is straight with several vehicles in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to the right. Photo
                        2 shows a white solid line clearly visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) are consistent with a white dashed line on the left and a white solid line on
                        the right. | roles: The white dashed line on the left and white solid line on the
                        right fit the roles of lane lines for same-direction traffic. | markings: No markings
                        are present, which is consistent with the lane boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the white solid line is discouraged or prohibited.
                        [US-3B.06-05-06]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane as it is marked with a
                        dashed line, but changing to the right lane is discouraged or prohibited by the solid
                        line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 834, 7.75 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway on a bridge or elevated structure. Ahead, there
                        is a fork or split in the road with overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on the left and a white line on the right
                        indicate a lane between two others. | roles: The white solid lines correctly function
                        as lane lines separating traffic in the same direction. | markings: The left-turn
                        arrow in my lane is consistent with the road geometry and the split ahead. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [US-3B.23-03]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to perform a left turn. Lane changes to the left or right are prohibited
                        by the solid white lines, and the lane-use arrow indicates that only a left turn is
                        permitted from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 714, 7.94 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a median on the left and a barrier on the right. The road
                        ahead is straight with several vehicles in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car. Further ahead, there is a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line/barrier on
                        the right. | roles: The white dashed line correctly identifies a lane line, and the
                        solid white line/barrier correctly identifies an edge line. | markings: No markings
                        were observed. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane as the boundary is a dashed line. Do not attempt to
                        move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 863, 8.8 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a barrier on the right. The road ahead appears to be a
                        continuous stretch of highway with several lanes of traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, followed by a metal guardrail and a concrete
                        curb. Photo 2 shows the white line is solid and the curb/barrier is immediately
                        adjacent.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the
                        center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a white edge line on the right.
                        | roles: The white lane line on the left and white edge line on the right fit the
                        roles of lane_line and edge_line respectively. | markings: The straight arrow in my
                        lane is consistent with the lane's role as a through lane. | unseen: none | result:
                        consistent
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 913, 9.33 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the left
                        and a raised embankment with a guardrail on the right. The road ahead appears to be a
                        straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line and a concrete barrier on the left. Photo 2 shows a
                        solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a red-colored pavement area in the center of the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my lane position
                        of 2 (middle) agree with the boundaries. The left boundary is a concrete barrier/edge
                        line, and the right boundary is an edge line. | roles: The white solid lines correctly
                        function as edge lines for the roadway. | markings: The red pavement is a decorative
                        or warning marking and does not conflict with the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid line with a barrier, but it
                        defines the left edge of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            symbol:other: No specific rule provided for red pavement markings. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead.
                        Lane changes to the left or right are prohibited by the solid white edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9491, out 718, 8.42 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with a guardrail on the right. The road ahead appears to
                        be a continuous stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line and a metal guardrail on the right. Photo 2 shows the
                        white solid line and the guardrail clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows white dashed lines across the lane ahead, forming a
                        grid-like pattern or a buffer zone. Photo 2 shows these dashed lines clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line/guardrail
                        on the right. | roles: The white dashed line on the left correctly functions as a lane
                        line, and the white solid line on the right correctly functions as an edge line. |
                        markings: The grid markings are consistent with a buffer or neutral area ahead. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white solid line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:grid: The grid markings are used to discourage travel on certain paved areas.
                        [US-3B.25-01]
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid right boundary and
                        guardrail [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 766, 8.14 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a clear view of the road ahead. There is a green overhead
                        sign and a white car in the lane to the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line
                        clearly visible next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_right (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:two_way_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        text:only (full): No markings visible in my lane in Photo 1 or Photo 2.; text:bus
                        (full): No markings visible in my lane in Photo 1 or Photo 2.; text:hov (full): No
                        markings visible in my lane in Photo 1 or Photo 2.; text:stop (full): No markings
                        visible in my lane in Photo 1 or Photo 2.; text:keep_clear (full): No markings visible
                        in my lane in Photo 1 or Photo 2.; text:speed_limit (full): No markings visible in my
                        lane in Photo 1 or Photo 2.; symbol:hov_diamond (full): No markings visible in my lane
                        in Photo 1 or Photo 2.; symbol:bike (full): No markings visible in my lane in Photo 1
                        or Photo 2.; symbol:other (full): No markings visible in my lane in Photo 1 or Photo
                        2.; area:left_turn_waiting (full): No markings visible in my lane in Photo 1 or Photo
                        2.; area:two_way_left_turn_lane (full): No markings visible in my lane in Photo 1 or
                        Photo 2.; area:grid (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:channelizing (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:crosswalk (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a white solid line
                        on the right. | roles: The white dashed line on the left correctly functions as a lane
                        line, and the white solid line on the right correctly functions as an edge line. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        movement instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white solid line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a white solid line, which
                        prohibits crossing onto the shoulder.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you should not move to the right of
                        the solid white line. Proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 9491, out 1372, 14.64 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on both sides. The road ahead
                        appears to be a straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:left_turn_waiting (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:two_way_left_turn_lane (full): No markings visible in my lane in Photo 1 or Photo
                        2.; arrow:merge_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_right (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:two_way_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        text:only (full): No markings visible in my lane in Photo 1 or Photo 2.; text:bus
                        (full): No markings visible in my lane in Photo 1 or Photo 2.; text:hov (full): No
                        markings visible in my lane in Photo 1 or Photo 2.; text:stop (full): No markings
                        visible in my lane in Photo 1 or Photo 2.; text:keep_clear (full): No markings visible
                        in my lane in Photo 1 or Photo 2.; text:speed_limit (full): No markings visible in my
                        lane in Photo 1 or Photo 2.; symbol:hov_diamond (full): No markings visible in my lane
                        in Photo 1 or Photo 2.; symbol:bike (full): No markings visible in my lane in Photo 1
                        or Photo 2.; symbol:other (full): No markings visible in my lane in Photo 1 or Photo
                        2.; area:grid (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:channelizing (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        markings are present, which is consistent with a standard through-lane on a highway. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for crossing into the left lane with care.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white dashed line allows for crossing into the right lane with
                        care. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane roadway. You may change lanes to the left
                        or right as needed, and you are permitted to continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov',
                        'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed []), actions
                        True, unsafe [], citation in_pack_not_accepted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 1303, 11.14 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a sound barrier on the right. The road ahead is straight
                        with several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a
                        guardrail/sound barrier. Photo 2 shows a solid white line clearly defining the right
                        edge of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        solid white line correctly functions as an edge line. | markings: No markings are
                        present, which is consistent with the lane boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change into the left lane
                        as it is marked with a dashed line, but you should not move to the right as it is the
                        edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 849, 8.72 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway with a curve ahead. My car is in a lane that
                        appears to be a dedicated lane or a lane near a median. There is a construction area
                        or barrier to the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line and a concrete barrier/median to the left. Photo 2
                        shows a solid white line and a concrete barrier with a metal railing.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right. Photo 2 shows a solid white line to the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a series of white rectangles (transverse markings)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree. The
                        left boundary is an edge line (barrier), and the right is a lane line separating me
                        from another lane. | roles: The white solid lines and barrier correctly define the
                        lane boundaries. | markings: The grid markings are consistent with a neutral area or a
                        specific zone within the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            area:grid: The grid markings indicate a neutral area or a 'Do Not Block' zone.
                        [US-3B.26-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid white lines on both sides prohibit lane
                        changes. Proceed straight through the marked grid area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 880, 9.54 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway, likely a bridge or overpass, with a bus directly
                        ahead in the same lane. The road is bordered by metal guardrails on both sides. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane lines separating traffic in the same
                        direction. | markings: No markings are present to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line per
                        US-3B.06-05-06
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line per
                        US-3B.06-05-06
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 699, 7.39 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane divided highway or bridge. Ahead, the road
                        continues straight with several lanes of traffic. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows a white line to the
                        left of my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a white line to the
                        right of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:stop (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:keep_clear (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_left (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_right (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:two_way_left (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        area:left_turn_waiting (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; area:two_way_left_turn_lane (full): No markings are visible in my lane in Photo 1
                        or Photo 2.; text:bus (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; text:hov (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        symbol:hov_diamond (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        symbol:bike (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        symbol:other (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        area:channelizing (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:speed_limit (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:other (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (3) agree with the boundaries. There is a white dashed line to my left and a white
                        dashed line to my right. | roles: The white dashed lines correctly function as lane
                        lines separating traffic in the same direction. | markings: No markings are present in
                        my lane, which is consistent with the dashed lane lines. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The dashed white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows a lane
                        change.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows a lane
                        change.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may change lanes to the left or right as
                        the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov',
                        'text:keep_clear', 'text:other', 'text:speed_limit', 'text:stop'], missed []), actions
                        True, unsafe [], citation in_pack_not_accepted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 1342, 13.28 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings and trees on both sides. My
                        car is in a lane heading straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a small planter area on the left. Photo 2 shows a
                        raised curb and a planter area on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The left side is a curb/edge, and the right side is a
                        lane line. | roles: The white dashed line on the right correctly identifies a lane
                        line, and the curb on the left identifies an edge line. | markings: No markings are
                        present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a curb edge line, but it defines the
                        roadway boundary. [null]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [US-3B.06-05-06]
Step 5  Rule            line:stop_line: No stop line is present. [null]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (WRONG, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane on your right. Changing to the left
                        is prohibited by the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 9491, out 675, 6.81 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a concrete median separating opposing traffic. Ahead,
                        there is a clear lane for my car with a motorcycle and a car in the adjacent lane.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a concrete median/barrier on the left. Photo 2 shows the concrete median
                        clearly defining the left edge of my lane.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a concrete median on the left and a white line on the
                        right. | roles: The concrete median acts as a left edge line, and the white line acts
                        as a right lane line. | markings: No markings are present to contradict the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The concrete median serves as a physical barrier for the left side of
                        the lane. [null]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the lane to the right.
                        [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are blocked by a
                        median, and lane changes to the right are discouraged by a solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 9491, out 820, 8.4 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian bridge on the right and a landscaped median
                        on the left. My car is in a lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        a solid yellow line next to my car and a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. Photo
                        1 shows a white right-turn arrow in the lane to my right.; arrow:right (full): Photo 1
                        shows a white right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the yellow center line on my left and white edge line on my right.
                        | roles: The yellow center line and white edge line fit the roles of center line and
                        edge line respectively. | markings: The arrows in adjacent lanes are consistent with
                        the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it separates lanes of the same direction (as per
                        US-3B.06-01, though the color is yellow). [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:left: The arrow indicates the mandatory or permissible movements in the adjacent
                        lane. [[US-3B.23-01]]
Step 5  Rule            arrow:right: The arrow indicates the mandatory or permissible movements in the
                        adjacent lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_left not_applicable although an arrow shows it', 'turn_right not_applicable
                        although an arrow shows it']
Tokens                  in 9491, out 837, 8.06 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a clear path ahead. The car is positioned in a lane
                        with a white line on its right and a physical barrier/curb on its left. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a raised curb and a metal fence on the left. Photo 2 shows a raised curb
                        and a metal fence on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a curb/fence on the left and a white line on the right.
                        | roles: The white solid line on the right correctly acts as a lane line, and the curb
                        on the left acts as an edge line. | markings: No markings are present to contradict
                        the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The curb/fence defines the left edge of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane to the right. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of this section. You may proceed straight ahead. Lane
                        changes to the right are discouraged or prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9491, out 655, 12.88 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a pedestrian bridge on the right. My
                        car is in a lane traveling straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows a solid
                        white line and a raised curb next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. No
                        markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The yellow line on the left separates my lane from the lane to my left,
                        and the white line/curb on the right defines the edge of the roadway. | roles: The
                        yellow center line and white edge line fit their respective roles. | markings: The
                        left-turn arrow is in the adjacent lane, which is consistent with the lane layout. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it separates lanes of the same direction (as per
                        US-3A.03-03-04). [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates the mandatory or permissible movements in the adjacent
                        lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of the roadway. You may proceed straight ahead. Lane
                        changes to the left are prohibited by the solid yellow line, and a lane change to the
                        right is prohibited by the curb and edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions ['go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it']
Tokens                  in 9491, out 768, 9.07 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a median separating opposing traffic.
                        My car is in a lane heading straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a white line on the left separates me from another lane,
                        and a white line/curb on the right marks the edge. | roles: The white solid lines
                        correctly function as a lane line and an edge line. | markings: The straight arrow
                        aligns with the lane's purpose and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        and avoid changing lanes or turning, as the solid white lines and lane markings
                        prohibit these actions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 884, 9.07 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a wide sidewalk and a bike lane on the right. The car
                        is traveling straight ahead in a lane bounded by a curb/median on the left and a white
                        line on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a raised concrete curb/median with a low hedge on the left. Photo 2
                        shows the same raised concrete curb/median clearly.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bike lane. Photo 2 shows
                        this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left edge (curb) and right lane line. | roles: The left curb
                        acts as an edge line and the white line acts as a lane line. | markings: No markings
                        are present in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The curb delineates the left-hand edge of the roadway. [US-3B.09-01-02]
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
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 807, 6.22 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overpass to the left and a tree-lined sidewalk to
                        the right. The road ahead appears to be a straight stretch with multiple lanes of
                        traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to its left. Photo 2 shows
                        this same white line clearly as a broken line near the car and a solid line further
                        ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this same solid white
                        line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: The close-up (Photo 2) clarifies that the left boundary is a solid-dashed
                        line (dashed side near my car) and the right boundary is a solid white line. The
                        straight arrow is clearly visible in Photo 2. | position: The lane count of 3 and my
                        position as lane 2 (middle) are consistent with a lane line on the left and an edge
                        line on the right. | roles: The white color and patterns (solid-dashed left, solid
                        right) are consistent with lane-use and edge-line roles. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose and the surrounding boundaries.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid-dashed line discourages or prohibits crossing depending on
                        the specific application, but the dashed portion indicates a permissive condition.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates the mandatory or permissible movement for this
                        lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead as indicated by
                        the pavement arrow. Lane changes to the left or right are discouraged/prohibited by
                        the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited with the broken line of
                        a solid-and-broken pair nearer my lane']
Tokens                  in 9491, out 949, 8.53 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a dedicated bicycle/scooter lane. My
                        car is positioned in a lane that appears to be a bicycle/scooter lane, as indicated by
                        the large white arrow and the presence of cyclists. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a large white arrow pointing straight
                        ahead in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The left boundary is a lane line separating my lane
                        from another lane to the left. The right boundary is an edge line against a curb. |
                        roles: The white solid lines and the curb fit the roles of a lane line and an edge
                        line respectively. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the mandatory or permissible movement for
                        this lane is straight ahead. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated lane for straight-ahead travel. You should continue straight
                        and avoid changing lanes or turning, as the markings and solid lines prohibit these
                        actions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 9491, out 902, 8.08 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban street in China. My car is in a lane moving
                        forward, with a car directly ahead and a parked SUV to the right. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a yellow line on the left and a white line on the right
                        define the leftmost lane of a one-way street or a right-hand edge. | roles: The yellow
                        line on the left acts as a left edge line, and the white line on the right acts as a
                        right edge line. | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the left-hand edge of the roadway.
                        [US-3A.03-03-04]
Step 5  Rule            right_boundary: The white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of a one-way street. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 9491, out 678, 7.2 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median or curb on the left and parked cars on the
                        right. The road ahead appears to be a straight stretch with a clear lane for my car.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line and a raised curb/median on the left. Photo 2 shows a
                        solid white line and a raised curb/median on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:merge_right (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        arrow:two_way_left (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        text:only (full): No markings visible in my lane in Photo 1 or Photo 2.; text:bus
                        (full): No markings visible in my lane in Photo 1 or Photo 2.; text:hov (full): No
                        markings visible in my lane in Photo 1 or Photo 2.; text:stop (full): No markings
                        visible in my lane in Photo 1 or Photo 2.; text:keep_clear (full): No markings visible
                        in my lane in Photo 1 or Photo 2.; text:speed_limit (full): No markings visible in my
                        lane in Photo 1 or Photo 2.; symbol:hov_diamond (full): No markings visible in my lane
                        in Photo 1 or Photo 2.; symbol:bike (full): No markings visible in my lane in Photo 1
                        or Photo 2.; symbol:other (full): No markings visible in my lane in Photo 1 or Photo
                        2.; area:left_turn_waiting (full): No markings visible in my lane in Photo 1 or Photo
                        2.; area:two_way_left_turn_lane (full): No markings visible in my lane in Photo 1 or
                        Photo 2.; area:grid (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:channelizing (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white edge line on the left and a white lane line on
                        the right. | roles: The white solid line on the left acts as an edge line, and the
                        white solid line on the right acts as a lane line. | markings: No markings were
                        observed, which is consistent with the lack of specific movement instructions. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white solid line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 9491, out 1331, 12.18 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a median and a sidewalk on the right.
                        Ahead, there is a clear roadway with multiple lanes of traffic moving in the same
                        direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb/median on the right. Photo 2 shows
                        a solid white line and a raised curb/median.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a single white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from another lane,
                        and a white line/curb on my right marks the edge. | roles: The white solid line on the
                        left is a lane line, and the white solid line/curb on the right is an edge line. |
                        markings: The straight arrow in my lane is consistent with the lane's function. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-lane roadway. You are permitted to proceed
                        straight ahead as indicated by the pavement arrow. Lane changes to the left are
                        discouraged or prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 744, 8.03 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk on the right.
                        Ahead, there is an intersection with traffic signals and a white car in the lane to
                        the left. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a white dashed line in the middle of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line on the left separates me from the
                        middle lane, and a solid white line on the right marks the edge. | roles: The white
                        dashed line on the left fits the role of a lane line, and the solid white line on the
                        right fits the role of an edge line. | markings: The dashed line in the middle of the
                        lane is not a standard marking for a specific movement but appears as a lane divider
                        or guide. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the lane to your left as it is marked with a dashed line. Do not
                        attempt to move to the right as the solid white line indicates the edge of the
                        roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 919, 8.57 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The car is in a lane
                        with a car directly ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line to the left of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line to the right of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow solid line fits the role of a center line (separating
                        opposite traffic), and the white solid line fits the role of an edge line. | markings:
                        No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but in this context, it delineates the separation of opposite traffic.
                        [[US-3B.01-05]]
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
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 839, 7.4 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bicycle lane on the right. My car is in a
                        lane adjacent to a bus lane and a bicycle lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a bus lane to the left.
                        Photo 2 shows a solid yellow line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bicycle lane on the right.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white lane-use arrow in the lane to my
                        left, but no markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. A yellow line on the left separates me from a bus lane
                        (same direction), and a white line on the right separates me from a bicycle lane. |
                        roles: The yellow line on the left and white line on the right fit the roles of lane
                        lines separating traffic flows in the same direction. | markings: No markings are
                        visible in my lane to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        bicycle lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Lane changes to the left (into the bus lane) or to the
                        right (into the bicycle lane) are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 858, 7.81 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with trees and buildings on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        a solid yellow line next to my car and a broken yellow line further ahead.
                        yellow solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a yellow line in the center of my lane.
Step 4  Cross-check     close_up: Photo 2 shows a solid yellow line next to the car and a broken yellow line
                        further ahead, while Photo 1 shows the overall context. The yellow line in the middle
                        of my lane in Photo 2 is actually the left boundary of the lane to my left, not a
                        marking in my lane. | position: The lane count (3) and my position (2) are consistent
                        with a yellow line on my left and a white line/curb on my right. | roles: The yellow
                        line on the left is a lane line separating traffic flows, and the white line on the
                        right is an edge line. | markings: The yellow line in the center of the road is a lane
                        boundary, not a marking within my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid portion of the yellow line discourages crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are
                        discouraged/prohibited by the solid yellow line, and the right edge is bounded by a
                        curb.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 9491, out 900, 9.6 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide roadway and a median/curb on the left. There is a
                        building and a wall on the right. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:left_turn_waiting (full): No markings visible in my lane in Photo 1 or Photo 2.;
                        area:two_way_left_turn_lane (full): No markings visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) agree with the boundaries: a white line on the left separates me from the
                        2nd lane, and a white line on the right marks the edge of the roadway. | roles: The
                        white solid line on the left is a lane line, and the white solid line on the right is
                        an edge line. | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may proceed straight ahead, but lane
                        changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 880, 8.42 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a turn
                        arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, bordering a sidewalk/curb
                        area. Photo 2 shows a solid white line next to my car and a solid white line further
                        ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow in my lane pointing
                        straight and to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on the left separates me from another lane,
                        and a white line/curb on the right marks the edge. | roles: The white solid lines
                        correctly function as a lane line and an edge line. | markings: The straight-right
                        arrow is consistent with the lane's position and the surrounding boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight_right: The arrow indicates that the mandatory or permissible movements
                        in this lane are straight ahead or a right turn. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through or right-turn movements. You may
                        proceed straight or turn right, but you are prohibited from turning left or changing
                        lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 903, 7.76 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a tunnel or underpass ahead. The road is bounded by
                        concrete walls and a sidewalk on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, bordering a sidewalk. Photo
                        2 shows the same solid white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows white dashed lines separating the
                        lanes.; line:stop_yield (insufficient): Photo 1 shows white dashed lines separating
                        the lanes.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the double yellow center line on the left and the white edge line
                        on the right. | roles: The double yellow line correctly identifies the center line
                        separating opposing traffic, and the white line correctly identifies the right edge. |
                        markings: The dashed lines are standard lane dividers. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_yield: no marking governs this action
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the double solid yellow center line
                        [US-3B.01-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and the
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead.
                        Lane changes to the left are prohibited by the double yellow line, and a change to the
                        right is restricted by the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 759, 8.96 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway with a concrete barrier on the right and a
                        wall on the left. An overpass is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my car. Photo 2 shows a white solid
                        line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line separating the lanes
                        ahead.; line:yield_line (insufficient): Photo 1 shows a white dashed line separating
                        the lanes ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left separates me from the
                        lane to my left, and a white solid line on the right marks the edge of the roadway. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: No specific arrows
                        or words are visible in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white solid line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a white solid line and a
                        curb, which prohibits crossing.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change into the left lane
                        as the lane line is dashed. Do not attempt to move to the right as it is the edge of
                        the roadway marked by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line', 'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 794, 8.67 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide sidewalk and a bus stop on the right. The road
                        ahead appears to be a straight stretch with multiple lanes of traffic moving in the
                        same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line very close to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, which appears to be the edge
                        of the roadway. Photo 2 shows a solid white line very close to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line in the middle of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left separates me from the
                        leftmost lane, and a solid white line on the right marks the edge of the roadway. |
                        roles: The white dashed line on the left fits the role of a lane line, and the solid
                        white line on the right fits the role of an edge line. | markings: The dashed line in
                        the middle of the lane is not a standard marking and does not clearly define a
                        movement. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:stop_yield: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which is permissive.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line and a curb, which
                        prohibits moving onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane if needed, but you are
                        prohibited from moving to the right onto the sidewalk. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 782, 8.63 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow paved roadway, possibly a service road or a side path, passing
                        under a bridge. There is a wall on the right and a hedge/barrier on the left. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a hedge on the left. Photo 2 shows a raised curb and a
                        hedge on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a red wall and a sidewalk on the right. Photo 2 shows a red wall and a
                        sidewalk on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree with
                        the boundaries; the lane is bounded by a curb/hedge on the left and a wall/curb on the
                        right. | roles: The boundaries correctly function as edge lines. | markings: No
                        markings are present in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule for a curb/hedge boundary, but it defines the edge of
                        the roadway. [null]
Step 5  Rule            right_boundary: No specific rule for a wall/curb boundary, but it defines the edge of
                        the roadway. [null]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your lane. Lane changes to the left or right are prohibited as
                        the lane is bounded by a curb and a wall.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 9491, out 598, 7.69 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection with a pedestrian crossing
                        and a metal fence on the right. The sun is high, creating significant glare. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line and a metal fence on the right. Photo 2 shows a solid white
                        line immediately adjacent to a raised curb and a metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large white left-turn arrow in my lane.;
                        line:stop_line (full): Photo 1 shows a white stop line across the lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a white edge line/curb on the
                        right. | roles: The white solid line on the left correctly functions as a lane line,
                        and the white solid line/curb on the right correctly functions as an edge line. |
                        markings: The left-turn arrow in my lane is consistent with the lane's purpose and the
                        surrounding geometry. | unseen: none | result: consistent
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
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Your lane is designated for a left turn only. You must come to a full stop at the
                        white stop line before making your left turn. Do not attempt to change lanes or go
                        straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 1014, 10.16 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. The car is traveling straight ahead under
                        an overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white lane-use arrow in my lane pointing
                        straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly delineate lanes in the same direction of travel. | markings: The straight
                        arrow in my lane is consistent with the lane boundaries and the straight-ahead
                        movement. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead travel.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited: prohibited by the straight arrow marking
Step 6  turn_right      prohibited: prohibited by the straight arrow marking
Step 6  u_turn          prohibited: prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        and avoid changing lanes, as the solid white lines on both sides prohibit lane
                        changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 711, 5.43 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view of the road ahead. The car is
                        traveling in a lane with speed limit markings. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line near the car and becomes a broken white line further
                        ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a guardrail. Photo 2 shows
                        a solid white line very close to the car, then a gap, then another solid white line
                        before the guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a large circular marking with '60' inside it in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white line on my left separates me from another lane, and
                        a white line/guardrail on my right marks the edge. | roles: The white lane line on the
                        left and white edge line on the right fit their roles. | markings: The speed limit
                        marking is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid portion of the line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            text:speed_limit: The marking provides a guidance message for the speed limit.
                        [US-3B.20-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are
                        discouraged/prohibited by the solid line marking near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 907, 8.79 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a bus and a van in adjacent lanes. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between same-direction traffic. | markings: No
                        markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        per US-3B.06-05-06
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        per US-3B.06-05-06
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 661, 7.02 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway with a bridge structure. Ahead, there are several
                        vehicles and a motorcycle moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my lane. Photo 2 shows a white solid
                        line clearly visible next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        no_turn:right (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        no_turn:u_turn (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left correctly identifies a
                        lane line, and the white solid line on the right correctly identifies an edge line. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        lane-use instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The white solid line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            no_turn:left: no marking governs this action
Step 5  Rule            no_turn:right: no marking governs this action
Step 5  Rule            no_turn:u_turn: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits moving beyond it.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change to the left lane as
                        the line is dashed, but you cannot move to the right beyond the solid edge line.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 875, 9.01 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with a median and a guardrail on the right. The road
                        ahead is straight with several vehicles in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary line
                        per [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary line
                        per [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 677, 6.37 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. The road ahead appears to be a straight
                        stretch with a slight curve to the right in the distance. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car, which appears to be the edge
                        of the roadway. Photo 2 shows a solid white line and a raised concrete barrier/curb to
                        the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (3) are consistent with the boundaries: a white dashed line on the left indicates
                        another lane of the same direction, and a solid white line with a curb on the right
                        indicates the edge of the roadway. | roles: The white dashed line on the left
                        correctly functions as a lane line, and the solid white line on the right correctly
                        functions as an edge line. | markings: No markings are present in the lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows for a lane
                        change.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line and a curb, which
                        prohibits moving to the right.
Step 6  go_straight     allowed (contested, correct): No markings or boundaries prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may change into the lane to your left,
                        but you are prohibited from moving to the right as it is the edge of the roadway.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 726, 6.64 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane roadway under an overpass. Ahead, there is a wide
                        intersection or merging area with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car, and further ahead, it appears to be a solid yellow line
                        separating my lane from the lane to its left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line very close to the car, and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow line on the left and a white line on the right. |
                        roles: The yellow line on the left and white line on the right fit the roles of lane
                        lines for a right-hand traffic system. | markings: No markings are in my lane, and the
                        lane to the left has a left-turn arrow. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing.
                        [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid lines on both sides prohibit lane changes. You
                        may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 860, 8.26 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a divided median and an overhead gantry. The road ahead is
                        clear of immediate intersections. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white lane-use arrow in my lane pointing
                        straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited: prohibited by the straight arrow marking
Step 6  turn_right      prohibited: prohibited by the straight arrow marking
Step 6  u_turn          prohibited: prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should continue straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 712, 7.36 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. The road ahead is straight with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my lane. Photo 2 shows a white solid
                        line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left separates me from the
                        lane to my left, and a white solid line on the right marks the edge of the roadway. |
                        roles: The white dashed line correctly functions as a lane line, and the white solid
                        line correctly functions as an edge line. | markings: No markings are present in my
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right beyond the edge line. Continue straight in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 674, 6.51 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a truck ahead. The road is bounded by a metal guardrail on
                        the left and a concrete barrier on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a concrete barrier on the right. Photo 2 shows a
                        solid white line and a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a white lane line separating my lane
                        from the lane to the right.; line:stop_yield (insufficient): Photo 1 shows a white
                        lane line separating my lane from the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on the left and the white edge line/barrier on
                        the right. | roles: The white solid line on the left is a lane line; the white solid
                        line and barrier on the right are an edge line. | markings: No specific arrows or
                        words are visible in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:stop_yield: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        concrete barrier on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid markings and the
                        concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9491, out 771, 8.68 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a divided median and a shoulder on the right. There is a
                        truck and a bus ahead in the adjacent lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is solid white near the car and becomes a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this line is solid white
                        and continuous.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on the left and the white edge line on the
                        right. | roles: The white lane line on the left and white edge line on the right fit
                        the roles of lane-line and edge-line respectively. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid portion of the left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are discouraged or prohibited by the solid
                        line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 733, 7.54 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass and signs overhead. The road ahead
                        is a straight stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white lane line on my left and a white edge line on
                        my right. | roles: The white lane line on the left and white edge line on the right
                        fit the roles of lane-line and edge-line respectively. | markings: The straight arrow
                        in my lane is consistent with the straight road ahead and the lane boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead travel.
                        [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and physical barrier on
                        the right (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed by the straight-ahead arrow (US-3B.23-01)
Step 6  turn_left       prohibited: prohibited by the straight-ahead arrow (US-3B.23-01)
Step 6  turn_right      prohibited: prohibited by the straight-ahead arrow (US-3B.23-01)
Step 6  u_turn          prohibited: prohibited by the straight-ahead arrow (US-3B.23-01)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should continue straight ahead. Lane changes to the
                        left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 838, 8.17 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with trees and buildings on both sides. The car is
                        traveling straight ahead in a lane with other vehicles nearby. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left.;
                        arrow:right (full): Photo 2 shows a white right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between same-direction traffic. | markings: The
                        arrows in adjacent lanes are consistent with the lane layout. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The white dashed line indicates that crossing into the right lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            arrow:left: The arrow indicates the lane to my left is for left turns. [[US-3B.23-01]]
Step 5  Rule            arrow:right: The arrow indicates the lane to my right is for right turns.
                        [[US-3B.23-01]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, which allows crossing
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action, but the lane to my left has
                        a left-turn arrow.
Step 6  turn_right      not_applicable: No markings in my lane govern this action, but the lane to my right
                        has a right-turn arrow.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may change lanes to the left or right as the lane
                        markings are dashed. Use the left lane for left turns and the right lane for right
                        turns at the upcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_left not_applicable although an arrow shows it', 'turn_right not_applicable
                        although an arrow shows it']
Tokens                  in 9491, out 872, 8.41 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test C | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming intersection or interchange. My
                        car is in a lane that appears to be a dedicated turn lane or a lane ending in a
                        specific movement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line near the car and becomes a dashed white line further
                        ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a solid white line
                        near the car and remains solid further ahead, bordering a shoulder or barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane. Photo 1 shows a white arrow pointing left in the lane to my left.; text:other
                        (full): Photo 2 shows large white characters painted in my lane. Photo 1 shows these
                        characters are '直行' (straight ahead).; line:stop_line (full): Photo 2 shows a white
                        line across the lane ahead, appearing as a stop line or a boundary for a turn area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lane lines on both sides. | roles: The white lines correctly
                        delineate same-direction traffic and the right edge. | markings: The 'straight' arrow
                        and '直行' text are consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line near the car discourages a lane change to the
                        left. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line marks the right edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane. [[US-3B.23-01]]
Step 5  Rule            text:other: The '直行' text confirms the lane is for straight-through traffic.
                        [[US-3B.20-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Do not attempt to change lanes or turn,
                        as the markings and lane lines indicate this lane is for straight-through traffic
                        only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line', 'text:other'], missed ['text:speed_limit']),
                        actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 1071, 11.33 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overhead gantry containing traffic signals and
                        signs. The road ahead appears to be a large intersection or a major junction with
                        multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.; no_turn:u_turn (insufficient): No markings are visible in my lane in Photo 1
                        or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a double yellow center line is on my left, and a white
                        lane line is on my right. | roles: The double yellow line correctly identifies a
                        center line (opposite traffic), and the white line identifies a lane line (same
                        direction traffic). | markings: No markings were observed in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
                        [US-3B.01-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed []), actions None, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 790, 8.69 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a median or barrier on the right. The road ahead
                        appears to be a straight stretch with multiple lanes of traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken yellow line near my car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a green barrier/curb on the right. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow lane line on the left and a white edge line on the right.
                        | roles: The yellow dashed line on the left correctly identifies a lane line between
                        same-direction traffic, and the white solid line on the right correctly identifies the
                        edge line. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white/yellow line indicates that crossing into the left lane
                        is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): allowed by the broken yellow lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [US-3B.23-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change into the left lane.
                        Changing into the right lane is prohibited by the edge line and curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 783, 8.54 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a tram or light rail system on the
                        right. My car is in a lane traveling straight ahead toward a distant intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car's left side.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, separating it from the tram
                        lane. Photo 2 shows a solid white line very close to the car's right side.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (partial): Photo 2 shows a double yellow line to the left
                        of my lane, which is the boundary between my lane and the lane to its left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left, and a white lane line
                        is on my right. | roles: The yellow center line and white lane line fit their
                        respective roles. | markings: The presence of a two-way left-turn lane to the left is
                        consistent with the yellow markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line shall not be used as a center line marking
                        on a two-way roadway, but here it delineates the separation of opposite traffic.
                        [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [[US-3B.06-05-06]]
Step 5  Rule            area:two_way_left_turn_lane: The markings delineate a lane that can be used by traffic
                        in either direction as part of a left-turn maneuver. [[US-3B.05-01]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 949, 9.67 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a bus lane or special lane on the right. The road
                        continues straight ahead with an intersection or signalized area in the distance.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my car. Photo 2 shows the same
                        double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car, separating it from a lane
                        with a bus symbol. Photo 2 shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (partial): Photo 1 shows a bus symbol in the lane to the right of my car.;
                        arrow:merge_right (partial): Photo 1 shows a white arrow in the lane to the right of
                        my car.
Step 4  Cross-check     close_up: the same in both photos | position: The double solid yellow line on the left
                        indicates a center line separating opposite traffic. The white line on the right
                        separates my lane from a special lane. My lane is the middle of three lanes in my
                        direction. | roles: The double solid yellow line correctly functions as a center line.
                        The solid white line correctly functions as a lane line. | markings: The bus symbol
                        and arrow are in the adjacent lane, not my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [US-3B.01-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right', 'symbol:bike'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 716, 7.85 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a transit station on the right. Ahead,
                        there is an intersection or a transition area with various lane markings and traffic
                        signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line very close to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a large white triangle pointing forward in the
                        center of my lane.; arrow:straight (full): Photo 2 shows a white arrow pointing
                        straight ahead in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The yellow line on the left separates my lane from the lane to the left
                        (center line), and the white line on the right marks the edge of the roadway. | roles:
                        The yellow center line and white edge line fit their respective roles. | markings: The
                        straight arrow and triangle are consistent with a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it delineates the separation of traffic in opposite
                        directions. [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes or making turns. Follow the straight-ahead arrow and stay within the
                        white edge line and yellow center line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 763, 8.34 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the right. There is a bus
                        stop on the left and a white van ahead in the center. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows a solid yellow line next to my car and a broken yellow line further ahead.
                        yellow solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a wide yellow hatched area on the right. Photo 2
                        shows a solid yellow line next to my car and a wide yellow hatched area further ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 shows yellow lane-use arrows in the lane to my
                        right. Photo 2 shows a yellow hatched area (channelizing) on the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the yellow lane line on my left and the yellow edge line/hatched
                        area on my right. | roles: The yellow color and solid/dashed patterns fit the roles of
                        lane lines and edge lines for a right-hand traffic system. | markings: The
                        channelizing area on the right correctly identifies the boundary of the roadway. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white (or yellow in this context) line discourages or
                        prohibits crossing into the left lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid yellow line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:channelizing: The channelizing lines form a neutral area where traffic is not
                        permitted to travel. [US-3B.08-01-03]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid yellow lines and the channelizing area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 767, 6.76 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The sun is low in the sky,
                        creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the boundaries: a double yellow center line on the left and a
                        white edge line on the right. | roles: The double yellow line correctly identifies a
                        center line separating opposite traffic, and the white line correctly identifies the
                        right edge. | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [US-3B.01-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 647, 7.98 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center lane. The road appears to be a one-
                        way street or a multi-lane roadway where traffic flows in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the dashed lane lines. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The dashed white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [US-3B.23-01]
Step 6  change_left     allowed (correct): allowed by the dashed white left boundary line per US-3B.06-05-06
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary line per US-3B.06-05-06
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking per US-3B.23-01
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking per US-3B.23-01
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking per US-3B.23-01
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking per US-3B.23-01
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change lanes to the left or right as needed, but
                        you should proceed straight ahead as indicated by the pavement arrow.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 788, 14.13 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows a solid yellow line
                        next to my car and a broken yellow line further ahead.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. Photo
                        1 shows a white left-turn arrow in the lane to my left.; arrow:right (full): Photo 2
                        shows a white right-turn arrow in the lane to my right. Photo 1 shows a white right-
                        turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow solid-dashed line fits the role of a center line
                        (separating opposite directions), and the white solid line fits the role of an edge
                        line. | markings: The arrows in adjacent lanes are consistent with the lane layout. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the opposite direction of
                        traffic. [US-3B.01-04]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates the permissible movement for the adjacent lane.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_left not_applicable although an arrow shows it', 'turn_right not_applicable
                        although an arrow shows it']
Tokens                  in 9491, out 773, 6.9 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching a large intersection with a
                        crosswalk. My car is positioned in a lane heading toward the intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly near the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is solid and white.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. A white line on the left indicates a lane to the left,
                        and a white line on the right indicates the edge of the roadway. | roles: The white
                        solid lines correctly serve as a lane line and an edge line. | markings: The crosswalk
                        is consistent with an intersection approach. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:crosswalk: no marking governs this action
Step 6  change_left     prohibited: prohibited by the solid white lane line (US-3B.06-05-06)
Step 6  change_right    prohibited: prohibited by the solid white edge line (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight through the intersection. Lane
                        changes to the left or right are prohibited by the solid lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 721, 13.72 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a dedicated bus lane on the right. An overhead gantry
                        with signs is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line to the left. Photo 2 shows a double yellow line
                        consisting of two solid yellow lines side by side.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, bordering a red-colored lane. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left
                        indicates a center line, and the white line on the right indicates a lane line,
                        consistent with being in the middle lane of three. | roles: The yellow double solid
                        line correctly identifies a center line (no passing). The white solid line correctly
                        identifies a lane boundary. | markings: The straight arrow is consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [US-3B.01-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 869, 9.56 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a dedicated transit lane or special
                        lane configuration. Ahead, the road continues straight with several lanes visible.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car, which appears to be the boundary between my lane and the
                        lane to its left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a yellow-painted area with diagonal markings to
                        the right. Photo 2 shows a solid yellow line and a yellow-painted area with diagonal
                        markings (chevron-like) immediately to the right of my lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show yellow-painted diagonal lines
                        (chevrons) in the area to the right of my lane.; area:two_way_left_turn_lane (full):
                        Photo 1 and Photo 2 show yellow-painted lines in the center of the road, appearing as
                        a two-way left-turn lane or a similar special lane configuration to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the boundaries: a yellow line on the left separates me from the
                        leftmost lane, and a yellow line/channelized area on the right defines the edge. |
                        roles: The yellow lines correctly indicate a special lane or separation of traffic
                        flows. | markings: The channelizing area to the right and the markings to the left are
                        consistent with a central lane in a special roadway configuration. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid yellow line delineates the edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            area:channelizing: Channelizing lines are used to form neutral areas where traffic is
                        not permitted to travel. [US-3B.08-01-03]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line and the
                        channelizing area
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane of a special roadway. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left or right due to the solid yellow
                        lines and the channelized area on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:two_way_left_turn_lane'], missed []), actions None, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 878, 8.07 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a green-colored surface, likely a dedicated transit or high-
                        speed corridor. There are several lanes ahead with vehicles moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a double solid yellow line to the right of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the double solid yellow lines on both sides, which
                        delineate the separation of traffic flows in opposite directions or special lanes. |
                        roles: The double solid yellow lines correctly function as center lines separating my
                        lane from adjacent lanes. | markings: No markings are present, which is consistent
                        with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [US-3B.01-06]
Step 5  Rule            right_boundary: The double solid yellow line prohibits crossing into the lane to the
                        right. [US-3B.01-06]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by double solid yellow lines on both sides, which prohibits
                        lane changes to the left or right. You should continue straight in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 830, 8.54 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus and other vehicles. The road ahead has multiple
                        lanes for through traffic and a dedicated bus lane on the right. (lanes 4, mine 2,
                        full)
Step 2  Left            Photo 1 shows a yellow double solid line to the left of my lane. Photo 2 shows a
                        yellow double solid line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with a double yellow center line on my left and a white lane
                        line on my right. | roles: The double yellow line correctly identifies the center line
                        separating opposite traffic, and the white line separates my lane from the bus lane. |
                        markings: The straight arrow in my lane is consistent with the lane's function. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [US-3B.01-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-through
                        traffic. [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 707, 8.12 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass ahead. My car is in a lane approaching an
                        intersection or a point where lanes are organized for different movements. (lanes 4,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to its left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to its right. Photo 2
                        shows this line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a large white arrow pointing left in the lane
                        to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) agree with the white lane lines on both sides. | roles: The white solid
                        lines correctly function as lane lines between same-direction traffic. | markings: The
                        straight arrow in my lane is consistent with the lane's role as a through lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 9491, out 916, 9.77 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be a through lane or a turn lane depending on the specific markings. (lanes 4, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this white line as solid next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white left-turn arrow in the lane to my left.
                        Photo 1 shows a white straight-ahead arrow in my lane.; text:only (full): Photo 2
                        shows white text 'ONLY' in the lane to my left. Photo 1 shows white text 'ONLY' in the
                        lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. I am in a middle lane bounded by white lines. | roles:
                        The white solid lines correctly function as lane lines separating traffic in the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'text:only'], missed ['line:stop_line']), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 946, 8.54 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus and other vehicles. The road ahead appears to be a
                        straight stretch with an intersection or pedestrian area further ahead. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line to the left of my car. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line to the right of my car. Photo 2 shows a solid yellow line
                        next to my car and a solid yellow line further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white lane-use arrow in my lane pointing
                        straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from another
                        lane, and a yellow line on the right marks the edge of the roadway. | roles: The white
                        lane line on the left and yellow edge line on the right fit the roles of a lane line
                        and an edge line respectively. | markings: The straight arrow in my lane is consistent
                        with the lane's function and the surrounding boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line (though yellow here, the rule for edge lines
                        applies) delineates the right-hand edge of the roadway. [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the mandatory or permissible movement for
                        this lane is to go straight. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should stay in your lane
                        and proceed straight; lane changes to the left or right are prohibited by the solid
                        markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 756, 7.76 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane approaching a crosswalk and a set of traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white crosswalk across the lane ahead of my
                        car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane) agree with the white lane lines on both sides. | roles: The white solid
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The crosswalk is consistent with an approach to an intersection. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: No specific rule provided for crosswalks in the list, but they
                        indicate a pedestrian crossing area.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight through the intersection. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 690, 7.07 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line with short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. Photo
                        2 shows a white left-turn arrow in the lane to my left.; arrow:right (full): Photo 1
                        shows a white right-turn arrow in the lane to my right. Photo 2 shows a white right-
                        turn arrow in the lane to my right.; arrow:merge_left (full): Photo 1 shows a white
                        straight arrow in my lane. Photo 2 shows a white straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle of three lanes. | roles: The white
                        dashed lines correctly identify the boundaries of my lane. | markings: The arrows in
                        the adjacent lanes and the straight arrow in my lane are consistent with the lane
                        layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line to the left is permitted.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Crossing the white dashed line to the right is permitted.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:merge_left: The arrow indicates that going straight is a permitted movement.
                        [[US-3B.23-01]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): The arrow in my lane indicates that going straight is a
                        permitted movement.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight, or change lanes to the left or
                        right as needed. Turn movements are not indicated for your specific lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:merge_left', 'arrow:right'], missed []), actions True, unsafe
                        [], citation in_pack_not_accepted, contradictions ['go_straight allowed although no
                        arrow shows it', 'turn_left not_applicable although an arrow shows it', 'turn_right
                        not_applicable although an arrow shows it']
Tokens                  in 9491, out 828, 7.73 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with specific
                        markings and arrows. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows the
                        solid white line and the curb clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; text:other
                        (full): Photo 2 shows the Chinese character '直' (straight) in my lane.; arrow:right
                        (full): Photo 2 shows a white right-turn arrow in the lane to my right.; text:other
                        (full): Photo 2 shows the Chinese character '直' (straight) in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white dashed line on the left and a solid white
                        line/curb on the right. | roles: The white dashed line correctly functions as a lane
                        line, and the solid white line/curb correctly functions as an edge line. | markings:
                        The left-turn arrow and 'straight' character in my lane are consistent with a multi-
                        movement lane. The right-turn arrow and 'straight' character in the adjacent lane are
                        consistent with its role. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line and curb delineate the right edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [US-3B.23-01]
Step 5  Rule            text:other: The character '直' (straight) indicates that going straight is a
                        permissible movement from this lane. [US-3B.20-01]
Step 6  change_left     allowed (contested, correct): allowed by the dashed white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white line and curb [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the 'straight' character [US-3B.20-01]
Step 6  turn_left       allowed: allowed by the left-turn arrow [US-3B.23-01]
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may go straight or turn left from your current lane. You are permitted to change
                        into the lane to your left, but you are prohibited from moving to the right onto the
                        curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 9491, out 966, 9.98 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test C | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly delineate lanes in the same direction of travel. | markings: The straight
                        arrow is consistent with the lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow marking.
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow marking.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow marking.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow marking.
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should continue straight
                        and avoid changing lanes or turning, as the markings and solid lines prohibit these
                        actions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 726, 7.74 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road in China. Ahead, there is a wide lane with a
                        large upward-pointing arrow, and a bicycle/pedestrian path to the right. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a white line on the left. Photo 2 shows a solid white
                        line next to a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white upward-pointing arrow in the center
                        of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (edge line on left, lane line on right). | roles: The
                        white solid lines and curb correctly define the lane boundaries. | markings: The
                        straight arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: No specific rule provided for this white edge line, but it defines the
                        left limit of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-through
                        traffic. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-through traffic. You should continue
                        straight and avoid changing lanes, as the solid white lines on both sides indicate
                        that lane changes are discouraged or prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 9491, out 689, 7.61 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead has multiple
                        lanes of traffic moving in the same direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows this same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this same solid white
                        line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line in the middle of my
                        lane, but it appears to be a lane divider for a bicycle lane or a similar sub-
                        division, not a primary lane marking. However, looking at the overall lane, there are
                        no primary arrows or words.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2,
                        the rightmost lane) agree with the boundaries: a yellow center line on the left and a
                        white edge line on the right. | roles: The yellow center line and white edge line fit
                        the roles of center line and edge line respectively. | markings: No primary markings
                        are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it separates lanes in the same direction (as per the
                        prompt's context of right-hand traffic). [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. Lane changes to the
                        left are prohibited by the solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 874, 7.65 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a sidewalk and trees on the right. The road ahead
                        appears to be a straight stretch with an intersection or signalized area in the
                        distance. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a sidewalk and a curb.
                        Photo 2 shows the solid white line and the raised curb clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the
                        center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a yellow center line is to my left and a white edge
                        line/curb is to my right. | roles: The yellow center line and white edge line fit
                        their respective roles. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the adjacent lane for
                        passing. [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You are permitted to proceed straight ahead as
                        indicated by the pavement arrow. Lane changes to the left are prohibited by the solid
                        yellow line, and the right boundary is the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 890, 8.82 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching a large intersection with a
                        pedestrian crosswalk. My car is in a lane that appears to be a dedicated turn lane or
                        a lane leading into a turn area. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb/sidewalk to the right. Photo 2
                        shows a solid white line immediately adjacent to a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in
                        the center of my lane.; line:crosswalk (full): Photo 1 shows a white crosswalk ahead
                        of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. A white line on the left indicates another lane of my
                        direction, and a white line with a curb on the right indicates the edge of the
                        roadway. | roles: The white solid lines and curb fit the roles of lane line and edge
                        line. | markings: The straight arrow and crosswalk are consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line and curb delineate the right-hand edge of the
                        roadway. [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        movement. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You should proceed straight
                        and avoid attempting to change lanes or turn left/right at the upcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 874, 7.84 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. A bus is directly
                        ahead in the center of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this white line clearly,
                        bordering a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow center line on the left and a white edge line on the
                        right. | roles: The yellow solid line correctly identifies a center line (opposite
                        traffic), and the white solid line correctly identifies an edge line. | markings: No
                        markings are present, which is consistent with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but in this context (China, right-hand traffic), it delineates the separation
                        of opposite traffic. [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 829, 6.74 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane roadway or ramp, possibly an elevated structure
                        or a tunnel entrance, with a large building on the right and a covered structure on
                        the left. Ahead, the road appears to continue straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; the
                        yellow line on the left and white line on the right define a single lane. | roles: The
                        yellow line on the left correctly identifies the left edge of the roadway, and the
                        white line on the right identifies the right edge. | markings: No markings are present
                        in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the right-hand edge of the roadway, but
                        here a yellow line is used for the left-hand edge. [US-3B.09-01-02]
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
Advice                  Stay in your lane; lane changes to the left or right are prohibited by the solid edge
                        lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9491, out 634, 5.7 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a dedicated bike lane on the right. The car is
                        traveling straight ahead in a lane with a bike lane to its right. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-painted bike lane.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white bicycle symbol on a red-painted area to the
                        right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on the left separates me from another lane,
                        and a white line on the right separates me from the bike lane. | roles: The white
                        dashed line on the left and solid white line on the right fit the roles of lane lines.
                        | markings: The bike symbol is in the adjacent lane, not my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the dashed white line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: Crossing the solid white line is discouraged or prohibited.
                        [US-3B.06-05-06]
Step 5  Rule            symbol:bike: No specific rule provided for the bike symbol in the adjacent lane.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane as the boundary is a dashed line. Do not move into
                        the bike lane on your right as it is separated by a solid line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9491, out 875, 7.56 s
```
