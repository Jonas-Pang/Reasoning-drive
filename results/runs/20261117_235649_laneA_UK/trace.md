# Reasoning of lane run 20261117_235649_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic
                        appears to be moving through or preparing to turn. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary on
                        the left side of my lane, and a white dashed line marking the lane boundary on the
                        right side of my lane. Photo 1 shows the same lines further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The stop line is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes in either direction,
                        and you are permitted to go straight through the intersection. You must stop before
                        the solid white line at the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['symbol:bike']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3815, out 995, 6.57 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching a junction or intersection. There are multiple
                        lanes visible in my direction of travel near the bottom of the photo. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white dashed line marking the stop line is visible
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed/solid
                        lines fit the role of lane_line. | markings: The stop line is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes across this boundary.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes across this boundary.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a white
                        dashed line, which permits lane changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in the lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and you are permitted to change lanes left or right, or
                        proceed straight ahead. You must stop at the visible stop line before entering the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions []
Tokens                  in 3815, out 992, 6.61 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, leading towards what appears to be a
                        junction or crossing area. My car is in one of the lanes near the bottom of the photo.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane. Photo 2 also shows a white arrow pointing right ahead in my lane.; symbol:bike
                        (full): Photo 2 shows a white bicycle symbol in my lane. Photo 2 also shows a white
                        bicycle symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both are lane_lines, indicating my lane is between
                        two other lanes). | roles: The white dashed lines fit the role of lane_line. |
                        markings: The arrows and bicycle symbols are consistent with the lane boundaries and
                        each other. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            arrow:straight_right: This arrow permits movement straight ahead and turning right.
Step 5  Rule            symbol:bike: This symbol indicates a shared space or designated area for bicycles.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): The lane marking includes an arrow pointing straight ahead, which
                        allows going straight.
Step 6  turn_left       prohibited (correct): The lane marking does not show an arrow permitting a left turn,
                        and there is no indication of a two-way left-turn lane, so it is prohibited.
Step 6  turn_right      allowed (WRONG, label prohibited): The lane marking includes an arrow pointing right
                        ahead, which allows turning right.
Step 6  u_turn          prohibited (correct): The lane marking does not show an arrow permitting a U-turn, and
                        there is no indication of a two-way left-turn lane, so it is prohibited.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a waiting area or a two-way left-
                          turn lane ahead of my lane, so it is not applicable.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in a lane that allows you to go straight or turn right, and you may change
                        lanes in either direction. Be aware that this lane also accommodates bicycles.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['turn_right'], citation None, contradictions []
Tokens                  in 3815, out 1147, 8.35 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there appears to be a junction
                        or intersection where the road continues and other lanes are present. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car, and Photo 2 shows a broken yellow
                        line next to my car. Further ahead, Photo 1 shows a broken yellow line continuing, and
                        Photo 2 shows a broken yellow line continuing.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a solid yellow line marking the right
                        boundary, and Photo 1 shows a broken yellow line marking the right boundary. The line
                        next to my car is the broken yellow line.
Step 4  Cross-check     close_up: Photo 2 shows the line next to my car as a broken yellow line, while Photo 1
                        shows it as a broken yellow line. The line further ahead is consistent in both photos.
                        No correction needed. | position: The left boundary is a lane line, indicating another
                        lane to the left. The right boundary is a lane line, indicating another lane to the
                        right. My lane is the middle lane (index 2) out of 3 lanes, which is consistent with
                        having a lane line on both sides. | roles: The left boundary is a solid white lane
                        line, and the right boundary is a dashed yellow lane line, which fits the roles of
                        lane_line. | markings: The stop line is visible in Photo 2, and it is consistent with
                        the boundaries. No contradictions found. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed yellow lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        proceeding.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (correct): The right boundary is a dashed yellow lane line, which permits
                        changing right.
Step 6  go_straight     allowed (contested, correct): Nothing in my lane prohibits going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern turning left.
Step 6  turn_right      not_applicable: No markings in my lane govern turning right.
Step 6  u_turn          not_applicable: No markings in my lane govern U-turning.
Step 6  enter_waiting_areanot_applicable: No markings in my lane govern entering a waiting area.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        before the visible stop line if you intend to stop for any reason.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 1074, 7.66 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic
                        appears to be moving through or approaching a junction. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary
                        ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: the color (white) and pattern (dashed)
                        of both boundaries fit the role of lane_line. | markings: the stop line marking is
                        consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            line:stop_line: A stop line indicates that vehicles must come to a complete stop
                        before proceeding into the intersection.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and the rule allows lane changes when safe.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, and the rule allows lane changes when safe.
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
Advice                  You are in the left lane of two lanes. You may change lanes when safe, and you may
                        proceed straight through the intersection. You must come to a complete stop before
                        crossing the stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 970, 6.54 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there appears to be an
                        intersection or a junction where traffic flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a dashed white line marking the right boundary of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane line separating
                        it from the leftmost lane, and the right boundary is a lane line separating it from
                        the rightmost lane. This is consistent. | roles: The left boundary is a solid white
                        lane line, and the right boundary is a dashed white lane line. This fits the role of
                        lane_line. | markings: The stop line is visible in Photo 2 and is consistent with the
                        lane boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which permits
                        changing right.
