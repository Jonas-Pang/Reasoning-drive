# Reasoning of lane run 20261117_234328_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a dashed white line marking the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a lane_line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane_line, and the right boundary is a solid
                        yellow lane_line, which fits the roles. | markings: The stop line marking is
                        consistent with the boundaries and does not contradict any other markings. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates that my car must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  go_straight     stop_first (contested, label allowed): allowed, as there are no arrows or prohibitions
                        in my lane, but it is governed by the line:stop_line which requires stopping first.
Step 6  turn_left       prohibited: prohibited, as there are no arrows or prohibitions in my lane, and no
                        left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      prohibited: prohibited, as there are no arrows or prohibitions in my lane, and no
                        right-turn arrow is visible.
Step 6  u_turn          prohibited: prohibited, as there are no arrows or prohibitions in my lane, and no
                        U-turn arrow is visible.
Step 6  enter_waiting_areaprohibited: prohibited, as there is no left-turn waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before the stop line. You are restricted to
                        proceeding straight ahead from your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1071, 7.06 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible further ahead. Photo 2: A broken yellow line
                        is visible further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A solid white line is visible at the end of the
                        visible road segment ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to
                        it. | markings: the stop line marking is consistent with the boundaries and general
                        road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of the lane and prohibits
                        crossing it to enter an adjacent lane.
Step 5  Rule            right_boundary: The broken yellow line indicates a lane division that permits crossing
                        into the adjacent lane when safe.
Step 5  Rule            line:stop_line: The stop line indicates that vehicles must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line on the left
                        boundary.
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken yellow center_line on the
                        right boundary.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no markings governing turning movements.
Step 6  turn_right      not_applicable: not_applicable as there are no markings governing turning movements.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change right if safe, or proceed straight. You
                        must stop before the visible stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 917, 6.27 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        major road ahead. There are at least two lanes visible in my direction near the bottom
                        of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary on
                        the right side, which is the right boundary of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of both boundaries (white dashed) fit the
                        role of a lane_line. | markings: the stop line marking is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white dashed line on the left allows for lane changes into the
                        adjacent lane.
Step 5  Rule            right_boundary: The white dashed line on the right allows for lane changes into the
                        adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection or stopping.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane and can change left or right, and you are permitted to go
                        straight. You must stop at the visible stop line before proceeding through the
                        intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 1010, 6.54 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues straight under
                        an overpass structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: there are no markings to check for
                        agreement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows for lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to allow or prohibit
                        turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to allow or prohibit
                        turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to allow or prohibit
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to change lanes in either
                        direction, go straight, or remain in your lane. No specific turning movements are
                        indicated or prohibited by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3793, out 937, 6.19 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with an elevated structure (likely a bridge
                        or overpass) ahead. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is one of several lanes). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the lane
                        markings list is empty, which is consistent with the boundaries being lane lines and
                        no arrows/text being visible. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted where the
                        line is visible.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted where
                        the line is visible.
Step 5  Rule            no_turn:right: This marking prohibits the movement indicated (though no specific
                        movement is shown, the general rule for a prohibited movement applies).
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and the rule allows lane changes where the line is visible.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the rule
                        allows lane changes where the line is visible.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited markings in my lane
                        to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited markings in my lane
                        to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited markings in my lane
                        to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to change lanes in either
                        direction, and you may proceed straight ahead. No specific lane usage is mandated by
                        the markings visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3793, out 1029, 7.06 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road continues straight, and there are no
                        immediate intersections or ramps visible in the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: the solid white lines on both sides fit the role of lane_line. |
                        markings: the stop line marking is consistent with the lane boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to enter an adjacent lane.
Step 5  Rule            right_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to enter an adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates the point where my car must come to a complete
                        stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane ahead.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides, and you must stop at the visible
                        stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 964, 6.37 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a bridge or overpass
                        structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line to the right of my car, and Photo 2 shows a broken
                        yellow line to the right of my car. Further ahead, Photo 1 shows a broken yellow line
                        continuing, and Photo 2 shows a broken yellow line continuing.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane line on left, yellow dashed line for lane line on right). |
                        markings: the arrow in my lane agrees with the boundaries (it allows straight
                        movement, and the boundaries allow lane changes if the lines permit). | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed yellow lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (element_rules for left_boundary).
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed yellow lane line on the
                        right (element_rules for right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed by the white arrow pointing straight ahead in
                        the lane (element_rules for arrow:straight).
Step 6  turn_left       prohibited: prohibited because the lane marking (arrow:straight) does not show a left
                        turn.
Step 6  turn_right      prohibited: prohibited because the lane marking (arrow:straight) does not show a right
                        turn.
Step 6  u_turn          prohibited: prohibited because the lane marking (arrow:straight) does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight ahead. You may change right,
                        but changing left is prohibited by the solid white line. No specific stopping or
                        waiting areas are marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1017, 6.65 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and ahead there is a continuation of the
                        road with traffic moving in the same direction. My car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        a lane between other lanes). | roles: the color and pattern of both boundaries (white
                        dashed lines) fit the role of lane_line. | markings: the lane markings list is empty
                        except for a placeholder, and there are no contradictions with the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes between lanes of the same
                        direction.
Step 5  Rule            right_boundary: A broken white line allows for lane changes between lanes of the same
                        direction.
Step 5  Rule            line:stop_line: This marking indicates the stopping point for the vehicle.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You are permitted to change lanes in either
                        direction, and you may proceed straight ahead. No specific lane is required for your
                        intended movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 984, 6.79 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues, possibly
                        leading to an interchange or another section of the highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car, and further ahead, it is a broken
                        yellow line. Photo 2 shows a broken yellow line next to my car, and further ahead, it
                        is a broken yellow line.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane line on left, yellow dashed line for lane line on right). |
                        markings: the arrow in my lane agrees with the boundaries (it governs movement within
                        the lane defined by the boundaries). | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A broken yellow lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left
                        (Rule: A solid white lane line prohibits crossing it to change lanes).
Step 6  change_right    allowed (correct): allowed by the broken yellow lane line on the right (Rule: A broken
                        yellow lane line permits crossing it to change lanes).
Step 6  go_straight     allowed (contested, correct): allowed by the white arrow pointing straight ahead in
                        the lane (Rule: The arrow indicates that proceeding straight ahead is permitted in
                        this lane).
Step 6  turn_left       prohibited: prohibited by the white arrow pointing straight ahead in the lane (Rule:
                        The arrow indicates that proceeding straight ahead is permitted in this lane).
Step 6  turn_right      prohibited: prohibited by the white arrow pointing straight ahead in the lane (Rule:
                        The arrow indicates that proceeding straight ahead is permitted in this lane).
Step 6  u_turn          prohibited: prohibited by the white arrow pointing straight ahead in the lane (Rule:
                        The arrow indicates that proceeding straight ahead is permitted in this lane).
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane and are permitted to go straight or change right. Lane
                        changes to the left are prohibited by the solid white line. Use the right lane if you
                        wish to change right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 1062, 6.92 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, this line
                        appears to continue as a solid white line. Photo 2: A solid white line is visible next
                        to the car. Further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible next to the car. Further ahead, this line
                        appears to continue as a broken yellow line. Photo 2: A broken yellow line is visible
                        next to the car. Further ahead, this line continues as a broken yellow line.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white painted arrow pointing straight ahead is
                        visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane line, and the right boundary is a
                        dashed yellow lane line, which fits the role of lane lines. | markings: The white
                        arrow pointing straight ahead is consistent with the lane boundaries and does not
                        contradict any other markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The broken yellow line permits changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line,
                        as per the rule for solid lane lines.
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken yellow right boundary
                        line, as per the rule for broken lane lines.
Step 6  go_straight     allowed (contested, correct): allowed by the white arrow indicating straight movement,
                        as per the rule for lane-use arrows.
Step 6  turn_left       prohibited: prohibited by the white arrow indicating straight movement, as per the
                        rule for lane-use arrows.
Step 6  turn_right      prohibited: prohibited by the white arrow indicating straight movement, as per the
                        rule for lane-use arrows.
Step 6  u_turn          prohibited: prohibited by the white arrow indicating straight movement, as per the
                        rule for lane-use arrows.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are currently in the middle lane. You may proceed straight ahead, or you may
                        change lanes to the right. Changing lanes to the left is prohibited. No specific
                        stopping area is marked for you.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1059, 6.13 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in
                        road configuration. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this line
                        appears to continue as a solid white line. Photo 2: A solid white line is visible next
                        to my car. Further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken white line is visible next to my car. Further ahead, this line
                        appears to continue as a broken white line. Photo 2: A broken white line is visible
                        next to my car. Further ahead, this line continues as a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane). The left boundary is a lane line, and the right boundary is
                        a lane line, which is consistent with my lane being the middle lane. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the role of lane lines. | markings: The arrow in my lane points
                        straight ahead, which is consistent with the lane markings. | unseen: No unseen
                        attributes were reported. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow in my lane permits movement straight ahead.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left boundary.
Step 6  change_right    allowed (correct): allowed by the dashed white lane line on the right boundary.
Step 6  go_straight     allowed (contested, correct): allowed by the white arrow pointing straight ahead in my
                        lane.
Step 6  turn_left       prohibited: prohibited by the white arrow pointing straight ahead in my lane.
Step 6  turn_right      prohibited: prohibited by the white arrow pointing straight ahead in my lane.
Step 6  u_turn          prohibited: prohibited by the white arrow pointing straight ahead in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, which is currently marked to proceed straight ahead. You
                        may change to the right, but changing to the left is prohibited. You should proceed
                        straight ahead if you intend to continue on this road.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 1014, 6.67 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight,
                        possibly leading to an interchange or another section of the highway. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 2: A solid yellow line is visible in the lane, extending
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The color and pattern of both boundaries (solid white lines) fit
                        the role of a lane_line. | markings: The solid yellow line (line:stop_yield) is
                        present in the lane and is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left indicates the boundary of the lane and
                        prohibits crossing it to enter another lane.
Step 5  Rule            right_boundary: The solid white line on the right indicates the boundary of the lane
                        and prohibits crossing it to enter another lane.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the car to come to a
                        full stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane_line on the left
                        (element_rules for left_boundary).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane_line on the right
                        (element_rules for right_boundary).
Step 6  go_straight     stop_first (contested, label allowed): allowed because there are no markings
                        prohibiting straight movement in the lane, although the stop-and-yield line requires
                        stopping first (element_rules for line:stop_yield).
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn in the lane.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn in the lane.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and all prohibitions are governed by visible features.
Advice                  You must come to a full stop before proceeding straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1041, 7.07 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a bridge structure leading to what
                        appears to be a continuation of the road, possibly an intersection or another section
                        of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid white
                        line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car. Photo 1 shows a dashed white line further ahead. Photo 2 shows a
                        dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary on
                        the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane). The left boundary is a lane line, and the right boundary is
                        a lane line, which is consistent with my lane being the middle lane. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the role of lane_line. | markings: The stop line is located in my
                        lane, which is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane on the
                        left.
Step 5  Rule            right_boundary: The dashed white line permits crossing into the adjacent lane on the
                        right.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed white lane line,
                        which permits changing right.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibitions in my lane, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        prohibit turning left.
Step 6  turn_right      allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        prohibit turning right.
Step 6  u_turn          allowed: There are no arrows or prohibitions in my lane, and the boundaries do not
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: There are no markings for a waiting area or two-way left-turn lane
                          in my lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane. You may proceed straight, turn left, or turn right. You
                        may change to the right lane, but changing to the left is prohibited by the solid
                        white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1053, 7.09 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        or a point where traffic flow changes, indicated by the road markings and signs.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (partial): Photo 1: A blue overhead sign with white arrows
                        pointing straight and up, and a white arrow pointing right, is visible ahead. Photo 2:
                        The overhead sign is not visible in the close-up.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane line (white dashed) and
                        the right boundary is a lane line (yellow solid), indicating my lane is one of two
                        lanes in my direction. | roles: The white dashed line on the left fits the role of a
                        lane_line, and the solid yellow line on the right fits the role of a lane_line. |
                        markings: The overhead sign shows arrows for going straight and turning right, which
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            right_boundary: The solid yellow line prohibits lane changes across it.
Step 5  Rule            arrow:straight_right: The arrow indicates that going straight and turning right are
                        permitted movements from this lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        which allows lane changes.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid yellow line, which
                        prohibits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking (arrow:straight_right) permits
                        going straight.
Step 6  turn_left       prohibited: prohibited: The lane marking (arrow:straight_right) does not show a left
                        turn.
