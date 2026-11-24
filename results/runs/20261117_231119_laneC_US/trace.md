# Reasoning of lane run 20261117_231119_laneC_US

```text
bdd100k_val__b1c66a42-6f7d68ca | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a median on the left. My car is in a
                        lane that has a school zone marking ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from a median/left lane. Photo 2
                        shows two solid yellow lines side by side.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a single white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'SCHOOL' painted in white in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a double yellow line on the left indicates a center line
                        separating opposing traffic or a median, and a white line on the right indicates an
                        edge line. | roles: The double yellow line correctly acts as a center line, and the
                        white line acts as an edge line. | markings: The 'SCHOOL' text is a general pavement
                        marking and does not conflict with the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            text:other: No specific rule governs the 'SCHOOL' text for lane usage.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow line [CN-6.1.2]
Step 6  change_right    prohibited: prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 719, 8.19 s

bdd100k_val__b1f0efd9-e900c6e5 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection. My car is in a
                        lane that appears to be the leftmost lane of a multi-lane direction. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (1)
                        agree with the yellow center line on the left and white lane line on the right. |
                        roles: The yellow solid line correctly identifies a center line separating opposing
                        traffic, and the white dashed line correctly identifies a lane line. | markings: The
                        left-turn arrow in my lane is consistent with the yellow center line on the left. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the opposite
                        direction of travel. [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The broken white lane line allows for lane changes. [[CN-5.2.3]
                        [mandatory] GB 5768.3-2025, section 5.2.3, page 44]
Step 5  Rule            arrow:left: The left-turn arrow indicates that the lane is for turning left.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow
Step 6  turn_left       allowed: allowed by the left-turn arrow
Step 6  turn_right      prohibited: prohibited by the left-turn arrow
Step 6  u_turn          prohibited: prohibited by the left-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to turn left at the upcoming intersection. Lane changes to the right are
                        permitted, but crossing the yellow line to the left or proceeding straight is
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 8313, out 806, 8.01 s

bdd100k_val__b1f4491b-dd8dfed5 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or arterial road with several lanes of traffic
                        moving in the same direction. There is a concrete barrier on the right side and a
                        fence/barrier on the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a separation from a shoulder/curb. Photo 2 shows this line as solid and
                        very close to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; arrow:straight (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a white dashed line on the left and a solid white
                        line/curb on the right. | roles: The white dashed line on the left correctly
                        identifies a crossable lane line, and the solid white line on the right correctly
                        identifies an edge line. | markings: No markings were observed, which is consistent
                        with the lack of specific movement restrictions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line next
                        to a curb, prohibiting a move to the right.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane as the line is broken. You
                        are prohibited from moving to the right as there is a solid edge line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read']
Tokens                  in 8313, out 816, 8.5 s

bdd100k_val__b20b69d2-e31380a7 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching a fork or a split in the roadway. A large
                        sign for 'West View City' is visible ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow curb and a solid yellow line separating my lane from a
                        median/island. Photo 2 shows a solid yellow line and a yellow curb.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; the
                        yellow line on the left separates my lane from the median/island, and the white line
                        on the right marks the edge of the roadway. | roles: The yellow center line and white
                        edge line fit their respective roles. | markings: No markings are present in the lane.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the area to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to change lanes to the left or
                        right as the boundaries are solid.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8313, out 657, 7.14 s

bdd100k_val__b263f57d-1ccf6e51 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street in wet conditions. Ahead, there is an
                        intersection with traffic signals and a building on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with a clear gap and a dash segment.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a separation from a sidewalk/curb area. Photo 2 shows a solid white line
                        very close to the car's right side.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across the lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        solid white line correctly functions as an edge line. | markings: The stop line is
                        consistent with the intersection ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited: prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary. You must come to a complete stop at
                        the white stop line before proceeding through the intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 917, 8.02 s

bdd100k_val__b2fbf86d-d5de82a4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings on both sides. The car is
                        traveling straight ahead in a lane with several other lanes of traffic in the same
                        direction. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows white dashed lines separating the lanes.;
                        area:left_turn_waiting (insufficient): No words, arrows, or special areas are visible
                        in my lane in Photo 1 or Photo 2.; area:two_way_left_turn_lane (insufficient): No two-
                        way left-turn lane is visible to the left of my lane in Photo 1.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (2) are consistent with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings are present in my lane to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a standard lane with broken white lines on both sides, allowing you to
                        change lanes to the left or right if needed. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:crosswalk'], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 790, 6.61 s

bdd100k_val__b3060c96-d2391b61 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight continuation or a slight curve, with other vehicles visible in the distance.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a yellow edge line on the left and a white lane line on
                        the right. | roles: The yellow solid line on the left correctly identifies the edge of
                        the roadway, and the white dashed line on the right separates my lane from the
                        adjacent lane. | markings: No markings were observed in the lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the direction of travel. You may proceed straight or
                        change into the lane on your right. Changing to the left is prohibited as it is the
                        edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 812, 7.94 s

bdd100k_val__b306fb3f-f02e46cc | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road with a grassy embankment on the left. The car is traveling in a lane
                        bounded by a yellow line on the left and a white line on the right. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (1) agree with the boundaries: a yellow edge line on the left and a white lane line on
                        the right. | roles: The yellow solid line correctly identifies the left edge of the
                        roadway, and the white solid line separates my lane from the one to the right. |
                        markings: No markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the right are prohibited by
                        the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 794, 7.92 s

bdd100k_val__b321c6b6-ab603d42 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings on both sides. My car is in a
                        lane heading straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol in the lane to the left of
                        mine.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane lines separating traffic in the same
                        direction. | markings: The bike symbol is in the adjacent lane, not my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 726, 5.66 s

bdd100k_val__b4542860-0b880bb4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in one
                        of the middle lanes of a multi-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): Photo 1 shows a white left-turn arrow in
                        the lane to my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        markings are in my lane; the left-turn arrow is in the adjacent lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary line [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a middle lane with dashed lines on both sides, allowing you to change lanes
                        to the left or right if needed. You may proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 847, 6.79 s

bdd100k_val__b48c7b5f-800d31b4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a taxi directly ahead in my lane. There
                        is a bus in the adjacent left lane and a car in the adjacent right lane. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows a solid yellow line next to my car and a broken yellow line further ahead.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow center line and white edge line fit their respective
                        roles. | markings: No markings are in my lane; the left-turn arrow is in the adjacent
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side of the broken-solid yellow line may not
                        cross. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            no_turn:left: no marking governs this action
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid side of the broken-solid
                        yellow line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 744, 7.35 s

bdd100k_val__b49d6c0d-457e13b3 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a bike lane on the right. My car is in a
                        lane heading straight toward a city area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, separating it from a bike
                        lane. Photo 2 shows this solid white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol and a white bicycle lane
                        marking in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a double solid yellow center line is on my left, and a
                        white edge line is on my right. | roles: The double solid yellow line correctly
                        identifies a center line, and the white line correctly identifies an edge line. |
                        markings: The bike symbol is in the lane to my right, not in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized vehicle lanes. [[CN-5.4.3]]
Step 5  Rule            symbol:bike: The bike symbol indicates space for non-motorized vehicles to travel or
                        park. [[CN-5.15.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (contested, correct): prohibited by the white edge line and the bike lane
                        marking
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight in your current lane. Do not attempt to change lanes to the
                        left or right, as the left boundary is a no-crossing center line and the right
                        boundary is a bike lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 747, 6.56 s

bdd100k_val__b4d18d1a-193e24a1 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection. My car is in a
                        lane that appears to have a grid marking ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line very close to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line very close to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a white grid marking in the center of my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line on the left correctly identifies a crossable
                        lane line, and the solid white line on the right correctly identifies a no-crossing
                        lane line. | markings: The grid marking is centered in my lane and is consistent with
                        the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane to my
                        right. [[CN-6.2.1]]
Step 5  Rule            area:grid: The grid marking indicates an area where stopping for any reason is
                        prohibited. [[CN-6.8.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving into
                        the right lane. Do not stop in the grid area ahead of your car.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 747, 6.01 s

bdd100k_val__b5042634-1034573c | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road under an overpass. Ahead, there is an
                        intersection with traffic signals and a taxi in the adjacent lane. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly in the foreground.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows this white dashed line clearly in the foreground.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line in the center of the
                        road, but no specific arrows or words are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        specific markings were identified in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is a crossable
                        lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the boundaries are broken white lines. Proceed straight through the
                        intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 876, 7.63 s

bdd100k_val__b54c065e-8b13cfe7 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane traveling straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a double solid yellow center line is on my left, and a
                        white lane line is on my right. | roles: The double solid yellow line correctly
                        identifies as a center line (separating opposing traffic), and the white line
                        correctly identifies as a lane line. | markings: No markings are present to contradict
                        the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 681, 6.11 s

bdd100k_val__b5661732-3684230b | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line to the left of my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line to the right of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        area:left_turn_waiting (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; area:two_way_left_turn_lane (full): No markings are visible in my lane in Photo 1
                        or Photo 2.; area:grid (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; area:channelizing (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; text:stop (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:keep_clear (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        text:bus (full): No markings are visible in my lane in Photo 1 or Photo 2.; text:hov
                        (full): No markings are visible in my lane in Photo 1 or Photo 2.; text:speed_limit
                        (full): No markings are visible in my lane in Photo 1 or Photo 2.; symbol:hov_diamond
                        (full): No markings are visible in my lane in Photo 1 or Photo 2.; symbol:bike (full):
                        No markings are visible in my lane in Photo 1 or Photo 2.; symbol:other (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; arrow:merge_left (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; arrow:merge_right (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; arrow:two_way_left (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; no_turn:left (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; no_turn:right (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.; no_turn:u_turn (full): No
                        markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries (white dashed lines on both sides). | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        movement restrictions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you can proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'no_turn:left', 'no_turn:right', 'no_turn:u_turn', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:speed_limit', 'text:stop'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8313, out 1416, 13.73 s

bdd100k_val__b577827c-28fc9b0d | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road approaching an intersection with a subway station on
                        the right. My car is in one of the lanes heading toward the intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a separation from a sidewalk/curb area. Photo 2 shows this solid white line
                        clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to my left. Photo
                        1 shows a white right-turn arrow in the lane to my right.; arrow:right (full): Photo 1
                        shows a white right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a solid white
                        line on the right. | roles: The white dashed line on the left correctly functions as a
                        lane line, and the solid white line on the right functions as an edge line. |
                        markings: The arrows in adjacent lanes are consistent with the lane layout. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right beyond the edge line. You can proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed although no arrow shows
                        it', 'turn_left not_applicable although an arrow shows it', 'turn_right not_applicable
                        although an arrow shows it']
Tokens                  in 8313, out 925, 8.48 s

bdd100k_val__b59e50fa-ca034dd0 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car. Photo 2 shows a solid white
                        line clearly visible next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows white dashed lines separating the lanes
                        ahead.; line:stop_line (insufficient): Photo 1 shows white dashed lines separating the
                        lanes ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left separates me from the
                        lane to my left, and a solid white line on the right marks the edge of the roadway. |
                        roles: The white dashed line on the left fits the role of a crossable lane line, and
                        the solid white line on the right fits the role of a road edge line. | markings: No
                        specific arrows or words are visible in my lane to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: no marking governs this action
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which marks the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane as it is separated by a
                        broken white line. Do not move to the right as the solid white line marks the edge of
                        the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 815, 8.19 s

bdd100k_val__b5cd5f72-32232751 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road approaching an intersection. My car is in a
                        dedicated right-turn lane. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a large white right-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white line on the left separates me from the middle lane,
                        and a white line on the right marks the edge. | roles: The white solid line on the
                        left is a lane line, and the white solid line on the right is an edge line. |
                        markings: The right-turn arrow in my lane is consistent with the lane's function as a
                        turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:right: The right-turn arrow restricts the allowed movements to turning right.
                        [[CN-5.13.2] [mandatory] GB 5768.3-2025, section 5.13.2, page 27]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line on the right
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow in the lane
Step 6  u_turn          prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Use this lane specifically for making a right turn at the upcoming intersection. Do
                        not attempt to go straight or change lanes, as these actions are prohibited by the
                        lane markings and boundaries.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8313, out 848, 7.8 s

bdd100k_val__b5f84825-c97df380 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection. My car is in a
                        lane that leads into a turn area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow in my lane pointing straight
                        ahead and to the left.; arrow:right (full): Photo 1 shows a white arrow in the lane to
                        my right pointing right.; arrow:left (full): Photo 1 shows a white arrow in the lane
                        to my left pointing left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The straight-left arrow in my lane is consistent with the dashed boundaries
                        and the intersection layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_left: The arrow indicates that my lane is designated for traveling
                        straight ahead or turning left. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white left boundary line
                        [CN-5.2.3]
Step 6  change_right    allowed (contested, correct): allowed by the broken white right boundary line
                        [CN-5.2.3]
Step 6  go_straight     allowed (correct): allowed by the straight-left arrow [CN-5.13.1]
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the straight-left arrow [CN-5.13.1]
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the straight-left arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-left arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight_left'], missed ['arrow:straight_right',
                        'line:stop_line']), actions False, unsafe ['turn_left'], citation
                        in_pack_not_accepted, contradictions ['turn_right prohibited although an arrow shows
                        it']
Tokens                  in 8313, out 1027, 9.53 s

bdd100k_val__b65fd3df-87ed965a | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street with parked cars on the right. My car is in a lane
                        moving forward, with an intersection or a continuation of the street ahead. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a motor/non-motor
                        separation line or a road edge line next to parked cars. Photo 2 shows this solid
                        white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a white line on my left separates me from another lane, and
                        a white line on my right marks the edge of the roadway. | roles: The white solid line
                        on the left fits the role of a no-crossing lane line, and the white solid line on the
                        right fits the role of an edge line. | markings: No markings are present in my lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left due to the solid white line. No turn
                        markings are present, so stay in your lane for straight travel.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 921, 9.19 s

bdd100k_val__b7041acc-6de39959 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or major road with an overpass ahead. My car is in a lane
                        traveling straight toward the overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line to the left of my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car. Photo 2 shows a solid white
                        line to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.;
                        no_turn:right (insufficient): No markings visible in my lane in Photo 1 or Photo 2.;
                        no_turn:u_turn (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane-
                        changeable boundary, and the solid white line on the right correctly identifies the
                        edge of the roadway. | markings: No markings were observed in my lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            no_turn:left: no marking governs this action
Step 5  Rule            no_turn:right: no marking governs this action
Step 5  Rule            no_turn:u_turn: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        marks the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change into the left lane as it is separated by a broken white line. Do not
                        move to the right as the solid white line marks the edge of the roadway. Proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed []), actions True, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 862, 8.37 s

bdd100k_val__b7935597-13c4b9dd | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with parked cars on both sides. My car is in
                        a lane moving forward towards an intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, which appears to be a lane line or edge
                        line. Photo 2 shows a solid white line very close to the car's left side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line
                        clearly separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a white line on the left (edge line) and a white line on
                        the right (lane line). | roles: The white solid lines correctly represent an edge line
                        on the left and a lane line on the right. | markings: No markings were observed, which
                        is consistent with the lack of specific lane-use indicators. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my side into the
                        right lane. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane roadway. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the right due to the solid white line. No
                        turn markings are present, so turns are not specifically governed by lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 856, 7.91 s

bdd100k_val__b7aa329e-25d68dec | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A two-way residential or suburban road with trees and houses on both sides. My car is
                        traveling forward in a lane with a double yellow line to its left and a white edge
                        line to its right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right side of my lane. Photo 2 shows a single solid
                        white line on the right side of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries: a double yellow center line on the left indicates my
                        lane is the rightmost lane of my direction (or the only lane if it's a two-lane road).
                        | roles: The yellow double solid line correctly identifies as a center line, and the
                        white line correctly identifies as an edge line. | markings: No markings are present
                        in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        double solid yellow line, and the white line on your right marks the edge of the
                        roadway.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 788, 7.11 s

bdd100k_val__b80018ef-3a620af0 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night with parked cars on both sides. The road ahead
                        appears to be a straight stretch with an intersection or continuation further ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the lane to my left.
                        Photo 2 shows the same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a single solid white line on
                        the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on my left indicates a
                        center line separating opposing traffic, and a white line on my right indicates an
                        edge line. | roles: The yellow double solid line correctly identifies as a center
                        line, and the white line correctly identifies as an edge line. | markings: No markings
                        are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 809, 7.98 s

bdd100k_val__b84146a1-a5f588ef | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane with other vehicles moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.; no_turn:u_turn (insufficient): No markings are visible in my lane in Photo 1
                        or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line on the
                        right. | roles: The white dashed line on the left correctly functions as a lane line,
                        and the white solid line on the right correctly functions as an edge line. | markings:
                        No markings were observed in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            no_turn:left: no marking governs this action
Step 5  Rule            no_turn:right: no marking governs this action
Step 5  Rule            no_turn:u_turn: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane
                        changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits moving onto the shoulder or sidewalk.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. You are prohibited from moving
                        to the right beyond the solid edge line. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 860, 8.54 s

bdd100k_val__b8fe9f2b-d63131a3 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane moving forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows a single white line
                        next to my car and a single white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows a single white line
                        next to my car and a single white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white line on the road surface ahead of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane lines separating traffic in the same
                        direction. | markings: The stop line is consistent with the approach to an
                        intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing to the left into the adjacent
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing to the right into the adjacent
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary line
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it
Step 6  turn_left       stop_first: allowed as no markings prohibit it
Step 6  turn_right      stop_first: allowed as no markings prohibit it
Step 6  u_turn          stop_first: allowed as no markings prohibit it
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You must come to a complete stop at the white stop line
                        before proceeding into the intersection. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 8313, out 825, 8.06 s

bdd100k_val__b91cdc5d-bce994ce | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with a row of residential buildings and a commercial building
                        on the right. The road ahead appears to be an intersection or a wide area where lanes
                        might merge or change. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows a white broken
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my car. Photo 2 shows a white solid
                        line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. Photo
                        2 shows a white left-turn arrow in the lane to my left.; arrow:left (full): Photo 1
                        shows a white left-turn arrow in the lane to my left. Photo 2 shows a white left-turn
                        arrow in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white broken line on my left and a white solid line
                        on my right. | roles: The white broken line on the left and white solid line on the
                        right fit the roles of lane lines separating traffic in the same direction. |
                        markings: The left-turn arrow is in the lane to my left, which is consistent with the
                        lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane on my
                        right. [[CN-6.2.1]]
Step 5  Rule            arrow:left: The arrow in the left lane indicates that the left lane is for left turns.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane, but you are prohibited
                        from changing into the right lane. You can proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it']
Tokens                  in 8313, out 820, 7.78 s

bdd100k_val__b928271b-fe5cc5d1 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight toward the intersection. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to a concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; arrow:straight (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white dashed line on my left and a solid white
                        line/curb on my right. | roles: The white dashed line on the left correctly functions
                        as a lane line, and the solid white line on the right correctly functions as an edge
                        line. | markings: No markings were observed in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line next to
                        a curb, which prohibits moving onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane allow or prohibit a left turn.
Step 6  turn_right      not_applicable: No markings in my lane allow or prohibit a right turn.
Step 6  u_turn          not_applicable: No markings in my lane allow or prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. You should stay within your
                        lane and avoid moving to the right onto the sidewalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read']
Tokens                  in 8313, out 794, 8.42 s

bdd100k_val__b9429f07-33ae3ff1 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane heading straight toward the intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly, with the lines being parallel and solid.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line to the right of my lane. Photo 2 shows this
                        same solid white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line on the right indicates an
                        edge line. | roles: The yellow double solid line correctly identifies as a center
                        line, and the white solid line correctly identifies as an edge line. | markings: No
                        markings are present in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The solid white line prohibits vehicles on the solid-line side from
                        crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 816, 8.31 s

bdd100k_val__ba2db972-f29458c8 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a sidewalk and a fence on the right.
                        Ahead, there is a clear roadway with multiple lanes of traffic. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway next to a sidewalk. Photo 2 shows this solid white line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 2 shows a white dashed line between the lanes.;
                        line:stop_line (insufficient): No other markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white dashed line is on my left and a white solid
                        line/curb is on my right. | roles: The white dashed line on the left correctly
                        functions as a lane line, and the white solid line/curb on the right correctly
                        functions as an edge line. | markings: No markings were identified in my lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line and a curb, which
                        prohibits crossing to the right.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change to the left lane as the boundary is a
                        broken white line. You are prohibited from moving further right as there is a solid
                        edge line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 780, 6.6 s

bdd100k_val__ba9f6c98-2a75a096 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A two-lane two-way road in a rural area. The road continues straight ahead into the
                        distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line on the left. Photo 2 shows the same double
                        solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line on the right. Photo 2 shows the same single
                        solid white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (partial): Photo 2 shows a small, faint, dark marking in the center of
                        the lane, but it is not a standard arrow or word.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree. A
                        double solid yellow line on the left indicates a center line separating opposing
                        traffic, and a white line on the right indicates the edge of the roadway. | roles: The
                        colors and patterns fit the roles: yellow for the center line and white for the right
                        edge line. | markings: The faint symbol does not contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            symbol:other: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way road. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left due to the double solid yellow
                        center line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 852, 7.69 s

bdd100k_val__bab692c9-4d1f2bdd | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a light rail or tram system in the
                        center. My car is in a lane to the right of the rail tracks. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the rail tracks. Photo 2
                        shows a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The yellow line on the left separates my lane from the rail tracks
                        (center/left boundary), and the white line on the right separates me from the adjacent
                        lane. | roles: The yellow solid line correctly acts as a center line (separating
                        opposing/different flows), and the white solid line acts as a lane line. | markings:
                        No markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the rail track
                        area. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The single solid white line prohibits crossing into the lane to the
                        right. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow line [CN-6.1.4]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by a solid yellow line on the left and a solid white line on
                        the right. You may proceed straight ahead, but lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 8313, out 705, 6.35 s

bdd100k_val__bb289fdb-4bc01501 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road at night with an intersection or signalized area ahead. My car
                        is in one of the middle lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: No markings were identified in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows for lane changes in both directions. You may proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 817, 6.75 s

bdd100k_val__bb8dba97-3537805c | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass structure on the left. The road
                        ahead appears to be a straight stretch of highway. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): No markings visible in my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (1) agree with the boundaries: a yellow edge line on the left and a white lane line on
                        the right. | roles: The yellow solid line fits the role of a left-hand edge line, and
                        the white dashed line fits the role of a lane line. | markings: No markings were
                        observed in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the highway. You may proceed straight or change to the
                        right lane. Changing to the left is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 803, 6.88 s

bdd100k_val__bbf0f5d7-ea2f1cc3 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on an elevated urban roadway or overpass. Ahead, there is a white
                        vehicle in the adjacent lane and a clear view of the road continuing forward. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white edge
                        line is on my right. | roles: The yellow solid line correctly acts as a center line
                        (separating opposing traffic) and the white solid line acts as an edge line. |
                        markings: No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the left lane.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the physical curb/edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left due to the solid yellow center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8313, out 710, 5.72 s

bdd100k_val__bbf48d08-b6a11dd8 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road approaching an intersection. My car is in a lane
                        that appears to be the rightmost lane of its direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows this solid
                        white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a double solid yellow center line is on my left, and a
                        white edge line is on my right. | roles: The double solid yellow line correctly
                        identifies as a center line, and the white line correctly identifies as an edge line.
                        | markings: No markings were observed, which is consistent with the lack of specific
                        lane-use instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the white edge line and curb [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 719, 7.44 s

bdd100k_val__bbfe3b4f-5137ff9f | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is approaching a large intersection with a pedestrian crosswalk. There are
                        multiple lanes of traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line (dashed) near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line as a solid white line
                        near the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in
                        the center of my lane.; line:stop_line (full): Photo 1 shows a white stop line across
                        the lane just before the crosswalk.
Step 4  Cross-check     close_up: The left boundary is dashed in Photo 2, while the right boundary is solid in
                        Photo 2. Both are white. The straight arrow is clearly visible in Photo 2. | position:
                        The lane count of 3 and my position as 2 (middle) is consistent with a white line on
                        my left and a white line on my right. | roles: The white lines correctly function as
                        lane lines separating traffic in the same direction. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose. The stop line is consistent with the
                        approach to an intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The solid white line prohibits me from crossing into the lane to my
                        right. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is intended for straight ahead
                        movement. [[CN-5.13.2]]
Step 5  Rule            line:stop_line: The stop line marks where I must stop before entering the
                        intersection. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white left boundary [CN-5.2.3]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right boundary
                        [CN-6.2.1]
Step 6  go_straight     stop_first (WRONG, label allowed): allowed by the straight arrow [CN-5.13.2]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [CN-5.13.2]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [CN-5.13.2]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you are prohibited from changing to the right.
                        You should proceed straight ahead but must come to a complete stop at the white stop
                        line before entering the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:crosswalk']), actions False,
                        unsafe [], citation in_pack_not_accepted, contradictions ['turn_right prohibited
                        although an arrow shows it']
Tokens                  in 8313, out 1085, 9.67 s

bdd100k_val__bc19c993-c0a0f85f | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane with a white line on its right and a yellow line on its left. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows white text 'ONLY' in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line on the left and a white edge line
                        on the right. | roles: The yellow solid line correctly identifies as a center line,
                        and the white solid line correctly identifies as an edge line. | markings: The 'ONLY'
                        text is visible in the lane, though the specific movement it refers to is not clearly
                        legible in the provided photos. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            text:only: The 'ONLY' marking indicates a specific movement is required for this lane,
                        but the specific movement is not clearly visible.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes to the left and right are prohibited by the
                        solid lines. Proceed straight ahead as allowed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:only'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 863, 8.12 s

bdd100k_val__bc9b5bfb-51ebcf39 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night with an intersection ahead. My car is in a lane that
                        appears to be the center lane of a three-lane direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line to the right of my lane. Photo 2 shows the
                        same single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a white grid pattern (crosshatch) ahead of my lane,
                        marking a buffer zone before the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a double solid yellow line on the left indicates a center
                        line separating opposing traffic, and a white line on the right separates my lane from
                        the lane to its right. | roles: The double solid yellow line correctly acts as a
                        center line, and the white line acts as a lane line. | markings: The grid marking is
                        consistent with an intersection approach. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 711, 6.8 s

bdd100k_val__bcbf328d-953430de | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road approaching an intersection. My car is in a
                        dedicated turn lane on the right side of the road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my car. Photo 2 shows the same
                        double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line and a curb to the right of my car. Photo 2 shows a solid
                        white line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow and the word 'ONLY' in white
                        paint in my lane.; text:only (full): Photo 2 shows the word 'ONLY' in white paint in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (3) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line/curb on the right indicates
                        an edge line. | roles: The double solid yellow line correctly acts as a center line,
                        and the white line/curb acts as an edge line. | markings: The left-turn arrow and
                        'ONLY' text are consistent with a dedicated left-turn lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite flow
                        of traffic. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:left: The left-turn arrow restricts the lane's use to left turns only.
                        [[CN-5.13.2]]
Step 5  Rule            text:only: The 'ONLY' text reinforces that the lane is for left turns only. [no
                        marking governs this action]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the white edge line and curb
                        [CN-5.4.3]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow [CN-5.13.2]
Step 6  turn_left       allowed: allowed by the left-turn arrow [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the left-turn arrow [CN-5.13.2]
Step 6  u_turn          prohibited: prohibited by the left-turn arrow [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn lane. You must turn left at the upcoming
                        intersection; going straight, turning right, or changing lanes is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'text:only'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 883, 9.55 s

bdd100k_val__bd338426-4b27de63 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road with an intersection ahead. My car is in a lane that appears to be
                        the rightmost lane of the main roadway, adjacent to a turn lane or a curb. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows this same white broken line clearly as a series of long dashes with gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which then transitions into a solid
                        white line and a curb/sidewalk area. Photo 2 shows a solid white line very close to
                        the car, and further ahead, a solid white line marks the edge of the roadway before a
                        turn area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white broken line is on my left (lane_line) and a white
                        solid line/curb is on my right (edge_line). | roles: The white broken line on the left
                        fits the role of a crossable lane line. The white solid line on the right fits the
                        role of an edge line. | markings: No markings were observed in my lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left across the broken white line. Do not attempt to move
                        to the right as it is bounded by a solid white line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 920, 9.28 s

bdd100k_val__bd354e59-e5a9e8c6 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with parked cars on the right. The road ahead
                        appears to be a straight stretch leading towards a distant intersection or
                        continuation of the street. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, with parked cars beyond it. Photo 2
                        shows this solid white line clearly next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from another
                        lane, and a white line on the right marks the edge of the roadway. | roles: The white
                        solid line on the left fits the role of a no-crossing lane line, and the white solid
                        line on the right fits the role of a road edge line. | markings: No markings are
                        present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but you
                        are prohibited from changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 902, 8.61 s

bdd100k_val__bd3bd3ab-8e38f822 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection or a transit hub.
                        My car is in a lane that appears to be the leftmost lane of a multi-lane roadway,
                        possibly near a transit station. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line very
                        close to the car's left side.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right side of the lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white line on the left acts as an edge line, and a
                        white line on the right acts as a lane line. | roles: The white solid lines correctly
                        represent an edge line (left) and a lane line (right) in a right-hand traffic
                        jurisdiction. | markings: The left-turn arrow in my lane is consistent with the lane's
                        role as a turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1]
Step 5  Rule            arrow:left: The left-turn arrow indicates that the lane is restricted to left turns.
                        [CN-5.13.2]
Step 6  change_left     not_applicable (contested, label prohibited): no marking governs this action
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1)
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow (CN-5.13.2)
Step 6  turn_left       allowed: allowed by the left-turn arrow (CN-5.13.2)
Step 6  turn_right      prohibited: prohibited by the left-turn arrow (CN-5.13.2)
Step 6  u_turn          prohibited: prohibited by the left-turn arrow (CN-5.13.2)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn at the upcoming intersection. Lane changes to the
                        right are prohibited by the solid white line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8313, out 951, 8.56 s

bdd100k_val__bd656105-ed6f8161 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street at an intersection during sunset. My car is positioned
                        in a lane approaching a crosswalk and a stop line. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows this line as a solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a solid white stop line across the lane ahead of
                        my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position
                        (rightmost lane, index 2) agree with the boundaries: a white lane line is on my left
                        and a white edge line/curb is on my right. | roles: The white lane line on the left
                        and white edge line on the right fit the roles of lane_line and edge_line
                        respectively. | markings: The stop line is consistent with the lane's position at an
                        intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the left lane. [[CN-6.2.1]
                        [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line [CN-6.4.1-2]
Step 6  turn_left       stop_first: stop_first due to the stop line [CN-6.4.1-2]
Step 6  turn_right      stop_first: stop_first due to the stop line [CN-6.4.1-2]
Step 6  u_turn          stop_first: stop_first due to the stop line [CN-6.4.1-2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white stop line before proceeding. Lane
                        changes to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': None, 'right': None}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions ['turn_left, turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 8313, out 905, 8.89 s

bdd100k_val__bd65dd37-4c3cdf2d | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway approaching an intersection or a junction. My car
                        is in a lane that appears to be the rightmost lane of the direction of travel. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line near the car and a broken line further
                        ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a road edge line. Photo 2
                        shows this line as a solid white line near the car and a solid white line further
                        ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white line on the left that becomes
                        broken further ahead, but no arrows or words are visible in my lane.
Step 4  Cross-check     close_up: The left boundary is solid near the car and broken further ahead in both
                        photos. The right boundary is solid in both. | position: The lane count (2) and my
                        position (2) agree with the boundaries: a white line on the left separates me from
                        another lane, and a white line on the right marks the edge. | roles: The white lane
                        line on the left and white edge line on the right fit their roles. | markings: No
                        markings are clearly visible in my lane to contradict the boundaries. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross; vehicles on the broken side
                        may cross. [[CN-6.2.3]]
Step 5  Rule            right_boundary: Crossing the solid edge line is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. Lane changes to the
                        left are prohibited where the line is solid near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 872, 9.04 s

bdd100k_val__bd8d420d-ec34c634 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a bus stop area on the right. My car is
                        in a lane adjacent to a bus stop lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bus stop lane on the right.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (partial): Photo 1 shows a white bus stop area with a solid white line on
                        its right and a solid white line on its left. Photo 2 shows the solid white line on
                        the left of the bus stop area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a solid white line
                        on the right. | roles: The white dashed line on the left is a lane line, and the solid
                        white line on the right is a lane line separating my lane from the bus stop area. |
                        markings: The bus stop area is clearly marked and consistent with the solid white line
                        on its left. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from crossing into the bus stop lane
                        to the right. [[CN-6.2.1]]
Step 5  Rule            area:grid: The bus stop area is a designated zone for buses. [no passage covers this
                        element]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left across the dashed line, but you are prohibited from
                        moving into the bus stop lane on your right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed ['arrow:straight_right']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8313, out 773, 7.32 s

bdd100k_val__bdc0dc52-b4d05890 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection. My car is in a
                        lane that appears to be the middle lane of a three-lane roadway. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line very close to the car's left side.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line very close to the car's right side.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (partial): Photo 1 shows a white left-turn arrow in the lane to
                        my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The left-turn arrow is in the adjacent lane, not my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change lanes to the left or right as needed, and
                        you may proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting'], missed ['line:stop_line']), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 852, 7.56 s

bdd100k_val__bdf6ab8b-3ebe8356 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road on a bridge or elevated structure. Ahead, there are
                        other vehicles and a green overhead sign. My car is in a lane moving forward. (lanes
                        2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:straight (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a yellow edge line on the left and a white lane line on
                        the right. | roles: The yellow solid line on the left correctly identifies the edge of
                        the roadway, and the white solid line on the right separates my lane from the adjacent
                        lane. | markings: No markings are present in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent lane on
                        the right. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane roadway. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the right due to the solid white line. The
                        yellow line on your left marks the edge of the road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 750, 14.01 s

bdd100k_val__be0a188d-c47bac51 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane bridge or elevated roadway with a metal truss structure
                        overhead. My car is traveling forward on a multi-lane road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a solid white line
                        near my car. Further ahead in Photo 1, the line appears to remain solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a white grid-like pattern (box) on the pavement ahead
                        of my car.
Step 4  Cross-check     close_up: The close-up (Photo 2) confirms the left boundary is dashed and the right
                        boundary is solid. The grid marking is clearly visible in Photo 2. | position: The
                        lane count of 3 and my position as lane 2 (middle) are consistent with a lane line on
                        the left and an edge line on the right. | roles: The white dashed line on the left
                        correctly functions as a crossable lane line, and the solid white line on the right
                        functions as an edge line. | markings: The grid marking is consistent with an area
                        where stopping is prohibited, which is common on bridge approaches. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            area:grid: The grid marking prohibits stopping for any reason in that area.
                        [[CN-6.8.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken, but you should not move to the
                        right as it is the edge of the roadway. Do not stop in the grid area ahead.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 966, 9.48 s

bdd100k_val__be22a1e1-cbcd82a6 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night with an intersection ahead. My car is in one of the
                        middle lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my lane. Photo 2 shows a white broken
                        line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my lane. Photo 2 shows a white
                        broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white broken lines on both sides. | roles: The white broken
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings were identified in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows for lane changes in both directions. You may proceed
                        straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 812, 6.67 s

bdd100k_val__be60191c-2dea5114 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane traveling
                        straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line next
                        to my car. Further ahead in Photo 1, the line remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): Photo 1 shows a white left-turn arrow in
                        the lane to my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white broken line is on my left and a white solid line is
                        on my right. | roles: The white broken line fits the role of a crossable lane line,
                        and the white solid line fits the role of a right-hand edge line. | markings: No
                        markings are in my lane; the left-turn arrow is in the adjacent lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you should not move to the right of
                        your current lane. You are clear to proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 885, 8.12 s

bdd100k_val__be839b4c-fba3ea45 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching an intersection with a crosswalk.
                        My car is in a lane that appears to be a dedicated turn lane or a lane ending at the
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a lane line or an
                        edge line. Photo 2 shows a solid white line very close to the car's right side, and a
                        sidewalk/curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows white text 'ONLY' and 'LEFT' painted in my lane.;
                        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane ahead of the
                        crosswalk.; line:stop_line (full): Photo 1 and 2 show a white stop line at the
                        crosswalk.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid line/curb on the
                        right. | roles: The white dashed line on the left correctly identifies a crossable
                        lane line, and the solid white line/curb on the right identifies the edge of the
                        roadway. | markings: The 'LEFT ONLY' text and the left-turn arrow are consistent with
                        each other and the lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            text:other: The 'LEFT ONLY' text restricts the lane's use to left turns only.
                        [[CN-5.13.2]]
Step 5  Rule            arrow:left: The left-turn arrow restricts the movement to a left turn. [[CN-5.13.2]]
Step 5  Rule            line:stop_line: The stop line marks where I must stop before entering the
                        intersection. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb
                        [CN-5.4.3]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the 'LEFT ONLY' text and left-
                        turn arrow [CN-5.13.2]
Step 6  turn_left       allowed: allowed by the 'LEFT ONLY' text and left-turn arrow [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the 'LEFT ONLY' text and left-turn arrow [CN-5.13.2]
Step 6  u_turn          prohibited: prohibited by the 'LEFT ONLY' text and left-turn arrow [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn at the upcoming intersection. You must come to a
                        complete stop at the white stop line before turning. Lane changes to the left are
                        permitted, but moving to the right is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'line:stop_line', 'text:other'], missed ['line:crosswalk']), actions
                        False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 1251, 10.85 s

bdd100k_val__be926190-5293afb9 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with traffic moving in both directions. There is an
                        intersection ahead with traffic lights. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line. Photo 2
                        shows a solid white line next to the car and a curb further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line/curb on the right indicates
                        an edge line. | roles: The yellow double solid line correctly identifies a no-crossing
                        center line, and the white line correctly identifies an edge line. | markings: No
                        markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of your direction. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left due to the double solid yellow
                        center line. No turn markings are present, so turns are not applicable.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 842, 7.83 s

bdd100k_val__bfa92b30-f12f3535 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road with a hillside on the right and buildings on the left. The road
                        ahead appears to be a straight stretch leading toward a distant intersection or
                        continuation. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the lane to my left.
                        Photo 2 shows the same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right, which appears to be the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on my left indicates a
                        center line separating opposing traffic, and a white line on my right indicates an
                        edge line. | roles: The yellow double solid line correctly identifies as a center
                        line, and the white line correctly identifies as an edge line. | markings: No markings
                        were observed in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way road. You may proceed straight ahead, but
                        you are prohibited from crossing the double solid yellow line to the left or moving
                        beyond the white edge line to the right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 849, 8.49 s

bdd100k_val__bfe2b817-505676ef | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with residential buildings on the left and
                        trees/parked cars on the right. The road ahead appears to be a straight stretch with
                        an intersection or continuing road in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, and further right, another
                        solid white line. Photo 2 shows the solid white line immediately to the right of my
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line on the right indicates the
                        edge of the roadway. | roles: The yellow double solid line correctly identifies as a
                        center line, and the white line correctly identifies as an edge line. | markings: No
                        markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way road. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left due to the double solid yellow
                        center line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 858, 8.61 s

bdd100k_val__bff4bb8b-152c6105 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass or bridge structure ahead. My car
                        is in a lane traveling straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line and a physical barrier (guardrail) to the left.
                        Photo 2 shows a solid yellow line immediately adjacent to the guardrail.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right. Photo 2 shows a white dashed line with
                        clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow center line on the left and a white lane line on the
                        right. | roles: The yellow solid line correctly identifies a center line separating
                        opposing traffic, and the white dashed line correctly identifies a lane line. |
                        markings: No markings were observed. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the opposing traffic
                        flow. [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-5.2.3] [mandatory] GB 5768.3-2025, section 5.2.3, page 4]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the right lane. Changing to the left is
                        prohibited by the solid yellow center line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 844, 6.87 s

bdd100k_val__c02d18db-f5278de0 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the left and commercial
                        buildings on the right. The road ahead appears to be a straight stretch leading toward
                        a distant intersection. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; line:yield_line (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.; line:stop_yield (insufficient): No markings are visible in my lane in Photo
                        1 or Photo 2.; area:left_turn_waiting (insufficient): No markings are visible in my
                        lane in Photo 1 or Photo 2.; area:two_way_left_turn_lane (insufficient): No markings
                        are visible in my lane in Photo 1 or Photo 2.; area:grid (insufficient): No markings
                        are visible in my lane in Photo 1 or Photo 2.; area:channelizing (insufficient): No
                        markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white dashed line on my left and a white solid line
                        on my right. | roles: The white dashed line on the left correctly functions as a lane
                        line, and the white solid line on the right correctly functions as an edge line. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        lane-use instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            left_boundary: The broken line means it may be crossed. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows for lane
                        changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits crossing onto the shoulder/curb.
Step 6  go_straight     allowed (contested, correct): No markings govern this action.
Step 6  turn_left       not_applicable: No markings govern this action.
Step 6  turn_right      not_applicable: No markings govern this action.
Step 6  u_turn          not_applicable: No markings govern this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. You should stay within the
                        roadway and avoid moving to the right beyond the solid edge line. Proceed straight
                        ahead as there are no specific turn restrictions in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8313, out 999, 10.48 s

bdd100k_val__c068a67b-03b6e200 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with parked cars on both sides. The road
                        ahead appears to be a straight continuation of the current street. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line clearly as a solid line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:yield_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        line:stop_yield (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        area:left_turn_waiting (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; area:two_way_left_turn_lane (full): No markings are visible in my lane in Photo 1
                        or Photo 2.; area:grid (full): No markings are visible in my lane in Photo 1 or Photo
                        2.; area:channelizing (full): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white lane
                        line is on my right. | roles: The yellow solid line correctly identifies as a center
                        line (separating opposing traffic) and the white solid line as a lane line. |
                        markings: No markings are present, which is consistent with the straight road ahead. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the lane to the
                        left. [CN-6.1.4]
Step 5  Rule            right_boundary: The single solid white line prohibits crossing into the lane to the
                        right. [CN-6.2.1]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8313, out 930, 7.8 s

bdd100k_val__c07733d0-7525eae7 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        left. Ahead, there is a green overhead sign and several vehicles in the distance.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows a solid yellow line next to the car and a solid yellow line further ahead.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line next
                        to the car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows a white dashed line separating my lane
                        from the lane to the right.; line:stop_line (insufficient): Photo 1 shows a white
                        dashed line separating my lane from the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white lane
                        line is on my right. | roles: The yellow solid line correctly identifies as a center
                        line (separating opposing traffic or a special lane, but here it marks the left edge
                        of my direction's flow against a barrier/median). The white dashed line correctly
                        identifies as a lane line. | markings: No markings were found in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [CN-6.1.1]
Step 5  Rule            right_boundary: The broken white line allows crossing into the lane to the right.
                        [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may move to the right lane if needed, but you are
                        prohibited from moving to the left lane due to the solid yellow line. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 909, 8.59 s

bdd100k_val__c07733d0-aebb8786 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road with a clear view ahead. The road appears to be a divided highway or
                        a large arterial road with multiple lanes in the same direction. (lanes 4, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line to the left of my lane. Photo 2 shows a white broken
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my lane. Photo 2 shows a white
                        broken line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.;
                        arrow:straight (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (2) agree with the white broken lines on both sides, indicating I am in one of the
                        middle lanes. | roles: The white broken lines correctly function as lane lines
                        separating traffic in the same direction. | markings: No markings are present in my
                        lane, which is consistent with a standard through-lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a standard through-lane. You may change lanes to the left or right as
                        needed, and you are permitted to continue straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 746, 6.67 s

bdd100k_val__c0e7271a-a3c8d55f | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road with a concrete barrier on the right. Ahead, there
                        is an intersection or a point where the road layout changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a concrete barrier on the right. Photo 2 shows a
                        solid white line immediately adjacent to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line/curb on the
                        right. | roles: The white dashed line on the left correctly identifies a lane-change
                        boundary, and the white solid line/curb on the right correctly identifies the edge of
                        the roadway. | markings: No markings were observed, which is consistent with the clear
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane
                        changes.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white line and a curb,
                        which prohibits moving to the right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as there is a solid line and a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 734, 7.22 s

bdd100k_val__c0efbe92-2ee3e529 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings on both sides. My car is in a
                        lane heading forward, with other vehicles in adjacent lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line near the
                        parked cars. Photo 2 shows this line as a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        white solid line functions as an edge line. | markings: No markings were observed,
                        which is consistent with the lack of specific lane-use instructions. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the left lane. Do not attempt to move into the
                        area beyond the solid white line on your right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 857, 7.57 s

bdd100k_val__c100db13-71b423e5 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        right. Ahead, there is a large green overhead directional sign and an intersection or
                        interchange area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with a clear gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car, followed by a concrete
                        barrier. Photo 2 shows a solid white line very close to the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; line:yield_line (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.; line:stop_yield (insufficient): No markings are visible in my lane in Photo
                        1 or Photo 2.; area:left_turn_waiting (insufficient): No markings are visible in my
                        lane in Photo 1 or Photo 2.; area:two_way_left_turn_lane (insufficient): No markings
                        are visible in my lane in Photo 1 or Photo 2.; area:grid (insufficient): No markings
                        are visible in my lane in Photo 1 or Photo 2.; area:channelizing (insufficient): No
                        markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line is on my left and a white solid
                        line/curb is on my right. | roles: The white dashed line on the left fits the role of
                        a crossable lane line, and the white solid line on the right fits the role of an edge
                        line. | markings: No markings were observed, which is consistent with the absence of
                        specific lane-use instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid line on the right prohibits crossing onto the shoulder or
                        beyond. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white line and a
                        concrete barrier, prohibiting crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as there is a solid line and a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8313, out 995, 8.1 s

bdd100k_val__c107c2f1-b2b8fff0 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or elevated roadway with a concrete barrier on the left and a
                        metal guardrail on the right. The road ahead appears to be a continuous stretch of
                        highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line to the right of my lane. Photo 2 shows the
                        same single solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line on the right separates my
                        lane from the lane to its right. | roles: The double solid yellow line correctly
                        identifies as a center line, and the white line correctly identifies as a lane line. |
                        markings: No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 770, 7.14 s

bdd100k_val__c121b93f-b2ee73d4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane that appears to be the rightmost lane of its direction, adjacent to a white
                        curb/edge line. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows this same white broken line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a road edge line.
                        Photo 2 shows this solid white line clearly next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.; no_turn:left (insufficient): Photo 1 shows
                        a white left-turn arrow in the lane to my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white broken line is on my left and a white solid
                        line/curb is on my right. | roles: The white broken line on the left fits the role of
                        a crossable lane line. The white solid line on the right fits the role of a road edge
                        line. | markings: No markings are in my lane, which is consistent with the lane's
                        position as a right-turn or straight-through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            no_turn:left: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white line and a curb,
                        prohibiting a move to the right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change into the lane to
                        your left. Do not attempt to move further to the right as it is the edge of the
                        roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 833, 7.69 s

bdd100k_val__c1589305-200e315b | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is at an intersection in a city. A crosswalk and stop lines are visible
                        directly ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines separating traffic in the same direction.
                        | markings: The stop line is consistent with the intersection ahead. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule for a white solid lane line is provided in the text,
                        but it generally separates lanes of the same direction. [null]
Step 5  Rule            right_boundary: No specific rule for a white solid lane line is provided in the text,
                        but it generally separates lanes of the same direction. [null]
Step 5  Rule            line:stop_line: No specific rule for a stop line is provided in the text, but it marks
                        where vehicles stop. [null]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white stop line before proceeding in any
                        direction. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk']), actions None, unsafe [], citation unlisted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8313, out 683, 7.22 s

bdd100k_val__c15c29a5-74788f46 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on the right and trees on the left. The road
                        ahead is straight with several lanes of traffic moving in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this line is a single solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is a single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a yellow center line on the left and a white lane
                        line on the right. | roles: The yellow solid line correctly identifies a center line
                        (separating opposing traffic), and the white solid line correctly identifies a lane
                        line. | markings: No markings were observed in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the lane to the
                        left. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The single solid white line prohibits crossing into the lane to the
                        right. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 814, 8.05 s

bdd100k_val__c1627cd8-d8c10968 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street at night with an intersection ahead. My car
                        is in a dedicated left-turn lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a left-turn arrow and the word 'ONLY' in my lane.;
                        text:only (full): Photo 1 shows the word 'ONLY' in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white lane line is
                        on my right. | roles: The yellow solid line correctly identifies as a center line
                        (separating opposing traffic) and the white solid line as a lane line. | markings: The
                        left-turn arrow and 'ONLY' text are consistent with the lane's role as a dedicated
                        turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the opposite
                        traffic flow. [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane to the
                        right. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:left: The left-turn arrow restricts the lane's use to left turns only.
                        [[CN-5.13.2] [mandatory] GB 5768.3-2025, section 5.13.2, page 27]
Step 5  Rule            text:only: The 'ONLY' text reinforces that the lane is for left turns only. [no
                        marking governs this action]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the left-turn arrow
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow
Step 6  u_turn          prohibited (correct): prohibited by the left-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn lane. You must turn left at the upcoming
                        intersection; going straight, turning right, or changing lanes is prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight']), actions False, unsafe ['turn_left'],
                        citation unlisted, contradictions []
Tokens                  in 8313, out 890, 8.96 s

bdd100k_val__c173438f-01b0b013 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road at night with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right, which appears to be the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white broken line on the left and a white solid line on the
                        right. | roles: The white broken line correctly functions as a lane line, and the
                        white solid line correctly functions as an edge line. | markings: No markings were
                        observed, which is consistent with the lack of specific lane-use indicators. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not move to the right as it
                        is the edge of the roadway. Proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 850, 7.77 s

bdd100k_val__c1b3582d-b9c87c82 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane that appears to be the middle lane of three lanes of traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a solid line near my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line near my car
                        and a broken line further ahead. Photo 2 shows a solid white line near my car. Photo 1
                        shows a sidewalk and a curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.; no_turn:left (insufficient): Photo 1 shows
                        a white left-turn arrow in the lane to my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on my left and a white edge line on my right. |
                        roles: The white lane line on the left and white edge line on the right fit their
                        roles. | markings: No markings are in my lane, which is consistent with the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white edge line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line and the curb/edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 824, 8.21 s

bdd100k_val__c1b5a91c-9e402e78 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or arterial road with a concrete barrier on the
                        left. Ahead, there is a slight curve and a bridge structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows a solid yellow line clearly visible next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white lane
                        line is on my right. | roles: The yellow solid line correctly identifies as a center
                        line (separating opposing traffic or a median-like boundary) and the white dashed line
                        as a lane line. | markings: No markings are present in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The broken white line allows crossing into the lane to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.1]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change into the lane to your right, but you are prohibited from changing into
                        the lane to your left. You may proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 671, 6.68 s

bdd100k_val__c2021c8c-474a8eda | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with vehicles moving in the same direction.
                        The road ahead appears to be a straight stretch of urban street. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line to the left of my car. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my car. Photo 2 shows a solid white line
                        next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from the left side into the
                        adjacent lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from the right side into the
                        adjacent lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        per [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        per [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 751, 6.94 s

bdd100k_val__c264943c-5e493c9f | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane that features a large 'SCHOOL' marking on the pavement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'SCHOOL' painted in white in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a center line on the left and a lane line on the right. | roles:
                        The double solid yellow line correctly identifies a center line, and the solid white
                        line correctly identifies a lane line. | markings: The 'SCHOOL' text is a pavement
                        marking within my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite
                        direction of travel. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            text:other: The 'SCHOOL' marking is a pavement text marking and does not govern
                        specific movements.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane with a 'SCHOOL' marking. You may proceed straight ahead, but you are
                        prohibited from changing lanes to the left or right due to the solid lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 704, 7.66 s

bdd100k_val__c28b60fb-a5e9b955 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road with a concrete barrier on the left and a hillside
                        on the right. Ahead, there is a commercial area with several buildings and a gas
                        station. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line further ahead that appears to be a lane line. Photo 2 shows
                        a white line next to my car that is broken.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows a white line further ahead that is
                        broken.
Step 4  Cross-check     close_up: The right boundary is a broken white line in Photo 2, while it appears more
                        solid in the distance in Photo 1. Photo 2 decides the pattern next to my car. |
                        position: The lane count (3) and my position (2) are consistent with a yellow center
                        line on the left and a white lane line on the right. | roles: The yellow solid line on
                        the left correctly identifies a center line separating opposing traffic (or a
                        restricted lane), and the white dashed line on the right correctly identifies a lane
                        line. | markings: No specific arrows or words are visible in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The broken white line allows crossing into the lane to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the right lane. Changing to the left is
                        prohibited by the solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 691, 7.38 s

bdd100k_val__c2fb790e-4cd5a630 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane traveling straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a road edge line. Photo 2
                        shows this line as a solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Photo 1 shows a white 'ONLY' text and a left-turn
                        arrow in the lane to my left. Photo 2 shows the 'ONLY' text and arrow clearly in the
                        lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on my left and a white edge line on my right. |
                        roles: The white solid line on the left is a lane line; the white solid line on the
                        right is an edge line. | markings: The 'ONLY' text and arrow are in the lane to my
                        left, identifying it as a special lane (two-way left-turn lane). | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the lane to
                        my left. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            area:two_way_left_turn_lane: The lane to my left is a two-way left-turn lane. [null]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8313, out 782, 7.33 s

bdd100k_val__c300fd4b-8ff92c2d | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road under an overpass. Ahead, there is a
                        clear roadway with multiple lanes of traffic. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line clearly as a solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier/wall on the right. Photo 2 shows a solid concrete
                        barrier immediately to the right of the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a concrete barrier
                        is on my right. | roles: The yellow solid line correctly identifies as a center line
                        (separating opposing traffic) and the concrete barrier as an edge line. | markings: No
                        markings are present in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the lane to the
                        left. [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The concrete barrier marks the edge of the roadway. [[CN-5.4.1]
                        [informative] GB 5768.3-2025, section 5.4.1, page 5]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid yellow center line, and the right side is bounded by a concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8313, out 676, 13.39 s

bdd100k_val__c3026ac7-8105e9a9 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an overpass and an intersection ahead. My
                        car is in a lane with a white vehicle directly in front. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a solid line near my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line as a solid line near my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; arrow:right
                        (full): Photo 2 shows a white right-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The left and right turn arrows in my lane are consistent with the lane's function at
                        the upcoming intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the left lane.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the right lane.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permitted movement.
                        [[CN-5.13.1]]
Step 5  Rule            arrow:right: The arrow indicates that a right turn is a permitted movement.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the lane-use arrows which only
                        show left and right turns [CN-5.13.2]
Step 6  turn_left       allowed: allowed by the left-turn arrow [CN-5.13.1]
Step 6  turn_right      allowed: allowed by the right-turn arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the lane-use arrows which do not show a U-turn [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Your lane is designated for left and right turns only at the upcoming intersection.
                        You should not attempt to go straight or change lanes, as these actions are prohibited
                        by the markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 855, 8.05 s

bdd100k_val__c308561a-1b698bb4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        right. My car is in a lane that appears to be the rightmost lane of the main roadway,
                        adjacent to a shoulder or emergency lane. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which then transitions into a solid white
                        line further ahead. Photo 2 shows a solid white line very close to the car, which is
                        the edge of the lane. Further ahead in Photo 1, this line remains solid and separates
                        the lane from the shoulder/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:keep_clear (partial): Photo 2 shows white text painted in my lane, but it is
                        partially obscured by the car's rear and the angle. It appears to be 'KEEP CLEAR' or
                        similar, but is not fully legible.
Step 4  Cross-check     close_up: The close-up confirms the right boundary is a solid white line and the left
                        boundary is a broken white line. The text in the lane is visible but partially
                        obscured. | position: The lane count (3) and my position (3) are consistent with a
                        white dashed line on the left and a solid white line on the right. | roles: The white
                        dashed line on the left correctly identifies a lane-change possibility, and the solid
                        white line on the right correctly identifies the edge of the roadway. | markings: The
                        'KEEP CLEAR' text is consistent with a lane near an exit or intersection, though its
                        specific meaning is secondary to the lane boundaries. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            text:keep_clear: The 'KEEP CLEAR' marking indicates that the area should not be
                        blocked by stopped vehicles.
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right onto the shoulder, as the solid white line and concrete barrier prohibit this.
                        Ensure you do not block the area marked 'KEEP CLEAR'.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:keep_clear'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 1043, 9.98 s

bdd100k_val__c31d9531-694298f0 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        right. The road ahead is clear of immediate intersections, and my car is traveling in
                        one of the middle lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the lane to my right. Photo 2
                        shows this white solid line clearly. Further right, there is a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line/barrier on
                        the right. | roles: The white dashed line on the left correctly identifies a lane-
                        change possibility, and the white solid line/barrier on the right correctly identifies
                        the edge of the roadway. | markings: No markings were observed, which is consistent
                        with the clear lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid line on the right prohibits crossing into the area beyond
                        the roadway. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line and a
                        concrete barrier, which prohibits crossing [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as it is bounded by a solid line and a concrete barrier. Continue straight in
                        your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 790, 8.0 s

bdd100k_val__c3321660-e6b60390 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street at night with an intersection ahead. My car is in a lane
                        that leads straight through the intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow pointing straight ahead
                        in the center of my lane.; line:stop_line (full): Photo 1 shows a solid white stop
                        line across the lane ahead of the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow and stop line are consistent with a lane intended for straight
                        movement through an intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing to the left. [CN-6.2.1]
Step 5  Rule            right_boundary: The solid white line prohibits crossing to the right. [CN-6.2.1]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for straight movement.
                        [CN-5.13.2]
Step 5  Rule            line:stop_line: The stop line marks where the vehicle must stop before proceeding.
                        [CN-6.4.1]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     stop_first (WRONG, label allowed): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight movement only. You must come to a complete
                        stop at the white stop line before proceeding straight through the intersection. Lane
                        changes are prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe [],
                        citation unlisted, contradictions ['leftmost lane, but a lane line on the left',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 8313, out 932, 7.09 s

bdd100k_val__c3bb4925-f78e285a | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with several vehicles ahead. The road appears
                        to be a divided highway or a large boulevard with a concrete barrier on the left.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car. Further ahead in Photo 1, the line appears to remain solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. No
                        markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left correctly identifies a
                        crossable lane line, and the white solid line on the right correctly identifies an
                        edge line. | markings: The left-turn arrow is in the adjacent lane, which is
                        consistent with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:left: The arrow in the left lane indicates that lane is for left turns.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which is
                        an edge line, and the rule for edge lines generally prohibits crossing onto the
                        shoulder/curb.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane if needed as the
                        boundary is a dashed line. Do not attempt to move to the right beyond the solid white
                        edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it']
Tokens                  in 8313, out 793, 8.18 s

bdd100k_val__c4057c0c-000a6aaf | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is
                        positioned in a lane that appears to be a turn lane or a lane leading into an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line to the left of my lane. Photo 2 shows a solid yellow
                        line very close to the car's left side.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line clearly visible just ahead of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows a white 'S' painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow center line on the left and a white lane line on the
                        right. | roles: The yellow solid line correctly identifies a center line separating
                        opposing traffic, and the white dashed line correctly identifies a lane line. |
                        markings: The 'S' marking is visible in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits the car from crossing into the
                        opposing traffic flow. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The broken white lane line allows the car to change into the lane on
                        the right. [[CN-5.2.3]]
Step 5  Rule            text:other: No specific rule governs the 'S' marking.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, label stop_first): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane on your right. Crossing the solid
                        yellow line to the left is prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:other'], missed ['text:stop']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 853, 8.49 s

bdd100k_val__c47fb4ff-92db68d6 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road passing under a bridge. There is a concrete
                        wall on the right side of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid white line clearly, separating the lane from a paved
                        area/shoulder next to a concrete wall.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead. Photo 2 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white broken line on the left and a white solid line on the
                        right. | roles: The white broken line on the left correctly functions as a lane line,
                        and the white solid line on the right correctly functions as an edge line. | markings:
                        The straight-right arrow in my lane is consistent with the lane's position and the
                        surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is intended for straight ahead
                        or right turn movements. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the guide arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the guide arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      allowed: allowed by the guide arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the guide arrow which does not show a U-turn [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. You are permitted to
                        change lanes to the left, but you are prohibited from changing lanes to the right or
                        making a left turn/U-turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 1001, 9.03 s

bdd100k_val__c4b3ab99-a4a09eeb | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road with an overpass structure above. Ahead, the road
                        appears to continue straight towards an intersection or a continuation of the roadway.
                        My car is in a lane bounded by white lines. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line near my car and remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right side of my lane. Photo 2 shows this line is a
                        solid white line near my car and remains solid further ahead. There is a curb/wall
                        further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a grid pattern (crosshatched lines) to the left of my
                        lane, but not inside my lane. No markings are visible inside my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on my left and the white edge line on my
                        right. | roles: The white solid line on the left is a lane line; the white solid line
                        on the right is an edge line. | markings: The grid area is to the left of my lane, not
                        in it. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            area:grid: The grid marking indicates an area where stopping is prohibited.
                        [[CN-6.8.1-2] [mandatory] GB 5768.3-2025, section 6.8.1, 6.8.2, page 53]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight. Lane changes to the left or
                        right are prohibited by the solid white lines. Do not stop in the grid area to your
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 8313, out 1020, 8.64 s

bdd100k_val__c4b3ce3d-cdc056ce | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming interchange or exit. My car is in
                        a lane heading straight toward a set of overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be an edge line. Photo
                        2 shows a white solid line very close to the car, and further ahead, it remains solid
                        before meeting a barrier/guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): Photo 1 shows a white left-turn arrow in the
                        lane to my left, but no markings are visible in my own lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        white solid line correctly functions as an edge line. | markings: No markings are in
                        my lane; the left-turn area is in the adjacent lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left if needed, but you should not move to the right as it
                        is the edge of the roadway. Proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 888, 8.97 s

bdd100k_val__c4e97226-7be7eef5 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road with a brick wall on the right. An
                        intersection or overpass is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line to the left of my car. Photo 2 shows a solid white line
                        next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line to the right of my car. Photo 2 shows a dashed white
                        line next to the car.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): Photo 1 shows a dashed white line to the right of my car,
                        which appears to be a lane-change line or edge line.
Step 4  Cross-check     close_up: Photo 2 shows a solid white line next to the car and a dashed white line
                        further ahead on the left. Photo 1 shows the same. Photo 2 shows a dashed white line
                        on the right. The same in both photos. | position: The lane count is 3. My lane is the
                        middle one (index 2). The left boundary is a lane line, and the right boundary is an
                        edge line. This is consistent. | roles: The white solid-dashed line on the left is a
                        no-crossing lane line (solid side). The white dashed line on the right is an edge
                        line. This is consistent. | markings: No specific arrows or words are visible in my
                        lane. The dashed line on the right is an edge line. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from the solid side (my side)
                        into the left lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The dashed edge line indicates the boundary of the roadway.
                        [[CN-5.4.2] [recommended] GB 5768.3-2025, section 5.4.2, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or move to the right. Changing to the left lane is
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        ['change_right allowed across a curb']
Tokens                  in 8313, out 945, 8.01 s

bdd100k_val__c4ee0cc4-b7af9602 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road at night with an intersection ahead. My car is in a lane with
                        a vehicle to its right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a white dashed line on the right side of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line on the left and a white lane line on
                        the right. | roles: The yellow solid line correctly identifies a center line
                        (separating opposing traffic), and the white solid line correctly identifies a lane
                        line. | markings: The white dashed line on the right is a lane line, not a stop-yield
                        marking. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the opposite flow
                        of traffic. [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane to the
                        right. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe [], citation unlisted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 8313, out 858, 8.07 s

bdd100k_val__c5588233-b03622f3 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the
                        left. Ahead, there are several lanes of traffic moving in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line is solid near my car and continues ahead.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this white line is dashed (broken) near my car and continues ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a yellow center line on the left and a white lane line on the
                        right. | roles: The yellow solid line correctly identifies a center line (separating
                        opposing traffic or a median), and the white dashed line correctly identifies a lane
                        line. | markings: The straight arrow is consistent with the lane's purpose. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The broken white line allows crossing into the lane to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead or change into the lane on
                        your right. Changing into the lane on your left is prohibited by the solid yellow
                        line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 708, 7.71 s

bdd100k_val__c561cb9a-aafc0bad | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road approaching an intersection. My car is in a lane
                        with a straight-ahead arrow, and there is a left-turn-only lane to its left. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the left-turn lane. Photo 2 shows
                        this same white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows this line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; text:only (full): Photo 2 shows the word 'ONLY' in the left lane, which is not
                        my lane.; arrow:left (full): Photo 2 shows a left-turn arrow in the left lane, which
                        is not my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from another lane,
                        and a white line on my right marks the edge. | roles: The white solid line on the left
                        is a lane line, and the white solid line on the right is an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's function. The 'ONLY' and left
                        arrow in the adjacent lane are consistent with its role as a turn lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the left-turn lane.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow marking
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may proceed straight but
                        are prohibited from changing lanes or turning left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 8313, out 911, 8.42 s

bdd100k_val__c65c2462-96e8ae92 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway passing under an overpass. The road
                        ahead appears to be a continuous stretch of highway with multiple lanes in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a concrete barrier on the right. Photo 2 shows a
                        solid white line immediately adjacent to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; arrow:straight (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white broken line is on my left and a white solid
                        line/barrier is on my right. | roles: The white broken line on the left fits the role
                        of a crossable lane line, and the white solid line/barrier on the right fits the role
                        of an edge line. | markings: No markings were observed in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white line and a
                        concrete barrier, which prohibits crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change lanes to the left
                        as the line is broken, but you are prohibited from moving to the right due to the
                        solid edge line and concrete barrier. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read']
Tokens                  in 8313, out 794, 8.29 s

bdd100k_val__c66d2237-f9c0a1ef | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with a grid-like marking on the left. My car
                        is in a lane heading straight toward an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a yellow grid area to the left of my lane.;
                        area:two_way_left_turn_lane (full): Photo 1 shows a yellow solid line to the left of
                        the grid area, which appears to be a left-turn lane boundary.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a white solid line on the
                        right. | roles: The white dashed line on the left correctly identifies a crossable
                        lane line, and the white solid line on the right correctly identifies the edge of the
                        roadway. | markings: The grid area and the two-way left-turn lane to the left are
                        consistent with the urban intersection layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            area:grid: The grid marking indicates an area where stopping is prohibited.
                        [[CN-6.8.1-2]]
Step 5  Rule            area:two_way_left_turn_lane: The area to the left is a two-way left-turn lane. [null]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left if needed, but you should not move to the right
                        beyond the edge line. You can proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'area:two_way_left_turn_lane'], missed []), actions False, unsafe
                        ['change_left'], citation unlisted, contradictions []
Tokens                  in 8313, out 839, 8.05 s

bdd100k_val__c68f8fd2-61681484 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or urban arterial road with an upcoming intersection or exit. My
                        car is in a lane heading forward. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a road edge line or
                        a barrier-adjacent line. Photo 2 shows a solid white line very close to the right edge
                        of the pavement.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): Photo 1 shows a white left-turn arrow in
                        the lane to my left, but no markings are visible in my own lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3)
                        are consistent with a white dashed line on the left and a white solid line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane-line,
                        and the white solid line on the right correctly identifies an edge-line. | markings:
                        No markings are visible in my lane; the lane to the left has a turn arrow. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as it is the edge of the roadway. You are clear to proceed straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 890, 8.0 s

bdd100k_val__c6d77a40-03423c96 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings and trees on both sides.
                        Ahead, there is an intersection with a white van currently making a turn or stopped in
                        a turn lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a sidewalk/curb on the right. Photo 2 shows a
                        solid white line very close to the right edge of the lane, followed by a sidewalk and
                        a white van.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across the lane ahead of the
                        van.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white broken line is on my left and a white solid
                        line/curb is on my right. | roles: The white broken line on the left fits the role of
                        a crossable lane line, and the white solid line on the right fits the role of an edge
                        line. | markings: The stop line is consistent with the intersection ahead. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where I must stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
                        [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. You must stay within the lane
                        on the right as it is bounded by a solid line and a curb. Stop at the white line
                        before entering the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 957, 7.95 s

bdd100k_val__c6dca574-6e641016 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and parked cars on both sides. The road ahead
                        appears to be a straight stretch with an intersection or continuing flow in the
                        distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my car. Photo 2 shows the same
                        double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line near the car
                        and a broken line further ahead. Photo 2 shows a solid white line next to the car.
                        Photo 1 shows a raised curb on the far right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a double solid yellow line on the left indicates a
                        center line separating opposing traffic, and a white line/curb on the right indicates
                        an edge line. | roles: The yellow double solid line correctly identifies a no-crossing
                        center line, and the white line/curb correctly identifies a right-hand edge line. |
                        markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way road. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left due to the double solid yellow
                        center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 870, 6.92 s

bdd100k_val__c6dcc1a9-0fa80e62 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway bridge with several lanes of traffic moving in the same
                        direction. There is a large overhead sign indicating directions to various locations.
                        (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 shows a white dashed
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and my position as
                        lane 2 (from the left) are consistent with the white dashed lines on both sides. |
                        roles: The white dashed lines correctly function as lane lines separating traffic in
                        the same direction. | markings: No markings were observed, which is consistent with
                        the absence of specific lane-use indicators. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken line means it may be crossed. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The broken line means it may be crossed. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): The left boundary is a broken line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a standard highway lane. You may change lanes to the left or right as
                        needed, as the lane markings are broken. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 823, 14.12 s

bdd100k_val__c6e1c974-906461f4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with buildings and trees on both sides. My
                        car is in a lane that appears to be a dedicated turn lane or a lane with specific
                        movement restrictions approaching an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line (dashed) near my car, but it transitions into a solid
                        white line further ahead as it approaches the intersection area.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line very
                        close to the car's right side.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow pointing straight ahead
                        in my lane.; text:other (full): Photo 2 shows the word 'ONLY' in white paint in my
                        lane.; arrow:left (full): Photo 1 shows a white left-turn arrow and a white right-turn
                        arrow further ahead in the lane to the left of mine.
Step 4  Cross-check     close_up: The same in both photos. Photo 2 confirms the dashed pattern near the car
                        and the solid line further ahead. | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on the left and a white line on the right. |
                        roles: The white lines correctly function as lane lines separating traffic in the same
                        direction. | markings: The 'ONLY' text and the straight arrow in my lane are
                        consistent with a dedicated lane for straight movement. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from crossing into the lane on the
                        right. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for straight ahead or right
                        turn movements. [[CN-5.13.1]]
Step 5  Rule            text:other: The 'ONLY' text indicates that the lane is restricted to the movements
                        shown by the arrow.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (WRONG, label prohibited): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead or right-turn movements only. You may
                        change lanes to the left where the line is broken, but you must not cross the solid
                        line to the right. Do not attempt to turn left from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight_right', 'text:other'], missed ['arrow:straight',
                        'text:only']), actions False, unsafe ['turn_right'], citation in_pack_not_accepted,
                        contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 8313, out 1085, 9.03 s

bdd100k_val__c6ed8102-2bbcbcc2 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with an overpass above. The road
                        ahead appears to be a straight stretch of highway. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail and a
                        fence. Photo 2 shows the solid white line and the guardrail clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. No
                        markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left and a white solid
                        line/guardrail is on my right. | roles: The white dashed line on the left is a lane
                        line, and the white solid line on the right is an edge line. | markings: The left-turn
                        arrow is in the adjacent lane, not my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:left: The arrow in the left lane indicates that lane is for left turns.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line and a
                        physical guardrail, which prohibits moving to the right [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No arrow in my lane allows a left turn; the left-turn arrow is in the
                        adjacent lane.
Step 6  turn_right      not_applicable: No marking in my lane allows a right turn.
Step 6  u_turn          not_applicable: No marking in my lane allows a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is marked in or next to my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the highway. You may proceed straight or change into
                        the middle lane to the left. You cannot turn left or right from this lane, and you
                        cannot move further to the right due to the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions ['go_straight allowed although no arrow shows it', 'turn_left
                        not_applicable although an arrow shows it']
Tokens                  in 8313, out 828, 7.31 s

bdd100k_val__c85416bd-db975d94 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be the rightmost lane of its direction. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line very close to the car's right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.; arrow:straight (insufficient): No markings are visible in my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left and a white solid line is
                        on my right. | roles: The white dashed line on the left fits the role of a crossable
                        lane line, and the white solid line on the right fits the role of a road edge line. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        movement instructions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: no marking governs this action
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        marks the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change to the left lane if needed, but you
                        cannot move further right as you are at the edge of the road. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided from an arrow that cannot
                        be read']
Tokens                  in 8313, out 794, 7.13 s

bdd100k_val__c8a7a62d-e58e7297 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street with multiple lanes of traffic moving in the same
                        direction. There is an intersection ahead with traffic signals and a pedestrian
                        crossing. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line near the car
                        and a broken line further ahead. Photo 2 shows a solid white line next to the car.
                        Photo 1 shows the line becomes a broken white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow pointing straight ahead and
                        slightly to the left, and a white arrow pointing to the right. Photo 1 shows these
                        markings clearly in my lane.; text:other (full): Photo 2 shows the word 'ONLY' in
                        white text. Photo 1 shows this text clearly in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow solid line correctly identifies as a center line
                        (separating opposing traffic or a no-crossing zone) and the white line as an edge
                        line. | markings: The straight-left arrow and 'ONLY' text are consistent with a
                        dedicated lane for those movements. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_left: The guide arrow restricts the allowed movements to straight ahead
                        or turning left. [[CN-5.13.2]]
Step 5  Rule            text:other: The 'ONLY' text reinforces that the lane is restricted to the movements
                        shown by the arrow.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead or left-turn movements only. Do not
                        attempt to change lanes or turn right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 1023, 9.0 s

bdd100k_val__c8e01103-9ff8595d | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street with an intersection ahead. My car is in a lane that
                        appears to be a dedicated turn lane or a lane leading into an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line. Photo 2
                        shows a solid white line very close to the car's right side, and further ahead, it
                        seems to transition or end near the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow pointing straight ahead
                        in my lane.; line:stop_line (full): Photo 1 shows a white stop line across the lane
                        ahead of the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (white line on left, white edge line on right). |
                        roles: The white lines and curb correctly identify the lane boundaries. | markings:
                        The straight-ahead arrow and stop line are consistent with a lane leading into an
                        intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (WRONG, label prohibited): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from this lane. You must come to a complete
                        stop at the white stop line before proceeding into the intersection. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right', 'line:stop_line'], missed ['arrow:straight',
                        'line:crosswalk']), actions False, unsafe ['turn_right'], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8313, out 1118, 10.24 s

bdd100k_val__c909551e-fb24caeb | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is
                        positioned in one of the central lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to my left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to my right. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (partial): Photo 1 shows a white left-turn arrow in the lane to
                        my left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The left-turn area is in the adjacent lane, not my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows for lane changes to both the left and right. You may
                        proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 833, 6.82 s

bdd100k_val__c90b5398-8d49f2f2 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane that appears to be the middle lane of three lanes moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a broken line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a broken line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white dashed lines
                        correctly function as crossable lane lines. | markings: No markings are in my lane;
                        the left-turn arrow is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a middle lane with broken white lines on both sides, allowing you to change
                        lanes to the left or right if needed. You may proceed straight through the upcoming
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8313, out 861, 7.91 s

bdd100k_val__c90c8198-f73aed79 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a center median and parked cars on both sides. Ahead,
                        there is a crosswalk and an intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 shows the same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line near the car
                        and a broken line further ahead. Photo 2 shows a solid white line next to the car.
                        Photo 1 shows the line becoming broken further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: The close-up (Photo 2) confirms the double solid yellow line on the left and
                        the solid white line on the right next to the car. Photo 1 shows the right boundary
                        becomes broken further ahead. | position: The lane count (2) and my position (2) agree
                        with the boundaries: a center line is on my left and an edge line is on my right. |
                        roles: The yellow double solid line correctly identifies as a center line, and the
                        white line as an edge line. | markings: The crosswalk is consistent with an urban
                        intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The solid white line normally prohibits crossing. [[CN-4.2.2-a]]
Step 5  Rule            line:crosswalk: No specific rule provided for crosswalks in the list, but they
                        generally indicate a pedestrian crossing area.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 902, 9.01 s

bdd100k_val__c9283177-4ac407c3 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with buildings on the right and a
                        barrier/trees on the left. My car is in a lane heading straight ahead. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        the same white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the far left and a white line on the right. Photo 2
                        shows a white line on the right side of my lane, which appears to be a lane line or an
                        edge line near a curb/sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white line on my left and the white line/curb on my right. |
                        roles: The white solid line on the left is a lane line; the white solid line on the
                        right is an edge line. | markings: The straight arrow in my lane is consistent with
                        the lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in the lane.
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn.
Step 6  turn_right      allowed: allowed by the arrow which shows a right turn.
Step 6  u_turn          prohibited: prohibited by the arrow which does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 857, 7.37 s

bdd100k_val__c94d8213-1f593522 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection or a point where the road
                        layout changes. There are multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line and a concrete barrier on the right. Photo 2 shows a solid
                        white line immediately next to the car, followed by a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 1 shows a white left-turn arrow in the lane to my left.
                        Photo 2 shows a white right-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with a white lane line on my left and a white edge line/barrier on my
                        right. | roles: The white solid line on the left is a lane line; the white solid line
                        on the right is an edge line. | markings: The right-turn arrow in my lane is
                        consistent with the lane's function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:right: The right-turn arrow indicates that the lane is for turning right.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and concrete
                        barrier
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the right-turn arrow
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the right-turn arrow
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Your lane is designated for turning right only. You should prepare to turn right at
                        the upcoming intersection and are prohibited from changing lanes or going straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:right'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8313, out 841, 8.29 s

bdd100k_val__c9b099e4-6ab2e4f4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. Ahead, there are overhead
                        signs and a merging area or exit point. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to the car, followed by a concrete
                        barrier/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left and a solid white
                        line/curb is on my right. | roles: The white dashed line on the left fits the role of
                        a crossable lane line, and the solid white line on the right fits the role of a road
                        edge line. | markings: No markings were reported in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line next to
                        a curb, which prohibits moving onto the shoulder or sidewalk.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the highway. You may change to the left lane as the
                        line is broken. Do not attempt to move to the right as there is a solid edge line and
                        a physical barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 710, 7.61 s

bdd100k_val__ca146661-7f70d0c4 | lane | Test C | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane road with an intersection or merging area ahead. My car is in a lane
                        traveling straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line
                        marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line is on my left and a white solid line is
                        on my right. | roles: The white dashed line fits the role of a crossable lane line,
                        and the white solid line fits the role of a right-hand edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. You should not move to the
                        right as it is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8313, out 847, 8.33 s
```