Step 6  go_straight     allowed (contested, correct): Nothing in my lane prohibits going straight.
Step 6  turn_left       allowed: Nothing in my lane prohibits turning left.
Step 6  turn_right      allowed: Nothing in my lane prohibits turning right.
Step 6  u_turn          allowed: Nothing in my lane prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: No marking governs entering a waiting area.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You may change right, go straight, turn left, turn right, or perform a U-turn. You
                        must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3815, out 970, 7.12 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there appears to be a
                        junction or a continuation of the road with lane markings indicating possible turns.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows the white dashed line continuing,
                        and Photo 2 shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white dashed line marking the lane
                        boundary to the left, and a white dashed line marking the lane boundary to the right.
                        Further ahead, Photo 2 shows white arrows painted on the road surface in my lane,
                        pointing straight ahead and to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The boundaries are lane lines, which is consistent with my lane
                        being one of three lanes. | roles: The white dashed lines on both sides are consistent
                        with the role of a lane_line. | markings: The arrows in my lane (straight and right)
                        are consistent with the boundaries (dashed lines allow lane changes/straight movement)
                        and the general road context. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            arrow:straight_right: The arrows indicate that going straight and turning right are
                        permitted movements from this lane.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows for lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking includes an arrow pointing
                        straight ahead, and the boundaries allow for movement.
Step 6  turn_left       prohibited: prohibited: There is no arrow indicating a left turn in my lane.
Step 6  turn_right      allowed: allowed: The lane marking includes an arrow pointing to the right, and the
                        boundaries allow for movement.
Step 6  u_turn          not_applicable: not_applicable: There are no markings or boundaries governing a U-turn
                        in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight or turning right. You may
                        change lanes left or right as the boundaries are dashed. Do not attempt to turn left
                        from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3815, out 1058, 7.74 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary on
                        the right side, which is the right boundary of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The stop line is visible and is consistent with the
                        lane boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows for
                        lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
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
Advice                  You are in the middle lane and can change left or right if necessary. You may proceed
                        straight through the intersection, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 997, 6.31 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a pedestrian crossing leading to an
                        intersection or crossing area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows the line further ahead is a solid white line. Photo 2 shows
                        the line further ahead is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Photo 1 shows the line further ahead is a broken white line. Photo 2
                        shows the line further ahead is a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the boundary to the
                        right. Photo 2 shows a white solid line marking the boundary to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is a lane_line, indicating my lane is the leftmost of the two lanes visible.
                        | roles: The left boundary is a solid white lane_line, and the right boundary is a
                        dashed white lane_line, which fits the role of lane_lines separating adjacent lanes. |
                        markings: The stop line is located at the end of the lane, consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates that my car must come to a complete stop
                        before proceeding into the intersection area.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line, as
                        per the rule for solid lane lines.
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed white right boundary
                        line, as per the rule for dashed lane lines.
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
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You must stop at the white stop line before proceeding. You may go straight or change
                        right, but changing left is prohibited by the solid line. Use the right lane if you
                        intend to change right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1069, 6.69 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection with a
                        pedestrian crossing and a roundabout. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is a white dashed line. Photo 2
                        shows the line further ahead is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the edge of the lane
                        near my car. Photo 2 shows a white dashed line marking the edge of the lane further
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the line:stop_line marking is
                        consistent with the lane boundaries and does not contradict any other markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes into or out of my lane.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes into or out of my lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows for lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road approaching an intersection with a
                        roundabout. You may change lanes in either direction, and you are permitted to go
                        straight. You must stop at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1040, 6.66 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is a junction or area where traffic flow is directed by lane markings. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line further ahead. Photo 2 shows a dashed white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing right ahead in the
                        lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating two lanes in my direction. | roles: The solid
                        white line on the left and the dashed white line on the right fit the role of
                        lane_line. | markings: The arrow in my lane (straight) is consistent with the lane
                        markings, and the arrow in the adjacent lane (right) is also visible and consistent. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line on the left prohibits changing into the adjacent
                        lane.
Step 5  Rule            right_boundary: The dashed white line on the right permits changing into the adjacent
                        lane.
Step 5  Rule            arrow:straight: The arrow in my lane permits going straight ahead.
Step 5  Rule            arrow:right: The arrow in the adjacent lane permits turning right.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white left boundary
                        line, as per the rule for solid lane lines.
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary line, as per the rule
                        for dashed lane lines.
Step 6  go_straight     allowed (correct): allowed by the white arrow in my lane, as per the rule for lane-use
                        arrows.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited because there is no arrow or marking in
                        my lane permitting a left turn.
Step 6  turn_right      prohibited (correct): prohibited because there is no arrow or marking in my lane
                        permitting a right turn.
