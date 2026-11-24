# Reasoning of lane run 20261118_001726_laneC_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line near the car, and Photo 2 shows a yellow line near the
                        car. Further ahead, Photo 1 shows a yellow line continuing, and Photo 2 shows a yellow
                        line continuing.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line near the car, and Photo 2 shows a white line near the car.
                        Further ahead, Photo 1 shows a white line continuing, and Photo 2 shows a white line
                        continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line segment ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is center_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (line:stop_line) agree with the boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a yellow dashed
                        center line, which indicates separation of opposite directions of travel, and there is
                        no marking allowing a lane change.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        lane line, and crossing the lane line markings is not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to allow turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to allow turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to allow a U-turn or a turn toward the opposite traffic direction that allows
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change right, and you may proceed
                        straight ahead. You should be aware of the stop line ahead, which indicates where you
                        are required to stop if a traffic control device requires it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 943, 7.74 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining both sides, and it appears to continue
                        straight ahead into the distance. There are three lanes visible in my direction near
                        the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow dashed line next to my car, and Photo 2 shows a yellow dashed
                        line next to my car. Photo 1 shows a yellow dashed line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a yellow dashed line marking the right
                        boundary, which serves as the center line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow dashed for center_line). | markings: the markings
                        (yellow dashed line) agree with the boundaries (right boundary is a center_line). |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on two-lane, two-way roadways shall be one of
                        the following: A. Two-direction passing zone markings consisting of a normal width
                        broken yellow line where crossing the center line markings for passing with care is
                        permitted for traffic traveling in either direction; B. One-direction no-passing zone
                        markings consisting of a double yellow line, one of which is a normal width broken
                        yellow line and the other is a normal width solid yellow line, where crossing the
                        center line markings for passing with care is permitted for traffic traveling adjacent
                        to the broken line, but is prohibited for traffic traveling adjacent to the solid
                        line; or C. Two-direction no-passing zone markings consisting of two normal width
                        solid yellow lines where crossing the center line markings for passing is prohibited
                        for traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a yellow
                        dashed center_line, and [US-3B.01-04] allows for two-direction passing zone markings
                        consisting of a normal width broken yellow line where crossing the center line
                        markings for passing with care is permitted for traffic traveling in either direction.
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
Advice                  You are in the middle lane, and you are permitted to change left or right, as well as
                        proceed straight. Since there are no specific turn markings, you may proceed straight
                        or make a turn if the road geometry allows, but you should be aware that the right
                        boundary is a center line allowing passing with care.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 1355, 11.28 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues straight, and there is a directional sign visible on the right side. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane,
                        indicating the lane boundary. This is the right boundary line.; line:stop_line
                        (partial): Photo 2: A white dashed line is visible across the lane, indicating the
                        lane boundary. This is the left boundary line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes of the same
                        direction). | roles: the white dashed lines fit the role of lane_line as they separate
                        lanes traveling in the same direction. | markings: the markings (line:stop_line) are
                        consistent with the lane boundaries, although the interpretation of the dashed line as
                        a stop line is based on its position at the end of the visible road segment in Photo
                        2. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane or to the left of it.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change left or right, and you may proceed straight. Be aware of the dashed line ahead,
                        which indicates a required stopping point or the end of the current segment.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1043, 7.68 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a highway or overpass)
                        ahead. My car is in the rightmost lane visible in the immediate foreground. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1: A white line is visible next to the car, and a white line is visible further
                        ahead. Photo 2: A white line is visible next to the car, and a white line is visible
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white line is visible next to the car, and a white line is visible further
                        ahead. Photo 2: A white line is visible next to the car, and a white line is visible
                        further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the white dashed lines fit the roles of lane_line and edge_line.
                        | markings: no markings were reported, so there is no contradiction. | unseen: no
                        attributes were reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white edge line, and
                        [US-3B.09-01-02] permits delineation of the right-hand edge.
Step 6  go_straight     allowed (contested, correct): allowed: No markings in my lane prohibit going straight,
                        and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane indicating a
                          waiting area.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is an edge lane. You may change left or right,
                        and you may proceed straight. Since there are no specific turn markings, turning
                        movements are not governed by lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 998, 6.88 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with an elevated structure (likely a bridge or overpass)
                        ahead. My car is in the rightmost lane visible in the immediate foreground. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1: A continuous white line is visible next to my car, and further ahead, the
                        line continues. Photo 2: A continuous white line is visible next to my car, and
                        further ahead, the line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A continuous white line is visible next to my car, and further ahead, the
                        line continues. Photo 2: A continuous white line is visible next to my car, and
                        further ahead, the line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: A solid white lane line marking may be used on approaches to
                        intersections to separate a through lane from a mandatory turn lane. [[US-3B.06-07]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a solid white
                        lane_line, and [US-3B.06-05-06] states that crossing is discouraged, which permits the
                        change.
Step 6  change_right    allowed (correct): allowed because the right boundary is a solid white edge_line, and
                        [US-3B.09-01-02] defines it as the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          entering a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is the edge lane. You may change left or right,
                        and you may proceed straight. Since there are no specific turn arrows or waiting
                        areas, you should proceed straight unless you intend to turn, in which case you must
                        check for appropriate lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 921, 7.66 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 2: A solid white line is visible across the lane, near
                        the bottom of the image.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line, indicating my lane is the middle lane of three lanes traveling in the same
                        direction). | roles: the color (white) and pattern (solid) of both boundaries fit the
                        role of a lane_line. | markings: the solid white line across the lane
                        (line:stop_yield) is consistent with the lane boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and the rule [US-3B.06-05-06] indicates that crossing is discouraged,
                        implying a restriction on lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane_line, and the rule [US-3B.06-05-06] indicates that crossing is discouraged,
                        implying a restriction on lane changes.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The presence of the line:stop_yield
                        marking requires the movement to be permitted only after a full stop.
Step 6  turn_left       prohibited: prohibited: There are no markings in my lane allowing a left turn.
Step 6  turn_right      prohibited: prohibited: There are no markings in my lane allowing a right turn.
Step 6  u_turn          prohibited: prohibited: There are no markings in my lane allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding straight ahead, as indicated by the
                        yield line. Lane changes are prohibited by the solid white lane lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 9487, out 973, 7.5 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a bridge or overpass
                        structure, suggesting the road continues forward. There are at least three lanes
                        visible in my direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to my left, and further ahead, this line
                        continues as a solid white line. Photo 2 shows a solid white line immediately to my
                        left, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line immediately to my right, and further ahead, this
                        line continues as a broken yellow line. Photo 2 shows a broken yellow line immediately
                        to my right, and further ahead, this line continues as a broken yellow line.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: the arrow in my lane agrees with the boundaries (it is in the lane between
                        a lane_line and a center_line) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions. [[US-3B.01-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and crossing it is discouraged, which implies a restriction on changing
                        left.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a broken yellow
                        center_line, and a broken line indicates a permissive condition for crossing.
Step 6  go_straight     allowed (contested, correct): allowed: The lane has a white arrow pointing straight
                        ahead, and this arrow permits going straight.
Step 6  turn_left       prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a left turn.
Step 6  turn_right      prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a right turn.
Step 6  u_turn          prohibited: prohibited: The lane has a white arrow pointing straight ahead, and this
                        arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is designated for straight travel. You may change
                        right into the right lane, but you must not change left. You may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 918, 7.92 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and the road continues ahead into the
                        distance. There are three lanes visible in my direction near the bottom of the photo.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of traffic flows in the same direction, and my lane is the leftmost of the
                        three visible lanes). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: no markings were reported, so there
                        is no agreement to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit it, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          this action.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific turn markings, you may turn left or right, but you should be
                        aware of surrounding traffic.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 9487, out 877, 7.09 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane elevated roadway, and ahead there is a continuation of the road
                        structure, possibly leading to an interchange or another section of the highway. My
                        car is in the lane closest to the left side of the visible roadway. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line near my car, and Photo 2 shows a solid yellow line
                        near my car. Further ahead, Photo 1 shows the solid yellow line continuing, and Photo
                        2 shows the solid yellow line continuing.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line near my car, and Photo 2 shows a white line near my car.
                        Further ahead, Photo 1 shows the white line continuing, and Photo 2 shows the white
                        line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right boundary
                        of my lane. Further ahead, Photo 1 shows a white dashed line continuing.;
                        line:yield_line (partial): Photo 2 shows a white dashed line marking the right
                        boundary of my lane. Further ahead, Photo 1 shows a white dashed line continuing.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white dashed for lane_line) | markings: the markings
                        (line:stop_line and line:yield_line) are present in the lane and are consistent with
                        the boundaries and each other | unseen: no | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 5  Rule            line:yield_line: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid yellow
                        center_line, which prohibits crossing into the adjacent lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        crossing is permitted when care is taken.
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
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead. You
                        should be aware of the yield line and stop line markings ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line', 'line:yield_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1102, 9.06 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        or a major road crossing. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues until it meets a yellow line marking the edge of the adjacent lane.
                        Photo 2: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, the solid
                        yellow line continues until it meets a white line marking the edge of the roadway.
                        Photo 2: A solid yellow line is visible next to the car. Further ahead, the solid
                        yellow line continues.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white painted arrow pointing straight ahead is
                        visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrow in my lane is consistent with the boundaries and markings |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid yellow line delineates the separation of traffic traveling
                        in opposite directions or the right-hand edge of the roadway. [[US-3A.03-03-04]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The solid white line on the left
                        indicates that crossing the lane line markings is discouraged, and the lane-use arrow
                        only permits straight movement.
Step 6  change_right    prohibited (contested, correct): prohibited: The solid yellow line on the right
                        indicates the edge of the roadway, and the lane-use arrow only permits straight
                        movement.
Step 6  go_straight     allowed (contested, correct): allowed: The white arrow in my lane permits straight
                        movement, and no boundary prohibits it.
Step 6  turn_left       prohibited: prohibited: The white arrow in my lane only permits straight movement,
                        prohibiting turns.
Step 6  turn_right      prohibited: prohibited: The white arrow in my lane only permits straight movement,
                        prohibiting turns.
Step 6  u_turn          prohibited: prohibited: The white arrow in my lane only permits straight movement,
                        prohibiting U-turns (as it does not show a U-turn movement).
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane to proceed straight through the intersection. Lane
                        changes are prohibited by the solid lines, and the lane-use arrow only permits
                        straight movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 927, 8.42 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or intersection
                        where traffic flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines fit the
                        role of lane_line as they separate traffic flows in the same direction. | markings:
                        the stop line is located across my lane, consistent with the lane boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a white dashed
                        lane_line, and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because the lane contains a
                        line:stop_line, and [US-3B.19-01-02] indicates the point where the stop is required.
Step 6  turn_left       stop_first: stop_first because the lane contains a line:stop_line, and
                        [US-3B.19-01-02] indicates the point where the stop is required.
Step 6  turn_right      stop_first: stop_first because the lane contains a line:stop_line, and
                        [US-3B.19-01-02] indicates the point where the stop is required.
Step 6  u_turn          stop_first: stop_first because the lane contains a line:stop_line, and
                        [US-3B.19-01-02] indicates the point where the stop is required.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop behind the stop line before proceeding in any
                        direction. You may change lanes left or right if necessary, but all movements must
                        begin after stopping.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 9487, out 1151, 7.39 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, there is a section of the road
                        continuing, possibly leading to an interchange or another section of the highway.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible immediately to the right of my car. Further
                        ahead, this solid yellow line continues.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1: A solid yellow line is visible in the right
                        boundary, which acts as a center line.; line:stop_yield (insufficient): Photo 1: A
                        solid yellow line is visible in the right boundary, which acts as a center line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white solid for lane_line, yellow solid for center_line) | markings: the markings
                        (which are only the boundary lines) agree with each other and with the boundaries |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on undivided two-way roadways with four or
                        more lanes for moving motor vehicle traffic always available shall be the two-
                        direction no-passing zone markings consisting of normal width double solid yellow
                        lines, although here only a single solid yellow line is visible. [[US-3B.01-06]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        lane_line, and the rule [US-3B.06-05-06] only discourages crossing, not prohibits it.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        center_line, and the rule [US-3B.01-06] implies a restriction on crossing the center
                        line.
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
Advice                  You are in the middle lane, which allows you to proceed straight ahead. Lane changes
                        to the left are discouraged, and changing to the right is prohibited by the solid
                        yellow center line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 937, 7.23 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian overpass ahead. There are multiple lanes
                        in my direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking on the right side
                        of my lane, further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicate separation of traffic
                        flows in the same direction, consistent with multiple lanes in the same direction). |
                        roles: the white dashed lines fit the role of lane_line as they separate traffic flows
                        in the same direction. | markings: the stop line marking is visible in Photo 2 and is
                        consistent with the lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a white
                        dashed line, and [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane markings are broken white lines, and
                        you may proceed straight. You must stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 923, 6.97 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with commercial buildings on the right side. Ahead,
                        there is an intersection or a point where the road continues, and there is a crosswalk
                        visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car, and further ahead, the line
                        appears to be a white dashed line. Photo 2: The line next to the car is a white dashed
                        line, and the line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A yellow solid line is visible next to the car, and further ahead, the line
                        appears to be a yellow solid line. Photo 2: The line next to the car is a yellow solid
                        line, and the line further ahead is also a yellow solid line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 1: A blue overhead sign with white arrows indicating
                        straight and right turn is visible ahead. Photo 2: The same blue overhead sign is
                        visible ahead.; arrow:straight (full): Photo 1: A blue overhead sign with white arrows
                        indicating straight and right turn is visible ahead. Photo 2: The same blue overhead
                        sign is visible ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is a lane_line,
                        indicating another lane of travel to the left. The right boundary is an edge_line.
                        Since there are two lanes visible, and the left boundary is a lane_line, my lane is
                        the rightmost lane (index 2) if the left boundary is the line separating lane 1 and
                        lane 2. However, the lane count is 2, and the left boundary is a lane_line, suggesting
                        my lane is not the leftmost. Given the context of the right boundary being an
                        edge_line, my lane is the rightmost lane (index 2). Re-evaluating: If there are 2
                        lanes, and the left boundary is a lane_line, my lane is lane 2. If the left boundary
                        is a lane_line, it separates my lane from lane 1. If the right boundary is an
                        edge_line, it is the end of the road. This configuration suggests my lane is the
                        rightmost lane (index 2). Let's assume the lane count of 2 refers to the lanes visible
                        in my direction. If the left boundary is a lane_line, my lane is not the leftmost. If
                        the right boundary is an edge_line, my lane is the rightmost. Thus, ego_lane_index =
                        2. Correcting ego_lane_index from 1 to 2. | roles: The left boundary (white dashed
                        line) is a lane_line, and the right boundary (yellow solid line) is an edge_line. This
                        fits the roles. | markings: The arrows indicate allowed movements, and they are
                        consistent with the lane configuration. | unseen: No attributes were reported that
                        were not seen. | result: corrected
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The yellow solid line delineates the right-hand edge of the roadway.
                        [[US-3A.03-03-04]]
Step 5  Rule            arrow:right: Lane-use arrow markings indicate the permissible movements in certain
                        lanes. [[US-3B.23-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings indicate the permissible movements in certain
                        lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a lane_line, and the rule
                        [US-3B.06-05-06] implies that while crossing is not discouraged, the presence of a
                        lane line suggests a boundary to another lane, and the arrows do not permit a change
                        left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is an edge_line, and
                        the rule [US-3A.03-03-04] defines this line as the right-hand edge of the roadway, but
                        the arrows do not explicitly prohibit a change right.
Step 6  go_straight     allowed (contested, correct): allowed: The arrow:straight marking allows this
                        movement, and the rule [US-3B.23-01] confirms the arrow indicates permissible
                        movements.
Step 6  turn_left       prohibited: prohibited: The lane-use arrows visible do not show a left turn movement,
                        and the rule [US-3B.23-01] dictates that arrows indicate mandatory or permissible
                        movements.
Step 6  turn_right      allowed: allowed: The arrow:right marking allows this movement, and the rule
                        [US-3B.23-01] confirms the arrow indicates permissible movements.
Step 6  u_turn          prohibited: prohibited: The lane-use arrows visible do not show a U-turn movement, and
                        the rule [US-3B.23-01] dictates that arrows indicate mandatory or permissible
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or turn right at the
                        intersection. A lane change to the left is prohibited by the lane line, and you should
                        not attempt a left turn or U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed []), actions False, unsafe ['change_right'],
                        citation in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the
                        left', 'change_left prohibited across a broken lane line']
Tokens                  in 9487, out 1420, 12.08 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated roadway. Ahead, the road continues straight,
                        and there are overhead signs indicating lane designations and speed limits. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line marking the lane
                        boundary to the left, and a white dashed line marking the lane boundary to the right.
                        Photo 2 shows the same white dashed lines.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicating separation between
                        lanes of the same direction). | roles: The white dashed lines fit the role of
                        lane_line, indicating separation between lanes traveling in the same direction. |
                        markings: The lane markings observed (white dashed lines) are consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a white
                        dashed line, and [US-3B.06-05-06] permits crossing the lane line markings.
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
Advice                  You are in the middle lane of a multi-lane highway, and you are permitted to change
                        lanes left or right, as well as proceed straight. No specific lane is required for
                        turning movements, as no turn arrows or waiting areas are present.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1210, 8.76 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, and there are traffic signals visible in the distance. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white solid line is visible next to the car. Photo 2: A white solid line is
                        visible next to the car. Further ahead, the line remains a white solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): None visible in Photo 1 or Photo 2.; line:yield_line
                        (insufficient): None visible in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed/solid lines are lane_lines). | markings: there are no markings in my
                        lane to check for agreement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            left_boundary: A solid white lane line marking should be used on approaches to
                        intersections to separate a through lane from a mandatory turn lane, but this boundary
                        is dashed. [[US-3B.06-07]]