Step 6  turn_right      allowed: allowed: The lane marking (arrow:straight_right) permits turning right.
Step 6  u_turn          prohibited: prohibited: The lane marking (arrow:straight_right) does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes. You are permitted to go straight or turn right,
                        and you may change lanes to the left. Lane changes to the right are prohibited by the
                        solid yellow line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe ['change_left'], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 1030, 7.28 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues straight, and
                        there are overhead signs indicating lane designations and speed limits. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1: Overhead sign above my lane reads '行车道 Through Lane' with
                        speed limits 100 and 80.; text:other (full): Photo 1: Overhead sign above my lane
                        reads '行车道 Through Lane' with speed limits 120 and 90.; text:other (full): Photo 1:
                        Overhead sign above my lane reads '行车道 Through Lane' with speed limits 100 and 60.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The boundaries are lane lines, which is consistent with my lane
                        being one of three lanes. | roles: The white dashed lines on both sides are consistent
                        with the role of a lane_line separating my lane from adjacent lanes. | markings: The
                        overhead signs are consistent with the lane markings, indicating through lanes with
                        speed limits. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes into the adjacent lane.
Step 5  Rule            text:other: The overhead signs indicating 'Through Lane' and speed limits do not
                        restrict movement other than by indicating the intended use of the lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You are permitted to change lanes
                        in either direction, and you may proceed straight ahead. Use the lane appropriate for
                        your intended movement, keeping in mind the posted speed limits on the overhead signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 1112, 7.97 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues straight, and
                        there are traffic signals visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within a flow of traffic). | roles: the white dashed lines on both sides fit the role
                        of lane_line. | markings: there are no markings to check against boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A broken white line indicates that lane changes are permitted when
                        safe.
Step 6  change_left     allowed (correct): allowed, because the left boundary is a white dashed line, which
                        permits lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed, because the right boundary is a white
                        dashed line, which permits lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to change lanes left or right,
                        and you may proceed straight ahead. No specific turn movements are indicated for this
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 915, 6.68 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where traffic
                        flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The straight arrow in my lane is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            arrow:straight: The straight arrow indicates that proceeding straight ahead is
                        permitted in this lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        which allows lane changes.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and no other
                        marking prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane marking only shows a straight arrow, which
                        prohibits turning left.
Step 6  turn_right      prohibited (correct): prohibited: The lane marking only shows a straight arrow, which
                        prohibits turning right.
Step 6  u_turn          prohibited (correct): prohibited: The lane marking only shows a straight arrow, which
                        prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, which permits you to go straight, change left, or change
                        right. You are prohibited from turning left, turning right, or making a U-turn from
                        this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 973, 6.93 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues straight, and there is no immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white dashed arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3). | roles: the color and pattern of each boundary fit the role
                        (white dashed/solid lines are lane_lines). | markings: the arrow in my lane agrees
                        with the boundaries (it allows straight movement, which is consistent with the lane
                        structure). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        which permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a white dashed arrow
                        pointing straight ahead, and no other marking prohibits it.
Step 6  turn_left       prohibited: prohibited: The lane marking only shows an arrow for straight ahead,
                        prohibiting turns.
Step 6  turn_right      prohibited: prohibited: The lane marking only shows an arrow for straight ahead,
                        prohibiting turns.
Step 6  u_turn          prohibited: prohibited: The lane marking only shows an arrow for straight ahead,
                        prohibiting U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to go straight, change left, or
                        change right. You should proceed straight ahead as indicated by the lane arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 974, 6.34 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major thoroughfare, and there is a set
                        of traffic lights and buildings ahead, suggesting an intersection or a continuation of
                        the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing to the right in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing to the left in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed/solid lines fit the role of
                        lane_line. | markings: The arrows (straight, right, left) are present in my lane and
                        are consistent with the boundaries. | unseen: No attributes were reported that were
                        not seen. | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            arrow:straight: This marking allows my car to proceed straight ahead.
Step 5  Rule            arrow:right: This marking allows my car to turn right.
Step 5  Rule            arrow:left: This marking allows my car to turn left.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, which
                        permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a white dashed line, which
                        permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking includes an arrow pointing
                        straight ahead.
Step 6  turn_left       allowed (WRONG, label prohibited): Allowed because the lane marking includes an arrow
                        pointing left.
Step 6  turn_right      allowed (WRONG, label prohibited): Allowed because the lane marking includes an arrow
                        pointing right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no specific
                        marking or boundary governing a U-turn, and the arrows shown do not explicitly
                        prohibit it.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in a lane that permits straight, left, and right turns, and you may change
                        lanes in either direction. You may proceed straight, turn left, or turn right at the
                        upcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe ['turn_left',
                        'turn_right'], citation None, contradictions []
Tokens                  in 3793, out 1150, 7.3 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road with lane
                        markings indicating movement options. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in the lane
                        to the left of my lane. Photo 2 shows a white arrow pointing straight ahead in my
                        lane. Photo 2 shows a white arrow pointing straight ahead in the lane to the right of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The arrows in my lane (straight ahead) agree with the
                        boundaries (dashed lines allow lane changes). | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes in either direction.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes in either direction.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking shows an arrow pointing straight
                        ahead.
Step 6  turn_left       prohibited (correct): Prohibited because there is no arrow or marking indicating a
                        left turn is allowed.
Step 6  turn_right      prohibited (correct): Prohibited because there is no arrow or marking indicating a
                        right turn is allowed.
Step 6  u_turn          prohibited (correct): Prohibited because there is no arrow or marking indicating a
                        U-turn is allowed.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and you are permitted to go straight, change left, or
                        change right. You should use this lane for straight travel, as it is marked for it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 1008, 7.07 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the color and pattern of both boundaries fit their assigned roles
                        (solid white lines). | markings: the arrow pointing straight ahead in my lane is
                        consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line marks the edge of the roadway and prohibits
                        driving beyond it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited by the left_boundary, which is a solid white
                        lane_line.
Step 6  change_right    prohibited (correct): prohibited by the right_boundary, which is a solid white
                        edge_line.
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking, which permits proceeding
                        straight ahead.
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        left turn.
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        right turn.
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 945, 6.77 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a major
                        road junction where traffic is moving forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Photo 2; arrow:merge_right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left. The left boundary is a lane line, and the right boundary is a lane
                        line, which is consistent with my lane being in the middle. | roles: The left boundary
                        is a solid white lane line, and the right boundary is a dashed white lane line, which
                        fits the roles of lane_line. | markings: The two_way_left_turn_lane area is to the
                        left of my lane, and the merge_right arrow is in my lane, which is consistent. |
                        unseen: No unseen attributes were reported. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line permits crossing into the adjacent lane.
Step 5  Rule            area:two_way_left_turn_lane: This area indicates a lane designated for two-way left
                        turns directly to the left of my lane.
Step 5  Rule            arrow:merge_right: This arrow indicates that traffic in this lane is permitted to
                        merge to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line, as per the
                        rule for solid lane lines.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white right boundary line, as
                        per the rule for dashed lane lines.
Step 6  go_straight     allowed (correct): allowed because the merge_right arrow does not prohibit going
                        straight.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited because the merge_right arrow does not
                        show a left turn.
Step 6  turn_right      prohibited (correct): prohibited because the merge_right arrow does not show a right
                        turn.
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited because the merge_right arrow does not
                        show a U-turn.
Step 6  enter_waiting_areaallowed: allowed because there is a two_way_left_turn_lane directly to the left of
                          my lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You may change right, go straight, or enter the left-turn waiting area. Changing left
                        is prohibited by the solid line, and all turning movements are prohibited by the merge
                        right arrow.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'arrow:merge_right'], missed ['arrow:straight_left']),
                        actions False, unsafe ['change_right'], citation None, contradictions ['turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3793, out 1109, 7.56 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching it. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows no markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the stop line marking is consistent with the boundaries and the general
                        road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A broken white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left boundary.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line on the right
                        boundary.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       allowed: allowed because there are no markings prohibiting left turn in my lane.
Step 6  turn_right      allowed: allowed because there are no markings prohibiting right turn in my lane.
Step 6  u_turn          allowed: allowed because there are no markings prohibiting U-turn in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You may change right, go straight, turn left, turn right, or U-turn. You must stop
                        before the stop line before proceeding through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 916, 6.93 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an underpass/overpass structure. Ahead,
                        there is a junction or area where lane movements are indicated. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead, separating the lane from the
                        adjacent lane. Photo 2: A solid white line is visible further ahead, separating the
                        lane from the adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A large yellow arrow pointing straight ahead is
                        visible in the lane.; arrow:right (full): Photo 2: A large yellow arrow pointing right
                        is visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The arrows (straight and right) are present in the lane and are consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the adjacent lane on the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the adjacent lane on the
                        right.
Step 5  Rule            arrow:straight: The arrow indicating straight movement allows the car to proceed
                        straight ahead.
Step 5  Rule            arrow:right: The arrow indicating a right turn allows the car to turn right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line and the rule
                        that a solid line prohibits lane changes.
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line and the rule
                        that a solid line prohibits lane changes.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the yellow arrow indicating straight
                        movement and the rule that the arrow allows the movement it shows.
Step 6  turn_left       prohibited (correct): prohibited because there is no arrow indicating a left turn in
                        the lane.
Step 6  turn_right      allowed (correct): allowed by the yellow arrow indicating a right turn and the rule
                        that the arrow allows the movement it shows.
Step 6  u_turn          prohibited (correct): prohibited because there is no arrow indicating a U-turn in the
                        lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You must stay in the middle lane to go straight or turn right. Lane changes are
                        prohibited by the solid white lines on both sides. Proceed with caution as you
                        approach the underpass.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation None,
                        contradictions []
Tokens                  in 3793, out 1091, 6.96 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where the road continues with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid/dashed lines are lane lines). | markings: the lane markings list is
                        empty, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: The broken white line permits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): allowed: The left boundary is a solid white line, which
                        prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which permits
                        changing right.
Step 6  go_straight     allowed (correct): allowed: No arrow or prohibited movement marking governs this
                        action.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed: No arrow or prohibited movement marking
                        governs this action.
Step 6  turn_right      prohibited (correct): prohibited: The marking 'no_turn:right' prohibits turning right.
Step 6  u_turn          allowed (WRONG, label prohibited): allowed: No arrow or prohibited movement marking
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change right, go straight, turn left, or make a
                        U-turn, but you are prohibited from turning right or changing left. Use the middle
                        lane for straight travel or left turns.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe ['turn_left',
                        'u_turn'], citation None, contradictions []
Tokens                  in 3793, out 944, 6.2 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white upward arrow in the lane.; arrow:straight
                        (full): Photo 2 shows a white upward arrow in the lane further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (3) agree with the boundary roles (both boundaries are lane lines). | roles: The white
                        dashed lines fit the role of lane_line. | markings: The straight arrows in the lane
                        agree with the boundaries (they are within the lane defined by the boundaries). |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and the rule
                        allows proceeding straight ahead.
Step 6  turn_left       prohibited (correct): prohibited: There are no markings indicating a permitted left
                        turn in this lane.
Step 6  turn_right      prohibited (correct): prohibited: There are no markings indicating a permitted right
                        turn in this lane.
Step 6  u_turn          prohibited (correct): prohibited: There are no markings indicating a permitted U-turn
                        in this lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which permits going straight ahead. Lane changes to the
                        left or right are permitted when safe due to the dashed lines. No specific markings
                        govern turning movements, so turning left, right, or U-turning is prohibited by the
                        lane markings shown.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 3793, out 1039, 7.05 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching a crossing area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to my right.; arrow:straight (full): Photo 2 shows a white arrow pointing
                        straight ahead in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines on both sides fit the
                        role of lane_line. | markings: The arrows in my lane (straight ahead) are consistent
                        with the lane boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed lane line allows for lane changes when safe.
Step 5  Rule            right_boundary: A dashed lane line allows for lane changes when safe.
Step 5  Rule            arrow:straight: The arrow in my lane permits movement straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed lane
                        line, which permits lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed lane
                        line, which permits lane changes when safe.
Step 6  go_straight     allowed (correct): Allowed because the lane marking in my lane is an arrow pointing
                        straight ahead.
Step 6  turn_left       prohibited (correct): Prohibited because the lane marking in my lane is an arrow
                        pointing straight ahead, and no left turn is shown.
Step 6  turn_right      prohibited (correct): Prohibited because the lane marking in my lane is an arrow
                        pointing straight ahead, and no right turn is shown.
Step 6  u_turn          prohibited (correct): Prohibited because the lane marking in my lane is an arrow
                        pointing straight ahead, and no U-turn is shown.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane ahead.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane and are permitted to go straight, change left, or change
                        right when safe. Do not attempt to turn left, turn right, or make a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3793, out 1096, 7.71 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with trees lining the sides. Ahead, there is a marked
                        intersection or a designated area for turning/stopping. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2: A large yellow hatched area covers the lane ahead,
                        indicating a stop/yield area. Photo 1: The yellow hatched area extends further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: The left boundary (white solid) fits the role of a lane_line, and
                        the right boundary (yellow solid) fits the role of a lane_line. | markings: The
                        area:grid marking is present and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes are prohibited
                        across this line.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes are prohibited
                        across this line.