Step 6  u_turn          prohibited (correct): prohibited because there is no arrow or marking in my lane
                        permitting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane in my lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the left lane and are permitted to go straight or change right. Do not
                        attempt to change left, turn left, or make a U-turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe [], citation None, contradictions ['leftmost lane, but a lane line on the
                        left', 'turn_right prohibited although an arrow shows it']
Tokens                  in 3815, out 1083, 9.15 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection or junction
                        where the road continues and meets other traffic flow. There are two lanes visible in
                        my direction near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the stop line ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction). | roles: the color and pattern of
                        both boundaries (white dashed lines) fit the role of a lane_line. | markings: the stop
                        line marking is consistent with the boundaries and general road markings. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and the rule
                        allows lane changes when safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the rule
                        allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road approaching an intersection. You may
                        change lanes when safe, and you are permitted to go straight. You must stop at the
                        marked stop line before proceeding through the junction.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1041, 7.04 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        where traffic is moving forward and turning. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.;
                        arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my left.;
                        arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to my
                        right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The color and pattern of both boundaries (white
                        dashed lines) fit the role of lane_line. | markings: The arrows in my lane (straight
                        and right) are consistent with the lane boundaries and the general flow of traffic. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            arrow:straight: This marking allows my car to proceed straight ahead.
Step 5  Rule            arrow:right: This marking allows my car to turn right.
Step 5  Rule            arrow:left: This marking allows the vehicle in the adjacent left lane to turn left.
Step 5  Rule            arrow:right: This marking allows the vehicle in the adjacent right lane to turn right.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking includes an arrow pointing
                        straight ahead.
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited because there is no arrow or marking in
                        my lane permitting a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): Allowed because the lane marking includes an arrow
                        pointing right.
Step 6  u_turn          prohibited (correct): Prohibited because there is no arrow or marking in my lane
                        permitting a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane ahead.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, proceed straight, or turn right at the
                        intersection. Do not attempt to turn left or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['arrow:straight_left']),
                        actions False, unsafe ['turn_right'], citation None, contradictions ['turn_left
                        prohibited although an arrow shows it']
Tokens                  in 3815, out 1211, 7.46 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection where the road
                        appears to split or continue. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A white dashed line marking the edge of the lane is
                        visible further ahead, leading into the intersection area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in this direction). | roles: the color and pattern of
                        both boundaries (white dashed lines) fit the role of a lane_line. | markings: the stop
                        line marking is consistent with the boundaries and the general road layout. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
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
Advice                  You are in the left lane of a two-lane road approaching an intersection. You may
                        change lanes in either direction, and you are permitted to go straight. You must stop
                        at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 991, 6.76 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, leading towards what appears to be a
                        junction or continuation of the road. My car is in one of the lanes near the bottom of
                        the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line further ahead. Photo 2 shows a broken white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:merge_right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating my lane is between two lanes of my direction. |
                        roles: The solid white line on the left and the dashed white line on the right both
                        fit the role of a lane_line. | markings: The arrows (straight and merge_right) are
                        present in my lane and are consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: This arrow permits my car to proceed straight ahead.
Step 5  Rule            arrow:merge_right: This arrow permits my car to merge right into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        which prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which permits
                        changing right.
Step 6  go_straight     allowed (correct): allowed: The lane marking includes an arrow showing straight ahead,
                        and no other marking prohibits it.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: There are no markings in my lane
                        allowing a left turn.
Step 6  turn_right      prohibited (correct): prohibited: There are no markings in my lane allowing a right
                        turn.
Step 6  u_turn          prohibited (correct): prohibited: There are no markings in my lane allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane ahead.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid white line. No specific stopping or waiting areas are marked
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:merge_right', 'arrow:straight'], missed ['arrow:straight_left']), actions
                        False, unsafe [], citation None, contradictions []
Tokens                  in 3815, out 1028, 7.3 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road, and ahead there is a pedestrian crossing and what appears to be
                        an intersection or crossing area. My car is in the lane closest to the left side of
                        the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line further ahead. Photo 2 shows a broken white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line further ahead, which is the
                        right boundary.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is edge_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (solid white edge_line, dashed white lane_line) | markings: the line:stop_line marking
                        agrees with the boundaries (it is located at the end of the lane defined by the right
                        boundary) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white edge line indicates the boundary of the roadway.
Step 5  Rule            right_boundary: The dashed white lane line indicates that lane changes are permitted
                        where the line is visible.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is an edge_line, and
                        no markings prohibit changing left.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed
                        lane_line, and the rule allows lane changes where the line is visible.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the lane continues until the stop line.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions []
Tokens                  in 3815, out 986, 7.1 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where the road configuration changes. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the text:bus marking is consistent with the lane boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            text:bus: This marking indicates that this lane is reserved for buses.
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white lane line on the
                        left boundary.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no markings governing turning
                        movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings governing turning
                        movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings governing turning
                        movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to its restrictions. You may change right,
                        go straight, or stay in your lane, but you cannot change left or turn in any direction
                        as no markings permit it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 924, 6.15 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be an
                        intersection or a point where lanes diverge/merge. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color and pattern of
                        both boundaries (white dashed lines) fit the role of lane_line. | markings: the
                        no_turn:left marking is present in my lane and is consistent with the lane boundaries.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            no_turn:left: This marking prohibits my car from turning left from my lane.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight.