Step 5  Rule            right_boundary: A solid white lane line marking should be used on approaches to
                        intersections to separate a through lane from a mandatory turn lane, but this boundary
                        is solid. [[US-3B.06-07]]
Step 5  Rule            left_boundary: Where crossing the lane line markings is prohibited, the lane line
                        markings shall consist of a double solid white line, but this boundary is dashed.
                        [[US-3B.06-12]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is prohibited, the lane line
                        markings shall consist of a double solid white line, but this boundary is solid.
                        [[US-3B.06-12]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed lane_line, and [US-3B.06-05-06]
                        permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a white solid lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings (as it is not a double solid
                        line prohibiting crossing).
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change left or
                        right as long as you observe traffic conditions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line', 'line:yield_line'], missed []), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1073, 8.4 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, the road
                        continues straight, and there is a barrier/median on the right side. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid green/brown barrier/median is visible next to the car. Photo 2: A
                        solid green/brown barrier/median is visible next to the car. Further ahead, the
                        barrier continues.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A large white arrow pointing straight ahead is visible
                        in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on the left and an
                        edge/barrier on the right. | roles: The left boundary is a white dashed lane line,
                        consistent with separating lanes of the same direction. The right boundary is a
                        physical barrier/median, consistent with an edge line. | markings: The white arrow
                        pointing straight ahead is visible in Photo 2 and is consistent with the lane
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway, although here
                        it is a physical barrier. [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed lane
                        line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a physical barrier/median,
                        which functions as an edge line, and lane changes are restricted by physical barriers.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and
                        [US-3B.23-01] indicates permissible movements.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and [US-3B.23-01] indicates permissible movements.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and [US-3B.23-01] indicates permissible movements.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and [US-3B.23-01] indicates permissible movements, as the arrow does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane or to my left.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You must stay in your current lane to proceed straight ahead. Lane changes to the left
                        are permitted, but changing to the right is prohibited by the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1036, 9.06 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into a more open area with trees. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white dashed arrow pointing straight ahead is
                        visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines fit the
                        role of lane_line as they separate traffic flows in the same direction. | markings:
                        the white dashed arrow pointing straight ahead is consistent with the lane markings
                        observed. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        while this generally permits lane changes, the arrow in the lane only permits straight
                        movement, which implies no lane change is permitted.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a white dashed lane line, and
                        while this generally permits lane changes, the arrow in the lane only permits straight
                        movement, which implies no lane change is permitted.
Step 6  go_straight     allowed (contested, correct): allowed: The lane has a white dashed arrow pointing
                        straight ahead, and no other marking prohibits this movement.
Step 6  turn_left       prohibited: prohibited: The lane has a white dashed arrow pointing straight ahead, and
                        this arrow does not show a left turn.
Step 6  turn_right      prohibited: prohibited: The lane has a white dashed arrow pointing straight ahead, and
                        this arrow does not show a right turn.
Step 6  u_turn          prohibited: prohibited: The lane has a white dashed arrow pointing straight ahead, and
                        this arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the lane-use arrow marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line', 'change_right prohibited across a broken lane line']
Tokens                  in 9487, out 967, 7.38 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection visible in the distance.
                        My car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of traffic flows in the same direction) | roles: the white dashed lines fit
                        the role of lane_line as they delineate the separation of traffic flows in the same
                        direction | markings: the arrows in my lane agree with the boundaries as they indicate
                        allowed movements within the lane structure | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 5  Rule            arrow:right: Lane-use arrow markings are used to indicate the mandatory or permissible
                        movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (correct): allowed: The lane has a straight arrow, and [US-3B.23-01] indicates
                        permissible movements.
Step 6  turn_left       prohibited (correct): prohibited: There is no arrow indicating a left turn in my lane,
                        and [US-3B.23-01] implies that movements not shown are prohibited when an arrow is
                        present.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane has a right arrow, and
                        [US-3B.23-01] indicates permissible movements.
Step 6  u_turn          prohibited (correct): prohibited: There is no arrow indicating a U-turn in my lane,
                        and [US-3B.23-01] implies that movements not shown are prohibited when an arrow is
                        present.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, go straight, or turn right at the upcoming
                        intersection. Do not attempt to turn left or make a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions False, unsafe ['turn_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1042, 7.44 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road with traffic
                        signals visible in the distance. My car is in the lane closest to the left side of the
                        visible lanes. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line near the car, and Photo 2 shows a white line near the car.
                        Photo 1 shows a white line further ahead, and Photo 2 shows a white line further
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line near the car, and Photo 2 shows a white line near the car.
                        Photo 1 shows a white line further ahead, and Photo 2 shows a white line further
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:straight (full): Photo 2; arrow:straight (full):
                        Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating my lane is the leftmost of the three lanes). | roles: the color
                        (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: the three straight arrows in my lane agree with the boundaries as they are
                        within the lane defined by the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a dashed white lane line, and
                        while this permits lane changes, the lane markings do not explicitly allow a change
                        left in the visible stretch.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and since crossing the lane line markings is not discouraged or prohibited, the
                        lane line markings allow a lane change right.
Step 6  go_straight     allowed (correct): allowed: The lane contains a straight arrow, and the boundaries do
                        not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane contains a straight arrow, which does not
                        show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane contains a straight arrow, which does not
                        show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane contains a straight arrow, which does not
                        show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane or to its left.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is designated for straight travel. You may change
                        right into the middle lane, but you must stay in your lane or change right to proceed
                        straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_left prohibited across a broken lane line']
Tokens                  in 9487, out 980, 8.43 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection visible in the distance.
                        My car is in the rightmost lane visible in the immediate foreground. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1: A solid yellow line is visible to the left of my lane, separating traffic
                        flows. Photo 2: A solid yellow line is visible to the left of my lane, separating
                        traffic flows.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible to the right of my lane, delineating the edge
                        of the roadway. Photo 2: A solid white line is visible to the right of my lane,
                        delineating the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for edge_line) | markings: the arrow in my
                        lane agrees with the boundaries (it is in the rightmost lane, which is consistent with
                        an edge_line on the right) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Yellow markings delineate the separation of traffic traveling in
                        opposite directions. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The solid yellow center_line boundary prohibits
                        crossing into the adjacent lane.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The solid white edge_line boundary does
                        not prohibit changing right, as it is the edge of the roadway.
Step 6  go_straight     allowed (correct): allowed: The white arrow pointing straight ahead in my lane permits
                        going straight.
Step 6  turn_left       prohibited (correct): prohibited: The white arrow pointing straight ahead in my lane
                        does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The white arrow pointing straight ahead in my lane
                        does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The white arrow pointing straight ahead in my lane
                        does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is permitted to go straight. You may change right
                        if necessary, but you are prohibited from changing left. You should proceed straight
                        through the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 899, 7.41 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a merging
                        area where traffic is moving forward. My car is in the lane closest to the center of
                        the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2: A large white arrow pointing up and to the right is
                        visible on the road ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the arrow
                        (merge_right) is present in my lane and is consistent with the lane boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:merge_right: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a dashed white lane line, and
                        no marking permits a change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and the arrow permits movement to the right.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: The lane-use arrow indicates a
                        mandatory merge to the right, prohibiting straight movement.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The lane-use arrow indicates a
                        mandatory merge to the right, prohibiting a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane-use arrow indicates a mandatory merge to
                        the right, prohibiting a right turn.
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: The lane-use arrow indicates a
                        mandatory merge to the right, prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must prepare to merge right into the adjacent lane as indicated by the arrow. Do
                        not attempt to go straight, turn left, turn right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:straight_left']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['change_left
                        prohibited across a broken lane line', 'go_straight, turn_left, turn_right, u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 9487, out 947, 8.53 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a wide
                        area where traffic is merging/diverging. My car is in the lane closest to the center
                        of the visible traffic flow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows the solid white line continuing, and Photo 2
                        shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows the broken white line continuing, and
                        Photo 2 shows the broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white for lane line, dashed white for lane line). | markings: the stop line
                        marking is consistent with the lane boundaries and does not contradict any other
                        visible markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed white, crossing the lane line markings is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white lane line, and
                        [US-3B.06-05-06] states that crossing the lane line markings is discouraged, which
                        implies a lane change is prohibited or discouraged.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed white lane line, and
                        [US-3B.06-05-06] states that crossing the lane line markings is permitted.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibitions in my lane, and the
                        boundaries do not govern going straight, so it is allowed.
Step 6  turn_left       allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        govern turning left, so it is allowed.
Step 6  turn_right      allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        govern turning right, so it is allowed.
Step 6  u_turn          allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        govern U-turns, so it is allowed.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a waiting area in my lane, so this
                          action is not applicable.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a rule from step 5.
Advice                  You may change right, go straight, turn left, turn right, or make a U-turn. You must
                        stop behind the solid white stop line before proceeding.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 9487, out 1143, 8.36 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road passing under an overpass. Ahead, there is a junction or
                        area where lanes diverge/merge, and there is a pedestrian area to the right. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the junction area. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line appears to be a white
                        dashed line continuing into the junction area.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the junction area. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line appears to be a white
                        dashed line continuing into the junction area.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A large white arrow pointing straight ahead is
                        visible in my lane. Photo 2: A large white arrow pointing to the right is visible in
                        the lane to my right. Photo 2: A large white arrow pointing to the left is visible in
                        the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines on both
                        sides fit the role of lane_line as they separate lanes traveling in the same
                        direction. | markings: the arrow in my lane (straight ahead) is consistent with the
                        lane boundaries (white dashed lines allow lane changes if permitted by the arrow, but
                        the arrow dictates movement). | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight_right: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The lane-use arrow in my lane only shows straight
                        ahead and right, prohibiting a left change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The lane-use arrow in my lane shows a
                        right movement, and the boundary is a dashed line, which permits crossing with care.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane-use arrow in my lane shows
                        straight ahead, and the boundary is a dashed line, which permits crossing with care.
Step 6  turn_left       prohibited (correct): prohibited: The lane-use arrow in my lane does not show a left
                        turn.
Step 6  turn_right      allowed (correct): allowed: The lane-use arrow in my lane shows a right movement, and
                        the boundary is a dashed line, which permits crossing with care.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: No marking in my lane
                        governs a U-turn movement, and the boundaries do not govern it for this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of three. You may proceed straight or turn right, and you
                        may change right, but you must not turn left or change left. Use the lane indicated by
                        the straight/right arrow for your intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:right']), actions False, unsafe
                        ['change_right', 'go_straight'], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left', 'change_left prohibited across a broken
                        lane line']
Tokens                  in 9487, out 1041, 8.55 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where the road continues with other lanes visible in the distance. My car is in the
                        lane closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, words, or areas are
                        visible within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: no markings
                        were observed in my lane, so they agree with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (correct): allowed: No markings restrict carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting ahead of my
                          lane or to my left.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn arrows or waiting areas visible, you should proceed according to
                        standard right-hand traffic rules for the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe ['change_left'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 918, 7.96 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrow in my lane agrees with the boundaries (it is in the rightmost
                        lane, which is bounded by an edge line on the right) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway, but the
                        observed dashed line does not strictly conform to this mandatory rule for the edge
                        line. [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white edge
                        line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  go_straight     allowed (correct): allowed: The lane has a straight arrow, and [US-3B.23-01] indicates
                        permissible movements.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a straight arrow, and [US-3B.23-01]
                        indicates that movements not shown by the arrow are prohibited.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a straight arrow, and [US-3B.23-01]
                        indicates that movements not shown by the arrow are prohibited.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a straight arrow, and [US-3B.23-01]
                        indicates that movements not shown by the arrow are prohibited.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is designated for straight travel. You may change
                        left or right, but you must proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1038, 7.76 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane, and Photo 2 shows a solid
                        white line to the right of my lane. Further ahead, Photo 1 shows a solid white line
                        continuing, and Photo 2 shows a solid white line continuing.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the middle lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight
                        ahead in the leftmost lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrows in my lane agree with the boundaries (they are in the lane
                        defined by the boundaries) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a dashed lane line, but no
                        marking prohibits a lane change, and the rule for lane lines does not prohibit it,
                        however, the lane change is not explicitly allowed by a marking.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white edge
                        line, and the rule for edge lines does not prohibit a lane change, and the lane change
                        is not explicitly allowed by a marking.
Step 6  go_straight     allowed (correct): allowed: The lane has a straight arrow, and the rule for lane-use
                        arrows allows the movement shown.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no marking in my
                        lane that allows or prohibits a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no marking in my
                        lane that allows or prohibits a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no marking in my
                        lane that allows or prohibits a U-turn, and the arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is designated for straight travel. You may change
                        right if safe, but you should proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_right'],
                        citation in_pack_not_accepted, contradictions ['change_left prohibited across a broken
                        lane line']
Tokens                  in 9487, out 1020, 8.22 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with traffic moving in both directions. Ahead, there
                        is an intersection or a complex area with lane markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and a solid yellow line further
                        ahead. Photo 2 shows a solid yellow line next to my car, and a solid yellow line
                        further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a large yellow cross-hatching pattern covering the
                        area ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid for lane_line, yellow solid for center_line). | markings: the area:grid
                        marking is consistent with the boundaries and does not contradict them. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The double solid yellow lines indicate that crossing the center line
                        markings for passing is prohibited for traffic traveling in either direction.
                        [[US-3B.01-06]]
Step 5  Rule            area:grid: The grid marking indicates an area that vehicles must not block.
                        [[US-3B.26-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        left, which discourages crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid yellow center line on
                        the right, which prohibits crossing.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn or a specific arrow allowing it.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are prohibited by the solid lines on both
                        sides. You may proceed straight, but be aware that the area ahead is marked as a grid
                        and must not be blocked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 867, 7.23 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is a junction or intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, and Photo 2 shows a solid white line
                        next to the car. Further ahead in Photo 1, the line appears to be a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to the car, and Photo 2 shows a broken yellow
                        line next to the car. Further ahead in Photo 1, the line appears to be a broken yellow
                        line.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a center_line, placing the ego lane in the middle. | roles: The left
                        boundary is a solid white lane_line, and the right boundary is a dashed yellow
                        center_line, which fits their roles. | markings: The white arrow in the lane is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the lane line markings delineate the separation of traffic flows
                        in the same direction, they shall consist of a normal width broken white line where
                        crossing is not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [US-3A.04-01] states that a solid line discourages or prohibits crossing.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed yellow center_line, and
                        [US-3A.04-01] states that a broken line indicates a permissive condition.
Step 6  go_straight     allowed (contested, correct): allowed: The lane has a white arrow pointing straight
                        ahead, and [US-3B.23-01] indicates that the arrow shows permissible movements.
Step 6  turn_left       prohibited: prohibited: The lane has a white arrow pointing straight ahead, and
                        [US-3B.23-01] indicates that the arrow shows permissible movements.
Step 6  turn_right      prohibited: prohibited: The lane has a white arrow pointing straight ahead, and
                        [US-3B.23-01] indicates that the arrow shows permissible movements.
Step 6  u_turn          prohibited: prohibited: The lane has a white arrow pointing straight ahead, and
                        [US-3B.23-01] indicates that the arrow shows permissible movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: No marking governs this action.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You should stay in your current lane to go straight, but you may change right if
                        necessary. Do not attempt to turn left, turn right, or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['symbol:other']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1035, 8.53 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with an elevated structure (likely a highway or rail
                        line) to the left. Ahead, the road continues straight, and there are several vehicles
                        in the lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car, followed by
                        a yellow line further ahead. Photo 2: A solid white line is visible immediately to the
                        left of my car, and a yellow line is visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible immediately to the right of my car, followed by
                        a solid white line further ahead. Photo 2: A solid white line is visible immediately
                        to the right of my car, and a solid white line is visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrow in my lane agrees with the boundaries (it is in a lane delineated
                        by lane lines) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane has a straight-ahead arrow, and
                        no other marking prohibits it ([US-3B.23-01]).
Step 6  turn_left       prohibited (correct): prohibited: The lane has a straight-ahead arrow, and this arrow
                        does not show a left turn ([US-3B.23-01]).
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited: The lane has a straight-ahead arrow,
                        and this arrow does not show a right turn ([US-3B.23-01]).
Step 6  u_turn          prohibited (correct): prohibited: The lane has a straight-ahead arrow, and this arrow
                        does not show a U-turn ([US-3B.23-01]).
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines, and turning movements are prohibited by the lane-
                        use arrow.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 984, 7.87 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, and there is a barrier on the left side. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a concrete barrier on the left side, and Photo 2 shows the concrete
                        barrier continuing ahead.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right side, and Photo 2 shows a white dashed
                        line continuing ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge/barrier, right boundary is
                        a lane line separating my lane from the next lane to the right). | roles: the roles
                        (edge_line and lane_line) fit the observed boundaries. | markings: no markings were
                        observed in my lane, so they agree. | unseen: no attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is delineated by a boundary, which in this
                        case is a physical barrier. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            left_boundary: Edge line pavement markings delineate the left or right edges of a
                        roadway, and the right edge line pavement markings shall consist of a normal width
                        solid white line (though this rule applies to the right edge, the left edge is defined
                        by the barrier). [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is an edge line
                        and no prohibition is indicated.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a broken
                        white lane line, and crossing is not discouraged or prohibited [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed because no arrow or prohibited-movement marking
                        restricts this movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        turn left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings indicating a permitted
                        turn right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn or prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane and can proceed straight or change lanes left or right.
                        Since there are no specific markings for turns, you should proceed straight unless you
                        intend to change lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions ['change_left allowed across a curb']
Tokens                  in 9487, out 944, 7.35 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure ahead, and the road continues
                        straight ahead. There are three lanes visible in my direction near the bottom of the
                        photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicate separation between
                        lanes of the same direction). | roles: the white dashed lines fit the role of
                        lane_line. | markings: the white arrow pointing straight ahead is consistent with the
                        lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a white dashed
                        lane line, and there is no marking allowing a lane change to the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane line, and there
                        is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and no
                        other marking prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is marked for straight travel. You may change right
                        if necessary, but you must stay in this lane to proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left prohibited across a broken lane line']
Tokens                  in 9487, out 897, 6.1 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is a
                        junction or intersection where the road continues and potentially merges or splits.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A large white arrow pointing straight ahead is visible
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicate separation of same-
                        direction traffic flows). | roles: the white dashed lines fit the role of lane_line as
                        they separate lanes of the same direction. | markings: the white arrow pointing
                        straight ahead is consistent with the lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        there is no marking allowing a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and no
                        marking prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and this arrow does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and this arrow does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and this arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is marked for straight travel. You may change right
                        if necessary, but you must stay in the lane to go straight, as turning left, right, or
                        making a U-turn is prohibited by the lane arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 9487, out 942, 6.86 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        not an immediate intersection or ramp end. My car is in the rightmost lane visible in
                        the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed line for lane_line, solid white line for edge_line) | markings: there
                        are no markings in my lane to check for agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: A broken line indicates a permissive condition. [[US-3A.04-01]]
Step 5  Rule            right_boundary: A solid line discourages or prohibits crossing (depending on the
                        specific application). [[US-3A.04-01]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white solid edge_line, and
                        [US-3A.04-01] indicates a solid line discourages or prohibits crossing, but since it
                        is an edge line, it governs the change action, and no specific prohibition is found
                        for changing into the shoulder/edge area.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific markings for turns, you should proceed with caution regarding
                        turning movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 982, 8.4 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance with traffic lights visible in the distance. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, Photo 1 shows a solid white line. Photo 2
                        shows a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A double solid yellow line is visible next to the car. Photo 2: A double
                        solid yellow line is visible next to the car. Further ahead, Photo 1 shows a double
                        solid yellow line. Photo 2 shows a double solid yellow line.
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): None visible in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: no markings were listed, so they agree | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The double solid yellow lines indicate a two-direction no-passing
                        zone, prohibiting crossing the center line markings for passing in either direction.
                        [[US-3B.01-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a solid white
                        lane_line and the rule [US-3B.06-05-06] only discourages crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a double
                        solid yellow center_line, and the rule [US-3B.01-06] prohibits crossing the center
                        line markings for passing.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in the lane to govern
                          entering a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the right lane to proceed straight. Lane changes to the left are
                        discouraged, and changing to the right is prohibited by the double solid yellow line.
                        No specific stopping or turning maneuvers are governed by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 921, 8.28 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is a
                        distant intersection or area where the road widens/changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Photo 2: The
                        solid white line continues further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A double solid yellow line is visible next to the car. Photo 2: A double
                        solid yellow line is visible next to the car. Further ahead, the double solid yellow
                        line continues. Photo 2: The double solid yellow line continues further ahead.
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line (separating from
                        lane 1), and the right boundary is a center_line (separating from traffic in the
                        opposite direction). | roles: The solid white line on the left fits the role of a
                        lane_line, and the double solid yellow line on the right fits the role of a
                        center_line. | markings: The white arrow pointing straight ahead is consistent with
                        the lane markings and boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line, although in
                        this case it is solid, which discourages crossing. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Except where a reversible lane or a two-way left-turn lane is present,
                        the center line markings on undivided two-way roadways with four or more lanes for
                        moving motor vehicle traffic always available shall be the two-direction no-passing
                        zone markings consisting of normal width double solid yellow lines. [[US-3B.01-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The solid white line on the left indicates that
                        crossing the lane line markings is discouraged or prohibited, as per [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The double solid yellow line on the
                        right indicates a maximum restriction on crossing, as per [US-3B.01-06].
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The white arrow pointing straight ahead
                        permits this movement, as per [US-3B.23-01].
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The white arrow pointing straight ahead
                        does not show a left turn, as per [US-3B.23-01].
Step 6  turn_right      prohibited (correct): prohibited: The white arrow pointing straight ahead does not
                        show a right turn, as per [US-3B.23-01].
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: The white arrow pointing straight ahead
                        does not show a U-turn, as per [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of this lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the observed markings and rules.
Advice                  You must stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white line on the left and the double solid yellow line on the
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1094, 8.2 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with an elevated structure (likely a highway or rail
                        line) on the left. The road ahead appears to continue straight into the distance, with
                        buildings lining the right side. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid green barrier/retaining wall runs along the left side, adjacent to
                        the elevated structure. Photo 2: The solid green barrier/retaining wall continues
                        along the left side.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible, followed by a solid white line further ahead.
                        Photo 2: A white dashed line is visible next to the car, and a solid white line is
                        visible further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge line, right boundary is a
                        lane line separating my lane from the lane to the right). | roles: the color and
                        pattern of the left boundary (none/none) fit the role of an edge line, and the right
                        boundary (white/solid_dashed) fits the role of a lane line. | markings: the white
                        arrow pointing straight ahead in my lane is consistent with the boundaries and
                        markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: When used, white markings for longitudinal lines shall delineate the
                        right-hand edge of the roadway, or the right-hand edge and left-hand edge of a
                        reversible roadway. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is prohibited, the lane line
                        markings shall consist of a double solid white line. [[US-3B.06-12]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed: The left boundary is an edge line, and there is no marking
                        prohibiting a lane change to the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane line, and the arrow in my
                        lane does not prohibit changing right.
Step 6  go_straight     allowed (correct): allowed: The white arrow in my lane indicates that going straight
                        is a permissible movement.
Step 6  turn_left       prohibited (correct): prohibited: The white arrow in my lane does not show a left
                        turn.
Step 6  turn_right      prohibited (correct): prohibited: The white arrow in my lane does not show a right
                        turn.
Step 6  u_turn          prohibited (correct): prohibited: The white arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and the markings permit you to go straight or change lanes
                        left or right. Since the arrow only shows straight, turning left, right, or making a
                        U-turn is prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left allowed across a curb']
Tokens                  in 9487, out 988, 8.52 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with an overpass on the left. Ahead, the road
                        continues into a built-up area with buildings on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane ahead,
                        indicating a stop line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white lane lines separating lanes of the same
                        direction). | roles: the color (white) and pattern (solid) of both boundaries fit the
                        role of lane_line. | markings: the stop line marking is consistent with the visual
                        evidence. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        crossing it is discouraged, which prohibits the change.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        crossing it is discouraged, which prohibits the change.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a stop line,
                        which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first: The lane contains a stop line, which turns all allowed
                        movements into stop_first.
Step 6  turn_right      stop_first: stop_first: The lane contains a stop line, which turns all allowed
                        movements into stop_first.
Step 6  u_turn          stop_first: stop_first: The lane contains a stop line, which turns all allowed
                        movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane or adjacent to it.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop behind the solid white stop line before proceeding.
                        Lane changes are prohibited by the solid white lines on both sides of your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 9487, out 916, 7.87 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into a built-up area with buildings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line is visible in Photo 1, appearing
                        as a white dashed line. Photo 2 shows the line further ahead as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line is visible in Photo 1, appearing
                        as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No specific markings like arrows, words, or areas are
                        visible within my lane in Photo 2. Photo 1 shows no such markings in the visible
                        portion of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines fit the
                        role of lane_line as they separate lanes traveling in the same direction. | markings:
                        the lack of visible markings in my lane is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change lanes left or right, as
                        well as proceed straight ahead. No specific turn or waiting area markings govern your
                        movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 903, 7.91 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where traffic flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in
                        the lane.; arrow:straight (full): Photo 2: A white arrow pointing straight ahead is
                        visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation between lanes of the same direction). | roles: the white dashed lines fit
                        the role of lane_line as they separate lanes traveling in the same direction. |
                        markings: the white arrows pointing straight ahead are consistent with the lane
                        markings observed. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        there is no marking allowing a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and the dashed pattern indicates a permissive condition for crossing with care.
Step 6  go_straight     allowed (correct): allowed: The lane contains a white arrow pointing straight ahead,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane contains a white arrow pointing straight
                        ahead, which does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane contains a white arrow pointing straight
                        ahead, which does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane contains a white arrow pointing straight
                        ahead, which does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of this lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is marked to proceed straight ahead. You may change
                        right if necessary, but turning left, turning right, or making a U-turn is prohibited
                        by the lane arrow. Proceed straight ahead in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line']
Tokens                  in 9487, out 967, 6.6 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        My car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, the solid white
                        line continues until it meets the intersection markings. Photo 2: A solid white line
                        is visible next to my car. Further ahead, the solid white line continues until it
                        meets the intersection markings.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken white line is visible next to my car. Further ahead, the broken
                        white line continues until it meets the intersection markings. Photo 2: A broken white
                        line is visible next to my car. Further ahead, the broken white line continues until
                        it meets the intersection markings.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2: A white dashed line is visible across the lane ahead
                        of my car, indicating a lane division or transition.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid/dashed lines are lane lines). | markings: the white dashed line across
                        the lane ahead is consistent with the lane line markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line, although the
                        left boundary is solid. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop, except YIELD signs that are not associated with
                        passive grade crossings. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a solid white lane line, and
                        there is no rule prohibiting a lane change.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane line, and
                        there is no rule prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight.
Step 6  turn_left       allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict turning left.
Step 6  turn_right      allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict turning right.
Step 6  u_turn          allowed: allowed because there are no arrows or prohibited-movement markings in my
                        lane that restrict U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked areas for waiting ahead
                          of my lane or to its left.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and all movements (straight, left, right, U-turn)
                        are permitted at the intersection. Be aware of the crosswalk marking ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 9487, out 970, 6.76 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, there is an
                        intersection where traffic appears to be moving through. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines fit the
                        role of lane_line as they separate lanes traveling in the same direction. | markings:
                        no markings were observed in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane to prohibit
                        going straight.
Step 6  turn_left       allowed: allowed: There are no markings in the lane to prohibit turning left.
Step 6  turn_right      allowed: allowed: There are no markings in the lane to prohibit turning right.
Step 6  u_turn          allowed: allowed: There are no markings in the lane to prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes left or right, and all
                        movements (straight, left, right, U-turn) are permitted as no lane-use markings
                        restrict you. Proceed with caution given the urban environment.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 9487, out 820, 6.31 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, there
                        is an overpass/exit ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line marking the lane
                        boundary to the left, and a white dashed line marking the lane boundary to the right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the lane
                        markings observed (dashed lines) are consistent with the boundaries, although the stop
                        line marking is not clearly visible/applicable based on the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        white lane line, and [US-3B.06-05-06] permits crossing when not discouraged or
                        prohibited.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes; you may change left or right as the dashed
                        lines permit. You may proceed straight ahead, but turning movements are not explicitly
                        permitted by lane markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1173, 8.5 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, the road
                        continues straight, and there are no immediate intersections or ramps visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead, and Photo 2
                        shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead, and Photo 2
                        shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines fit the role of lane_line
                        separating traffic flows in the same direction. | markings: the stop line is present
                        in my lane and is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows prohibiting it, and
                        the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right, or proceed straight ahead. You must stop at the visible
                        stop line if a traffic control device requires it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1077, 7.62 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight with no immediate
                        intersection or ramp visible in the frame. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line next to my car, and Photo 2 shows a yellow solid
                        line next to my car. Photo 1 shows a yellow solid line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a white dashed line marking in my lane.;
                        text:other (partial): Photo 2 shows a white dashed line marking in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line). | markings: the markings
                        (line:stop_yield and text:other) are present in my lane and are consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on undivided two-way roadways with four or
                        more lanes for moving motor vehicle traffic always available shall be the two-
                        direction no-passing zone markings consisting of normal width double solid yellow
                        lines, although here it is a single solid yellow line. [[US-3B.01-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 5  Rule            text:other: No specific rule passage was found for the 'text:other' marking. [null]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        yellow center_line, and [US-3B.01-06] implies restrictions on crossing center lines.
Step 6  go_straight     allowed (contested, label prohibited): allowed because there are no markings in my
                        lane prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change left into the adjacent lane, but changing right is prohibited by the
                        solid yellow center line. You may proceed straight ahead, but you must yield to
                        traffic before proceeding due to the yield line marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield', 'text:other'], missed ['text:bus']), actions None, unsafe [],
                        citation unlisted, contradictions ['go_straight allowed without the stop that the STOP
                        or 停 marking in my lane requires']
Tokens                  in 9487, out 1014, 8.23 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the right side. Ahead, the road
                        continues straight, possibly towards an overpass or interchange structure. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car, and further ahead, it appears
                        to be a white dashed line continuing. Photo 2: A white dashed line is visible next to
                        my car, and further ahead, it continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car, and further ahead, it appears
                        to be a white dashed line continuing. Photo 2: A white dashed line is visible next to
                        my car, and further ahead, it continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in the lane,
                        indicating the boundary with the adjacent lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation between lanes of the same direction). | roles: The white dashed lines on
                        both sides fit the role of lane_line. | markings: The partial observation of a
                        line:stop_line in Photo 2 is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no marked waiting areas or two-way
                          left-turn lanes in view.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the rules cited.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line visible, you must stop before it if required by a traffic control device.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1135, 8.49 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with barriers on the left side. Ahead, the road continues
                        straight, possibly towards an overpass or another section of the highway. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues. Photo 2 shows a solid white line immediately to the left of my
                        car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately to the right of my car, and further
                        ahead, this line continues. Photo 2 shows a solid white line immediately to the right
                        of my car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line in the center of my lane,
                        separating it from the lane to the left.; line:stop_line (partial): Photo 2 shows a
                        dashed white line in the center of my lane, separating it from the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate separation
                        between lanes of the same direction). | roles: the solid white lines on both sides fit
                        the role of lane_line. | markings: the dashed white lines in the center of the lane
                        are interpreted as lane markings, but their specific function (stop line) is
                        questionable given the context of a highway and the visual appearance of dashed lines
                        in the center of a lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid, crossing it is discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid, crossing it is discouraged.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited because the left boundary is a solid
                        white lane_line, and crossing a solid line is discouraged [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white lane_line, and crossing a solid line is discouraged [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         The boundaries and markings are consistent with the close-up view, and no action is
                        allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        discouraged by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 989, 7.76 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight without an immediate intersection or ramp visible. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the adjacent lane to the left.
                        Photo 2: A white dashed line separates my lane from the adjacent lane to the left,
                        visible near the bottom of the close-up.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line separates my lane from the adjacent lane to the right.
                        Photo 2: A white dashed line separates my lane from the adjacent lane to the right,
                        visible near the bottom of the close-up.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2: A white dashed line is visible further ahead,
                        separating my lane from the lane to the left. This line appears to be the boundary of
                        the adjacent lane.; line:stop_line (insufficient): Photo 2: A white dashed line is
                        visible further ahead, separating my lane from the lane to the right. This line
                        appears to be the boundary of the adjacent lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation between lanes of the same direction). | roles: the white dashed lines on
                        both sides fit the role of lane_line. | markings: the markings listed are based on the
                        visual evidence of the lane boundaries and do not contradict the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a multi-lane highway. You may change lanes left or
                        right, and you may proceed straight ahead. No specific lane usage markings restrict
                        your movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 922, 7.48 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        curves slightly to the right and appears to continue as a highway. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes of the same
                        direction) | roles: the white dashed lines fit the role of lane_line separating
                        traffic flows in the same direction | markings: no markings were listed, so this is
                        consistent | unseen: no attributes were reported that were not seen | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking in my
                        lane restricts carrying on straight along my lane, and the boundaries do not govern
                        it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes to the left or right, and you may proceed straight ahead. No specific
                        lane markings restrict turning movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 870, 7.86 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with trees lining both sides. Ahead, the road continues
                        straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line
                        continuing. Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line
                        continuing. Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines on both sides fit the role of
                        lane_line. | markings: there are no markings in my lane to check against boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes left or
                        right, and you may proceed straight ahead. No specific lane usage is mandated by the
                        markings visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 821, 7.37 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines on both sides fit the role of
                        lane_line. | markings: there are no markings in the lane to check against boundaries.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane to govern U-turns or
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in the lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway, and you are permitted to change
                        lanes in either direction. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 794, 7.55 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway, and the road continues straight ahead with no immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in the lane ahead of
                        the car, separating the lane from the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of both boundaries (solid white) fit the
                        role of a lane line. | markings: the white dashed line ahead is interpreted as a stop
                        line, which is consistent with the lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line, although the
                        observed line is solid. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line,
                        although the observed line is solid. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and while the rule for solid lines is not explicitly stated for prohibiting lane
                        changes in this context, the solid line generally discourages crossing.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        while the rule for solid lines is not explicitly stated for prohibiting lane changes
                        in this context, the solid line generally discourages crossing.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may proceed straight ahead,
                        but you must stop before the white dashed line ahead. Lane changes are prohibited by
                        the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 979, 7.56 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight with no immediate intersection or ramp visible. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the lane to the left. Photo 2: A
                        white dashed line separates my lane from the lane to the left, visible near the car.
                        Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line separates my lane from the lane to the right. Photo 2: A
                        white dashed line separates my lane from the lane to the right, visible near the car.
                        Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2: A white dashed line marking is visible on the
                        right side of my lane, indicating the boundary.; line:stop_line (insufficient): Photo
                        2: A white dashed line marking is visible on the left side of my lane, indicating the
                        boundary.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicating separation between
                        lanes of the same direction). | roles: the white dashed lines fit the role of
                        lane_line. | markings: the markings listed are based on the boundaries and are not
                        fully discernible as specific markings within the lane itself, but the boundaries are
                        consistent. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific turn arrows or waiting areas marked, you should proceed straight
                        unless you intend to change lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 934, 7.35 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues into the distance with an overpass visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible to the left of my lane, separating traffic.
                        Photo 2: A solid yellow line is visible to the left of my lane, separating traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible to the right of my lane, delineating the edge
                        of the roadway. Photo 2: A solid white line is visible to the right of my lane,
                        delineating the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): No specific markings like arrows, words, or areas are visible
                        within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line). | roles: the yellow solid line fits the role of a center_line, and the
                        white solid line fits the role of an edge_line. | markings: the lack of markings in my
                        lane is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            no_turn:right: No rule passage specifically governs the absence of a right turn
                        prohibition marking in this context. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a solid yellow center_line, and the
                        rule [US-3A.04-01] states that a solid line discourages or prohibits crossing, but
                        since no specific prohibition is shown, and the lane is not designated as a mandatory
                        turn lane, a lane change is permitted if the boundary allows it, which it does not
                        explicitly prohibit.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and the
                        rule [US-3A.03-03-04] states that white markings delineate the right-hand edge of the
                        roadway, which does not prohibit changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is present.
Step 6  turn_right      allowed: allowed: There are no arrows or prohibited-movement markings in my lane, and
                        the boundaries do not prohibit turning right.
Step 6  u_turn          allowed: allowed: There are no arrows or prohibited-movement markings in my lane, and
                        no specific prohibition against U-turns is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting for a left turn
                          or a two-way left-turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change left or right, and
                        all movements including going straight, turning right, and U-turning are permitted.
                        Since there are no specific markings, you should proceed with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['turn_right allowed although a prohibited-movement marking forbids
                        it']
Tokens                  in 9487, out 1047, 7.79 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with barriers on both sides, and the road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line next to the car, and a white line further ahead. Photo 2
                        shows a white line next to the car, and a white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line next to the car, and a white line further ahead. Photo 2
                        shows a white line next to the car, and a white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right edge of
                        my lane.; line:stop_line (partial): Photo 2 shows a white dashed line marking the left
                        edge of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the color (white) and pattern (dashed) of each boundary fit the
                        role (lane_line) | markings: the markings (line:stop_line) are consistent with the
                        boundaries (lane_line) as they define the edge of the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop, except YIELD signs that are not associated with
                        passive grade crossings. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific stopping or turning maneuvers are governed by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 961, 7.63 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the right side and a guardrail on the
                        left side, leading towards a distant hill in the background. There are multiple lanes
                        in my direction visible near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a metal guardrail on the left side. Photo 2 shows the metal guardrail on
                        the left side.
                        none none, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a continuous white line painted on the concrete barrier on the right
                        side. Photo 2 shows a continuous white line painted on the concrete barrier on the
                        right side.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line segment immediately ahead
                        of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge line, right boundary is an
                        edge line). | roles: the color and pattern of each boundary fit the role given to it
                        (left is no line/edge, right is solid white edge line). | markings: the dashed white
                        line segment ahead is consistent with the lane markings observed. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Edge line pavement markings delineate the right or left edges of a
                        roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is an edge line with no
                        restrictions on lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is an edge line
                        with no restrictions on lane changes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as there are no solid lines
                        prohibiting them. You may proceed straight ahead, but be aware of the dashed white
                        line ahead, which may indicate a required stop or yield point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['change_left decided with nothing marked on that
                        side', 'change_right allowed across a curb']
Tokens                  in 9487, out 874, 6.23 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues into the distance with
                        buildings on both sides. My car is in the rightmost lane visible near the bottom of
                        the photo. (lanes 3, mine 3, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in my lane,
                        extending ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the line:stop_line marking is consistent with the boundaries and general
                        road markings | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed white
                        lane line, and while this permits crossing with care, the presence of a stop line
                        ahead requires stopping first.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white edge
                        line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a line:stop_line
                        marking, which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first: prohibited: The lane contains a line:stop_line marking, which turns all
                        allowed movements into stop_first, and there are no markings allowing a left turn.
Step 6  turn_right      stop_first: prohibited: The lane contains a line:stop_line marking, which turns all
                        allowed movements into stop_first, and there are no markings allowing a right turn.
Step 6  u_turn          stop_first: prohibited: The lane contains a line:stop_line marking, which turns all
                        allowed movements into stop_first, and there are no markings allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop behind the stop line before proceeding. You may
                        proceed straight or turn right after stopping, but changing lanes to the left is
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line', 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 9487, out 979, 8.31 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues straight ahead with
                        guardrails on both sides. My car is in the rightmost lane visible in the immediate
                        foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the white dashed lines fit the roles of lane_line and edge_line.
                        | markings: no markings were reported, so they agree with each other and the
                        boundaries. | unseen: no attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway, although the
                        observed line is dashed. [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: A broken line indicates a permissive condition. [[US-3A.04-01]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition. [[US-3A.04-01]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a white dashed
                        lane_line, and [US-3A.04-01] states a broken line indicates a permissive condition.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a white
                        dashed edge_line, and [US-3A.04-01] states a broken line indicates a permissive
                        condition.
Step 6  go_straight     allowed (contested, correct): allowed because no arrow prohibits it, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          this action.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns or waiting areas, you should proceed according to
                        general traffic laws.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 942, 7.85 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway, and the road continues straight ahead with no immediate
                        intersection or ramp visible in the close-up. (lanes 5, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line marking the lane
                        boundary next to my car, and a white dashed line marking the lane boundary further
                        ahead. Photo 2 shows the same white dashed lines.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (5) and my lane position
                        (3) agree with the boundary roles (white dashed lines indicate separation of traffic
                        flows in the same direction). | roles: the color (white) and pattern (dashed) of each
                        boundary fit the role of a lane_line. | markings: the lane markings (white dashed
                        lines) agree with the boundaries (white dashed lines). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you should proceed with caution regarding turning
                        movements.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1147, 8.2 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road continues into the distance with
                        buildings on both sides, and there is no immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues. Photo 2 shows a solid white line immediately to the left of my
                        car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately to the right of my car, and further
                        ahead, this line continues. Photo 2 shows a solid white line immediately to the right
                        of my car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings (arrows, text, areas) are visible
                        painted within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on both the left and
                        right boundaries. | roles: The solid white lines on both sides fit the role of
                        lane_line separating traffic flows in the same direction. | markings: No markings were
                        listed, so there is no agreement to check. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting ahead of my
                          lane or to my left.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes to the
                        left or right are discouraged by the solid white lane lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 875, 6.59 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section where the lanes appear to
                        converge or transition, possibly leading to an intersection or a change in road
                        geometry. My car is in one of the lanes near the bottom of the photo. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues as a solid white line. Photo 2 shows a solid white line
                        immediately to the left of my car, and further ahead, this line continues as a solid
                        white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately to the right of my car, and further
                        ahead, this line continues as a solid white line. Photo 2 shows a solid white line
                        immediately to the right of my car, and further ahead, this line continues as a solid
                        white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, words, or areas are
                        visible within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (solid white lines on both sides indicate separation
                        between lanes of the same direction). | roles: the solid white lines on both sides fit
                        the role of lane_line. | markings: no markings were observed in my lane, so they agree
                        with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            no_turn:right: No specific rule passage covers this marking as it was not observed.
                        [null]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
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
Advice                  You should proceed straight in your current lane, as lane changes are discouraged by
                        the solid white lines on both sides. No specific markings restrict your movement, but
                        be aware of the lane convergence ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9487, out 943, 7.74 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian overpass ahead. My car is in one of the
                        lanes traveling forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible near the left edge of the road, separated by a
                        curb/barrier. Photo 2: A solid yellow line is visible near the left edge of the road,
                        separated by a curb/barrier. The line next to the car is solid yellow. The line
                        further ahead is solid yellow.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible marking the right edge of the road. Photo 2: A
                        solid white line is visible marking the right edge of the road. The line next to the
                        car is solid white. The line further ahead is solid white.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: there are no markings in my lane to check against boundaries | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: Yellow markings for longitudinal lines shall delineate the separation
                        of traffic traveling in opposite directions, the left-hand edge of the roadways of
                        divided highways and one-way streets or ramps, or the separation of two-way left-turn
                        lanes and reversible lanes from other lanes when used. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line,
                        but since this is an edge line, the edge line rule applies. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which, as a center
                        line, prohibits crossing into the adjacent lane based on the general function of solid
                        lines discouraging crossing.
Step 6  change_right    allowed (correct): The right boundary is a solid white edge line, and there are no
                        markings indicating a prohibition for changing right, so it is allowed.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is allowed to proceed straight. You may change right
                        into the adjacent lane, but changing left is prohibited by the solid yellow center
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1120, 8.94 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white solid line is visible next to the car. Photo 2: A white solid line is
                        visible next to the car. Further ahead, the line remains a white solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): None visible in Photo 1 or Photo 2.; line:yield_line
                        (insufficient): None visible in Photo 1 or Photo 2.; area:left_turn_waiting
                        (insufficient): None visible in Photo 1 or Photo 2.; area:two_way_left_turn_lane
                        (insufficient): None visible in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating my lane is the middle lane of three lanes in my direction). |
                        roles: the color and pattern of each boundary fit the role given to it (white
                        dashed/solid lines are consistent with lane lines separating lanes of the same
                        direction of travel). | markings: the lane markings list is empty, which is consistent
                        with the boundaries and the lack of visible markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            left_boundary: The solid white lane line marking should be used on approaches to
                        intersections to separate a through lane from a mandatory turn lane, although this
                        line is dashed. [[US-3B.06-07]]
Step 5  Rule            right_boundary: Since the line is solid, crossing the lane line markings is
                        discouraged. [[US-3B.06-12]]
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, meaning crossing with care is not discouraged or prohibited [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited because the right boundary is a solid white line,
                        meaning crossing the lane line markings is discouraged [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane that
                        prohibit going straight [no marking governs this action].
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane that govern
                        turning movements [not_applicable].
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane that govern
                        turning movements [not_applicable].
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane that govern
                        turning movements [not_applicable].
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible [not_applicable].
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change left across the dashed line, but
                        changing right across the solid line is discouraged. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'line:stop_line',
                        'line:yield_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1184, 11.37 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with buildings lining the left side. Ahead, the road
                        continues straight, and there is a pedestrian overpass on the right side. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a broken white line segment in my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines delineate lanes of the same
                        direction) | roles: the color (white) and pattern (solid) of each boundary fit the
                        role (lane_line) | markings: the line:stop_line marking is consistent with the lane
                        markings observed | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited due to the solid white line on the left boundary, as
                        crossing is discouraged ([US-3B.06-05-06])
Step 6  change_right    prohibited (correct): prohibited due to the solid white line on the right boundary, as
                        crossing is discouraged ([US-3B.06-05-06])
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane, and the boundaries do not govern this action
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes in view
Step 7  Reflect         consistent
Advice                  You must stop at the visible stop line before proceeding. You are restricted to
                        traveling straight ahead in this lane, as lane changes are prohibited by the solid
                        white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 922, 7.38 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with buildings lining both sides. Ahead, the road continues
                        straight, and there are no immediate intersections or ramps visible in the close-up.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the stop
                        line marking is consistent with the lane boundaries and does not contradict any
                        observed markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a dashed white
                        lane line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows in my lane, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        before the solid white line visible ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1052, 7.25 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the roadway. My car is in
                        the lane closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines on both
                        sides fit the role of lane_line. | markings: no markings were reported, so there is no
                        agreement to check. | unseen: no attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific lane is required for turning movements as no arrows are present.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 882, 7.59 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a stretch of road with buildings on both
                        sides, suggesting a continuous road segment rather than an immediate intersection or
                        ramp end. My car is in the lane closest to the center of the visible lanes. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, words, or areas are
                        visible within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation between lanes of the same direction). | roles: the white dashed lines on
                        both sides fit the role of lane_line. | markings: no markings were observed in my
                        lane, so they agree with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific turn arrows or waiting areas, you should proceed according to
                        standard right-hand traffic rules.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 917, 6.78 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes of the same
                        direction) | roles: the color (white) and pattern (dashed) of both boundaries fit the
                        role of lane_line | markings: the arrow pointing straight ahead in my lane is
                        consistent with the lane markings | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        while this permits lane changes, the arrow in my lane only permits straight movement,
                        which governs lane changes.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a white dashed lane
                        line, and while this permits lane changes, the arrow in my lane only permits straight
                        movement, which governs lane changes.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and no
                        other marking prohibits this movement.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        which does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as the lane markings
                        only permit this movement. Lane changes are prohibited by the lane-use arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left prohibited across a broken lane line', 'change_right prohibited across a
                        broken lane line']
Tokens                  in 9487, out 938, 6.79 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with buildings on both sides. My car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (solid white lines on both sides indicate separation
                        between lanes of the same direction). | roles: the solid white lines on both sides fit
                        the role of lane_line. | markings: no markings were observed in my lane, so there is
                        no contradiction. | unseen: no attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited because the left boundary is a solid white lane_line,
                        and crossing a solid white lane line is discouraged [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white lane_line, and crossing a solid white lane line is discouraged [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight. Lane changes to the left or
                        right are discouraged by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 9487, out 856, 6.97 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight with buildings
                        lining the right side. My car is in one of the lanes near the right side of the
                        visible road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a dashed white
                        lane_line and [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a solid white
                        edge_line and [US-3B.09-01-02] delineates the edge of the roadway, which does not
                        prohibit changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          entering a waiting area.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific lane markings restrict your movement, but be aware of the adjacent traffic.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 899, 7.71 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with buildings on the left and right sides. Ahead, there is
                        a road sign indicating traffic flow, and the road continues forward. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Further ahead, Photo 1 shows a solid yellow line continuing.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a blue overhead sign with three upward arrows,
                        one in the center lane (my lane).
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is an
                        edge line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid for lane line, yellow solid for edge line). | markings: the arrow in my
                        lane (straight) is consistent with the boundaries and markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line is discouraged.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The yellow marking delineates the right-hand edge of the roadway.
                        [[US-3A.03-03-04]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        crossing it is discouraged, which implies a restriction on lane change.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        edge line, and crossing it is prohibited as it is the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): allowed: The lane-use arrow shows straight movement, and
                        no other marking prohibits it.
Step 6  turn_left       prohibited: prohibited: The lane-use arrow does not show a left turn.
Step 6  turn_right      prohibited: prohibited: The lane-use arrow does not show a right turn.
Step 6  u_turn          prohibited: prohibited: The lane-use arrow does not show a U-turn movement and there
                        is no exception noted for this arrow type.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in the middle lane to proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lane line and the roadway edge, respectively. No
                        special stopping or waiting areas are marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 888, 7.79 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        not an immediate intersection or ramp end. My car is in the lane closest to the center
                        of the visible traffic flow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car, and further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car, and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car, and further ahead, the line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car, and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines on both
                        sides fit the role of lane_line separating same-direction traffic flows. | markings:
                        there are no arrows, words, or areas painted in my lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that govern turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you should proceed with caution regarding potential
                        turns.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 853, 6.5 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and a solid yellow line further
                        ahead. Photo 2 shows a solid yellow line next to my car, and a solid yellow line
                        further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white for lane_line, solid yellow for center_line). | markings: the stop line
                        marking is consistent with the boundaries and general road markings. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on undivided two-way roadways with four or
                        more lanes for moving motor vehicle traffic always available shall be the two-
                        direction no-passing zone markings consisting of normal width double solid yellow
                        lines, although here only a single solid yellow line is visible. [[US-3B.01-06]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white lane_line
                        boundary, as crossing the lane line markings is discouraged [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid yellow center_line
                        boundary, as crossing the center line markings is prohibited [US-3B.01-06].
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You must stop behind the solid white stop line before proceeding. You are restricted
                        to going straight ahead in your current lane, as lane changes are prohibited by the
                        solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1154, 8.64 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance with traffic moving away from the camera. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1: A blue overhead sign is visible ahead, indicating
                        directions. Photo 2: The blue overhead sign is visible ahead, indicating directions.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line, indicating the ego lane is between two lanes of the same direction). |
                        roles: the color (white) and pattern (solid) of both boundaries fit the role of a
                        lane_line. | markings: the text marking is consistent with the boundaries and does not
                        contradict them. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            text:other: No specific traffic rule passage covers the blue overhead directional
                        sign. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and crossing it is discouraged ([US-3B.06-05-06]).
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane_line, and
                        crossing it is discouraged ([US-3B.06-05-06]).
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting ahead of my
                          lane or to my left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. Lane
                        changes to the left or right are discouraged due to the solid white lane lines. You
                        may proceed straight ahead in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9487, out 925, 7.41 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining the sides. Ahead, the road continues
                        into the distance, and there is no immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues. Photo 2 shows a solid white line immediately to the left of my
                        car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line immediately to the right of my car, and further
                        ahead, this line continues. Photo 2 shows a solid yellow line immediately to the right
                        of my car, and further ahead, this line continues.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No specific markings (arrows, text, symbols, areas, or
                        lines like stop/yield) are visible within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane line (white solid), and the right
                        boundary is a center line (yellow solid), which is consistent with my lane being the
                        middle lane. | roles: The left boundary is a white solid lane line, consistent with
                        separating traffic flows in the same direction [US-3B.06-05-06]. The right boundary is
                        a yellow solid line, consistent with delineating the separation of traffic traveling
                        in opposite directions [US-3B.01-01]. | markings: No markings were listed, so this
                        check is vacuously true. | unseen: No attributes were reported that were not seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane line indicates that crossing the lane line is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid yellow line delineates the separation of traffic traveling
                        in opposite directions. [[US-3B.01-01]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a solid white lane line, and
                        the rule [US-3B.06-05-06] only discourages crossing, not prohibits it.
Step 6  change_right    prohibited (correct): Prohibited because the right boundary is a solid yellow center
                        line, and the rule [US-3B.01-01] indicates separation of opposite traffic, implying a
                        restriction on crossing into the opposing flow.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane that
                        prohibit going straight.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane that permit or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed that is prohibited by a rule.
Advice                  You are in the middle lane, which is allowed to proceed straight. Lane changes to the
                        left are discouraged, and changing right is prohibited by the solid yellow line
                        separating opposing traffic.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1025, 8.93 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead with no immediate intersection or ramp visible in the close-up. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction) | roles: the white dashed lines fit the role of lane_line
                        separating lanes of the same direction | markings: no markings were observed in the
                        lane | unseen: no attributes were reported that were not seen | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in the lane to govern
                          entering a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right, and you may proceed straight ahead. No specific lane is
                        required for any movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 830, 6.47 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving forward. Ahead, there is an
                        intersection or a major crossing area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the left of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible immediately to the right of my car. Further
                        ahead, this line appears to continue as a solid yellow line. Photo 2: A solid yellow
                        line is visible immediately to the right of my car. Further ahead, this line continues
                        as a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2: A white arrow pointing to the right is visible on
                        the road ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line (white, separating
                        traffic in the same direction), and the right boundary is a center_line (yellow,
                        separating traffic in the opposite direction). | roles: The white solid line on the
                        left fits the role of a lane_line separating traffic in the same direction, and the
                        yellow solid line on the right fits the role of a center_line separating opposite
                        directions. | markings: The right-turn arrow is in my lane and is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions. [[US-3B.01-01]]
Step 5  Rule            arrow:merge_right: Lane-use arrow markings indicate the mandatory or permissible
                        movements in certain lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The solid white line on the left indicates that
                        crossing the lane line markings is discouraged, and the arrow only permits a right
                        movement.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The solid yellow line on the right is a
                        center line, and the arrow permits a right movement, which is consistent with the lane
                        configuration.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: The arrow marking indicates a mandatory
                        right movement, prohibiting straight travel.
Step 6  turn_left       prohibited (correct): prohibited: The arrow marking indicates a mandatory right
                        movement, prohibiting a left turn.
Step 6  turn_right      allowed (correct): allowed: The arrow marking permits a right movement, and the right
                        boundary is a center line.
Step 6  u_turn          prohibited (correct): prohibited: The arrow marking indicates a mandatory right
                        movement, prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: No markings for a waiting area were observed in my
                          lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the observed markings and rules.
Advice                  You must follow the lane indicated by the right-turn arrow, which permits turning
                        right or changing right. Do not attempt to go straight or turn left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe ['change_right'], citation in_pack_not_accepted, contradictions
                        ['go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 9487, out 972, 7.93 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues under an overpass structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car. Further ahead, the line remains a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car. Further ahead, the line remains a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line) | markings: there are no
                        markings in my lane to check for agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        center_line, and [US-3B.01-01] indicates separation of opposite directions of travel,
                        which implies restriction from crossing into the opposite direction.
Step 6  go_straight     allowed (contested, correct): allowed: No markings in my lane prohibit going straight,
                        and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change left
                        if necessary, but changing right is prohibited by the solid yellow center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 827, 6.3 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road, and ahead there is an overpass/bridge
                        structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows white dashed lines marking the lane
                        boundaries.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes of the same
                        direction). | roles: the white dashed lines fit the role of lane_line separating
                        traffic flows in the same direction. | markings: the lane markings observed (dashed
                        lines) are consistent with the boundaries, although no specific arrow or word markings
                        are clearly visible in the lane itself. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a multi-lane road, and you are permitted to change lanes
                        both left and right. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 937, 6.44 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, appearing to be a major
                        thoroughfare or highway. Ahead, the road continues, and there is a commercial area on
                        the right side. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right boundary
                        of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        line:stop_line marking is consistent with the boundaries and general road markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        white lane line, and [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you must proceed with caution for any turning
                        movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1152, 9.22 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a road under an overpass. Ahead, the road continues straight, and there are no
                        immediate intersections or ramps visible in the close-up. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a dense line of bushes/foliage on the left. Photo 2 shows the dense line
                        of bushes/foliage on the left.
                        none none, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid red retaining wall on the right. Photo 2 shows the solid red
                        retaining wall on the right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and ego_lane_index
                        (1) agree with the boundary roles (single lane bounded by edges) | roles: the color
                        and pattern of each boundary fit the role given (no painted lines, physical edges) |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Edge line pavement markings, if used, shall delineate the right or left
                        edges of a roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     not_applicable (WRONG, label prohibited): not_applicable
Step 6  change_right    not_applicable (WRONG, label prohibited): not_applicable
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a single lane with no lane markings or restrictions visible. You may
                        proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 634, 5.92 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a bridge or overpass, leading towards an
                        intersection ahead. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to continue as a white dashed line. Photo 2 shows a white dashed line next to my car,
                        and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to continue as a white dashed line. Photo 2 shows a white dashed line next to my car,
                        and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines on both
                        sides fit the role of lane_line. | markings: the white arrow pointing straight ahead
                        in my lane is consistent with the lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        there is no marking allowing a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane has a white arrow pointing
                        straight ahead, and no marking prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and this arrow does not show a left turn.
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited: The lane has a white arrow pointing
                        straight ahead, and this arrow does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and this arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are currently in the middle lane, which is marked to proceed straight ahead. You
                        may change to the right lane if necessary, but turning left, turning right, or making
                        a U-turn is prohibited by the lane arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['change_right', 'go_straight'], citation in_pack_not_accepted, contradictions
                        ['change_left prohibited across a broken lane line']
Tokens                  in 9487, out 938, 7.54 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, Photo 1 shows a solid white line continuing.
                        Photo 2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, Photo 1 shows a solid white line continuing.
                        Photo 2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines delineate same direction traffic
                        flows, indicating my lane is the middle lane of three). | roles: the color (white) and
                        pattern (solid) of both boundaries fit the role of lane_line separating same direction
                        traffic flows. | markings: there are no arrows, words, or areas in my lane to check
                        against the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        left, as crossing is discouraged [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        right, as crossing is discouraged [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: not_applicable as there are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable as there are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable as there are no markings indicating a permitted U-turn
                        or prohibiting it in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You should remain in the middle lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 825, 4.1 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance with a visible overhead sign. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2: A circular speed limit sign with '30' is visible in
                        the left lane.; text:speed_limit (full): Photo 2: A circular speed limit sign with
                        '60' is visible in the right lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the speed
                        limit markings are present in the lanes and do not contradict the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            text:speed_limit: No specific rule passage was found that dictates the action based on
                        a speed limit marking. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings when not discouraged or
                        prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Use the
                        lane appropriate for your desired speed, noting the posted speed limits of 30 mph in
                        the left lane and 60 mph in the right lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation unlisted, contradictions []
Tokens                  in 9487, out 958, 7.29 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, and there are no immediate intersections or ramps visible in
                        the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible to the left of my car, separating traffic in
                        opposite directions. Photo 2: A solid yellow line is visible to the left of my car,
                        separating traffic in opposite directions. The line further ahead is also a solid
                        yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible to the right of my car, delineating the edge of
                        the roadway. Photo 2: A solid white line is visible to the right of my car,
                        delineating the edge of the roadway. The line further ahead is also a solid white
                        line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2: A solid yellow line is visible immediately to
                        the left of my car, which is the boundary line. No other markings are visible within
                        my lane in Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line). | roles: the color and pattern of each boundary fit the role given to
                        it (yellow solid for center_line, white solid for edge_line). | markings: the markings
                        (insufficiently visible) do not contradict the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid yellow center_line
                        boundary, as crossing it is prohibited by [US-3B.01-01].
Step 6  change_right    allowed (correct): allowed as the right boundary is a solid white edge_line, and no
                        rule prohibits changing right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may proceed straight or change right. Do not cross
                        the solid yellow line to your left, and be aware that the visible marking suggests a
                        yield requirement, though it is not clearly defined.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 994, 7.95 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight, with a directional sign visible in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the lane to the left. Photo 2: A
                        white dashed line separates my lane from the lane to the left, visible near the bottom
                        of the close-up.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line separates my lane from the lane to the right. Photo 2: A
                        white dashed line separates my lane from the lane to the right, visible near the
                        bottom of the close-up.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines fit the role of lane_line. |
                        markings: there are no markings in my lane to check against boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a multi-lane highway. You may change lanes left or
                        right, and you may proceed straight ahead. No specific lane usage is mandated by the
                        markings visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 808, 6.48 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight, with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes of the same
                        direction) | roles: the color (white) and pattern (dashed) of both boundaries fit the
                        role of lane_line | markings: there are no markings in my lane to check against
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes left or
                        right, and you may proceed straight ahead. No specific lane is required for any
                        movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 808, 6.19 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the lane to the left. Photo 2: A
                        white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line separates my lane from the lane to the right. Photo 2: A
                        white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines on both sides fit the role of
                        lane_line. | markings: there are no markings in my lane to check against boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes to the left
                        or right, and you may proceed straight ahead. No specific lane is required for any
                        movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 797, 6.66 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway under an overpass. Ahead, the road continues straight,
                        and there is a visible barrier/guardrail on the left side. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a metal guardrail on the left side. Photo 2 shows the metal guardrail on
                        the left side.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right side. Photo 2 shows a broken white line
                        on the right side.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a broken yellow line marking the lane
                        boundary to the left of my lane. This line is further ahead than the line next to my
                        car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge/barrier, right boundary is
                        a lane line separating my lane from the next lane to the right). | roles: the left
                        boundary is an edge line (guardrail), and the right boundary is a lane line separating
                        lanes of the same direction. | markings: the broken yellow line is interpreted as a
                        yield line based on its appearance and context, although the specific marking is not
                        fully clear in the provided context for a yield line, the interpretation is based on
                        the visual evidence of a line ahead of the car. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Edge line pavement markings shall delineate the right or left edges of
                        a roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is an edge line
                        and no prohibition is visible.
Step 6  change_right    allowed (correct): allowed because the right boundary is a broken white lane line,
                        which indicates a permissive condition for crossing.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Be
                        aware of the yield line ahead, which requires you to yield to traffic or pedestrians
                        if necessary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions ['change_left allowed across a curb',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 908, 7.63 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance without an immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction). | roles: the white dashed lines on both sides fit the role of
                        lane_line. | markings: no markings were observed in the lane. | unseen: no attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway, and you are permitted to change
                        lanes in either direction. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 817, 7.33 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the line remains a solid white line. Further
                        ahead, the line remains a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [US-3A.03-03-04] permits delineation of the right-hand edge of the roadway.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific lane usage markings restrict your movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 834, 5.97 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance with no immediate intersection or ramp visible. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a metal guardrail on the left. Photo 2 shows the metal guardrail on the
                        left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a painted white line on the right. Photo 2 shows a painted white line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge line, right boundary is a
                        lane line separating my lane from another lane of the same direction). | roles: the
                        left boundary is an edge line (guardrail), and the right boundary is a lane line
                        (white dashed line). | markings: no markings were reported in the lane, which is
                        consistent with the observations. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Edge line pavement markings, if used, shall delineate the right or left
                        edges of a roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition. [[US-3A.04-01]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is an edge line, and no
                        rule prohibits changing into the adjacent lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and a
                        broken line indicates a permissive condition.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change left or right, and
                        you may proceed straight. Since there are no turn arrows, you may not turn left,
                        right, or make a U-turn unless the road geometry allows it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions ['change_left allowed across a curb']
Tokens                  in 9487, out 859, 7.46 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with guardrails on both sides, and it appears to be a
                        straight stretch of road ahead with no immediate intersection or ramp visible. There
                        are at least three lanes visible in my direction near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the white dashed lines fit the role of lane_line separating
                        traffic flows in the same direction | markings: no markings were reported, so this is
                        consistent | unseen: no attributes were reported that were not actually seen | result:
                        consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed
                        lane_line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right as long as you do so with
                        care. All movements, including going straight, are permitted by the current lane
                        markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 854, 7.47 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, possibly approaching an interchange or a section with
                        designated lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line marking the right
                        boundary of the lane, and a white dashed line marking the left boundary of the lane.
                        Photo 2 shows the same white dashed lines.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicating separation between
                        lanes of the same direction). | roles: The white dashed lines fit the role of
                        lane_line, as they separate lanes traveling in the same direction. | markings: The
                        lane markings observed (white dashed lines) are consistent with the boundaries, but no
                        specific arrows or areas were clearly identified in the lane itself. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed lane_line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a white
                        dashed lane_line, and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change left or right, as well as
                        proceed straight. Since there are no specific turn markings, you can proceed straight
                        or make a turn if the road geometry allows it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1206, 7.47 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight with no immediate
                        intersection or ramp visible in the close-up. My car is in the rightmost lane visible
                        in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the boundary
                        between my lane and the lane to the left.; line:stop_line (partial): Photo 2 shows a
                        white dashed line marking the boundary between my lane and the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the color (white) and pattern (dashed) of both boundaries fit
                        their roles as lane_line and edge_line. | markings: the markings (line:stop_line) are
                        consistent with the boundaries and each other. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The right edge line pavement markings, if used, shall consist of a
                        normal width solid white line to delineate the right-hand edge of the roadway, but
                        since this is dashed, it indicates a permissive condition for the edge.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white edge line, and
                        [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line visible, you must stop before it if required by a traffic control device.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 995, 7.24 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test C | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with guardrails on both sides, and the road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the truck. Photo 2: A white dashed
                        line is visible next to the truck.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A large white arrow indicating straight movement is
                        visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines fit the
                        role of lane_line as they separate lanes traveling in the same direction. | markings:
                        the straight arrow in the lane agrees with the boundaries as it indicates movement
                        within the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a white dashed
                        lane line, and there is no marking allowing a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed: The lane contains a straight arrow, and no
                        other marking prohibits going straight.
Step 6  turn_left       prohibited: prohibited: The lane contains a straight arrow, which does not show a left
                        turn.
Step 6  turn_right      prohibited: prohibited: The lane contains a straight arrow, which does not show a
                        right turn.
Step 6  u_turn          prohibited: prohibited: The lane contains a straight arrow, which does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight and allows you to change
                        right. You may change right if the lane is clear, but you must not change left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:speed_limit']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 9487, out 864, 6.93 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible next to my car. Further ahead, the solid
                        yellow line continues until the intersection. Photo 2: A solid yellow line is visible
                        next to my car. Further ahead, the solid yellow line continues until the intersection.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Further ahead, the solid white
                        line continues until the intersection. Photo 2: A solid white line is visible next to
                        my car. Further ahead, the solid white line continues until the intersection.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: Two parallel solid yellow lines are visible in the
                        center of the road, indicating the separation of traffic flows.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for lane_line). | markings: the markings
                        (line:stop_yield) are consistent with the boundaries (center_line and lane_line). |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid yellow
                        center_line, and a solid line discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        lane_line, and a solid line discourages or prohibits crossing [US-3A.04-01], but since
                        no specific prohibition is given for this lane change, it is allowed.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit or prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit or prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that permit or prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting ahead of my
                          lane or directly to its left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or change right. Be aware
                        that the markings indicate a yield point ahead, so you must yield to pedestrians or
                        traffic before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 1021, 8.44 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, the road
                        continues straight, and there is a sign visible in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow dashed line next to my car, and a yellow dashed line further
                        ahead. Photo 2 shows a yellow dashed line next to my car, and a yellow dashed line
                        further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow dashed for center_line). | markings: the
                        line:stop_line marking is consistent with the boundaries and general road markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on two-lane, two-way roadways shall be one of
                        the following: A. Two-direction passing zone markings consisting of a normal width
                        broken yellow line where crossing the center line markings for passing with care is
                        permitted for traffic traveling in either direction; B. One-direction no-passing zone
                        markings consisting of a double yellow line, one of which is a normal width broken
                        yellow line and the other is a normal width solid yellow line, where crossing the
                        center line markings for passing with care is permitted for the traffic traveling
                        adjacent to the broken line, but is prohibited for traffic traveling adjacent to the
                        solid line; or C. Two-direction no-passing zone markings consisting of two normal
                        width solid yellow lines where crossing the center line markings for passing is
                        prohibited for traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            line:stop_line: Stop lines may be used to indicate the point behind which vehicles are
                        required to stop in compliance with a STOP sign or some other traffic control device
                        that requires vehicles to stop, except YIELD signs that are not associated with
                        passive grade crossings. [[US-3B.19-01-02]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed yellow center_line,
                        and [US-3B.01-04] permits crossing with care for traffic adjacent to a broken yellow
                        line.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change left or
                        right if necessary, but you must stop behind the visible stop line if required by a
                        traffic control device.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1095, 8.9 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into a built-up area with buildings. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, the solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to the car.
                        Further ahead, the solid yellow line continues.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: A solid yellow line is visible immediately to the
                        right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white solid for lane_line, yellow solid for center_line) | markings: the markings
                        (solid yellow line) agree with the boundaries (center_line) | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the lane line markings delineate the separation of traffic flows
                        in the same direction, they shall consist of a normal width solid white line if
                        crossing is discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Except where a reversible lane or a two-way left-turn lane is present,
                        the center line markings on undivided two-way roadways with four or more lanes for
                        moving motor vehicle traffic always available shall be the two-direction no-passing
                        zone markings consisting of normal width double solid yellow lines, although here only
                        a single solid yellow line is visible. [[US-3B.01-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made, although here a solid
                        yellow line is present instead of a triangle. [[US-3B.19-10]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white lane
                        line, which discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        center line, which indicates a no-passing zone [US-3B.01-04].
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
Advice                  You must stay in your lane as both the left and right boundaries are solid lines
                        prohibiting lane changes. You are permitted to go straight ahead, but you should be
                        aware of the yield marking ahead, which suggests you may need to yield to traffic or
                        pedestrians.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 1040, 7.26 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there are directional signs indicating an entrance ramp.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible to the left of my lane, separating traffic in
                        opposite directions. Photo 2: A solid yellow line is visible to the left of my lane,
                        separating traffic in opposite directions.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible to the right of my lane, separating traffic
                        flows in the same direction. Photo 2: A solid white line is visible to the right of my
                        lane, separating traffic flows in the same direction.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): None visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for lane_line) | markings: no markings were
                        listed in my lane, so there is no agreement to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited because the left boundary is a solid yellow
                        center_line, which discourages crossing.
Step 6  change_right    allowed (correct): allowed because the right boundary is a solid white lane_line, and
                        no rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane that
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane that allow or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane that allow or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane that allow or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane that
                          indicate a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight or change right.
                        Since there are no specific markings for turns, you should follow the general flow of
                        traffic for your intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 915, 7.33 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into a built-up area with buildings on both sides. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid yellow line is visible near the left edge of the road. Photo 2: A
                        solid yellow line is visible near the left edge of the road, next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible defining the right edge of the travel lanes.
                        Photo 2: A solid white line is visible defining the right edge of the travel lanes,
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane,
                        indicating a stop line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center line, right boundary is
                        an edge line). | roles: the yellow solid line on the left fits the role of a center
                        line, and the white solid line on the right fits the role of an edge line. | markings:
                        the stop line is present and is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid yellow
                        center line, which discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        edge line, and there is no rule prohibiting crossing it in the visible stretch.
Step 6  go_straight     allowed (correct): allowed: There are no lane-use arrows or prohibitions in the lane,
                        and the boundaries do not govern this action.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no lane-use arrows
                        or prohibitions in the lane, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no lane-use arrows
                        or prohibitions in the lane, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no lane-use arrows
                        or prohibitions in the lane, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting to turn left or
                          a two-way left-turn lane directly to the left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you must stop at the solid white stop line ahead. You
                        may proceed straight or change right, but changing left is prohibited by the solid
                        yellow center line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 999, 7.8 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues straight, and there is a crosswalk visible in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the left of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible immediately to the right of my car. Further
                        ahead, this line continues as a broken yellow line. Photo 2: A broken yellow line is
                        visible immediately to the right of my car. Further ahead, this line continues as a
                        broken yellow line.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: A solid yellow line is visible immediately to the
                        right of my car, adjacent to the broken yellow line. This line is part of the boundary
                        description but is also a marking.; area:grid (full): Photo 2: A set of yellow hatched
                        markings (crosshatching) are visible in the road ahead, spanning across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left. The left boundary is a lane_line (white solid), and the right
                        boundary is a center_line (yellow dashed). This is consistent. | roles: The left
                        boundary is a white solid lane_line, which fits the role. The right boundary is a
                        yellow dashed center_line, which fits the role. | markings: The solid yellow line
                        observed in Photo 2 is part of the right boundary description (center_line), but the
                        markings list includes a 'line:stop_yield' based on the visual evidence of the solid
                        yellow line near the right boundary. The grid marking is clearly visible in Photo 2.
                        The markings are consistent with the boundaries and each other. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The broken yellow line indicates a permissive condition for crossing
                        the center line markings. [[US-3B.01-04]]
Step 5  Rule            line:stop_yield: The yield line indicates the point at which the yield is intended or
                        required to be made. [[US-3B.19-10]]
Step 5  Rule            area:grid: The grid marking indicates that vehicles must not block the intersection
                        area. [[US-3B.26-01]]
Step 6  change_left     allowed (contested, correct): Allowed because the left boundary is a solid white
                        lane_line, and the rule [US-3B.06-05-06] only discourages crossing, not prohibits it.
Step 6  change_right    prohibited (contested, correct): Prohibited because the right boundary is a yellow
                        dashed center_line, and the rule [US-3B.01-04] indicates a permissive condition for
                        crossing, but the presence of the grid marking [US-3B.26-01] suggests a restriction
                        near the intersection.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed against a rule from step 5.
Advice                  You are in the middle lane, which allows you to proceed straight. Do not change right
                        due to the intersection grid marking, and you should yield before proceeding due to
                        the yield line marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 1221, 9.33 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is a
                        section of the road continuing straight, with other vehicles and a bus visible in the
                        distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car. Photo 2 shows a broken yellow line
                        next to my car. Further ahead, Photo 1 shows a broken yellow line continuing.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white for lane_line, dashed yellow for center_line). | markings: the stop line
                        marking agrees with the boundaries (it is located in my lane). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The broken yellow line indicates a permissive condition for crossing
                        the center line markings. [[US-3B.01-04]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white lane line on the
                        left, which discourages crossing.
Step 6  change_right    allowed (correct): allowed because the broken yellow center line on the right
                        indicates a permissive condition for crossing.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because the stop line in my lane
                        requires a stop before proceeding.
Step 6  turn_left       stop_first: stop_first because the stop line in my lane requires a stop before
                        proceeding.
Step 6  turn_right      stop_first: stop_first because the stop line in my lane requires a stop before
                        proceeding.
Step 6  u_turn          stop_first: stop_first because the stop line in my lane requires a stop before
                        proceeding.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         consistent
Advice                  You must stop behind the stop line before proceeding in any direction. You may change
                        lanes to the right, but changing left is discouraged. Use the right lane for turning
                        or proceeding straight if necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 9487, out 1023, 7.26 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a bus and other vehicles, suggesting
                        continued travel on the road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car. Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car. Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane,
                        indicating the boundary of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (white dashed lines on both sides indicate lane
                        separation). | roles: the white dashed lines fit the role of lane_line. | markings:
                        the partial visibility of the line:stop_line in Photo 2 is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (correct): allowed because there are no markings in the lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in the lane governing a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in the lane governing a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in the lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight. Since there is a
                        stop line visible, you must stop before it if required by a traffic control device.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 9487, out 908, 10.11 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. Ahead, the
                        road continues into a more complex area with multiple lanes and potential
                        intersections/merges. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car. Further ahead, the dashed white line continues. Further
                        ahead, there is a solid white line marking the edge of the roadway on the far left.
                        Photo 2 shows the dashed white line next to the car and the solid white line further
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed yellow line is visible next to the car. Photo 2: A dashed yellow
                        line is visible next to the car. Further ahead, the dashed yellow line continues,
                        transitioning to a solid yellow line further ahead. Photo 2 shows the dashed yellow
                        line next to the car and the solid yellow line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A dashed white line is visible across the lane,
                        indicating a lane boundary. This is the lane line.; line:stop_line (partial): Photo 2:
                        A dashed white line is visible across the lane, indicating a lane boundary. This is
                        the lane line.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane). The left boundary is a lane line (white dashed), and the
                        right boundary is a center line (yellow dashed/solid), which is consistent with my
                        lane being the middle lane. | roles: The left boundary is a white dashed lane line,
                        consistent with separating traffic in the same direction. The right boundary is a
                        yellow dashed/solid line, consistent with a center line separating traffic in opposite
                        directions. | markings: The markings observed are dashed white lines, which are
                        consistent with lane lines, but the interpretation of 'line:stop_line' based on the
                        visual evidence of a dashed line is questionable; however, the markings listed are
                        based on the visual presence of lines across the lane. | unseen: No attributes were
                        reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        white lane line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed yellow center line,
                        and [US-3B.01-01] defines the yellow line as delineating separation of opposite
                        directions, which does not prohibit changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition from step 5.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you should proceed with caution regarding potential
                        intersections ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1233, 9.09 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic is
                        moving across a crosswalk. My car is in one of the lanes near the bottom of the photo.
                        (lanes 3, mine 2, full)
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
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes of
                        the same direction) | roles: the white dashed lines fit the role of lane_line |
                        markings: no markings were observed in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed: allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed: allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit it, and the boundaries do not govern this action.
Step 6  turn_left       allowed: allowed because there are no markings in my lane to prohibit it, and the
                        boundaries do not govern this action.
Step 6  turn_right      allowed: allowed because there are no markings in my lane to prohibit it, and the
                        boundaries do not govern this action.
Step 6  u_turn          allowed: allowed because there are no markings in my lane to prohibit it, and the
                        boundaries do not govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and all movements (straight, left, right,
                        U-turn) are permitted. Proceed with caution as you approach the intersection and
                        crosswalk.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 9487, out 839, 9.47 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely an arterial road or highway approach, with traffic
                        moving away from the camera. Ahead, there is a structure or intersection visible in
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible to the left of my lane, separating traffic in
                        opposite directions. Photo 2: A solid yellow line is visible to the left of my lane,
                        separating traffic in opposite directions.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible to the right of my lane, separating traffic
                        flows in the same direction. Photo 2: A solid white line is visible to the right of my
                        lane, separating traffic flows in the same direction.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No specific lane markings (arrows, text, symbols,
                        areas, or lines like stop/yield) are visible within my lane in either Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for lane_line) | markings: no markings were
                        reported, so they agree with each other and boundaries | unseen: no attributes were
                        reported that were not actually seen | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow center_line, and
                        the rule [US-3A.04-01] states that a solid line discourages or prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white lane_line, and
                        the rule [US-3B.06-05-06] states that a solid white lane line discourages crossing.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, as there is no arrow or prohibited-
                        movement marking in my lane.
Step 6  turn_right      not_applicable: No marking governs this action, as there is no arrow or prohibited-
                        movement marking in my lane.
Step 6  u_turn          not_applicable: No marking governs this action, as there is no arrow or prohibited-
                        movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: No marking governs this action, as there is no left-turn waiting
                          area or two-way left-turn lane visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed although a rule prohibits it, nor is any action decided without a
                        governing feature.
Advice                  You are in the center lane of three lanes; you should stay in this lane to proceed
                        straight. Lane changes to the left or right are prohibited by the solid lane lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1029, 7.7 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance with traffic moving in both directions. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, the solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to the car.
                        Further ahead, the solid yellow line continues.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        area:grid (full): Photo 2: Yellow markings resembling a 'Y' shape are visible on the
                        road ahead, indicating an intersection or merge area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left. The left boundary is a lane line (white) and the right boundary is
                        a center line (yellow), which is consistent with my lane being the middle lane. |
                        roles: The left boundary is a solid white lane line, and the right boundary is a solid
                        yellow center line, which fits their roles. | markings: The 'Y' shaped markings in
                        Photo 2 are consistent with the road ahead shown in Photo 1, and they are located
                        within my lane. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid yellow line on a two-way roadway indicates a two-direction
                        no-passing zone, meaning crossing the center line markings for passing is prohibited
                        for traffic traveling adjacent to the solid line. [[US-3B.01-06]]
Step 5  Rule            area:grid: The grid markings indicate an area that vehicles must not block.
                        [[US-3B.26-01]]
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        prohibited. [[US-3B.06-12]]
Step 5  Rule            right_boundary: The solid yellow line on a two-way roadway indicates a two-direction
                        no-passing zone, meaning crossing the center line markings for passing is prohibited
                        for traffic traveling adjacent to the solid line. [[US-3B.01-06]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white lane line on the left,
                        as crossing the lane line markings is discouraged/prohibited [US-3B.06-05-06] /
                        [US-3B.06-12].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid yellow center line on the
                        right, as crossing the center line markings for passing is prohibited [US-3B.01-06].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable as there are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not applicable as there are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not applicable as there are no markings in my lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable as there are no markings in my lane governing entry
                          into a waiting area.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed against a rule from step 5.
Advice                  You should remain in your current lane to proceed straight through the intersection
                        area marked by the grid. Lane changes are prohibited by the solid lines on both sides
                        of your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 1109, 9.18 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with a barrier on the right side. Ahead,
                        the road continues straight, and there are other vehicles in the lanes. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A broken white line is visible next to my car. Further ahead, the broken
                        white line continues. Photo 2: A broken white line is visible next to my car. Further
                        ahead, the broken white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car, adjacent to a concrete barrier.
                        Further ahead, the solid white line continues along the barrier. Photo 2: A solid
                        white line is visible next to my car, adjacent to a concrete barrier. Further ahead,
                        the solid white line continues along the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: Two parallel yellow dashed lines are visible in my
                        lane, indicating lane separation. These lines are centered in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed line for lane_line, white solid line for edge_line). | markings: the
                        yellow dashed lines are interpreted as a yield line based on the visual evidence and
                        the provided marking list, although they are not in a standard triangle shape. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a broken
                        white lane_line, and [US-3B.06-05-06] permits crossing when not discouraged or
                        prohibited.
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a solid
                        white edge_line, and [US-3A.03-03-04] permits delineation of the right-hand edge of
                        the roadway.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Be aware of
                        the yield line markings ahead, which require you to yield to traffic if necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_right allowed across a curb',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 1066, 8.59 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides, and traffic is moving forward.
                        There is no immediate intersection or ramp visible ahead, but the road continues
                        straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index: 2). The left boundary is a lane_line (white
                        dashed) separating my lane from the lane on the left, and the right boundary is a
                        center_line (yellow solid) separating my lane from the lane on the right. This is
                        consistent. | roles: The left boundary is a white dashed lane_line, which fits the
                        role of separating traffic flows in the same direction [US-3B.06-05-06]. The right
                        boundary is a solid yellow center_line, which fits the role of delineating separation
                        of traffic traveling in opposite directions [US-3B.01-01]. | markings: The white arrow
                        in my lane indicates a mandatory movement, which is consistent with the lane markings.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions. [[US-3B.01-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a white dashed lane_line,
                        and [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): The right boundary is a solid yellow center_line, and [US-3B.01-01]
                        delineates the separation of traffic traveling in opposite directions, which does not
                        prohibit a lane change if the line is not double solid.
Step 6  go_straight     allowed (correct): The white arrow in my lane indicates a mandatory movement that
                        includes going straight, as per [US-3B.23-01].
Step 6  turn_left       not_applicable (WRONG, label prohibited): The white arrow in my lane does not show a
                        left turn, and there is no left-turn waiting area or two-way left-turn lane, so it is
                        not applicable.
Step 6  turn_right      not_applicable (WRONG, label prohibited): The white arrow in my lane does not show a
                        right turn, and there is no right-turn waiting area or two-way left-turn lane, so it
                        is not applicable.
Step 6  u_turn          not_applicable (WRONG, label prohibited): The white arrow in my lane does not show a
                        U-turn, and there is no U-turn lane-use arrow marking, so it is not applicable.
Step 6  enter_waiting_areanot_applicable: There is no marked area for waiting to turn left, so it is not
                          applicable.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You are in the middle lane, which is permitted to go straight. You may change left or
                        right as the lane markings allow, but you should proceed straight if you intend to
                        continue in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1217, 10.84 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is
                        an overpass/bridge structure, suggesting the road continues forward through an urban
                        area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the left of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible immediately to the right of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the right of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A large white arrow pointing straight ahead is visible
                        on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate separation
                        of lanes traveling in the same direction). | roles: The solid white lines on both
                        sides fit the role of lane_line separating traffic flows in the same direction. |
                        markings: The single straight arrow in my lane is consistent with the lane boundaries.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line (Note: This
                        rule suggests broken, but the observed line is solid, which is permitted if crossing
                        is discouraged or prohibited, or if it is an edge line, but here it functions as a
                        lane line). [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line
                        (Note: This rule suggests broken, but the observed line is solid, which is permitted
                        if crossing is discouraged or prohibited, or if it is an edge line, but here it
                        functions as a lane line). [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and a solid line discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane_line, and a solid line discourages or prohibits crossing [US-3A.04-01].
Step 6  go_straight     allowed (correct): allowed: The lane has a straight arrow, and nothing restricts
                        carrying on straight along my lane [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited: The lane has a straight arrow, and an arrow that
                        does not show turn_left prohibits it [US-3B.23-01].
Step 6  turn_right      prohibited (correct): prohibited: The lane has a straight arrow, and an arrow that
                        does not show turn_right prohibits it [US-3B.23-01].
Step 6  u_turn          prohibited (correct): prohibited: The lane has a straight arrow, and an arrow that
                        does not show u_turn prohibits it [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane or to its left.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1113, 8.34 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line. Photo 2: A white dashed line is visible next to my
                        car. Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line. Photo 2: A white dashed line is visible next to my
                        car. Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A white dashed line is visible across the lane
                        ahead, indicating a lane division. Photo 2: A white dashed line is visible across the
                        lane ahead, indicating a lane division.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the line
                        marking (line:stop_line) is consistent with the boundaries (dashed lines allow lane
                        changes, and the stop line is a feature across the lane). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight. You must stop at the
                        visible stop line ahead if a traffic control device requires it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 976, 7.46 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road continues into a built-up area, and
                        there is no immediate intersection or ramp visible in the close-up. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid yellow line is visible near the left edge of the road. Photo 2: A
                        solid yellow line is visible near the left edge of the road.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible near the right edge of the road. Photo 2: A
                        solid white line is visible near the right edge of the road.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane,
                        indicating a stop line.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a center line (yellow), and
                        the right boundary is an edge line (white). | roles: The yellow line on the left fits
                        the role of a center line, and the white line on the right fits the role of an edge
                        line. | markings: The stop line is located within the lane and is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Yellow markings delineate the separation of traffic traveling in
                        opposite directions or the left-hand edge of roadways. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or other traffic control device that requires
                        vehicles to stop. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid yellow
                        center line, which discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge line, and no rule
                        prohibits changing right onto the shoulder/adjacent area.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking in the
                        lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by visible features or lack thereof.
Advice                  You must stop behind the solid white stop line before proceeding. You may proceed
                        straight or change right, but changing left is prohibited by the solid yellow center
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 943, 7.15 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        My car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white dashed line across the road ahead, which
                        appears to be a crosswalk.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane lines separating lanes of
                        the same direction) | roles: the color and pattern of each boundary fit the role given
                        to it (white dashed lines are lane lines) | markings: the crosswalk marking agrees
                        with the boundaries (it is across the lane) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: No specific rule passage was found that dictates the action based on
                        the presence of a crosswalk line.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed lane
                        line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and [US-3B.06-05-06] permits crossing with care.
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
Advice                  You may change lanes left or right, and you may proceed straight through the
                        intersection. Be aware of the crosswalk ahead and proceed with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 921, 7.56 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. Ahead,
                        there is a road intersection visible in the distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane,
                        indicating a lane division.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: the partial visibility of the stop
                        line marking is consistent with the lane markings observed. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
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
Advice                  You may change lanes left or right as the lane markings are broken. You may proceed
                        straight through the intersection, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 9487, out 942, 7.34 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection or a point where the
                        road continues with lane markings indicating movement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car, and Photo 2 shows a white solid line
                        next to my car. Photo 1 shows a white solid line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows white arrows pointing straight ahead in my lane,
                        and white arrows pointing straight ahead in the lane to my left. Photo 1 shows white
                        arrows pointing straight ahead in my lane, and white arrows pointing straight ahead in
                        the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on the left and a lane
                        line on the right. | roles: The left boundary is a white dashed lane line, and the
                        right boundary is a white solid lane line, which fits the role of lane_line. |
                        markings: The arrows in my lane show straight movement, which is consistent with the
                        lane boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a white dashed
                        lane line, and [US-3B.06-05-06] implies that while crossing is not discouraged, the
                        presence of a lane line generally governs lane changes, and the arrow in my lane only
                        permits straight movement.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white solid lane
                        line, and [US-3B.06-05-06] indicates that crossing is discouraged, but the arrow in my
                        lane only permits straight movement, so the boundary does not prohibit the change.
Step 6  go_straight     allowed (contested, correct): allowed: The lane-use arrow in my lane shows straight
                        ahead, and [US-3B.23-01] indicates that lane-use arrow markings indicate permissible
                        movements.
Step 6  turn_left       prohibited: prohibited: The lane-use arrow in my lane does not show a left turn, and
                        [US-3B.23-01] indicates that lane-use arrow markings indicate mandatory or permissible
                        movements.
Step 6  turn_right      prohibited: prohibited: The lane-use arrow in my lane does not show a right turn, and
                        [US-3B.23-01] indicates that lane-use arrow markings indicate mandatory or permissible
                        movements.
Step 6  u_turn          prohibited: prohibited: The lane-use arrow in my lane does not show a U-turn, and
                        [US-3B.23-01] indicates that lane-use arrow markings indicate mandatory or permissible
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to go straight, as the lane markings only permit
                        straight movement. While the right boundary is a solid line, the arrow restricts you
                        to straight movement, so changing right is not advisable for turning. No specific
                        stopping area is marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe ['change_right'],
                        citation in_pack_not_accepted, contradictions ['change_left prohibited across a broken
                        lane line']
Tokens                  in 9487, out 1294, 9.36 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test C | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. Ahead, the
                        road continues straight, and there is a visible white arrow indicating straight
                        movement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines indicate separation of traffic
                        flows in the same direction). | roles: the white dashed lines fit the role of
                        lane_line as they separate traffic flows in the same direction. | markings: the white
                        arrow pointing straight ahead is consistent with the lane markings. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        the arrow in the lane does not permit a change left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and the arrow in the lane does not prohibit a change right.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and no
                        marking prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is designated for straight movement. You may change
                        right, but you must stay in the lane to go straight. No specific stopping or waiting
                        areas are marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line']
Tokens                  in 9487, out 931, 7.27 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road continues
                        and turns are possible. My car is in one of the lanes near the bottom of the photo.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate
                        separation of same-direction traffic flows). | roles: the white dashed lines on both
                        sides fit the role of lane_line. | markings: the white arrow pointing straight ahead
                        is consistent with the lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane_line, and
                        the rule [US-3B.06-05-06] allows crossing, but the arrow only permits straight
                        movement.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a white dashed lane_line, and
                        the rule [US-3B.06-05-06] allows crossing, but the arrow only permits straight
                        movement.
Step 6  go_straight     allowed (correct): allowed: The lane has a white arrow pointing straight ahead, and
                        the boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a left turn.
Step 6  turn_right      prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane has a white arrow pointing straight ahead,
                        and the arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane to proceed straight through the intersection. Lane
                        changes are prohibited by the lane-use arrow marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left prohibited across a broken lane line', 'change_right prohibited across a
                        broken lane line']
Tokens                  in 9487, out 953, 7.57 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street lined with buildings, and the road continues straight ahead
                        into the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line near the car, and Photo 2 shows a solid yellow line
                        near the car. Further ahead, Photo 1 shows the solid yellow line continuing, and Photo
                        2 shows the solid yellow line continuing.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows the solid white line continuing, and Photo
                        2 shows the solid white line continuing.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a solid white line marking the right edge of
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is center_line, right boundary is
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for edge_line) | markings: the markings
                        (line:stop_yield) agree with the boundaries (solid white edge line) | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow center line,
                        which prohibits crossing.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge line, and no rule
                        prohibits changing right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no lane-use arrows or prohibitions in
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in the lane for
                        turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in the lane for
                        turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in the lane for
                        making a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but you must yield before entering the
                        intersection as indicated by the yield line. Do not change left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 9487, out 907, 7.24 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection visible in
                        the distance. My car is in the rightmost lane visible in the direction of travel.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color (white) and pattern (dashed) of both boundaries fit
                        their roles as lane_line and edge_line | markings: no markings were reported, so there
                        is no agreement to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway, although the
                        observed line is dashed. [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway, although the
                        observed line is dashed. [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing when not discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        white edge_line, and [US-3B.09-01-02] describes the edge line, but no rule prohibits
                        changing into the adjacent area.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit it, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          this action.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which allows you to go straight or change left or
                        right. Since there are no specific markings for turns, you should proceed with caution
                        based on traffic conditions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9487, out 1011, 8.13 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection with a crosswalk and
                        traffic signals. My car is in one of the lanes near the bottom of the photo. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to my car. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1: A white dashed line marking is visible across the lane
                        ahead, forming a crosswalk. Photo 2: A white dashed line marking is visible across the
                        lane ahead, forming a crosswalk.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        crosswalk marking is consistent with the lane markings and boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: No specific rule passage was found that dictates the action based on
                        the presence of a crosswalk marking.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and [US-3B.06-05-06] permits crossing the lane line markings when not
                        discouraged or prohibited.
Step 6  go_straight     allowed (correct): allowed: There are no arrows or prohibited-movement markings in my
                        lane to restrict going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern turning movements.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern turning movements.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane to govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn arrows or waiting areas marked, turning left, turning right, or
                        making a U-turn is not governed by lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['change_left', 'change_right'], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 9487, out 979, 8.01 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues straight, and there is a large truck in the center of the visible lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, the solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to the car.
                        Further ahead, the solid yellow line continues.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white solid for lane_line, yellow solid for center_line) | markings: there are no
                        markings in my lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on undivided two-way roadways with four or
                        more lanes for moving motor vehicle traffic always available shall be the two-
                        direction no-passing zone markings consisting of normal width double solid yellow
                        lines, although here only a single solid yellow line is visible. [[US-3B.01-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a solid white
                        lane_line, and the rule [US-3B.06-05-06] only discourages crossing, not prohibits it.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid yellow center_line,
                        and the rule [US-3B.01-06] implies a restriction on crossing the center line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. Lane changes to the
                        left are discouraged, and changing to the right is prohibited by the solid yellow
                        center line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9487, out 859, 5.97 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major thoroughfare, and the road
                        continues straight ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line near the car, and a solid white line further ahead.
                        Photo 2 shows a solid white line near the car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the car, and a solid white line further ahead.
                        Photo 2 shows a solid white line near the car, and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left_boundary is a lane_line, right_boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        prohibited. [[US-3B.06-12]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left, as
                        crossing is discouraged/prohibited by [US-3B.06-05-06] and [US-3B.06-12].
Step 6  change_right    allowed (WRONG, label prohibited): allowed as there is no marking governing this
                        action.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting movement
                        straight ahead.
Step 6  turn_left       not_applicable: not_applicable as there are no markings governing this action.
Step 6  turn_right      not_applicable: not_applicable as there are no markings governing this action.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings governing this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may proceed straight or change right,
                        but changing left is prohibited by the solid white line. No specific stopping or
                        waiting areas are marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 9487, out 840, 6.34 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with surrounding buildings, and the road continues ahead
                        into the distance. There are at least three lanes visible in my direction near the
                        bottom of the photo. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A white line is visible to the left of my car, separating my lane from the
                        adjacent lane. Photo 2: A white line is visible immediately to the left of my car, and
                        another white line is visible further ahead, separating my lane from the adjacent
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white line is visible to the right of my car, separating my lane from the
                        adjacent lane. Photo 2: A white line is visible immediately to the right of my car,
                        and another white line is visible further ahead, separating my lane from the adjacent
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2: A red painted area with a white bicycle symbol is
                        visible in the right portion of my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles | roles: the color and pattern of each boundary fit the
                        role you gave it | markings: the arrows, words and areas in my lane agree with each
                        other and with the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: Where crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            area:channelizing: Chevron or diagonal markings are used to discourage travel on
                        certain paved areas, such as shoulders, neutral areas, and flush median islands.
                        [[US-3B.25-01]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, and
                        [US-3B.06-05-06] permits crossing the lane line markings when not discouraged or
                        prohibited.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a dashed white lane line, but
                        the presence of the red bicycle area suggests a restriction, and the general rule for
                        lane lines does not explicitly permit entering a dedicated bicycle area.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is marked as a bicycle lane area ahead. You may
                        change left, but changing right into the bicycle area is prohibited. You may proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_right prohibited across a broken lane line']
Tokens                  in 9487, out 959, 7.11 s
```