Step 5  Rule            area:grid: The grid area indicates that the vehicle must stop or yield before
                        proceeding into the marked area.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left, as per the rule for solid lane lines.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane line on the
                        right, as per the rule for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no markings prohibiting straight
                        movement in the lane.
Step 6  turn_left       not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stop before entering the yellow hatched grid area ahead. You are restricted
                        to proceeding straight ahead in your current lane, as lane changes are prohibited by
                        solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 996, 6.89 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining the sides. Ahead, the road continues
                        into the distance, and there is a crosswalk visible further ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, this solid
                        white line continues. Photo 2: A solid white line is visible next to the car. Further
                        ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed yellow line is visible next to the car. Further ahead, this dashed
                        yellow line continues. Photo 2: A dashed yellow line is visible next to the car.
                        Further ahead, this dashed yellow line continues.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white dashed line is visible on the road surface
                        ahead of the car, indicating lane division. This line continues into the distance.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line separating my lane
                        from the leftmost lane, and the right boundary is a lane line separating my lane from
                        the rightmost lane. | roles: The left boundary (solid white) fits the role of a
                        lane_line, and the right boundary (dashed yellow) fits the role of a lane_line. |
                        markings: The lane markings (a dashed white line ahead) are consistent with the
                        boundaries and do not contradict them. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The dashed yellow line indicates the boundary of my lane and permits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where my car must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary, as per the rule for
                        solid lane lines.
Step 6  change_right    allowed (correct): allowed by the dashed yellow right boundary, as per the rule for
                        dashed lane lines.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: not_applicable as there are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable as there are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable as there are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You may proceed straight or change right, but you must stop before the visible dashed
                        white line ahead. Do not change left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['symbol:other']), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1061, 7.64 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with lane markings indicating movement options. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible further ahead. Photo 2: A dashed white line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane), which is consistent with having a lane line on the left and
                        a lane line on the right. | roles: The left boundary is a solid white lane line, and
                        the right boundary is a dashed white lane line, which fits the role of lane_line. |
                        markings: The single white arrow pointing straight ahead is present in the lane and is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The dashed white line permits changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        the rule prohibits changing lanes to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and the rule permits changing lanes to the right.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane marking shows an arrow pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       prohibited (correct): prohibited: The lane marking shows an arrow pointing straight
                        ahead, and the arrow does not show a left turn.
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited: The lane marking shows an arrow
                        pointing straight ahead, and the arrow does not show a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The lane marking shows an arrow pointing straight
                        ahead, and the arrow does not show a U-turn or a turn toward the opposite traffic.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the observed features.
Advice                  You should stay in the middle lane to go straight, but you are permitted to change
                        right if necessary. No specific stopping or turning maneuvers are indicated for this
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['change_right',
                        'go_straight'], citation None, contradictions []
Tokens                  in 3793, out 851, 6.3 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a continuation
                        of the road with multiple lanes. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The stop line is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The solid white line on the right prohibits changing into the adjacent
                        lane.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane_line on the left, as per the
                        rule for solid lane lines.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane_line on the right, as per the
                        rule for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stop at the solid white stop line before proceeding. You are restricted to
                        going straight in your current lane, as lane changes are prohibited by the solid white
                        lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 945, 5.88 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line. | markings: the arrow pointing straight ahead in my
                        lane agrees with the boundaries (dashed lines allow lane changes, but the arrow
                        restricts movement to straight ahead). | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes.
Step 5  Rule            arrow:straight: The arrow indicates that only proceeding straight ahead is permitted
                        in this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the white dashed left boundary
                        line and the arrow indicating only straight movement.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the white dashed right boundary
                        line and the arrow indicating only straight movement.
Step 6  go_straight     allowed (correct): allowed because the lane marking shows an arrow pointing straight
                        ahead.
Step 6  turn_left       prohibited (correct): prohibited because the lane marking shows an arrow pointing only
                        straight ahead.
Step 6  turn_right      prohibited (correct): prohibited because the lane marking shows an arrow pointing only
                        straight ahead.
Step 6  u_turn          prohibited (correct): prohibited because the lane marking shows an arrow pointing only
                        straight ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in the middle lane and proceed straight ahead, as the lane marking restricts
                        movement to straight ahead only. Lane changes are prohibited by the dashed lines and
                        the lane arrow.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['change_left prohibited
                        across a broken lane line', 'change_right prohibited across a broken lane line']
Tokens                  in 3793, out 976, 5.91 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection or a major road
                        crossing. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a large white arrow pointing straight
                        ahead in the lane to my right.; arrow:straight (full): Photo 2 shows a large white
                        arrow pointing straight ahead in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color and pattern of both boundaries (white
                        dashed lines) fit the role of lane_line. | markings: the arrows in my lane (straight
                        ahead) agree with the boundaries (dashed lines allow lane changes). | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A dashed lane line on the left allows my car to change lanes to the
                        left if safe.
Step 5  Rule            right_boundary: A dashed lane line on the right allows my car to change lanes to the
                        right if safe.
Step 5  Rule            arrow:straight: The arrow in my lane indicates that going straight ahead is permitted.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed lane line,
                        and the rule allows lane changes to the left if safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed lane line,
                        and the rule allows lane changes to the right if safe.
Step 6  go_straight     allowed (correct): allowed: The lane marking in my lane is an arrow pointing straight
                        ahead, and the rule permits this movement.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking in my lane that permits a left
                        turn.
Step 6  turn_right      prohibited (correct): prohibited: There is no marking in my lane that permits a right
                        turn.
Step 6  u_turn          prohibited (correct): prohibited: There is no marking in my lane that permits a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to go straight, change left, or
                        change right if safe. No specific lane is required for any movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 1107, 6.93 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban or suburban area, and ahead there appears to be
                        a junction or a continuation of the road with other traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the flow of traffic). | roles: the white dashed lines on both sides fit the
                        role of lane_line. | markings: the lack of markings in my lane is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white dashed line on the left allows my car to change lanes into
                        the adjacent lane.
Step 5  Rule            right_boundary: The white dashed line on the right allows my car to change lanes into
                        the adjacent lane.
Step 5  Rule            no_turn:right: This marking prohibits my car from making a right turn.
Step 6  change_left     allowed (correct): allowed: The white dashed line on the left allows lane changes.
Step 6  change_right    allowed (correct): allowed: The white dashed line on the right allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane and can change left or right, or proceed straight. However,
                        you are prohibited from turning right. Use the lane appropriate for your intended
                        movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 971, 6.67 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a wide intersection or a
                        major road junction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane_line, yellow solid line for center_line). | markings: there
                        are no markings to check for agreement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to enter an adjacent lane.
Step 5  Rule            right_boundary: The solid yellow line indicates a separation between traffic moving in
                        opposite directions and prohibits crossing it.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane_line on the left, as per the
                        rule that prohibits crossing lane boundaries.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow center_line on the
                        right, as per the rule that prohibits crossing center lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides of your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 932, 6.5 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where lanes diverge/merge, though the exact nature is not fully clear from the
                        immediate view. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car, and Photo 2 shows a broken yellow
                        line next to my car. Further ahead, Photo 1 shows a broken yellow line continuing, and
                        Photo 2 shows a broken yellow line continuing.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line (separating from
                        lane 1), and the right boundary is a lane line (separating from lane 3). | roles: The
                        left boundary is a solid white lane line, and the right boundary is a dashed yellow
                        lane line, which fits the roles of lane_line. | markings: The white arrow pointing
                        straight ahead is in my lane and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed yellow lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): Prohibited by the solid white left boundary, as per the rule for
                        solid lane lines.
Step 6  change_right    allowed (correct): Allowed by the dashed yellow right boundary, as per the rule for
                        dashed lane lines.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed because the white arrow in the lane permits
                        straight movement, and no other marking prohibits it.
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited because the white arrow in the lane does
                        not show a left turn.
Step 6  turn_right      prohibited (correct): Prohibited because the white arrow in the lane does not show a
                        right turn.
Step 6  u_turn          prohibited (WRONG, label allowed): Prohibited because the white arrow in the lane does
                        not show a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, which permits going straight ahead. You may change right
                        into the lane on your right, but changing left is prohibited by the solid white line.
                        No specific stopping or waiting areas are marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation None,
                        contradictions []
Tokens                  in 3793, out 1056, 7.06 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        junction or a continuation of the road with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead, and Photo 2 shows a
                        solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a dashed white line further ahead, and Photo 2
                        shows a dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to the right of my lane.; arrow:straight (full): Photo 2 shows a white arrow
                        pointing straight ahead in the lane to the left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line (separating lane 1
                        and 2), and the right boundary is a lane line (separating lane 2 and 3). | roles: The
                        color and pattern of each boundary fit the role given to it: both are white lane
                        lines. | markings: The arrows in my lane (arrow:straight) agree with the boundaries
                        and other markings. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing it to the left.
Step 5  Rule            right_boundary: The dashed white line permits crossing it to the right.
Step 5  Rule            arrow:straight: My car is permitted to go straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary and the
                        rule that prohibits crossing a solid line to the left.
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary and the rule that
                        permits crossing a dashed line to the right.
Step 6  go_straight     allowed (correct): allowed by the white arrow pointing straight ahead in my lane and
                        the rule that permits the movement shown by the arrow.
Step 6  turn_left       prohibited (correct): prohibited by the white arrow pointing straight ahead in my lane
                        and the rule that prohibits movements not shown by the arrow.
Step 6  turn_right      prohibited (correct): prohibited by the white arrow pointing straight ahead in my lane
                        and the rule that prohibits movements not shown by the arrow.
Step 6  u_turn          prohibited (correct): prohibited by the white arrow pointing straight ahead in my lane
                        and the rule that prohibits movements not shown by the arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are permitted to go straight or change right, but changing left or turning in any
                        direction is prohibited by the lane markings. Use the right lane if you intend to
                        change right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 1140, 7.53 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or intersection
                        where traffic flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate a lane
                        within a set of lanes). | roles: the solid white lines on both sides fit the role of
                        lane_line. | markings: the stop line marking is consistent with the boundaries and
                        general road markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, which prohibits
                        crossing it to change lanes.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, which prohibits
                        crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight through the intersection.
                        Lane changes are prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 962, 6.47 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection indicated by
                        overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1 shows a white dashed line marking the lane boundary
                        ahead. Photo 2 shows a white dashed line marking the lane boundary ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is not the edge lane). | roles: the color and pattern of
                        each boundary (white dashed) fit the role of a lane_line. | markings: the stop_line
                        marking is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across this boundary.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across this boundary.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change lanes left or right, and you may
                        proceed straight ahead. You must stop before the visible stop line at the intersection
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 995, 7.64 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching a junction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The straight arrow in my lane is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A broken white line allows lane changes in both directions.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in the
                        adjacent lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        which allows lane changes.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and no other
                        marking prohibits it.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking in my lane that permits a left
                        turn.
Step 6  turn_right      prohibited (correct): prohibited: There is no marking in my lane that permits a right
                        turn.
Step 6  u_turn          prohibited (correct): prohibited: There is no marking in my lane that permits a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to go straight, change left, or
                        change right. No specific stopping or waiting areas are marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 1033, 6.56 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white dashed line is visible across the lane,
                        indicating the lane ends ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is not the edge lane). | roles: The white dashed/solid
                        lines fit the role of lane_line. | markings: The stop line marking is consistent with
                        the lane boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the lane does not end in a merge.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the boundaries are
                        dashed. You may proceed straight, but you must stop before the solid white line
                        marking the end of the lane at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 1003, 6.38 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary
                        next to my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the stop
                        line marking is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       allowed: allowed: There are no markings in my lane prohibiting a left turn.
Step 6  turn_right      allowed: allowed: There are no markings in my lane prohibiting a right turn.
Step 6  u_turn          allowed: allowed: There are no markings in my lane prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes in either direction,
                        and all movements (straight, left, right, U-turn) are permitted at the intersection,
                        but you must stop before the stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3793, out 943, 5.77 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway. Ahead, there is an overpass with exit signs
                        indicating an exit. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1: White dashed arrows pointing straight ahead are
                        visible in my lane. Photo 2: White dashed arrows pointing straight ahead are visible
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The straight arrow in my lane is consistent with
                        the lane boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes in either direction.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes in either direction.
Step 5  Rule            arrow:straight: The straight arrow indicates that proceeding straight ahead is
                        permitted.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane marking shows a straight arrow,
                        and no other marking prohibits it.