Step 6  turn_left       prohibited: prohibited: The marking 'no_turn:left' in my lane prohibits turning left.
Step 6  turn_right      allowed: allowed: There are no markings in my lane prohibiting turning right.
Step 6  u_turn          allowed: allowed: There are no markings in my lane prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are allowed to go straight or turn right, and you can
                        change lanes in either direction. However, you are prohibited from turning left from
                        this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 3815, out 945, 6.51 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction as my car.
                        Ahead, there is an intersection where traffic appears to be directed. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane lines). | roles: The color
                        and pattern of both boundaries (white dashed) fit the role of a lane line. | markings:
                        The arrows (straight and right) are present in my lane and are consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            arrow:straight: The arrow indicating straight ahead allows my car to proceed straight.
Step 5  Rule            arrow:right: The arrow indicating right allows my car to turn right.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): The lane marking includes an arrow pointing straight ahead, which
                        allows going straight.
Step 6  turn_left       prohibited (correct): There is no arrow or marking in my lane that permits a left
                        turn, and no waiting area is visible.
Step 6  turn_right      allowed (WRONG, label prohibited): The lane marking includes an arrow pointing right,
                        which allows turning right.
Step 6  u_turn          prohibited (correct): There is no arrow or marking in my lane that permits a U-turn.
Step 6  enter_waiting_areaprohibited: There are no markings indicating a waiting area in my lane.
Step 7  Reflect         The boundaries and markings used for decisions are consistent with the close-up view,
                        and all actions are governed by visible features.
Advice                  You may change lanes left or right, proceed straight, or turn right at the
                        intersection ahead. A left turn or U-turn is prohibited from your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions False, unsafe ['turn_right'], citation None,
                        contradictions []
Tokens                  in 3815, out 1063, 7.54 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is an intersection where traffic
                        appears to be merging or splitting. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in my lane.;
                        arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lane line on left, dashed white lane line on right). | markings: the
                        arrows in my lane agree with each other and with the boundaries (the arrows indicate
                        allowed movements within the lane defined by the boundaries). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicating straight ahead allows my car to proceed straight.
Step 5  Rule            arrow:left: The arrow indicating left allows my car to turn left.
Step 5  Rule            arrow:right: The arrow indicating right allows my car to turn right.
Step 6  change_left     prohibited (WRONG, label allowed): The right boundary is a dashed white lane line,
                        which permits changing right, but the left boundary is a solid white lane line, which
                        prohibits changing left.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which permits
                        changing right.
Step 6  go_straight     allowed (correct): The lane marking includes an arrow pointing straight ahead, which
                        allows going straight.
Step 6  turn_left       allowed (WRONG, label prohibited): The lane marking includes an arrow pointing left,
                        which allows turning left.
Step 6  turn_right      allowed (WRONG, label prohibited): The lane marking includes an arrow pointing right,
                        which allows turning right.
Step 6  u_turn          allowed (WRONG, label prohibited): No marking governs this action, and the arrows do
                        not prohibit it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight, turn left, or turn right.
                        You may change lanes to the right, but changing left is prohibited by the solid white
                        line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['line:stop_line']), actions False, unsafe
                        ['turn_left', 'turn_right', 'u_turn'], citation None, contradictions []
Tokens                  in 3815, out 1123, 6.88 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with buildings on both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: The white dashed lines on both sides
                        fit the role of lane_line. | markings: There are no markings in my lane to check
                        against the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings observed, and no rule
                        prohibits any allowed action.
Advice                  You are in the leftmost lane of three. You are permitted to change lanes left or
                        right, and you may proceed straight ahead. No specific lane usage is mandated by the
                        current markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 957, 6.5 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street with buildings on both sides. Ahead, there is a junction or
                        intersection where traffic appears to be moving through. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car. Photo 2 shows a broken yellow line
                        next to my car. Further ahead, Photo 1 shows a broken yellow line continuing.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid line for lane_line, yellow dashed line for center_line). | markings: the
                        stop line is consistent with the lane configuration. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line indicates the boundary of my lane and prohibits
                        crossing it into the adjacent lane.
Step 5  Rule            right_boundary: The broken yellow line indicates a separation from opposing traffic,
                        and crossing it is permitted when safe.
Step 5  Rule            line:stop_line: The stop line requires my car to come to a complete stop before
                        proceeding into the intersection.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        boundary, which prohibits crossing into the adjacent lane.
Step 6  change_right    allowed (correct): allowed because the broken yellow line on the right boundary
                        permits crossing into the adjacent lane when safe.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because the stop line requires a
                        full stop before proceeding.
Step 6  turn_left       stop_first: stop_first because the stop line requires a full stop before proceeding.
Step 6  turn_right      stop_first: stop_first because the stop line requires a full stop before proceeding.
Step 6  u_turn          stop_first: stop_first because the stop line requires a full stop before proceeding.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the stop line before proceeding. You may change
                        right if safe, but changing left is prohibited. Use this lane for straight, left, or
                        right turns.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left', 'turn_left, turn_right, u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 3815, out 974, 6.54 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is an intersection visible in the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in this direction) | roles: the color and pattern of
                        both boundaries fit the role of a lane_line | markings: there are no markings in my
                        lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows lane changes across it.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You are allowed to change lanes in either
                        direction. You may proceed straight, but turning movements are not explicitly governed
                        by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3815, out 716, 5.84 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           The road appears to be an urban street with buildings on both sides. Ahead, there is a
                        junction or intersection visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid white
                        line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow dashed line next to my car. Photo 2 shows a yellow dashed line
                        next to my car. Photo 1 shows a yellow dashed line further ahead. Photo 2 shows a
                        yellow dashed line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white line for lane_line, yellow dashed line for center_line). | markings: the
                        stop line marking is consistent with the boundaries and context. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across this line
                        are prohibited.
Step 5  Rule            right_boundary: A yellow dashed center line indicates that crossing into the opposite
                        direction is permitted when safe.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left
                        boundary, as per the rule for solid lane lines.
Step 6  change_right    allowed: allowed because the yellow dashed center line on the right boundary permits
                        crossing when safe.
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
Advice                  You are in the left lane. You may proceed straight or change right, but changing left
                        is prohibited. You must stop at the solid white line ahead before proceeding.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 981, 6.81 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        where traffic appears to be moving through or approaching it. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the text 'BUS CUT TO SIZE' painted on the road in my
                        lane.; text:bus (full): Photo 2 shows the text 'BUS CUT TO SIZE' painted on the road
                        in the lane to my left.; text:bus (full): Photo 2 shows the text 'BUS CUT TO SIZE'
                        painted on the road in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of three lanes). | roles: the color and pattern of both boundaries
                        (white dashed lines) fit the role of lane_line. | markings: the text markings are
                        consistent across the lanes shown in Photo 2. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes across it.
Step 5  Rule            text:bus: The text indicates that the lane is designated for buses, which may restrict
                        general vehicle use or indicate a specific lane function.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows for lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, which allows
                        for lane changes.
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
Advice                  You are in the middle lane of three lanes, and lane changes are permitted as the
                        boundaries are dashed. You may proceed straight, but you should be aware that your
                        lane is marked for buses ('BUS CUT TO SIZE').
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3815, out 1108, 7.13 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road in an urban environment, and ahead there is an intersection
                        where the road appears to continue and potentially turn. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car, and further ahead, it appears to be a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car, and further ahead, it appears to be a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white dashed line marking the end of the lane
                        ahead, which is the stop line for the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white solid/dashed lines are lane lines). | markings: the stop line marking agrees
                        with the boundaries (it is at the end of the lane). | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane line, which prohibits crossing it.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white lane line,
                        which permits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       allowed: allowed, because there are no markings in the lane prohibiting left movement.
Step 6  turn_right      allowed: allowed, because there are no markings in the lane prohibiting right
                        movement.
Step 6  u_turn          allowed: allowed, because there are no markings in the lane prohibiting U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane and can proceed straight, turn left, or turn right. You may
                        change right, but you must stop before the intersection at the marked stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['area:grid']), actions True, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3815, out 971, 8.65 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or a
                        continuation of the road with traffic lanes visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows a broken white line continuing, and
                        Photo 2 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lane line on left, dashed white lane line on right). | markings: the bike
                        symbol in my lane agrees with the boundaries (it is in the lane between two lane
                        lines). | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            symbol:bike: The presence of a bicycle symbol indicates that this lane is designated
                        for bicycles or shared use.
Step 6  change_left     prohibited (contested, correct): allowed: The left boundary is a solid white lane
                        line, but since no specific prohibition is given for the change action, and the rule
                        for a solid line is to prohibit crossing, this action is prohibited.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and the
                        rule for a dashed line permits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane
                        that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or a two-
                          way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Do not attempt
                        to change left, as the solid white line prohibits it. Be aware that this lane is
                        marked for bicycle use.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3815, out 1044, 6.9 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes heading forward, and an intersection is
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid
                        white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows a white dashed line further ahead. Photo 2 shows a white
                        dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1 shows no markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed lines are lane lines). | markings: the stop line marking is consistent
                        with the boundaries and general road markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
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
Advice                  You are in the middle lane and can change left or right if necessary. You may proceed
                        straight through the intersection, but you must stop before the stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 956, 6.64 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        junction or intersection where the road continues and potentially changes direction.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it is a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it is a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating I am in the leftmost lane of the three lanes visible). | roles:
                        the color and pattern of both boundaries (white dashed lines) fit the role of a
                        lane_line. | markings: the stop line is present in my lane and is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            line:stop_line: The stop line indicates that vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and the rule allows lane changes when safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and the rule
                        allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in my lane, and no
                        U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change lanes left or right when safe. You must
                        come to a complete stop at the stop line before proceeding through the intersection.
                        Only going straight is explicitly permitted by the lack of directional markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1046, 6.92 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban road with buildings lining the left side. Ahead, there is an
                        intersection where traffic appears to be moving through or approaching a junction.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and a solid white
                        line further ahead. Photo 2 shows a solid white line immediately to the left of my
                        car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line immediately to the right of my car, and a broken
                        white line further ahead. Photo 2 shows a broken white line immediately to the right
                        of my car, and a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane. Photo 1 shows a large white arrow pointing straight ahead in my lane.;
                        symbol:bike (full): Photo 2 shows a white bicycle symbol in my lane. Photo 1 shows a
                        white bicycle symbol in my lane.; arrow:right (full): Photo 2 shows a white arrow
                        pointing right in the adjacent lane to my right. Photo 1 shows a white arrow pointing
                        right in the adjacent lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating two lanes of travel in my direction. | roles: The
                        left boundary is a solid white lane line, and the right boundary is a dashed white
                        lane line, which fits the role of lane lines between lanes of my direction. |
                        markings: The straight arrow in my lane is consistent with the boundaries and the
                        presence of the bicycle symbol. The adjacent lane's right arrow is noted but does not
                        contradict my lane's markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the adjacent lane on the
                        left.