Step 6  turn_left       prohibited: Prohibited because the lane marking only shows a straight arrow, not a
                        left turn.
Step 6  turn_right      prohibited: Prohibited because the lane marking only shows a straight arrow, not a
                        right turn.
Step 6  u_turn          prohibited: Prohibited because the lane marking only shows a straight arrow, not a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no rule
                        prohibits an allowed action.
Advice                  You are in the middle lane and are permitted to go straight, change left, or change
                        right. Since there are no specific turn arrows, you should proceed straight unless you
                        intend to change lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 969, 6.15 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight without an immediate
                        intersection visible in the frame. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The boundaries are lane lines, which is consistent with my lane
                        being one of three lanes. | roles: The white dashed lines on both sides are consistent
                        with the role of a lane_line separating my lane from adjacent lanes. | markings: There
                        are no markings in my lane to check against the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            line:stop_line: The presence of a stop line indicates that the vehicle must come to a
                        complete stop before the line if required by traffic control devices.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and the rule
                        allows lane changes when safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the rule
                        allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. Lane changes are permitted when safe, and you are
                        allowed to proceed straight ahead. No specific turn movements are indicated for your
                        current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 992, 6.45 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight without an immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows the line further ahead, and Photo 2 shows the line
                        further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows the line further ahead, and Photo 2 shows the line
                        further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows a white dashed line segment with Chinese characters
                        '公' (gōng) painted on it, indicating a lane designation.; text:other (full): Photo 2
                        shows a white dashed line segment with Chinese characters '公' (gōng) painted on it,
                        indicating a lane designation.; text:other (full): Photo 2 shows a white dashed line
                        segment with Chinese characters '公' (gōng) painted on it, indicating a lane
                        designation.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to
                        it. | markings: the text markings are consistent with the lane designation and do not
                        contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid yellow center line prohibits crossing it to change lanes into
                        the opposing traffic direction.
Step 5  Rule            text:other: Lane designation markings do not restrict or permit any specific movement.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        left boundary, as per the rule for solid lane lines.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow center line on the
                        right boundary, as per the rule for solid center lines.
Step 6  go_straight     allowed (contested, label prohibited): allowed as there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable as there are no markings allowing or prohibiting a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable as there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable as there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides of your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1087, 6.68 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight, with
                        some overpasses visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lane line on left, dashed white lane line on right). | markings: there
                        are no markings in my lane to check for agreement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The broken white line on the right permits changing lanes to the
                        right.
Step 5  Rule            line:stop_line: This marking indicates the stopping point for vehicles.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left, as per the rule for solid lane lines.
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right, as per the rule
                        for broken lane lines.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable as there are no markings in my lane governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change right, but changing
                        left is prohibited by the solid line. No specific stopping or turning maneuvers are
                        marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 961, 6.7 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway. Ahead, the road continues straight, possibly
                        leading to an interchange or another section of the highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line in the lane ahead,
                        indicating a lane division.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the direction of travel). | roles: The solid white lines
                        on both sides fit the role of lane_line. | markings: The dashed white line ahead is
                        interpreted as a stop line, which is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other signs or signals.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, which is a solid
                        white line and prohibits lane changes to the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the right_boundary, which is a solid
                        white line and prohibits lane changes to the right.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides of your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 993, 6.7 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway. Ahead, the road continues straight with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible ahead of the car,
                        separating the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The dashed line ahead is interpreted as a stop line, which is consistent
                        with the lane markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            line:stop_line: The stop line indicates where the vehicle must come to a complete stop
                        before proceeding, if required by other markings or signs.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, which is a solid
                        white lane_line and prohibits lane changes to the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the right_boundary, which is a solid
                        white lane_line and prohibits lane changes to the right.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides, and you must stop before the
                        visible dashed line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 969, 6.45 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues, and there are
                        signs indicating upcoming exits or directions. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1 shows a white dashed line marking the lane boundary
                        to the right, and Photo 2 shows this line clearly.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: the color (white) and pattern (dashed)
                        of both boundaries fit the role of a lane_line. | markings: the line:stop_line marking
                        is consistent with the boundaries and the general road context. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. Lane changes are permitted as the
                        boundaries are dashed. You may proceed straight, but you should be aware of the stop
                        line ahead, which may indicate a required stop depending on the upcoming intersection
                        or traffic control.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 1000, 6.88 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with trees lining both sides. Ahead, the road continues
                        straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in the lane ahead,
                        indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The visible dashed line ahead is interpreted as a stop line,
                        which is consistent with the lane markings. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes into or out of my lane.
Step 5  Rule            right_boundary: The broken white line allows for lane changes into or out of my lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows for
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
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
Advice                  You are in the middle lane of a three-lane highway. You are permitted to go straight,
                        change left, or change right. Be aware of the stop line ahead, which may require you
                        to stop if traffic signals or other markings dictate it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 977, 7.11 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or road, and ahead there is a continuation of the road,
                        not an intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed lines are lane lines). | markings: there are no markings in my lane to
                        check against the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A broken white line indicates that lane changes are permitted when
                        safe.
Step 6  change_left     allowed (correct): allowed, because the left boundary is a dashed white line, which
                        permits lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed, because the right boundary is a dashed
                        white line, which permits lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road, and lane changes are permitted when
                        safe. All movements, including going straight, are allowed, but you should proceed
                        with caution as there are no specific lane markings to guide your turns.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3793, out 848, 5.93 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight,
                        possibly leading to an interchange or another section of the highway. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead, separating the lane from the
                        shoulder/barrier. Photo 2: A solid white line is visible further ahead, separating the
                        lane from the shoulder/barrier.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A dashed white line marking the lane boundary is
                        visible ahead. Photo 2: A dashed white line marking the lane boundary is visible
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is an edge_line. | roles: The dashed white line on the left fits the role of
                        a lane_line, and the solid white line on the right fits the role of an edge_line. |
                        markings: The dashed line ahead is interpreted as a stop line, which is consistent
                        with the lane markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The solid white line indicates the edge of the roadway and prohibits
                        crossing it.
Step 5  Rule            line:stop_line: The stop line indicates where the vehicle must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows for
                        lane changes.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, which
                        prohibits crossing it.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a stop line,
                        which turns the allowed movement into stop_first.
Step 6  turn_left       prohibited: prohibited: There are no markings allowing a left turn.
Step 6  turn_right      prohibited: prohibited: There are no markings allowing a right turn.
Step 6  u_turn          prohibited: prohibited: There are no markings allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You must stop at the visible stop line before proceeding straight ahead. Lane changes
                        to the left are permitted, but changing right is prohibited by the solid edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3793, out 996, 6.31 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight, with
                        no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to the car. Photo 2: A dashed white line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A dashed white line is visible across the lane,
                        indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane line (separating
                        from lane 1) and the right boundary is a lane line (separating from lane 3). This is
                        consistent. | roles: The left boundary is a dashed white lane line, and the right
                        boundary is a solid white lane line. This fits the roles of lane_line. | markings: The
                        dashed white line across the lane is interpreted as a stop line, which is consistent
                        with the lane markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes between lanes.
Step 5  Rule            right_boundary: The solid white line prohibits lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by traffic control.
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed white lane line, which
                        permits lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid white
                        lane line, which prohibits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings prohibiting straight
                        movement in the lane.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and you are permitted to change left, but changing right
                        is prohibited by the solid white line. You may proceed straight ahead, but you must
                        stop at the marked line if required by traffic control.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1016, 6.95 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the right side. Ahead, the road
                        continues straight with overhead gantries and signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Photo 2: A solid white line is
                        visible next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car, followed by a yellow line
                        further ahead. Photo 2: A solid white line is visible next to my car. Further ahead, a
                        solid yellow line is visible.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1: No markings are visible within my lane in the
                        visible stretch.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The solid white line on the left is consistent with a lane_line, and the solid
                        white line on the right is consistent with a lane_line. | markings: The lane markings
                        list is empty except for a potential stop line which is not clearly visible or
                        governing any action. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary, as per
                        the rule that prohibits crossing lane lines.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary, as
                        per the rule that prohibits crossing lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  Stay in the middle lane to proceed straight ahead. Lane changes are prohibited by the
                        solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 998, 6.88 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight into
                        the distance, with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        next to my car, and a white dashed line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the white dashed line ahead is
                        interpreted as a stop line, which is consistent with the lane markings. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You are permitted to change lanes in
                        either direction, and you may proceed straight ahead. You should observe the stop line
                        ahead, as it may require you to stop.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 994, 6.23 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. The road continues straight ahead into the
                        distance with hills visible in the background. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible further ahead,
                        separating the lane from the right boundary.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (dashed lines on both sides indicate internal
                        lanes). | roles: The white dashed lines on both sides fit the role of lane_line. |
                        markings: The stop line marking is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates the designated stopping point for the lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no rule
                        prohibits an allowed action.
Advice                  You are in the middle lane of a multi-lane highway. You are permitted to change lanes
                        in either direction, and you may proceed straight ahead. Use the lane markings to
                        guide your movement, and be aware of the stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 959, 6.41 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line pattern across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The stop line marking is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, which
                        allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change left or right, and you are
                        permitted to go straight. You must stop before the visible stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 1019, 7.23 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible ahead, separating
                        the lane from the next lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The visible dashed line ahead is interpreted as a stop line,
                        which is consistent with the lane markings. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You are permitted to go straight,
                        change left, or change right. Be aware of the stop line ahead, which may require you
                        to stop if traffic signals or other markings dictate it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 977, 7.15 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight, and
                        there are no immediate intersections or ramps visible. (lanes 5, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (5) and my lane position
                        (3) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between other lanes). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of a lane_line. | markings: the straight arrow in my lane agrees
                        with the boundaries (no conflicting markings). | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            arrow:straight: The straight arrow indicates that proceeding straight ahead is
                        permitted in this lane.
Step 6  change_left     allowed (correct): allowed, because the left boundary is a dashed white line, which
                        permits lane changes when safe.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        permits lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed, because the lane contains a straight arrow, and
                        no other marking prohibits it.
Step 6  turn_left       prohibited: prohibited, because the lane contains a straight arrow, which does not
                        show a left turn.
Step 6  turn_right      prohibited: prohibited, because the lane contains a straight arrow, which does not
                        show a right turn.
Step 6  u_turn          prohibited: prohibited, because the lane contains a straight arrow, which does not
                        show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane, which permits straight travel and lane changes in either
                        direction. You may proceed straight ahead, but turning left, right, or making a U-turn
                        is prohibited in this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 993, 6.76 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road continues into the distance with
                        buildings on both sides, and there is no immediate intersection or ramp visible.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and a broken white line further
                        ahead. Photo 2 shows a broken white line next to my car, and a broken white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane line, and the right boundary is a
                        lane line, which is consistent with my lane being the middle lane. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the role of lane lines. | markings: There are no markings in my lane
                        to check against the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 6  change_left     prohibited (correct): The left boundary is a solid white lane line, which prohibits
                        changing left.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed white lane line,
                        which permits changing right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not prohibit going straight.
Step 6  turn_left       allowed: No marking governs this action, and there is no indication of a left turn
                        being prohibited.
Step 6  turn_right      allowed: No marking governs this action, and there is no indication of a right turn
                        being prohibited.
Step 6  u_turn          allowed: No marking governs this action, and there is no indication of a U-turn being
                        prohibited.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed that is prohibited by a rule.
Advice                  You may change right, go straight, turn left, or turn right. Do not change left, as
                        the solid white line prohibits it. Use the middle lane for straight travel or turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions ['turn_right allowed although a prohibited-movement marking forbids
                        it']
Tokens                  in 3793, out 957, 6.31 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in the
                        road layout, though the exact nature is not fully clear from the immediate view.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): Photo 1 shows no markings in my lane. Photo 2 shows no
                        markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane). The boundaries are lane lines, which is consistent with my
                        lane being one of three lanes. | roles: The boundaries are solid white lines, which
                        correctly fit the role of lane_line. | markings: There are no markings observed in my
                        lane, so there is no contradiction. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, as per the rule for
                        solid lane lines.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, as per the rule
                        for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane to prohibit
                        it, and the boundaries do not govern straight movement.
Step 6  turn_left       not_applicable: not_applicable as there are no markings in my lane to govern this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no markings in my lane to govern this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no markings in my lane to govern this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observed solid boundaries and the lack of
                        governing markings in the lane.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 967, 6.45 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where the
                        road continues and potentially merges or splits. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The color and pattern of both boundaries (solid white lines) fit
                        the role of lane_line. | markings: The stop line is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The solid white line on the right prohibits changing into the adjacent
                        lane.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        proceeding into the intersection.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, which prohibits
                        changing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary, which
                        prohibits changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stop at the solid white stop line before proceeding into the intersection.
                        You are restricted to going straight in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 936, 6.54 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a bridge or overpass
                        structure, suggesting the road continues forward. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white solid line is visible at the end of the
                        visible road segment.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in this direction). | roles: The color (white) and pattern (solid) of both
                        boundaries fit the role of lane_lines. | markings: The stop line is consistent with
                        the boundaries and markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The solid white line on the right prohibits changing into the adjacent
                        lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, which prohibits
                        changing into the adjacent lane.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, which prohibits
                        changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the settled boundaries and markings, and no rule
                        prohibits an allowed action.