Step 5  Rule            right_boundary: The dashed white line permits crossing into the adjacent lane on the
                        right.
Step 5  Rule            arrow:straight: The straight arrow in my lane permits proceeding straight ahead.
Step 5  Rule            symbol:bike: The bicycle symbol indicates that this lane is shared or designated for
                        bicycles, which may affect vehicle usage.
Step 5  Rule            arrow:right: The arrow in the adjacent lane permits turning right from that lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary and the
                        rule that a solid line prohibits crossing into the adjacent lane on the left.
Step 6  change_right    allowed (contested, correct): allowed by the dashed white right boundary and the rule
                        that a dashed line permits crossing into the adjacent lane on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane and the rule that the
                        arrow permits proceeding straight ahead.
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow in my lane and the rule that
                        the arrow prohibits movements not shown.
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow in my lane and the rule that
                        the arrow prohibits movements not shown.
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow in my lane and the rule that
                        the arrow prohibits movements not shown.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area or two-
                          way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are permitted to proceed straight or change right into the adjacent lane. Changing
                        left is prohibited by the solid line. Be aware that this lane is marked for bicycles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right'], missed ['line:stop_line']), actions True, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_right prohibited
                        although an arrow shows it']
Tokens                  in 3815, out 1309, 8.42 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        where the road continues and potentially merges or changes lanes. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1 shows no specific markings within my lane in the
                        visible stretch. Photo 2 shows no specific markings within my lane in the visible
                        stretch.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines on both sides fit the
                        role of lane_line. | markings: The stop line marking is consistent with the boundaries
                        and the general road layout. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
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
Advice                  You are in the middle lane of three. You may change lanes in either direction. You are
                        permitted to go straight through the intersection, but you must stop at the visible
                        stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 1006, 7.09 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues and potentially merges or changes direction. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Further ahead, Photo 1 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction). | roles: the color and pattern of
                        each boundary fit the role given to it (solid white line on the left, dashed white
                        line on the right). | markings: the stop line in my lane agrees with the boundaries
                        (it is located at the end of the lane segment shown). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line,
                        as per the rule for solid lane lines.
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary line, as per the rule
                        for dashed lane lines.
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
Advice                  You are in the left lane of two lanes. You may proceed straight or change right, but
                        you must stop before the stop line. Do not attempt to change left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 967, 6.93 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection visible in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary to
                        the right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is one of several lanes). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the stop
                        line marking is consistent with the lane boundaries and does not contradict any other
                        markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (correct): allowed, because the left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes in either direction,
                        and you are permitted to go straight ahead. You must stop at the visible stop line
                        before proceeding.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 965, 6.7 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic appears to be moving through or preparing to turn. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white dashed line marking the lane boundary to
                        the right, and Photo 2 shows this same line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the direction of travel). | roles: the color and pattern
                        of both boundaries (white dashed lines) fit the role of lane_line. | markings: the
                        stop line marking is consistent with the lane boundaries and does not contradict any
                        other visible markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed, because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in the lane allowing or
                        prohibiting a left turn.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in the lane allowing or
                        prohibiting a right turn.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in the lane allowing or
                        prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change left or right, and you may proceed
                        straight ahead. You must stop at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 1013, 6.5 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street with buildings on both sides. Ahead, there is a junction or
                        intersection where the road continues and other traffic is present. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken white line is visible further ahead. Photo 2: A broken white line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it.
                        | markings: the markings (stop line) agree with the boundaries (lane lines). | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A broken white line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: A stop line indicates where a vehicle must stop before proceeding
                        through the intersection.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line, as
                        per the rule for solid lane lines.
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary line, as per the rule
                        for dashed lane lines.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: not_applicable as there are no markings governing turning movements in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable as there are no markings governing turning movements in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing U-turns in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        line. You must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 911, 6.14 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        junction or a continuation of the road with multiple lanes. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car, and further ahead, it transitions to a white solid line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the edge of the lane
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating I am in the leftmost lane of my direction). | roles: the color
                        and pattern of both boundaries (white dashed/solid) fit the role of a lane_line. |
                        markings: the stop line marking is consistent with the lane boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows lane changes in both directions.
Step 5  Rule            right_boundary: The white dashed line allows lane changes in both directions.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed, because the left boundary is a white
                        dashed line, which allows lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a white dashed line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change lanes left or right, and you may proceed
                        straight ahead. You must stop at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 966, 6.56 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is a junction or
                        intersection where traffic appears to be moving forward and potentially turning.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line separating my lane
                        from the adjacent lane, and Photo 2 shows this solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Further ahead, Photo 1 shows a dashed white line continuing, and
                        Photo 2 shows this dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line). | roles: the color and pattern of each boundary fit the role given to it
                        (solid white lane line on left, dashed white lane line on right). | markings: the text
                        'BUS LANE' in my lane is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            text:bus: The presence of 'BUS LANE' indicates this lane is reserved for buses.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left
                        (element_rules for left_boundary).
Step 6  change_right    allowed (correct): allowed by the dashed white lane line on the right (element_rules
                        for right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting straight
                        movement in the lane (no marking governs this action).
Step 6  turn_left       not_applicable: not_applicable as there are no markings governing turning movements in
                        the lane (no marking governs this action).
Step 6  turn_right      not_applicable: not_applicable as there are no markings governing turning movements in
                        the lane (no marking governs this action).
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing turning movements in
                        the lane (no marking governs this action).
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no waiting areas or two-way left-turn
                          lanes visible (no marking governs this action).
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to its restrictions. You may proceed
                        straight or change right, but changing left is prohibited. No specific stopping or
                        turning instructions are visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1035, 7.32 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction or a change in lane
                        configuration indicated by road markings. There are three lanes visible in my
                        direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a white dashed line marking the lane boundary
                        ahead of my car, which is part of the lane structure.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines on
                        both sides fit the role of lane_line. | markings: The stop line marking is consistent
                        with the lane structure. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in both directions.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to change lanes in either
                        direction, and you may proceed straight ahead. You must stop at the visible stop line
                        before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 1016, 8.95 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes heading in the same direction. Ahead, there
                        is an intersection where traffic appears to be moving through or approaching a
                        junction. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid
                        white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid
                        white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane line (separating my
                        lane from the next lane to the left), and the right boundary is a lane line
                        (separating my lane from the next lane to the right). | roles: The white dashed/solid
                        lines fit the role of lane_line. | markings: The arrows (straight and right) are
                        present in my lane and are consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes into or out of the adjacent
                        lane.
Step 5  Rule            right_boundary: A broken white line allows lane changes into or out of the adjacent
                        lane.
Step 5  Rule            arrow:straight: The arrow indicating straight movement allows my car to proceed
                        straight ahead.
Step 5  Rule            arrow:right: The arrow indicating a right turn allows my car to turn right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a lane line, and
                        there is no marking allowing a change to the left.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a lane line, and
                        the markings allow movement into the adjacent lane.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane marking includes an arrow
                        indicating straight movement.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking in my lane allowing a left turn.
Step 6  turn_right      allowed (correct): allowed: The lane marking includes an arrow indicating a right
                        turn.
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: There is no marking in my lane allowing
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of three. You may proceed straight or turn right, and you
                        may change right into the adjacent lane. Turning left or making a U-turn is
                        prohibited. Use the right boundary line to change lanes if necessary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation None,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left prohibited
                        across a broken lane line']
Tokens                  in 3815, out 1092, 7.62 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with trees lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch of road. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the text 'BUS LANE' painted on the road in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating I am in the leftmost lane of my direction). | roles: the color
                        and pattern of both boundaries (white dashed lines) fit the role of a lane_line. |
                        markings: the text 'BUS LANE' is consistent with the boundaries and does not
                        contradict any movement markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            text:bus: This marking indicates that my lane is reserved for buses.
Step 6  change_left     allowed (contested, label prohibited): allowed, because the left boundary is a dashed
                        white line, which allows lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to the rules for this reserved lane. Lane
                        changes are permitted as the boundaries are dashed, and you are free to proceed
                        straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1010, 6.69 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in the lane ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: the color (white) and pattern (dashed)
                        of both boundaries fit the role of lane_line. | markings: the text:bus marking is
                        located within my lane and does not contradict the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            text:bus: This marking indicates that the lane is reserved for buses.
Step 6  change_left     allowed (contested, label prohibited): allowed, because the left boundary is a dashed
                        white line, which allows lane changes.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings prohibiting
                        straight movement in my lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in a bus-only lane, so you should not proceed unless you are a bus. Lane
                        changes are permitted as the boundaries are dashed. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 988, 6.78 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues straight, and there is no immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 1, full)
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
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (1) agree with the boundary roles (white dashed lines on both sides indicate lane
                        separation). | roles: The white dashed lines on both sides fit the role of lane_line.
                        | markings: There are no markings in my lane to check against boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 5  Rule            right_boundary: A dashed white line indicates that lane changes are permitted when
                        safe.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a dashed
                        white line, which permits lane changes when safe.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes when safe.
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
Step 7  Reflect         The actions are consistent with the observed boundaries and the rules derived from
                        them.