Advice                  You must stop at the solid white line before proceeding. You are restricted to going
                        straight ahead in this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 954, 22.78 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection visible in
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: the solid white lines on both sides fit the role of lane_line. |
                        markings: the stop line in Photo 2 is consistent with the lane markings. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, which prohibits
                        crossing it to change lanes.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, which prohibits
                        crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         consistent
Advice                  You must stop at the solid white stop line before proceeding. You are restricted to
                        going straight in your current lane, as lane changes and turns are not permitted by
                        the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 920, 6.67 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road, not an intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3 lanes). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the lane markings list is empty,
                        which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You are permitted to go straight, change
                        left, or change right. Since there are no specific turn arrows, you must proceed with
                        caution if you intend to turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3793, out 923, 6.15 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in
                        road configuration. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Photo 2: A solid white line is
                        visible next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2: No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The color and pattern of both boundaries fit the role of a
                        lane_line. | markings: The lane markings list is empty except for a potential stop
                        line which is not clearly visible as a governing marking. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The solid white line on the right prohibits changing into the adjacent
                        lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane_line on the left, as per the
                        rule for solid lane lines.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane_line on the right, as per the
                        rule for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in the lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You must remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides. Proceed with caution as you
                        approach the end of the visible road section.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 980, 7.23 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows a broken white line continuing, and
                        Photo 2 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right
                        boundary.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the line:stop_line marking is consistent with the right boundary being a
                        lane line. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The broken white line on the right permits changing into the adjacent
                        lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left, as
                        per the rule for a solid lane line.
Step 6  change_right    allowed (correct): allowed by the broken white line on the right, as per the rule for
                        a broken lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement in the lane.
Step 6  turn_left       not_applicable: not_applicable as there are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable as there are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable as there are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change right, but changing
                        left is prohibited by the solid line. Be aware of the stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 978, 6.42 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:straight (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction). | roles: the color and pattern of each boundary (white dashed)
                        fit the role of a lane_line. | markings: the two straight arrows in my lane agree with
                        each other and with the boundaries (no conflicting markings). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            arrow:straight: The straight arrow allows my car to proceed straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows lane changes.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
Step 6  go_straight     allowed (correct): allowed: The lane contains a straight arrow, and no other marking
                        prohibits going straight.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking allowing a left turn in this
                        lane.
Step 6  turn_right      prohibited (correct): prohibited: There is no marking allowing a right turn in this
                        lane.
Step 6  u_turn          prohibited (correct): prohibited: There is no marking allowing a U-turn in this lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you are permitted to go straight or
                        change lanes in either direction. No specific stopping or turning maneuvers are
                        indicated for this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 971, 6.23 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with no immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows no markings in my lane. Photo 2 shows no
                        markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lines are lane_lines). | markings: the lane markings (none visible) agree
                        with each other and with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where a vehicle must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary, as per the rule for
                        solid lane lines.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary, as per
                        the rule for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 961, 6.43 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead, and Photo 2 shows the line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead, and Photo 2 shows the line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        a lane between other lanes). | roles: the color and pattern of both boundaries (white
                        dashed lines) fit the role of lane_line. | markings: there are no markings to check
                        for agreement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' in my lane prohibits turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing U-turn
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change left or right, and you may proceed
                        straight, but you are prohibited from turning right. Use the lane markings and
                        surrounding traffic to safely execute any maneuvers.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 970, 6.88 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or a continuation of the road
                        with multiple lanes visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, the line appears
                        to be a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, the line
                        appears to be a solid yellow line continuing.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1: A blue overhead sign with three upward arrows is
                        visible ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line separating my lane
                        from the left lane, and the right boundary is a lane line separating my lane from the
                        right lane. | roles: The left boundary (white solid line) fits the role of a
                        lane_line, and the right boundary (yellow solid line) fits the role of a lane_line. |
                        markings: The overhead arrow indicates straight movement, which is consistent with the
                        lane markings. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to the left.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it to the right.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        the rule prohibits crossing it to the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        lane line, and the rule prohibits crossing it to the right.
Step 6  go_straight     allowed (contested, correct): allowed: The overhead arrow indicates straight movement
                        is permitted.
Step 6  turn_left       prohibited: prohibited: The overhead arrow does not show a left turn.
Step 6  turn_right      prohibited: prohibited: The overhead arrow does not show a right turn.
Step 6  u_turn          prohibited: prohibited: The overhead arrow does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in the middle lane to proceed straight ahead, as lane changes and turns are
                        prohibited by the lane markings and solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 969, 6.81 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in
                        road configuration, though the exact nature is not fully clear from the immediate
                        view. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead. Photo 2: A solid white line is
                        visible further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The color and pattern of both boundaries (solid white lines) fit
                        the role of a lane_line. | markings: The stop line marking is consistent with the
                        boundaries and does not contradict any other visible markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (element_rules for left_boundary).
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right
                        (element_rules for right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane (no marking governs this action).
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn (no marking governs this action).
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn (no marking governs this action).
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn (no marking governs this action).
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible (no marking governs this action).
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You must stop at the solid white line ahead. You are restricted to proceeding straight
                        ahead in your current lane, as lane changes are prohibited by the solid white lines on
                        both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1021, 6.76 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 1 shows a solid yellow line on the right boundary,
                        and Photo 2 shows a solid yellow line on the right boundary.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line on left, yellow solid line on right). | markings: the marking
                        (line:stop_yield) is consistent with the boundaries and the general road context. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left indicates the boundary of my lane and
                        separates it from another lane of my direction.
Step 5  Rule            right_boundary: The solid yellow line on the right indicates the boundary of my lane
                        and separates it from traffic in the opposite direction.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires my car to come to a
                        full stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line on the
                        left, as it indicates the boundary of my lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane_line on the
                        right, as it indicates the boundary of my lane.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because of the line:stop_yield
                        marking in my lane.
Step 6  turn_left       stop_first: stop_first because of the line:stop_yield marking in my lane.
Step 6  turn_right      stop_first: stop_first because of the line:stop_yield marking in my lane.
Step 6  u_turn          stop_first: stop_first because of the line:stop_yield marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must come to a full stop before proceeding in any direction. Lane changes are
                        prohibited by the solid lines on both sides of your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1006, 7.12 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into the distance with traffic signals and buildings on both sides.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1: A white arrow pointing straight ahead is visible in
                        the lane. Photo 2: A white arrow pointing straight ahead is visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The straight arrow in the lane agrees with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            arrow:straight: The straight arrow permits proceeding straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, which is a solid
                        white lane_line.
Step 6  change_right    prohibited (correct): prohibited by the right_boundary, which is a solid white
                        lane_line.
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking, which permits
                        proceeding straight ahead.
Step 6  turn_left       prohibited: prohibited by the arrow:straight marking, which does not show a left turn.
Step 6  turn_right      prohibited: prohibited by the arrow:straight marking, which does not show a right
                        turn.
Step 6  u_turn          prohibited: prohibited by the arrow:straight marking, which does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 945, 5.76 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining the sides. Ahead, the road continues
                        straight, and there is no immediate intersection or ramp visible in the close-up.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line just
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The stop line marking is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, which prohibits
                        crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the settled boundaries and markings, and no rule
                        prohibits an action that is allowed.
Advice                  You must stop at the solid white line ahead. You are permitted to proceed straight
                        ahead, but lane changes are prohibited by the solid white lines on both sides.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 1016, 7.41 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        continuation of the road, possibly leading to an intersection or another section of
                        the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: Two white dashed lines are visible across the lane,
                        indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The stop line marking is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You are permitted to change lanes in either
                        direction, and you may proceed straight ahead. You should stop at the visible stop
                        line if required by traffic conditions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 946, 5.97 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic
                        appears to be turning or continuing. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead, separating the lane from the
                        adjacent lane. Photo 2: A solid white line is visible further ahead, separating the
                        lane from the adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2: A white arrow pointing right is visible on the road
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The right-pointing arrow in the lane is consistent with the lane boundaries.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:merge_right: The arrow indicates that traffic in this lane must merge to the
                        right.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left boundary.
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line on the right boundary.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the right-pointing arrow in the lane,
                        which does not show going straight.
Step 6  turn_left       prohibited (correct): prohibited by the right-pointing arrow in the lane, which does
                        not show turning left.
Step 6  turn_right      allowed (correct): allowed by the right-pointing arrow in the lane, which shows
                        merging right (implying a right turn or exit).
Step 6  u_turn          prohibited (correct): prohibited by the right-pointing arrow in the lane, which does
                        not show U-turning.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the solid lane boundaries and the right-pointing merge
                        arrow, and no action was decided without the governing feature.
Advice                  You must stay in your current lane or merge right. The lane marking indicates that you
                        must merge right, which likely means you should prepare to turn right or exit the
                        road.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe [], citation None, contradictions ['go_straight, turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3793, out 990, 7.04 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues, possibly
                        leading to an overpass or another section of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible next to the car. Photo 2: A broken yellow
                        line is visible next to the car.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: No markings are visible within my lane in the
                        visible stretch.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane line, and the right boundary is a
                        dashed yellow lane line, which fits the roles of lane_line. | markings: The partial
                        visibility of a stop line in Photo 1 is consistent with the general view, and no other
                        markings contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The dashed yellow line permits crossing into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left boundary prohibits changing
                        left, as per the rule for solid lane lines.
Step 6  change_right    allowed (correct): The dashed yellow right boundary permits changing right, as per the
                        rule for dashed lane lines.
Step 6  go_straight     stop_first (contested, label allowed): The stop line requires the car to stop first
                        before proceeding straight, as per the rule for a stop line.
Step 6  turn_left       stop_first: The stop line requires the car to stop first before turning left, as per
                        the rule for a stop line.
Step 6  turn_right      stop_first: The stop line requires the car to stop first before turning right, as per
                        the rule for a stop line.
Step 6  u_turn          stop_first: The stop line requires the car to stop first before making a U-turn, as
                        per the rule for a stop line.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and all actions are governed by the stop line.
Advice                  You must come to a complete stop at the stop line before proceeding. You are permitted
                        to change right, but changing left is prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1021, 6.95 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass/bridge structure. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows white dashed lane markings across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate internal
                        lanes). | roles: the white dashed lines fit the role of lane_line. | markings: the
                        stop line marking is consistent with the lane markings shown in Photo 2. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes into or out of this lane.
Step 5  Rule            right_boundary: The broken white line allows for lane changes into or out of this
                        lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection or area ahead.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, which
                        allows lane changes.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a line:stop_line,
                        which turns allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first: The lane contains a line:stop_line, which turns allowed
                        movements into stop_first.
Step 6  turn_right      stop_first: stop_first: The lane contains a line:stop_line, which turns allowed
                        movements into stop_first.
Step 6  u_turn          stop_first: stop_first: The lane contains a line:stop_line, which turns allowed
                        movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the boundaries are
                        broken. You must come to a complete stop before proceeding straight, turning left,
                        turning right, or making a U-turn due to the stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3793, out 1007, 6.37 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a continuation
                        of the road with traffic signals visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible further ahead. Photo 2: A dashed white line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1: No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane line, and the right boundary is a
                        dashed white lane line, which fits the role of lane_line. | markings: The lane
                        markings list is empty except for a potential stop line which is not clearly visible
                        in the close-up or far ahead, so the markings are consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: A stop line indicates where a vehicle must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed white lane line,
                        which permits changing right.
Step 6  go_straight     allowed (contested, correct): No arrow or prohibiting marking governs this action, and
                        the boundaries do not prohibit going straight.
Step 6  turn_left       allowed: No arrow or prohibiting marking governs this action, and the boundaries do
                        not prohibit turning left.
Step 6  turn_right      allowed: No arrow or prohibiting marking governs this action, and the boundaries do
                        not prohibit turning right.
Step 6  u_turn          allowed: No arrow or prohibiting marking governs this action, and the boundaries do
                        not prohibit U-turning.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and you are permitted to go straight, turn left, or turn
                        right. You may change lanes to the right, but changing left is prohibited by the solid
                        white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1002, 6.16 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass/bridge structure. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible further ahead, separating the lane from the
                        shoulder/barrier. Photo 2: A solid white line is visible further ahead, separating the
                        lane from the shoulder/barrier.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is an edge_line. | roles: The solid white line on the left fits the role of a
                        lane_line, and the solid white line on the right fits the role of an edge_line. |
                        markings: There are no markings to check for agreement. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates that lane changes across this boundary
                        are prohibited.
Step 5  Rule            right_boundary: The solid white line indicates that lane changes across this boundary
                        are prohibited.
Step 6  change_left     prohibited (correct): prohibited by the left_boundary, as it is a solid white line.
Step 6  change_right    prohibited (correct): prohibited by the right_boundary, as it is a solid white line.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, as there are no markings in the lane governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable, as there are no markings in the lane governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable, as there are no markings in the lane governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 932, 6.16 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway or major road leading towards an intersection ahead.
                        There are multiple lanes visible in my direction near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white arrow pointing right in the lane
                        ahead.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines). | roles: The color
                        and pattern of both boundaries (white dashed/solid) fit the role of lane_lines. |
                        markings: The arrows (merge_right and straight) are present in the lane and are
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across it.
Step 5  Rule            arrow:merge_right: This marking indicates that traffic in this lane is allowed to
                        merge to the right.
Step 5  Rule            arrow:straight: This marking indicates that traffic in this lane is allowed to proceed
                        straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a white dashed line, which
                        allows for lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a white dashed line, which
                        allows for lane changes.
Step 6  go_straight     allowed (WRONG, label prohibited): The lane contains an arrow pointing straight ahead,
                        which allows going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No arrow or prohibited-movement marking
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      allowed (correct): The lane contains an arrow pointing right, which allows turning
                        right.
Step 6  u_turn          allowed (WRONG, label prohibited): No arrow or prohibited-movement marking governs
                        this action, and there is no specific restriction against U-turns.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible ahead
                          of the lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, which allows you to go straight or turn right, and you can
                        change lanes in either direction. If you wish to turn left, you must use a different
                        lane or wait for a suitable opportunity.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right', 'arrow:straight'], missed ['arrow:right', 'line:stop_line']),
                        actions False, unsafe ['change_left', 'change_right', 'go_straight', 'u_turn'],
                        citation None, contradictions ['turn_right allowed although no arrow shows it']
Tokens                  in 3793, out 1094, 7.34 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues straight into
                        the distance with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane division
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (dashed lines on both sides indicate internal
                        lanes). | roles: The white dashed lines fit the role of lane_line. | markings: The
                        stop line marking is consistent with the lane structure. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings prohibiting straight
                        movement in the lane.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is prohibited by a rule that was not seen.
Advice                  You are in the middle lane of a three-lane road. You are permitted to change lanes in
                        either direction, and you may proceed straight ahead. Be aware of the stop line ahead,
                        which may require you to stop if traffic signals or other signs dictate it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 958, 3.95 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes traveling in the same direction.
                        Ahead, the road continues into the distance without an immediate intersection or ramp
                        visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a circular speed limit marking '60' in my
                        lane.; text:speed_limit (full): Photo 2 shows a circular speed limit marking '30' in
                        the lane to the left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The speed limit markings are consistent with the
                        lane structure. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed in the
                        lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane of three. You are permitted to change lanes left or right,
                        and you may proceed straight ahead. Be aware of the posted speed limit of 60.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3793, out 1037, 7.08 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, there is a junction or a section
                        where lanes diverge/merge, indicated by the presence of a bus lane and other traffic
                        patterns. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line separating my lane from the
                        lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Further ahead, Photo 1 shows a solid yellow line separating my lane
                        from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a solid yellow line on the right boundary,
                        which is the lane line.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line (separating from
                        lane 1), and the right boundary is a lane line (separating from lane 3). | roles: The
                        left boundary is a white solid lane line, and the right boundary is a yellow solid
                        lane line, which fits the role of lane_line. | markings: The marking (line:stop_yield)
                        is present in my lane and is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across this line
                        are prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across this line
                        are prohibited.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the car to come to a
                        full stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        boundary, which prohibits lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane line on the
                        right boundary, which prohibits lane changes.
Step 6  go_straight     stop_first (contested, label allowed): allowed because there are no arrows or
                        prohibitions in the lane, but it is governed by the stop-and-yield line, making it
                        stop_first.
Step 6  turn_left       stop_first: prohibited because there are no arrows or prohibitions in the lane, but it
                        is governed by the stop-and-yield line, making it stop_first.
Step 6  turn_right      stop_first: prohibited because there are no arrows or prohibitions in the lane, but it
                        is governed by the stop-and-yield line, making it stop_first.
Step 6  u_turn          stop_first: prohibited because there are no arrows or prohibitions in the lane, but it
                        is governed by the stop-and-yield line, making it stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane in view.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and all prohibitions are correctly derived from the rules.
Advice                  You must come to a full stop before proceeding in your lane. Lane changes to the left
                        or right are prohibited by the solid lane lines. You may proceed straight, turn left,
                        turn right, or make a U-turn only after stopping.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1152, 7.82 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, suggesting a straight road
                        segment rather than an immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the lane
                        markings list is empty, which is consistent with the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits the specified movement, but since it is not
                        visible, this rule is not applicable.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You are permitted to change lanes
                        in either direction, and you may proceed straight ahead. No specific lane usage is
                        required for turning movements as no arrows are present.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 991, 6.31 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or road, and ahead there appears to be a continuation of
                        the road, possibly leading to an intersection or another section of the highway.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3 lanes). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the lane markings list is empty,
                        which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted turn left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted turn right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You are permitted to change lanes in either
                        direction, go straight, or remain in your lane. No specific turn movements are
                        indicated or permitted by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 924, 5.89 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a wide open road ahead, suggesting a continuation of
                        the current road segment rather than an immediate intersection or ramp. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings observed in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is
                        index 2 (the middle lane). The left boundary is a lane line separating it from lane 1,
                        and the right boundary is a lane line separating it from lane 3. This is consistent. |
                        roles: Both boundaries are white dashed lines, consistent with lane_line roles. |
                        markings: No markings were listed, so there is no contradiction. | unseen: No
                        attributes were reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The broken white line allows for lane changes into the adjacent lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no rules
                        prohibit any allowed action.
Advice                  You are in the middle lane of a three-lane highway. You are permitted to change lanes
                        in either direction, and you may proceed straight ahead. No specific lane is required
                        for your intended movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 959, 7.19 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues under an
                        overpass structure, with traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car, and a broken yellow line further
                        ahead. Photo 2 shows a broken yellow line next to my car, and a broken yellow line
                        further ahead.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the lane boundary next
                        to my car, and a solid white line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane line on left, yellow dashed line for lane line on right). |
                        markings: the line:stop_line marking is consistent with the boundaries and the general
                        road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates that lane changes across this boundary
                        are prohibited.
Step 5  Rule            right_boundary: The broken yellow line indicates that lane changes across this
                        boundary are permitted when safe.
Step 5  Rule            line:stop_line: The stop line indicates that the vehicle must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (correct): prohibited by the left_boundary, which is a solid white line.
Step 6  change_right    allowed (correct): allowed by the right_boundary, which is a dashed yellow line.
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
Advice                  You are in the middle lane. You may change right if safe, but changing left is
                        prohibited. You may proceed straight, but you must stop before the solid white line
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 987, 6.01 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway. Ahead, the road continues straight, and there
                        are overhead gantries suggesting upcoming traffic control or lane management. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: the color (white) and pattern (dashed)
                        of both boundaries fit the role of lane_line. | markings: there are no markings in my
                        lane to check against the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 6  change_left     allowed (WRONG, label prohibited): allowed, because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road, and lane changes are permitted in
                        both directions. You may proceed straight, but turning movements are not explicitly
                        governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3793, out 901, 6.49 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes going in the same direction. Ahead,
                        the road continues straight with no immediate intersection or ramp visible. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The stop line marking is consistent with the lane
                        markings observed. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates the point where the vehicle must stop if
                        required by traffic control devices.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is prohibited by a rule that is not visible.
Advice                  You are in the middle lane of three lanes. You may change lanes left or right, and you
                        may proceed straight ahead. Be aware of the stop line ahead, which indicates where you
                        should stop if necessary.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 970, 6.33 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with guardrails on the left and a barrier on the right.
                        The road continues straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a metal guardrail structure. Photo 2 shows the metal guardrail
                        structure.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the bottom, and a solid white line further
                        ahead. Photo 2 shows a solid white line near the bottom, and a solid white line
                        further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the right boundary.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is an edge_line (guardrail), and
                        the right boundary is a lane_line separating my lane from the next lane. | roles: The
                        left boundary is an edge_line (guardrail), and the right boundary is a lane_line
                        (solid white line). | markings: The solid white line on the right boundary is
                        consistent with the line:stop_line marking observed in Photo 2. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The guardrail indicates the physical edge of the roadway.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     not_applicable (WRONG, label prohibited): prohibited by the solid white line on the
                        left boundary (though the left boundary is an edge_line, the solid line on the right
                        boundary governs lane changes, and there is no solid line on the left boundary to
                        prohibit a change left, but the edge_line limits movement).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        boundary, as per the rule for lane_line.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable, as there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes to the
                        right are prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1034, 7.03 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with guardrails on both sides, and it appears to be a
                        straight road ahead with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows white dashed lines in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of 3). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: the white dashed lines in my lane
                        are consistent with the boundaries and do not contradict any visible markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other markings or signs.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        which allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change lanes in either direction. You may
                        proceed straight ahead, but you must stop before the visible stop line if required by
                        traffic control.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3793, out 1007, 7.2 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight,
                        possibly leading to an overpass or another section of the highway. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): Photo 1: No specific markings (arrows, text, etc.) are
                        visible within my lane in the immediate foreground or ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The lack of visible markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary, as per
                        the rule for solid lane lines.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, as per the rule
                        for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking, as per the rule for prohibited-
                        movement markings.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         The actions are consistent with the settled boundaries and markings, and no rule
                        prohibits an action that was decided as allowed.
Advice                  You must remain in your current lane to proceed straight, as lane changes and right
                        turns are prohibited by solid lines and markings. No specific stopping or waiting
                        areas are visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 956, 6.6 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary to
                        the right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the flow of traffic). | roles: the white dashed lines on both sides fit the
                        role of lane_line. | markings: the stop line marking is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes into or out of my lane.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes into or out of my lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane and can change left or right if necessary. You are
                        permitted to go straight ahead, but you must stop at the visible stop line before
                        proceeding.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 945, 6.62 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues straight, and
                        there are no immediate intersections or ramps visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows a large white painted symbol '30' (likely indicating
                        a lane number or a specific zone marker) painted across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed/solid lines indicating lane
                        separation). | roles: The white dashed/solid lines fit the role of lane_line. |
                        markings: The text marking is consistent with the boundaries. | unseen: No attributes
                        were reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes into or out of the adjacent
                        lane.
Step 5  Rule            right_boundary: A broken white line allows for lane changes into or out of the
                        adjacent lane.
Step 5  Rule            text:other: The painted text does not restrict or permit any specific movement for my
                        car.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is prohibited by a rule that was not seen.
Advice                  You are in the middle lane, and you are permitted to go straight or change lanes left
                        or right. Use the lane markings and boundaries to guide your lane changes safely.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed ['text:speed_limit']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 979, 6.96 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 2 shows double solid yellow lines marking the lane
                        boundaries.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid yellow lines on both sides indicate lane
                        separation). | roles: The solid yellow lines on both sides fit the role of lane_line.
                        | markings: The double solid yellow lines in Photo 2 are interpreted as
                        line:stop_yield, which is consistent with the lane boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the car to come to a
                        full stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow left_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right_boundary, which
                        prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no arrows or prohibitions in the
                        lane.
Step 6  turn_left       prohibited: prohibited, as there are no arrows or prohibitions in the lane, and no
                        left turn is indicated.
Step 6  turn_right      prohibited: prohibited, as there are no arrows or prohibitions in the lane, and no
                        right turn is indicated.
Step 6  u_turn          prohibited: prohibited, as there are no arrows or prohibitions in the lane, and no
                        U-turn is indicated.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a full stop before proceeding due to the stop-and-yield line. You are
                        restricted to going straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking', 'go_straight allowed without the stop that the STOP or 停 marking in
                        my lane requires']
Tokens                  in 3793, out 954, 6.89 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in
                        road configuration, though the exact nature is not fully clear from the immediate
                        view. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A dashed white line is visible next to my car. Photo 2: A dashed white line
                        is visible next to my car, and further ahead, it appears to transition into a solid
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to my car. Photo 2: A solid white line is
                        visible next to my car, and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line (separating my
                        lane from lane 1), and the right boundary is a lane line (separating my lane from lane
                        3). | roles: The left boundary is a dashed white lane line, and the right boundary is
                        a solid white lane line, which fits the role of lane_line. | markings: The white arrow
                        pointing straight ahead is present in my lane and is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes between lanes.