Advice                  You are in the leftmost lane of three. You are permitted to change lanes left or
                        right, and you may proceed straight ahead. Since there are no specific turn markings,
                        you must ensure the road ahead allows for turning movements if you wish to turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 957, 6.37 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with trees lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car, and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to my car. Photo 2 shows a dashed white line
                        next to my car, and further ahead, it remains a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the text 'BUS LANE' painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane line, and the right boundary is a
                        lane line, which is consistent with my lane being the middle lane. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the role of lane lines. | markings: The 'BUS LANE' text is in my lane
                        and is consistent with the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            text:bus: This marking indicates that my lane is reserved for buses.
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line on the left
                        boundary, as per the rule for solid lane lines.
Step 6  change_right    allowed (correct): Allowed by the dashed white line on the right boundary, as per the
                        rule for dashed lane lines.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting straight
                        movement in my lane.
Step 6  turn_left       not_applicable: Not applicable as there are no markings governing turning movements in
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there are no markings governing turning movements in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing U-turn movements in
                        my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in a bus lane, so you must adhere to its restrictions. You may proceed
                        straight or change right, but changing left is prohibited by the solid line. No
                        specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3815, out 1015, 6.5 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban area, and ahead there is a junction or
                        intersection where traffic flow changes. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a solid white line marking the stop line just
                        ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction). | roles: the color and pattern of
                        each boundary fit the role given to it (solid white line on the left, dashed white
                        line on the right, both acting as lane lines). | markings: the stop line marking
                        agrees with the boundaries as it is located within the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where the vehicle must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane line, which
                        prohibits changing left according to the rule.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which permits
                        changing right according to the rule.
Step 6  go_straight     allowed (contested, correct): Nothing in my lane restricts carrying on straight along
                        my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane and must stop at the solid white line ahead. You are
                        permitted to change right, go straight, or proceed, but turning left, right, or
                        U-turning is not governed by markings in this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 1026, 6.99 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into the distance with buildings on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): Photo 1 shows no markings in my lane. Photo 2 shows no
                        markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes). | roles: The white dashed lines on both sides fit the
                        role of lane_line. | markings: The lack of markings in my lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a dashed
                        white line, which permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       allowed: Allowed because there are no markings in my lane prohibiting left turns.
Step 6  turn_right      prohibited: Prohibited because the lane marking indicates no turning right.
Step 6  u_turn          allowed: Allowed because there are no markings in my lane prohibiting U-turns.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane and can change left or right. You may go straight, turn
                        left, or make a U-turn, but turning right is prohibited by the lane marking. No
                        specific stopping area is marked.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3815, out 999, 6.78 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, there is a
                        junction or intersection where traffic flow changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the lane to the left. Photo 2: A
                        white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line separates my lane from the lane to the right. Photo 2: A
                        white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A white dashed line marking the lane boundary is
                        visible ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (dashed lines on both sides indicate internal
                        lanes). | roles: The white dashed lines fit the role of lane_line. | markings: The
                        stop line marking is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A dashed lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed lane line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding through the intersection.
Step 6  change_left     allowed (contested, correct): Allowed because the left boundary is a dashed lane_line,
                        which permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed lane_line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibitions in
                        the lane.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observed dashed boundaries and the stop line
                        marking.
Advice                  You are in the middle lane of three. You may change left or right, and you may proceed
                        straight ahead. You must stop at the visible stop line before proceeding through the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 3815, out 942, 6.3 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, there is a
                        junction or area where lane configurations change, indicated by the road markings.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: The white dashed lines on
                        both sides fit the role of lane_line. | markings: The area:grid marking is present in
                        Photo 2 and is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            right_boundary: A dashed white line allows lane changes in either direction.
Step 5  Rule            area:grid: The grid marking indicates an area where stopping or waiting is prohibited.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing turning movements.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing turning movements.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no action is allowed against a prohibition.
Advice                  You are in the middle lane, and lane changes are permitted in both directions. You may
                        proceed straight, but be aware of the grid marking ahead, which prohibits stopping or
                        waiting in that area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3815, out 1025, 6.51 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides. Ahead, the road continues
                        straight, and there is no immediate intersection or ramp visible. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows a broken white line continuing. Photo 2
                        shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction). | roles: the color and pattern of
                        each boundary fit the role given to it (solid white line on the left, dashed white
                        line on the right). | markings: there are no markings in my lane to check against the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white line permits crossing it to change lanes.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, which is a solid
                        white line.
Step 6  change_right    allowed (contested, label prohibited): allowed by the right_boundary, which is a
                        dashed white line.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit it.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may proceed straight or change right,
                        but you must not change left. No specific stopping or waiting areas are marked ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 3815, out 934, 6.14 s
```