Step 5  Rule            right_boundary: The solid white line prohibits lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (contested, correct): The left boundary is a dashed white lane line, which
                        allows for lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white lane line,
                        which prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): The lane marking shows an arrow pointing straight ahead,
                        which allows going straight.
Step 6  turn_left       prohibited: The lane marking only shows an arrow pointing straight ahead, which
                        prohibits turning left.
Step 6  turn_right      prohibited: The lane marking only shows an arrow pointing straight ahead, which
                        prohibits turning right.
Step 6  u_turn          prohibited: The lane marking only shows an arrow pointing straight ahead, which
                        prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You should stay in the middle lane to proceed straight ahead, as lane changes to the
                        right are prohibited by the solid white line. Turning left, right, or making a U-turn
                        is prohibited by the lane arrow.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1021, 6.59 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into a city environment. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 1 shows a solid yellow line marking the right edge of
                        the lane next to my car, and a solid yellow line further ahead. Photo 2 shows a solid
                        yellow line marking the right edge of the lane next to my car, and a solid yellow line
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lines are lane lines). | markings: the line:stop_yield marking is
                        consistent with the boundaries and the general road context. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line indicates that lane changes across this boundary
                        are prohibited.
Step 5  Rule            right_boundary: The solid white line indicates that lane changes across this boundary
                        are prohibited.
Step 5  Rule            line:stop_yield: The presence of this marking requires the vehicle to come to a
                        complete stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left_boundary, which
                        prohibits lane changes.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right_boundary, which
                        prohibits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You must stop before the marked line before proceeding. You are restricted to going
                        straight in your current lane, and lane changes are prohibited.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3793, out 999, 6.61 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in China, and ahead there is an intersection or a road split
                        indicated by signage. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, this solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to my car. Further
                        ahead, this solid yellow line continues.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1: No markings are visible within my lane in the
                        visible stretch. Photo 2: No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane line (white
                        solid) and the right boundary is a lane line (yellow solid), which is consistent with
                        my lane being in the middle of three lanes. | roles: The left boundary is a white
                        solid lane line, and the right boundary is a yellow solid lane line, which fits the
                        roles of lane_line. | markings: There are no markings observed in my lane, so there is
                        no contradiction. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where my car must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left, as crossing
                        it is prohibited.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane line on the
                        right, as crossing it is prohibited.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no action is
                        allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides, and there are no specific markings for
                        turning or waiting.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3793, out 1063, 6.86 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, there is a pedestrian crossing and the road
                        continues straight, with a bus stop area on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car, and further ahead, it appears
                        to be a solid white line continuing. Photo 2: A solid white line is visible next to my
                        car, and further ahead, it appears to be a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car, and further ahead, it appears
                        to be a solid yellow line continuing. Photo 2: A solid yellow line is visible next to
                        my car, and further ahead, it appears to be a solid yellow line continuing.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line marking the stop line is visible
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a lane_line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane_line, and the right boundary is a solid
                        yellow lane_line, which fits the roles. | markings: The stop line marking is
                        consistent with the boundaries and general road markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates that my car must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane_line on the left,
                        as per the rule that prohibits crossing lane boundaries.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow lane_line on the
                        right, as per the rule that prohibits crossing lane boundaries.
Step 6  go_straight     allowed (correct): allowed because there are no markings prohibiting straight movement
                        in my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane ahead.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You must stop at the solid white line before proceeding. You are restricted to going
                        straight ahead in your current lane, as lane changes and turns are not permitted by
                        the markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 3793, out 1076, 6.83 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        junction or a continuation of the road with lane markings indicating movement options.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car, and Photo 2 shows a broken yellow
                        line next to my car. Further ahead, Photo 1 shows a broken yellow line continuing, and
                        Photo 2 shows a broken yellow line continuing.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a solid yellow arrow pointing straight ahead in
                        the lane immediately to the right of my lane. Photo 1 shows a solid yellow arrow
                        pointing straight ahead in the lane immediately to the right of my lane.;
                        arrow:straight (full): Photo 2 shows a solid yellow arrow pointing straight ahead in
                        my lane. Photo 1 shows a solid yellow arrow pointing straight ahead in my lane.;
                        arrow:straight (full): Photo 2 shows a solid yellow arrow pointing straight ahead in
                        the lane immediately to the left of my lane. Photo 1 shows a solid yellow arrow
                        pointing straight ahead in the lane immediately to the left of my lane.;
                        arrow:straight (full): Photo 2 shows a solid yellow arrow pointing straight ahead in
                        the lane furthest to the right. Photo 1 shows a solid yellow arrow pointing straight
                        ahead in the lane furthest to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane line (white solid) and the right
                        boundary is a lane line (yellow dashed), which is consistent with my lane being in the
                        middle. | roles: The left boundary is a white solid lane line, and the right boundary
                        is a yellow dashed lane line, which fits the roles of lane_line. | markings: The
                        markings show straight arrows in all visible lanes, which is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane on the
                        left.
Step 5  Rule            right_boundary: The broken yellow line permits crossing into the adjacent lane on the
                        right.
Step 5  Rule            arrow:straight: The arrow permits movement straight ahead.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white left boundary
                        line, which prohibits crossing into the adjacent lane on the left.
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken yellow right boundary
                        line, which permits crossing into the adjacent lane on the right.
Step 6  go_straight     allowed (contested, correct): allowed by the solid yellow arrow in my lane, which
                        permits movement straight ahead.
Step 6  turn_left       prohibited: prohibited by the solid yellow arrow in my lane, which prohibits movement
                        other than straight ahead.
Step 6  turn_right      prohibited: prohibited by the solid yellow arrow in my lane, which prohibits movement
                        other than straight ahead.
Step 6  u_turn          prohibited: prohibited by the solid yellow arrow in my lane, which prohibits movement
                        other than straight ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are currently in the middle lane, which is marked to proceed straight ahead. You
                        may change to the right lane, but changing to the left is prohibited. Use the middle
                        lane to go straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 1288, 7.31 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection visible in
                        the distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid white
                        line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Photo 1 shows a broken white line further ahead. Photo 2 shows a
                        broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating I am in the leftmost lane of the three visible lanes). | roles:
                        the color and pattern of each boundary fit the role given to it (solid white lane line
                        on the left, dashed white lane line on the right). | markings: the lane markings list
                        is empty, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 6  change_left     prohibited (contested, correct): allowed: The left boundary is a solid white lane
                        line, which prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, which
                        permits changing right.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change right, but changing
                        left is prohibited by the solid white line. No specific stopping or turning areas are
                        marked.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 945, 6.45 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a change in
                        road configuration, though the exact nature is unclear from the visible markings.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it appears to transition to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it appears to transition to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right boundary
                        of my lane near my car. Photo 1 shows this line continuing ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        a lane between other lanes of my direction). | roles: the color (white) and pattern
                        (dashed/solid) of each boundary fit the role of a lane_line. | markings: the stop line
                        marking is consistent with the boundaries and general road markings. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding, if required by traffic control.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows for
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
Step 6  go_straight     allowed (correct): allowed: There are no markings in my lane prohibiting straight
                        movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane governing a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane governing a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and can change left or right, and you are permitted to go
                        straight. Be aware that the lane markings ahead suggest a stop line, so prepare to
                        stop if required by traffic conditions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 995, 23.37 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road appears to continue straight,
                        possibly leading to an intersection or a continuation of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed yellow line next to my car, and a dashed yellow line further
                        ahead. Photo 2 shows a dashed yellow line next to my car, and a dashed yellow line
                        further ahead.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the lane boundary next
                        to my car, and a solid white line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane line on left, yellow dashed line for lane line on right). |
                        markings: the stop line marking is consistent with the lane boundaries and does not
                        contradict any other markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it.
Step 5  Rule            right_boundary: The dashed yellow line indicates the boundary of my lane and permits
                        crossing it when safe.
Step 5  Rule            line:stop_line: The stop line indicates that my car must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        prohibits changing left according to the rule for solid lane lines.
Step 6  change_right    allowed (correct): The right boundary is a dashed yellow line, which permits changing
                        right according to the rule for dashed lane lines.
Step 6  go_straight     stop_first (contested, label allowed): The lane has no arrow, and the boundaries do
                        not prohibit going straight, but the stop line requires stopping first.
Step 6  turn_left       stop_first: The lane has no arrow, and the boundaries do not prohibit turning left,
                        but the stop line requires stopping first.
Step 6  turn_right      stop_first: The lane has no arrow, and the boundaries do not prohibit turning right,
                        but the stop line requires stopping first.
Step 6  u_turn          stop_first: The lane has no arrow, and the boundaries do not prohibit U-turning, but
                        the stop line requires stopping first.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding past the stop line. You are
                        permitted to change right, but changing left is prohibited by the solid white line.
                        You may proceed straight, turn left, turn right, or U-turn after stopping.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3793, out 1045, 6.34 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, it transitions to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, it transitions to a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line just
                        ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am
                        between two lanes of my direction). | roles: the color and pattern of both boundaries
                        (white, dashed/solid) fit the role of lane_line. | markings: the stop line marking is
                        consistent with the boundaries and general road markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The dashed white line allows lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line allows lane changes into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed: allowed: The left boundary is a dashed white line, which allows lane changes.
Step 6  change_right    allowed: allowed: The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the boundaries are
                        dashed. You may proceed straight, but you must stop at the visible stop line before
                        proceeding through the intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 966, 22.59 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection or a major road ahead. There
                        are multiple lanes visible in my direction near the bottom of the photo. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Further ahead, Photo 1 shows a solid yellow line continuing. Photo 2
                        shows a solid yellow line continuing.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 1 shows a solid yellow line on the left boundary. Photo
                        2 shows a solid yellow line on the left boundary.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on the left and a lane
                        line on the right. | roles: The left boundary is a yellow solid line, which functions
                        as a lane_line separating my lane from the adjacent lane. The right boundary is a
                        white solid line, which functions as a lane_line separating my lane from the adjacent
                        lane. | markings: The line:stop_yield marking is present in my lane and is consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the car to come to a
                        complete stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line on the left
                        boundary and the rule that a solid yellow line prohibits crossing into the adjacent
                        lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        boundary and the rule that a solid white line prohibits crossing into the adjacent
                        lane.
Step 6  go_straight     stop_first (contested, label allowed): allowed because there are no markings
                        prohibiting straight movement in my lane.
Step 6  turn_left       prohibited: prohibited because there are no markings allowing a left turn in my lane.
Step 6  turn_right      prohibited: prohibited because there are no markings allowing a right turn in my lane.
Step 6  u_turn          prohibited: prohibited because there are no markings allowing a U-turn in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a rule.
Advice                  You must come to a complete stop before proceeding in your lane. Lane changes are
                        prohibited due to solid lines on both sides, and you are restricted to going straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1076, 7.07 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road. Ahead, the road continues into the distance with
                        multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and a solid yellow line further
                        ahead. Photo 2 shows a solid yellow line next to my car, and a solid yellow line
                        further ahead.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a solid yellow line marking the right
                        boundary, and a solid white line marking the left boundary. No other markings are
                        visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line is a lane_line, yellow solid line is a lane_line). | markings: the
                        markings (stop line) agree with the boundaries (no contradiction found). | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane_line on the left
                        boundary.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow lane_line on the right
                        boundary.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides, and there are no markings to indicate
                        specific turning maneuvers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 993, 7.21 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the highway. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane line (yellow), and the right
                        boundary is a lane line (white), which is consistent with my lane being the middle
                        lane. | roles: The left boundary is a yellow solid lane line, and the right boundary
                        is a white solid lane line, which fits the role of lane_line. | markings: The stop
                        line is present in my lane, which is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where the vehicle must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow lane line on the left
                        boundary, as per the rule that a solid yellow line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line on the right
                        boundary, as per the rule that a solid white line prohibits crossing into the adjacent
                        lane.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a rule from step 5.
Advice                  You must come to a complete stop at the stop line before proceeding. You are
                        restricted to going straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 1011, 6.78 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a solid white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a lane_line, indicating my lane is between two lanes of my direction. |
                        roles: The left boundary is a solid white lane_line, and the right boundary is a solid
                        yellow lane_line, which fits the roles. | markings: The solid white arrow pointing
                        straight ahead in my lane is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to the left.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary of my lane and prohibits
                        crossing it to the right.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane_line on the left
                        boundary.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow lane_line on the
                        right boundary.
Step 6  go_straight     allowed (correct): allowed by the solid white arrow pointing straight ahead in my
                        lane.
Step 6  turn_left       prohibited (correct): prohibited by the solid white arrow pointing straight ahead in
                        my lane.
Step 6  turn_right      prohibited (correct): prohibited by the solid white arrow pointing straight ahead in
                        my lane.
Step 6  u_turn          prohibited (correct): prohibited by the solid white arrow pointing straight ahead in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 963, 6.75 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass/bridge structure, suggesting
                        the road continues forward, possibly towards an intersection or another section of the
                        road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows the line further ahead is solid white. Photo 2 shows the line
                        further ahead is solid white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows the line further ahead is solid white. Photo 2 shows the line
                        further ahead is solid white.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The straight arrow in my lane is consistent with the lane boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, which is a solid
                        white line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the right_boundary, which is a solid
                        white line.
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking, which permits proceeding
                        straight ahead.
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        left turn.
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        right turn.
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking, which does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane to proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 962, 6.15 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching a junction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
                        Photo 2 shows the same white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane lines, indicating I am in
                        the middle lane of 3). | roles: the white dashed lines fit the role of lane_line. |
                        markings: the straight arrow in my lane is consistent with the lane boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            arrow:straight: The straight arrow indicates that proceeding straight ahead is
                        permitted in this lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        and the rule allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a straight arrow, and
                        the rule allows proceeding straight ahead.
Step 6  turn_left       prohibited: prohibited: The lane marking only shows a straight arrow, and the rule
                        prohibits turning left.
Step 6  turn_right      prohibited: prohibited: The lane marking only shows a straight arrow, and the rule
                        prohibits turning right.
Step 6  u_turn          prohibited: prohibited: The lane marking only shows a straight arrow, and the rule
                        prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to go straight, and you may
                        change lanes left or right if safe. Turning left, turning right, or making a U-turn is
                        prohibited in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3793, out 982, 6.12 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        junction or a continuation of the road with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary
                        ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane_line, yellow solid line for center_line). | markings: the
                        line:stop_line marking is consistent with the boundaries and does not contradict any
                        other markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it to the left.
Step 5  Rule            right_boundary: The solid yellow line indicates a separation from opposing traffic and
                        prohibits crossing it.
Step 5  Rule            line:stop_line: The stop line indicates that my car must come to a complete stop
                        before proceeding past this line.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line boundary
                        (Step 5).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow center_line boundary
                        (Step 5).
Step 6  go_straight     stop_first (contested, label allowed): allowed because there are no arrows or
                        prohibitions in my lane, but it is governed by the stop_line (Step 5).
Step 6  turn_left       stop_first: prohibited because there are no arrows or prohibitions in my lane, and the
                        stop_line requires a stop first (Step 5).
Step 6  turn_right      stop_first: prohibited because there are no arrows or prohibitions in my lane, and the
                        stop_line requires a stop first (Step 5).
Step 6  u_turn          stop_first: prohibited because there are no arrows or prohibitions in my lane, and the
                        stop_line requires a stop first (Step 5).
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane (Step 5).
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before the stop line. Since there are no lane
                        markings indicating specific turns, you may proceed straight, turn left, turn right,
                        or make a U-turn after stopping, provided the intersection allows it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 3793, out 1054, 7.38 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection. There are multiple lanes
                        visible in my direction near the bottom of the photo. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows no markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (4) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line. | markings: the stop line marking is consistent
                        with the boundaries and the general road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (WRONG, label prohibited): allowed, because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed, because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the second lane from the left. You may change lanes in either direction as
                        the boundaries are dashed. You may proceed straight through the intersection, but you
                        must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3793, out 955, 6.1 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where lanes diverge/end, though the exact nature is not fully clear from the visible
                        markings. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it appears to transition into a solid
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it appears to transition into a solid
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white dashed line is visible across the lane ahead,
                        indicating a lane division or change area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (1) agree with the boundary roles, as both boundaries are lane lines. | roles: The
                        white dashed lines on both sides fit the role of lane_line. | markings: The stop line
                        marking is consistent with the lane boundaries. | unseen: No attributes were reported
                        that were not seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection or area ahead.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings prohibiting going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change left or right, and you may proceed
                        straight ahead. You must stop before the visible stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 958, 7.41 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or an area where lanes are
                        marked for turning/merging. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows white arrows pointing straight ahead in my lane.;
                        arrow:straight (full): Photo 1 shows white arrows pointing straight ahead in the lane
                        to my left.; arrow:straight (full): Photo 1 shows white arrows pointing straight ahead
                        in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The color and pattern of both boundaries (white,
                        dashed) fit the role of a lane_line. | markings: The arrows in my lane (straight
                        ahead) are consistent with the boundaries (lane_lines) and do not contradict any other
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            arrow:straight: The arrow in my lane permits movement straight ahead.
Step 6  change_left     allowed (contested, correct): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane marking shows an arrow pointing
                        straight ahead.
Step 6  turn_left       prohibited: Prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  turn_right      prohibited: Prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  u_turn          prohibited: Prohibited because the lane marking only shows an arrow pointing straight
                        ahead.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the second lane from the left. You are permitted to go straight, change
                        left, or change right. Turning left, right, or making a U-turn is prohibited by the
                        lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 1071, 6.87 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is a clear intersection where traffic
                        is moving forward. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and further ahead, it appears to be
                        a dashed white line. Photo 2 shows a dashed white line next to my car, and further
                        ahead, it is a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrow in my lane agrees with the boundaries (it governs movement within
                        the lane) | unseen: no | result: consistent
Step 5  Rule            left_boundary: This solid white line prohibits crossing into the adjacent lane on the
                        left.
Step 5  Rule            right_boundary: This dashed white line permits crossing into the adjacent lane on the
                        right.
Step 5  Rule            arrow:straight: This arrow permits my car to proceed straight ahead through the
                        intersection.
Step 6  change_left     prohibited (correct): prohibited by the solid white line on the left boundary, as per
                        the rule for a solid lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white line on the right
                        boundary, as per the rule for a dashed lane line.
Step 6  go_straight     allowed (correct): allowed by the white arrow pointing straight ahead in my lane, as
                        per the rule for a lane-use arrow.
Step 6  turn_left       prohibited (correct): prohibited by the white arrow pointing straight ahead in my
                        lane, as per the rule for a lane-use arrow.
Step 6  turn_right      prohibited (correct): prohibited by the white arrow pointing straight ahead in my
                        lane, as per the rule for a lane-use arrow.
Step 6  u_turn          prohibited (correct): prohibited by the white arrow pointing straight ahead in my
                        lane, as per the rule for a lane-use arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are currently in the middle lane. You may change right, proceed straight, but
                        turning left, turning right, or making a U-turn is prohibited by the lane markings.
                        Use the middle lane for straight travel.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3793, out 860, 5.71 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection indicated by traffic
                        lights and road markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the arrow in my lane shows straight movement, which is consistent with the
                        lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited by the solid white line on the left boundary, as per
                        the rule for solid lane lines.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white line on the right
                        boundary, as per the rule for dashed lane lines.
Step 6  go_straight     allowed (correct): allowed because the lane marking shows a straight arrow, and no
                        other marking prohibits it.
Step 6  turn_left       prohibited (correct): prohibited because the lane marking only shows a straight arrow,
                        not a left turn.
Step 6  turn_right      prohibited (correct): prohibited because the lane marking only shows a straight arrow,
                        not a right turn.
Step 6  u_turn          prohibited (correct): prohibited because the lane marking only shows a straight arrow,
                        not a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid white line. No specific stopping or waiting areas are marked
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3793, out 937, 6.1 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street in a built-up area, and the road continues ahead into the
                        distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A white dashed line is visible further ahead in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line as lane_line, yellow solid line as center_line). | markings: the
                        line:stop_line is consistent with the lane boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line indicates the edge of the lane and prohibits
                        crossing it.
Step 5  Rule            right_boundary: The solid yellow line indicates a separation between traffic
                        directions and prohibits crossing it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane_line on the left boundary.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow center_line on the
                        right boundary.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You must stop at the visible stop line before proceeding. You are restricted to going
                        straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3793, out 926, 6.26 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a junction or a continuation
                        of the road with traffic signals visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: The solid white lines on both sides fit the role of lane_line. |
                        markings: The partial visibility of a stop line in Photo 1 is consistent with the
                        general view. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary, which prohibits
                        lane changes.
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary, which prohibits
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings allowing or prohibiting a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no rule
                        prohibits an action that is allowed.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides of your lane. Be prepared to stop at
                        the visible stop line ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3793, out 955, 6.02 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection or a large crossing area
                        ahead. There are multiple lanes visible in my direction near the bottom of the photo.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large green arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a large green arrow pointing straight
                        ahead in the lane to my left.; arrow:straight (full): Photo 2 shows a large green
                        arrow pointing straight ahead in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane lines). | roles: The color
                        and pattern of both boundaries (white dashed lines) fit the role of a lane_line. |
                        markings: The arrows in my lane (straight ahead) agree with the boundaries (dashed
                        lines allow lane changes). | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking shows a green arrow pointing
                        straight ahead.
Step 6  turn_left       prohibited (correct): Prohibited because the lane marking only shows an arrow pointing
                        straight ahead.
Step 6  turn_right      prohibited (correct): Prohibited because the lane marking only shows an arrow pointing
                        straight ahead.
Step 6  u_turn          prohibited (correct): Prohibited because the lane marking only shows an arrow pointing
                        straight ahead.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and you are permitted to go straight, change left, or
                        change right. You should proceed straight ahead as indicated by the lane arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3793, out 1089, 7.59 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues straight, and there is a large bus in the center of the visible lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues. Photo 2: A solid white line is visible next to my car. Further ahead,
                        this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, this solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to my car. Further
                        ahead, this solid yellow line continues.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1: No markings are visible within my lane in the
                        visible stretch.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line on the left, yellow solid line on the right). | markings: the lane
                        markings list is consistent with the boundaries (no markings contradict the solid
                        boundaries). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary between my lane and the
                        adjacent lane, prohibiting lane changes across it.
Step 5  Rule            right_boundary: The solid yellow line indicates the boundary between my lane and the
                        adjacent lane, prohibiting lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left, as per the
                        rule for lane lines.
Step 6  change_right    prohibited (correct): prohibited by the solid yellow lane line on the right, as per
                        the rule for lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides of your lane. Be aware of the stop line
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3793, out 1024, 6.37 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major thoroughfare, and the road
                        continues ahead into the distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1: No painted line visible immediately next to the car. The boundary is formed
                        by a concrete barrier/retaining wall. Photo 2: No painted line visible immediately
                        next to the car. The boundary is formed by a concrete barrier/retaining wall.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1: No painted line visible immediately next to the car. The boundary is formed
                        by a metal guardrail/barrier. Photo 2: No painted line visible immediately next to the
                        car. The boundary is formed by a metal guardrail/barrier.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and ego_lane_index
                        (1) agree with the boundary roles (both are edge_lines). | roles: the roles
                        (edge_line) fit the observations (concrete/metal barriers). | markings: no markings
                        were reported, so there is no agreement to check. | unseen: no attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The concrete barrier defines the edge of the roadway on the left.
Step 5  Rule            right_boundary: The metal guardrail defines the edge of the roadway on the right.
Step 6  change_left     prohibited (correct): prohibited: The left boundary is an edge_line, and no markings
                        allow a lane change.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is an edge_line, and no markings
                        allow a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings (arrow or prohibited-movement
                        marking) in my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no markings (arrow or prohibited-movement
                        marking) in my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no markings (arrow or prohibited-movement
                        marking) in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in a single lane with no lane markings to restrict movement. You are allowed
                        to proceed straight ahead, but lane changes are prohibited by the physical barriers on
                        both sides. No specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 3793, out 926, 5.95 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a transition area or
                        intersection, indicated by the road markings and the presence of a dedicated bike lane
                        area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible further ahead. Photo 2: A dashed white line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2: A red painted area with a white bicycle symbol is
                        visible in the foreground, extending across the right side of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane line, and the
                        right boundary is a lane line, which is consistent with my lane being in the middle of
                        three lanes. | roles: The left boundary is a solid white lane line, and the right
                        boundary is a dashed white lane line, which fits the roles of lane_line. | markings:
                        The red area with the bicycle symbol is noted as an area marking, and it is consistent
                        with the boundaries and lane structure. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line permits crossing into the adjacent lane.
Step 5  Rule            area:channelizing: The bicycle symbol indicates that this area is reserved for
                        bicycles.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed white lane line,
                        which permits changing right.
Step 6  go_straight     allowed (contested, correct): Nothing in my lane restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The boundaries and markings were settled in the close-up check, and no action is
                        allowed against a prohibition.
Advice                  You are in the middle lane. You may proceed straight or change right, but changing
                        left is prohibited by the solid white line. Be aware that the area to your right is
                        designated for bicycles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions False, unsafe ['change_right'], citation
                        None, contradictions []
Tokens                  in 3793, out 968, 5.92 s
```
