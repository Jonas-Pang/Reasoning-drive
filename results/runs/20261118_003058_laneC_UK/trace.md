# Reasoning of lane run 20261118_003058_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, leading towards an intersection. My
                        car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): Photo 2 shows a white dashed line marking the lane boundary
                        on the left side of my lane, and a white dashed line marking the lane boundary on the
                        right side of my lane.; line:crosswalk (partial): Photo 2 shows a white dashed line
                        marking the lane boundary on the left side of my lane, and a white dashed line marking
                        the lane boundary on the right side of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        markings (crosswalk lines) are consistent with the boundaries and do not contradict
                        them. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop before the stop line
                        preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed line, which permits
                        lane changes after signaling [IN-6(1)]
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        line, which permits lane changes after signaling [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not prohibit it [IN-6(1)]
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the boundaries are
                        dashed. You may proceed straight, but be aware of the pedestrian crossing markings
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line', 'symbol:bike']), actions False, unsafe
                        ['change_right'], citation unlisted, contradictions []
Tokens                  in 6662, out 991, 7.21 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road leading towards an intersection. There are at least two lanes visible
                        in my direction near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles | roles: the color and pattern of each boundary fit the
                        role you gave it | markings: the arrows, words and areas in my lane agree with each
                        other and with the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing a U-turn or
                        prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may change lanes left or right after signaling. You may
                        proceed straight ahead, but you must not stop within the marked grid area ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 822, 5.43 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes in my direction. Ahead, there is a junction
                        or crossing area marked with bicycle symbols and directional arrows. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this solid white
                        line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible next to my car. Further ahead, this dashed
                        white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in
                        the lane next to my car (left lane).; arrow:straight (full): Photo 2: A white arrow
                        pointing straight ahead is visible in my lane.; arrow:straight (full): Photo 2: A
                        white arrow pointing straight ahead is visible in the lane to the right of my car.;
                        symbol:bike (full): Photo 2: A white bicycle symbol is visible in the center of the
                        road ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles: the left boundary is a lane line, and the right
                        boundary is a lane line, indicating I am in the middle lane of three. | roles: The
                        solid white line on the left and the dashed white line on the right both fit the role
                        of a lane_line. | markings: The arrows in Photo 2 show straight movement for all three
                        lanes, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The driver shall use that lane while taking a left turn if direction
                        arrows pointing to the left are marked on the road. [[IN-8(1)(c)]]
Step 5  Rule            symbol:bike: No specific rule passage covers the bicycle symbol in this context.
                        [null]
Step 6  change_left     allowed (correct): The left boundary is a solid white lane_line, and [IN-6(1)]
                        mandates that lane changes must be made after signaling or road marking.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane_line, and [IN-6(1)]
                        mandates that lane changes must be made after signaling or road marking.
Step 6  go_straight     allowed (correct): The lane marking in my lane is an arrow:straight, and this allows
                        going straight.
Step 6  turn_left       prohibited (correct): The lane marking in my lane is an arrow:straight, which does not
                        show a left turn, so it is prohibited.
Step 6  turn_right      prohibited (correct): The lane marking in my lane is an arrow:straight, which does not
                        show a right turn, so it is prohibited.
Step 6  u_turn          prohibited (correct): The lane marking in my lane is an arrow:straight, which does not
                        show a U-turn, so it is prohibited.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no rule prohibits an allowed action.
Advice                  You are in the middle lane, which is marked for going straight ahead. You may change
                        lanes left or right after signaling, but you are prohibited from turning left, right,
                        or making a U-turn from this lane. Be aware of the bicycle symbol ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6662, out 1285, 9.14 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings on the left and residential houses on the right.
                        Ahead, the road continues straight, and there is no immediate intersection or ramp
                        visible in the close-up. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues. Photo 2 shows a solid white line immediately to the left of my
                        car, and further ahead, this line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a double yellow line immediately to the right of my car, and further
                        ahead, this line continues. Photo 2 shows a double yellow line immediately to the
                        right of my car, and further ahead, this line continues.
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: no markings were listed, so this is consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single or double longitudinal
                        solid line, or on a painted traffic island except in case of obstructions on the road.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: No vehicle shall overtake by crossing the continuous single or double
                        solid longitudinal lane marking dividing the road. [[IN-14(5)(c)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        lane_line, and [IN-6(1)] permits driving within the lane, but changing lanes requires
                        a signal or marking.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a double_solid
                        yellow center_line, and [IN-6(6)] and [IN-14(5)(c)] prohibit driving on or crossing
                        this line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes in view.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is the lane for driving. You may proceed straight
                        ahead, but changing lanes to the right is prohibited by the double yellow line. No
                        specific turn movements are indicated by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 941, 7.46 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides. Ahead, there is a pedestrian
                        crossing and what appears to be an intersection or junction. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2: A white dashed line marking is visible across the road
                        ahead, indicating a pedestrian crossing.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in the direction of travel) | roles: the color and
                        pattern of both boundaries (white dashed) fit the role of a lane_line | markings: the
                        crosswalk marking is consistent with the visual evidence | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: At uncontrolled pedestrian crossings, the driver shall give way to
                        pedestrians. [[IN-8(2)(e)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: No markings prohibit going straight, and the
                        boundaries do not restrict this action.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in view.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, but
                        you must give way to pedestrians at the crossing ahead. You may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 6662, out 841, 6.36 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is an intersection or
                        junction where traffic appears to be merging or crossing. My car is in the rightmost
                        lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the lane to the left. Photo 2: A
                        white dashed line separates my lane from the lane to the left, and this line continues
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line marks the edge of the road/lane to the right. Photo 2: A
                        white dashed line marks the edge of the road/lane to the right, and this line
                        continues ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): None visible in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: no markings were listed, so they agree with each other and with the
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed edge_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: No markings prohibit going straight, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is suitable for proceeding straight ahead. You
                        may change lanes left or right after signaling, as the lane markings permit this.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 824, 6.86 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road with traffic moving in both directions. My car is in one of the lanes
                        traveling forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line near my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line immediately to the left of my car,
                        and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line immediately to the right of my car,
                        and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: the solid white lines fit the role of lane_line. | markings: the
                        straight arrow in my lane is consistent with the lane markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The driver shall use that lane while taking a left turn (this rule is
                        not directly applicable as the arrow shows straight, but it implies adherence to lane
                        use for the indicated movement). [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and [IN-6(1)] mandates driving within the lane and changing lanes only after proper
                        signaling/marking.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        proper signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed: The lane has a straight arrow, and nothing
                        restricts carrying on straight along my lane.
Step 6  turn_left       prohibited: prohibited: The lane has a straight arrow, and [IN-8(1)(c)] implies that
                        only the indicated movement is allowed when an arrow is present.
Step 6  turn_right      prohibited: prohibited: The lane has a straight arrow, and [IN-8(1)(c)] implies that
                        only the indicated movement is allowed when an arrow is present.
Step 6  u_turn          prohibited: prohibited: The lane has a straight arrow, and [IN-8(1)(c)] implies that
                        only the indicated movement is allowed when an arrow is present.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines, and the lane arrow only permits straight
                        movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 949, 7.77 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a stretch of
                        road with traffic moving in both directions. My car is in one of the lanes moving
                        forward. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction) | roles: the color and pattern of each boundary
                        fit the role given to it | markings: there are no markings in my lane to check for
                        agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed line, which permits
                        lane changes after signaling [IN-6(1)]
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed line, which permits
                        lane changes after signaling [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing this
                        action
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing this
                        action
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane governing
                          this action
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes moving in your direction. You may change lanes
                        left or right after signaling, and you may proceed straight ahead. No specific lane
                        markings restrict your movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6662, out 784, 5.85 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection. There are at least two
                        lanes visible in my direction near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this line
                        appears to continue as a solid white line. Photo 2: A solid white line is visible next
                        to my car. Further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible next to my car. Further ahead, this line
                        appears to continue as a dashed white line. Photo 2: A dashed white line is visible
                        next to my car. Further ahead, this line continues as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2: A white dashed line is visible ahead of my car,
                        indicating a lane division.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (dashed line ahead) agree with the boundaries (dashed line to
                        the right) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop before the stop line
                        preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        lane line, and there is no rule prohibiting a lane change based on this line type for
                        this action.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        lane line, and there is no rule prohibiting a lane change based on this line type for
                        this action.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes. You may change lanes left or right, and you may
                        proceed straight ahead. Be aware of the pedestrian crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 6662, out 918, 6.68 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is a
                        junction/intersection where the road continues and crosses. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line continuing. Photo 2 shows a white dashed line next to my car, and
                        further ahead, it appears to be a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white dashed line marking the edge of the lane,
                        and further ahead, there is a white dashed line marking the edge of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color and pattern of
                        both boundaries (white dashed) fit the role of lane_line. | markings: the
                        line:crosswalk marking is consistent with the boundaries and general road markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a white
                        dashed line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted after signaling. You may
                        proceed straight, but you should be aware of the pedestrian crossing ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 6662, out 1096, 6.84 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on the left side and trees on the right
                        side. Ahead, there is a junction or a point where the road continues straight and
                        possibly turns. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line next to my car. Photo 2 shows a broken yellow line
                        next to my car. Further ahead, Photo 1 shows a broken yellow line continuing. Photo 2
                        shows a broken yellow line continuing.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:straight (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: the arrows in my lane agree with the boundaries (they allow straight
                        movement within the lane) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver, proceeding in the same direction and trying to overtake
                        another vehicle ahead, shall not cross the said yellow or white solid line.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn (this rule is not directly applicable as the arrow shows straight, but it governs
                        lane usage for turns). [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the right are marked on the road, the driver shall remain in that lane while taking
                        right turn (this rule is not directly applicable as the arrow shows straight, but it
                        governs lane usage for turns). [[IN-8(2)(c)]]
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and changing lanes requires adherence to lane markings [IN-6(1)].
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed yellow center_line, which
                        permits overtaking/lane change under certain conditions [IN-6(7)].
Step 6  go_straight     allowed (correct): allowed: The lane markings show an arrow pointing straight ahead,
                        and no rule prohibits going straight [IN-8(2)(c) applies to right turn, but the arrow
                        allows straight].
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The lane markings do not show an arrow
                        permitting a left turn, and no waiting area is present [IN-8(1)(c) requires a left
                        arrow].
Step 6  turn_right      prohibited (correct): prohibited: The lane markings do not show an arrow permitting a
                        right turn, and no waiting area is present [IN-8(2)(c) requires a right arrow].
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings or
                        boundaries that govern a U-turn in this lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane present.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is designated for straight movement. You may change
                        right if safe, as the right boundary is a broken yellow line, but you must signal. You
                        are permitted to go straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 1091, 10.35 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction or intersection where
                        the road continues and meets another road. My car is in the lane closest to the left
                        side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows this solid white line continuing. Photo 2
                        shows this solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows this broken white line continuing. Photo
                        2 shows this broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: no markings were listed, so they agree | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a solid white line, and there is no
                        rule prohibiting a lane change based on this line type for this action.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and there is no
                        rule prohibiting a lane change based on this line type for this action.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       allowed: allowed: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  turn_right      allowed: allowed: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  u_turn          allowed: allowed: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is bordered by a solid white line on the left and a
                        dashed white line on the right. You may change lanes after signaling, and all
                        movements (straight, left, right, U-turn) are permitted as no specific lane markings
                        restrict them.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 6662, out 840, 6.93 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        where traffic is moving forward and turning. My car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: the arrows (straight and right) in
                        my lane agree with the boundaries (dashed lines allow lane changes, which is
                        consistent with the arrows showing movement options). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: This marking indicates that going straight is permitted in this lane.
                        [null]
Step 5  Rule            arrow:right: This marking indicates that turning right is permitted in this lane.
                        [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and the lane markings do not prohibit changing left, consistent with [IN-6(1)].
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and the lane markings
                        do not prohibit changing right, consistent with [IN-6(1)].
Step 6  go_straight     allowed (correct): allowed: The lane marking shows an arrow pointing straight, and no
                        rule prohibits going straight in this lane.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: There is no arrow or marking in the
                        lane that permits a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane marking shows an arrow pointing
                        right, and no rule prohibits turning right in this lane.
Step 6  u_turn          prohibited (correct): prohibited: There is no arrow or marking in the lane that
                        permits a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight and turning right. You may
                        change lanes left or right as the boundaries are dashed, but you cannot turn left or
                        make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe ['turn_right'], citation unlisted, contradictions []
Tokens                  in 6662, out 956, 7.06 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a street scene in a built-up area, and ahead there is an intersection where
                        the road appears to continue or change direction. My car is in the lane closest to the
                        left side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to my car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to my car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line immediately next to my car, and further ahead, this
                        line continues as a dashed white line. Photo 2 shows a dashed white line immediately
                        next to my car, and further ahead, this line continues as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): Photo 2 shows a white dashed line marking the edge of the
                        lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (a dashed line ahead) agree with the boundaries (dashed line
                        ahead) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white line,
                        and [IN-6(1)] mandates driving within the lane and changing lanes only after proper
                        signaling/marking.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        line, and [IN-6(7)] permits crossing a broken line to overtake, provided safety
                        precautions are observed.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       allowed: allowed: Nothing restricts turning left as there are no specific prohibitions
                        or arrows.
Step 6  turn_right      allowed: allowed: Nothing restricts turning right as there are no specific
                        prohibitions or arrows.
Step 6  u_turn          allowed: allowed: Nothing restricts U-turning as there are no specific prohibitions or
                        arrows.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is bordered by a solid white line on the left,
                        prohibiting lane changes to the left. You may change right into the adjacent lane, but
                        be mindful of the pedestrian crossing ahead. You may proceed straight, turn left, turn
                        right, or perform a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left', 'turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 6662, out 946, 7.21 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to lead towards a junction or continuation of
                        the street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car. Photo 2 shows a white dashed line
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line further ahead. Photo 2 shows a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within a flow of traffic) | roles: the white dashed lines fit the role of lane_line |
                        markings: the arrows (straight and right) are within the lane and are consistent with
                        the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The driver shall use that lane while taking a left turn (Note: This
                        rule is for left turns, but the arrow indicates straight movement, so it permits
                        straight movement if no other restriction applies). [[IN-8(1)(c)]]
Step 5  Rule            arrow:right: The driver shall remain in that lane while taking right turn.
                        [[IN-8(2)(c)]]
Step 5  Rule            arrow:straight: The driver shall remain in that lane while taking right turn (Note:
                        This rule is for right turns, but the arrow indicates straight movement, so it permits
                        straight movement if no other restriction applies). [[IN-8(2)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a white dashed
                        lane_line, and while dashed lines permit lane changes, the lane markings do not
                        explicitly permit a change left from this lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and the
                        lane markings permit movement to the right.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and the
                        boundaries are dashed lane_lines which do not prohibit going straight.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: There is no arrow indicating a left
                        turn in this lane.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane marking shows a right arrow, and
                        the boundaries are dashed lane_lines.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings or
                        boundaries that govern a U-turn in this lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or a two-
                          way left-turn lane ahead of this lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight and turning right. You may
                        change right into the adjacent lane if safe, but turning left or making a U-turn is
                        not permitted from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe ['turn_right'], citation unlisted, contradictions ['change_left prohibited
                        across a broken lane line']
Tokens                  in 6662, out 986, 8.19 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a wet urban road, and ahead there is a pedestrian crossing leading to an
                        intersection area. My car is in one of the lanes near the bottom of the photo. (lanes
                        2, mine 1, full)
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
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the boundary to
                        the right, and a white solid line marking the boundary to the left. No arrows, words,
                        or specific areas are visible within my lane in Photo 2.; line:crosswalk (full): Photo
                        1 shows white dashed markings forming a pedestrian crossing ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is a lane line (solid
                        white) and the right boundary is a lane line (dashed white). Since there are two lanes
                        visible, and my lane is the one on the left (ego_lane_index=1), the left boundary acts
                        as a lane line separating my lane from the next lane to the left, and the right
                        boundary acts as a lane line separating my lane from the next lane to the right. This
                        is consistent with the lane count and index. | roles: The left boundary is a solid
                        white lane line, and the right boundary is a dashed white lane line. This fits the
                        role of lane_line. | markings: The lane markings (crosswalk) are consistent with the
                        boundaries (lane lines) and do not contradict the lane structure. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: At uncontrolled pedestrian crossings, the driver shall give way to
                        pedestrians. [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white lane
                        line, and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        signaling/marking.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        lane line, and [IN-6(1)] allows lane changes after signaling/marking, and [IN-6(7)]
                        permits crossing a broken line to overtake.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow in my lane prohibits going straight,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed that is prohibited by a rule from step 5.
Advice                  You are in the left lane, which is bordered by a solid white line on the left. You may
                        change right after signaling, but you must yield to pedestrians at the crosswalk
                        ahead. You may proceed straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 1186, 8.96 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection. My
                        car is in the lane closest to the left side of the road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows the text 'BUS LANE' painted on the road in the lane to
                        the left of my lane. Photo 2 shows the text 'BUS LANE' painted on the road in the lane
                        to the left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the text:bus marking is in the adjacent lane, not in my lane, so it does not
                        contradict the boundaries or my lane's markings | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in that lane.
                        [[IN-6(3)]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a white dashed line, and
                        [IN-6(1)] requires changing lanes only after giving a proper signal or road marking or
                        signage.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, and [IN-6(1)] requires
                        changing lanes only after giving a proper signal or road marking or signage.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       allowed: Nothing restricts turning left as there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern it.
Step 6  turn_right      allowed: Nothing restricts turning right as there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern it.
Step 6  u_turn          allowed: Nothing restricts U-turning as there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is adjacent to a bus lane. You may change lanes
                        after signaling, and all movements (straight, left, right, U-turn) are permitted as no
                        specific lane markings restrict them.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left', 'turn_left, turn_right, u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6662, out 921, 7.05 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance with traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to the bus. Photo 2 shows a dashed white line
                        next to the bus.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line further ahead. Photo 2 shows a solid white line
                        further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the boundary of my
                        lane.; line:stop_line (partial): Photo 2 shows a white dashed line marking the
                        boundary of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (line:stop_line) are consistent with the boundaries and each
                        other | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing the red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a lane_line, and
                        [IN-6(1)] requires driving within the lane and changing lanes only after signaling or
                        marking.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane_line, and [IN-6(1)] allows
                        lane changes after signaling or marking, and no specific prohibition is visible.
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
Advice                  You are in the middle lane, which allows you to go straight or change right after
                        signaling. You should proceed cautiously, keeping within your lane boundaries.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 6662, out 903, 6.48 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is an intersection where traffic is moving forward and turning. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:merge_right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles, as the left boundary is a lane line (separating
                        lane 1 from lane 2) and the right boundary is a lane line (separating lane 2 from lane
                        3). | roles: The white dashed lines on both sides fit the role of lane_line. |
                        markings: The arrows (straight and merge_right) are present in my lane and are
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: This marking indicates that proceeding straight ahead is permitted.
                        [null]
Step 5  Rule            arrow:merge_right: This marking indicates that the lane ends and traffic merges to the
                        right. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a lane_line, and
                        [IN-6(1)] requires changing lanes only after giving a proper signal or road marking or
                        signage, which is not explicitly shown to permit this change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane_line, and [IN-6(1)] allows
                        lane changes after signaling, and the arrow:merge_right indicates a lane change is
                        occurring.
Step 6  go_straight     allowed (correct): allowed: The arrow:straight permits going straight ahead, and no
                        other marking prohibits it.
Step 6  turn_left       prohibited (correct): prohibited: There is no arrow or marking in my lane that permits
                        a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow:merge_right indicates a lane
                        change to the right, which is consistent with a right turn maneuver if the
                        intersection allows it, and no marking prohibits it.
Step 6  u_turn          prohibited (correct): prohibited: There is no arrow or marking in my lane that permits
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or merge right. You may change right
                        after signaling, but you must not change left. You should use this lane for straight
                        travel or to merge right at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_right'], missed []), actions False, unsafe ['turn_right'], citation
                        unlisted, contradictions ['change_left prohibited across a broken lane line',
                        'turn_right allowed although no arrow shows it']
Tokens                  in 6662, out 1204, 8.74 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is an intersection. My car is in the
                        lane closest to the left side of the road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_left (full): Photo 2 shows a white arrow pointing left, in the lane next
                        to my car (lane 2).; arrow:straight (full): Photo 2 shows a white arrow pointing
                        straight ahead, in my lane (lane 1).; arrow:merge_right (full): Photo 2 shows a white
                        arrow pointing right, in the lane next to my car (lane 3).; arrow:straight (full):
                        Photo 2 shows a white arrow pointing straight ahead, in the lane next to my car (lane
                        2).; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead, in
                        the lane next to my car (lane 3).
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within a multi-lane road) | roles: the white dashed lines fit the role of lane_line |
                        markings: the arrows in Photo 2 are consistent with the lane structure shown in Photo
                        1, and they govern the movements in their respective lanes. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:merge_left: The driver shall use that lane while taking a left turn when
                        direction arrows pointing to the left are marked on the road. [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: No specific rule passage governs the action of proceeding straight
                        when an arrow indicates it. [null]
Step 5  Rule            arrow:merge_right: The driver shall remain in that lane while taking right turn when
                        direction arrows pointing to the right are marked on the road. [[IN-8(2)(c)]]
Step 5  Rule            arrow:straight: No specific rule passage governs the action of proceeding straight
                        when an arrow indicates it. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited because the left boundary is a white
                        dashed line, and [IN-6(1)] requires changing lanes only after giving a proper signal
                        or road marking or signage.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [IN-6(1)] allows lane changes after signaling/marking.
Step 6  go_straight     allowed (correct): allowed because the arrow in my lane (lane 1) shows straight ahead,
                        and no rule prohibits it.
Step 6  turn_left       prohibited (correct): prohibited because there is no arrow in my lane (lane 1)
                        indicating a left turn, and the lane is not designated for it.
Step 6  turn_right      prohibited (correct): prohibited because there is no arrow in my lane (lane 1)
                        indicating a right turn, and the lane is not designated for it.
Step 6  u_turn          prohibited (correct): prohibited because there is no arrow in my lane (lane 1)
                        indicating a U-turn, and the lane is not designated for it.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to go straight ahead. You may change right after
                        signaling, but turning left, right, or making a U-turn is prohibited from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_left', 'arrow:merge_right'], missed ['line:stop_line']), actions False,
                        unsafe [], citation unlisted, contradictions ['leftmost lane, but a lane line on the
                        left', 'change_left prohibited across a broken lane line']
Tokens                  in 6662, out 1242, 8.77 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: no markings
                        were reported in my lane, so they agree with each other and the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        line, which permits lane changes under the general rule of driving within the lane and
                        changing only after signaling.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed line, which permits
                        lane changes under the general rule of driving within the lane and changing only after
                        signaling.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right, and you may proceed straight ahead. You should signal any
                        lane change before executing it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 827, 6.32 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings on both sides. Ahead, there is a junction or
                        intersection where traffic is moving. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the line remains solid white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car. Further ahead, the line remains solid yellow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver, proceeding in the same direction and trying to overtake
                        another vehicle ahead, shall not cross the said yellow or white solid line.
                        [[IN-6(4)]]
Step 5  Rule            left_boundary: A vehicle may be overtaken from the left if the vehicle which is to
                        overtake and the vehicle which is to be overtaken are both driving on a multi-lane
                        road and the vehicle ahead can be safely overtaken in a marked lane to the left of the
                        vehicle being overtaken. [[IN-14(2)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        lane_line, and there is no rule prohibiting a lane change based on this boundary.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        center_line, and [IN-6(4)] prohibits crossing a solid line when overtaking.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit a U-turn, and the right boundary is not a double solid line.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is the lane closest to the curb. You may proceed
                        straight ahead, but changing right is prohibited by the solid yellow line. Since there
                        are no specific markings for turns, you should proceed cautiously towards the
                        junction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 6662, out 877, 6.64 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        appears to be a junction or a continuation of the road with multiple lanes. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, words, or areas are
                        visible within my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is one of several lanes in the direction of travel). |
                        roles: the color (white) and pattern (dashed) of both boundaries fit the role of a
                        lane_line. | markings: the lack of markings in my lane is consistent with the
                        boundaries being simple lane lines. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn, and no solid lines prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right after signaling, and you may proceed straight ahead. No
                        specific markings restrict turning movements.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 869, 7.11 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban street with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp visible
                        in the close-up. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line remains solid white. Photo 2 shows a solid white line immediately to the
                        left of my car, and further ahead, this line remains solid white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line immediately to the right of my car, and further
                        ahead, this line remains solid yellow. Photo 2 shows a solid yellow line immediately
                        to the right of my car, and further ahead, this line remains solid yellow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single or double longitudinal
                        solid line, or on a painted traffic island except in case of obstructions on the road.
                        [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a solid white
                        lane_line, and [IN-6(1)] requires driving within the lane, but does not prohibit
                        changing lanes if signaled.
Step 6  change_right    prohibited: prohibited: The right boundary is a solid yellow center_line, and
                        [IN-6(6)] prohibits driving on or over a double longitudinal solid line (interpreted
                        as prohibiting crossing the solid line).
Step 6  go_straight     allowed (contested, correct): allowed: No markings in my lane prohibit going straight,
                        and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that govern U-turns,
                        and the boundaries do not prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane indicating a
                          waiting area.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may proceed straight, but changing
                        right is prohibited by the solid yellow line. You should signal if you intend to
                        change left.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6662, out 843, 6.56 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban area, and ahead there is an intersection where
                        traffic appears to be moving through or approaching a crossing area. My car is in the
                        lane closest to the left side of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line further ahead, and Photo 2 shows a white dashed line
                        further ahead. Next to my car, Photo 2 shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:hov (full): Photo 2; area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of both boundaries (white dashed) fit the
                        role of a lane_line | markings: the markings (text:hov, area:grid) are consistent with
                        the boundaries and each other | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:hov: A vehicle of a specified class shall drive in that lane only. [[IN-6(2)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a lane_line, and
                        [IN-6(1)] requires driving within the lane and changing lanes only after
                        signaling/marking.
Step 6  change_right    allowed (correct): allowed: The right boundary is a lane_line, and [IN-6(1)] allows
                        lane changes after signaling/marking, and no specific prohibition is visible.
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
Advice                  You are in an HOV lane, so ensure you meet the requirements for this lane. You may
                        change right after signaling, and you may proceed straight ahead. You should be aware
                        of the grid marking ahead, which prohibits stopping in that area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid', 'text:hov'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left prohibited
                        across a broken lane line']
Tokens                  in 6662, out 971, 7.16 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, there is a
                        junction/intersection area marked by road markings. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2: A white dashed line marking is visible across the road
                        ahead, forming a box junction/keep clear area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in the direction of travel) | roles: the color (white)
                        and pattern (dashed) of both boundaries fit the role of a lane_line | markings: the
                        area:grid marking is consistent with the road markings visible in both photos |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, but
                        you must not stop within the marked grid area ahead. Use the left lane for turning
                        left if required, and the right lane for turning right if required, though no specific
                        arrows dictate this.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6662, out 865, 8.68 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with traffic moving in both directions. Ahead, the road
                        continues into a built-up area, and there is a bus visible in the distance. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2: A white bicycle symbol is painted on the road in the left
                        part of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in this direction) | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line | markings: the bicycle symbol is in the lane and
                        does not contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            symbol:bike: No specific rule passage was found that dictates the action based on the
                        bicycle symbol. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in view.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is designated for bicycles. You may change lanes after
                        signaling, and you are permitted to go straight. Since there are no specific turn
                        arrows, turning left, right, or making a U-turn is not governed by a specific marking,
                        but you should observe traffic conditions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 888, 6.58 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road leading towards an intersection. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the stop
                        line is visible and is consistent with the lane markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        line, which permits lane changes under [IN-6(7)] (though [IN-6(1)] requires
                        signaling).
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a dashed
                        line, which permits lane changes under [IN-6(7)] (though [IN-6(1)] requires
                        signaling).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       allowed: allowed because there are no markings in my lane prohibiting a left turn.
Step 6  turn_right      allowed: allowed because there are no markings in my lane prohibiting a right turn.
Step 6  u_turn          allowed: allowed because there are no markings in my lane prohibiting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes if necessary, but you must signal before doing so. You must stop
                        before the stop line ahead, and from that point, you may proceed straight, turn left,
                        turn right, or make a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6662, out 899, 6.75 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
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
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: there are
                        no arrows, words, or areas in my lane to check against the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing a U-turn or
                        prohibiting it from crossing a solid line.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right after signaling, and you may proceed straight ahead. No
                        specific lane is required for turning movements.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6662, out 827, 6.32 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection. There are two
                        lanes visible in my direction near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car, and Photo 2 shows a broken
                        white line to the right of my car. Further ahead, Photo 1 shows a broken white line
                        continuing, and Photo 2 shows a broken white line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2; arrow:left (full): Photo
                        2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the arrows in my lane agree with each other and with the boundaries |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: This marking indicates that proceeding straight ahead is permitted.
                        [null]
Step 5  Rule            arrow:right: This marking indicates that turning right is permitted. [null]
Step 5  Rule            arrow:left: This marking indicates that turning left is permitted. [null]
Step 6  change_left     allowed (contested, label prohibited): The right boundary is a dashed white line, and
                        [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, correct): The right boundary is a dashed white line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (correct): The lane has an arrow pointing straight, and this is permitted by
                        the marking.
Step 6  turn_left       allowed (WRONG, label prohibited): The lane has an arrow pointing left, and this is
                        permitted by the marking.
Step 6  turn_right      allowed (WRONG, label prohibited): The lane has an arrow pointing right, and this is
                        permitted by the marking.
Step 6  u_turn          allowed (WRONG, label prohibited): No marking prohibits a U-turn, and no specific rule
                        prohibits it based on the visible markings.
Step 6  enter_waiting_areanot_applicable: No marking governs entering a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and can proceed straight, turn left, or turn right. You
                        may also change lanes left or right after signaling.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['line:stop_line', 'symbol:bike']), actions
                        False, unsafe ['turn_left', 'turn_right', 'u_turn'], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 916, 6.66 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues and other traffic is present. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        on the left side of my lane, and a white dashed line marking the lane boundary on the
                        right side of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        line:stop_line marking is consistent with the lane boundaries and does not contradict
                        them. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: When a traffic control signal shows a red light, the driver shall stop
                        the vehicle before the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a U-turn, and no solid lines prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and since both lane boundaries are dashed, you may change
                        lanes after signaling. You may proceed straight ahead, but you must stop before the
                        visible stop line if a red light is displayed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 970, 7.46 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is an intersection
                        where the road appears to continue and potentially turn. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        on the left side of my lane, and a white dashed line marking the lane boundary on the
                        right side of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating I am in
                        the middle lane of three lanes in my direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        line:stop_line marking is consistent with the lane boundaries and does not contradict
                        them. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes left or right after
                        signaling, and you may proceed straight ahead. You must stop before the stop line if a
                        traffic light is red or if you are approaching a pedestrian crossing.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 968, 7.2 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance with traffic and buildings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        on the left side of my car.; line:stop_line (partial): Photo 2 shows a white dashed
                        line marking the lane boundary on the right side of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction) | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line | markings: the
                        stop_line markings are consistent with the lane boundaries and do not contradict the
                        lane structure | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing the red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable based on markings.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable based on markings.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, so it is not applicable based on markings.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes; you may change lanes after signaling. You
                        may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6662, out 935, 7.53 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a
                        junction/intersection where traffic is moving through. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): Photo 2 shows a white dashed line marking the edge of the
                        lane near my car.; line:crosswalk (partial): Photo 2 shows a white dashed line marking
                        the edge of the lane near my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction) | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line | markings: the markings (line:crosswalk) are
                        consistent with the boundaries and do not contradict them | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       allowed: allowed: There are no markings in my lane prohibiting a left turn, and the
                        boundaries do not prohibit it.
Step 6  turn_right      allowed: allowed: There are no markings in my lane prohibiting a right turn, and the
                        boundaries do not prohibit it.
Step 6  u_turn          allowed: allowed: There are no markings in my lane prohibiting a U-turn, and the
                        boundaries do not prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and since both lane boundaries are
                        dashed, you may change lanes after signaling. You may proceed straight, turn left,
                        turn right, or make a U-turn, but be mindful of the pedestrian crossing markings
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 6662, out 968, 7.34 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street with buildings lining both sides. Ahead, the road continues
                        into the distance, appearing to be a standard urban road without an immediate
                        intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction) | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line | markings: there are no markings in my lane to
                        check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: No markings prohibit going straight, and the
                        boundaries do not restrict this action.
Step 6  turn_left       not_applicable: not_applicable: No markings govern this action.
Step 6  turn_right      not_applicable: not_applicable: No markings govern this action.
Step 6  u_turn          not_applicable: not_applicable: No markings govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No markings govern this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, and
                        you are permitted to proceed straight ahead. No specific lane use markings restrict
                        your movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6662, out 741, 5.58 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a stretch of road
                        ahead with buildings on both sides. My car is in one of the lanes near the bottom of
                        the photo. (lanes 3, mine 2, full)
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
                        (2) agree with the boundary roles (both boundaries are lane lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color and pattern of
                        both boundaries (white dashed lines) fit the role of lane_line. | markings: there are
                        no markings in my lane to check against the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a white
                        dashed line, which permits lane changes after signaling [IN-6(1)]
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, which
                        permits lane changes after signaling [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement [no marking governs this action]
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing this
                        action [not_applicable]
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing this
                        action [not_applicable]
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing this
                        action [not_applicable]
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane governing
                          this action [not_applicable]
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change lanes left or right after
                        signaling. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6662, out 809, 5.97 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and there is no immediate intersection
                        or lane end visible ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car, followed by
                        a painted area with text. Further ahead, the boundary is defined by the edge of the
                        bus lane markings and the curb/sidewalk area. Photo 2: A solid white line is visible
                        immediately to the left of my car. Further ahead, the boundary is defined by the
                        painted text 'BUS LANE' and the edge of the road/curb.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           Photo 1: A dashed white line is visible immediately to the right of my car. Further
                        ahead, the boundary is defined by another dashed white line separating my lane from
                        the adjacent lane. Photo 2: A dashed white line is visible immediately to the right of
                        my car. Further ahead, the boundary is defined by another dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1: The text 'BUS LANE' is painted on the road in my lane. Photo
                        2: The text 'BUS LANE' is painted on the road in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the text 'BUS LANE' in my lane is consistent with the boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of the specified class (bus) shall drive in that lane only.
                        [[IN-6(2)]]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in that lane.
                        [[IN-6(3)]]
Step 5  Rule            text:bus: A vehicle shall not be parked in a manner other than that specified in the
                        parking bays in a designated parking lot or in such a manner as to occupy excessive
                        space. [[IN-22.(2)(r)]]
Step 6  change_left     prohibited (contested, correct): prohibited because the left boundary is a solid white
                        line, and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        signaling/marking.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white line, and
                        [IN-6(1)] allows lane changes after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn or prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must remain in this lane as it is marked as a bus lane, and you are prohibited
                        from changing left. You may change right after signaling, and you are allowed to
                        proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 1052, 7.94 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is a marked area for turning/merging on the right
                        side. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane division
                        ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction). | roles: the color and pattern of
                        both boundaries (white dashed) fit the role of a lane_line. | markings: the
                        line:stop_line marking is consistent with the lane boundaries and does not contradict
                        any observed features. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a white dashed lane_line,
                        and [IN-6(1)] allows lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a white dashed lane_line,
                        and [IN-6(1)] allows lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): No arrow prohibits going straight, and the boundaries do
                        not prohibit it.
Step 6  turn_left       allowed: No arrow prohibits turning left, and the boundaries do not prohibit it.
Step 6  turn_right      allowed: No arrow prohibits turning right, and the boundaries do not prohibit it.
Step 6  u_turn          allowed: No arrow prohibits U-turning, and the boundaries do not prohibit it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you must stop before the marked stop
                        line ahead. You may change lanes after signaling, and all movements (straight, left,
                        right, U-turn) are permitted if you stop first.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 6662, out 1077, 9.65 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, and there is an intersection visible
                        in the distance. My car is in one of the lanes near the bottom of the photo. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2; arrow:right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes or is the leftmost of the three visible lanes, which is
                        consistent with ego_lane_index=1 if the lane to the left is the leftmost lane of my
                        direction). | roles: the color and pattern of both boundaries (white dashed) fit the
                        role of lane_line. | markings: the arrows (straight and right) are present in my lane
                        and are consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The driver shall use that lane while taking a left turn if direction
                        arrows pointing to the left are marked on the road (this arrow indicates straight
                        movement, so the rule for left turn is not directly applicable, but it permits
                        straight movement). [[IN-8(1)(c)]]
Step 5  Rule            arrow:right: The driver shall remain in that lane while taking right turn if direction
                        arrows pointing to the right are marked on the road. [[IN-8(2)(c)]]
Step 5  Rule            line:stop_line: No specific rule passage was found for a stop line in this context,
                        but general rules apply to stopping. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed
                        lane_line, and while a dashed line permits lane changes, the presence of the straight
                        arrow in my lane suggests a primary path, but the boundary itself allows it if
                        signaled.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed
                        lane_line, and the rule [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The straight arrow in my lane permits this
                        movement, and no solid line prohibits it.
Step 6  turn_left       prohibited (correct): prohibited: There is no arrow indicating a left turn in my lane,
                        and no waiting area is present.
Step 6  turn_right      allowed (correct): allowed: The right arrow in my lane permits this movement, and the
                        right boundary is a dashed lane_line.
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the three visible lanes. You may proceed straight or
                        turn right, and you may change right after signaling. Turning left or making a U-turn
                        is not permitted from this lane. Be aware of the lane markings indicating your
                        permitted movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left', 'change_left
                        prohibited across a broken lane line']
Tokens                  in 6662, out 1106, 8.54 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between other lanes). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of lane_line. | markings: the text:bus marking is consistent with
                        the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of the class specified for this lane shall drive in this lane
                        only. [[IN-6(2)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a white
                        dashed line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, and
                        [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to the rules for this special lane. You may
                        change lanes left or right after signaling, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 1039, 7.41 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining both sides, and the road continues
                        into the distance. There are at least two lanes visible in my direction near the
                        bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in my lane near the bottom.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line. | markings: the text:bus marking is present in
                        my lane and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of the class specified for this lane shall drive in that lane
                        only. [[IN-6(2)]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a dashed lane_line,
                        but the text:bus marking in my lane restricts movement to buses, and [IN-6(3)]
                        prohibits other vehicles from driving in a specially marked lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        permits lane changes after signaling, provided the lane is not restricted by a special
                        marking.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You must remain in this lane as it is marked for buses, but you may change right after
                        signaling. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left prohibited
                        across a broken lane line']
Tokens                  in 6662, out 919, 8.21 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
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
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color and pattern of
                        both boundaries (white dashed) fit the role of lane_line. | markings: there are no
                        markings in my lane to check against the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict going straight along my
                        lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes left or right
                        after signaling, and you are permitted to go straight. Since there are no specific
                        turn arrows, you may proceed straight, but you should be aware of the surrounding
                        traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6662, out 828, 5.89 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp visible
                        in the close-up. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of my direction). | roles: the color (white) and pattern (dashed)
                        of both boundaries fit the role of lane_line. | markings: the text:bus marking is in
                        my lane and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of the class specified for this lane shall drive in that lane
                        only. [[IN-6(2)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must drive in this lane only. You may change lanes left
                        or right after signaling, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 873, 6.15 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch without an immediate
                        intersection visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car, followed by
                        a dashed white line further ahead. Photo 2: The line next to my car is a solid white
                        line. The line further ahead is a dashed white line.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible immediately to the right of my car, followed by
                        a solid white line further ahead. Photo 2: The line next to my car is a solid white
                        line. The line further ahead is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line, indicating two lanes in my direction) | roles: the color and pattern of
                        each boundary fit the role given to it | markings: there are no markings in my lane to
                        check for agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a lane
                        line and no prohibition is visible.
Step 6  change_right    allowed (correct): allowed because the right boundary is a lane line and no
                        prohibition is visible.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing this
                        action.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing this
                        action.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane governing
                          this action.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change lanes left or right, and
                        you may proceed straight ahead. For turning movements, you must follow local traffic
                        laws as no specific lane markings are present.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left', 'change_left allowed with the solid line of a
                        solid-and-broken pair nearer my lane']
Tokens                  in 6662, out 775, 6.65 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into the distance with traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction) | roles: the color and pattern of
                        both boundaries (white dashed) fit the role of lane_line | markings: there are no
                        markings in my lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        prohibit them.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right after signaling, and you may proceed straight ahead. No
                        specific turning movements are marked or restricted in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6662, out 794, 6.36 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, there is a
                        junction or intersection where traffic appears to be slowing down. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2; symbol:other (full): Photo 2; symbol:other (full): Photo
                        2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the symbols
                        (speed limits) in my lane agree with the boundaries as they are not conflicting with
                        lane change rules. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            symbol:other: No specific traffic rule passage covers the speed limit symbols in this
                        context. [null]
Step 6  change_left     allowed (contested, correct): allowed: The left boundary is a dashed line, and
                        [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing a U-turn, and no solid lines prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes. You may change lanes left or right after
                        signaling, and you are permitted to go straight. Use the lane appropriate for your
                        intended turn, as no specific turn arrows are present.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 6662, out 942, 7.31 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street with buildings lining both sides. Ahead, there is an
                        intersection where the road continues straight and curves slightly to the right.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows a white dashed line continuing. Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in my direction) | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line | markings: the area:grid marking is consistent
                        with the boundaries and general road markings | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        going straight, and the boundaries do not prohibit it.
Step 6  turn_left       allowed: allowed: There are no markings in my lane prohibiting turning left, and the
                        boundaries do not prohibit it.
Step 6  turn_right      allowed: allowed: There are no markings in my lane prohibiting turning right, and the
                        boundaries do not prohibit it.
Step 6  u_turn          allowed: allowed: There are no markings in my lane prohibiting a U-turn, and the
                        boundaries do not prohibit it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is marked with a grid area ahead, so you must not stop
                        there. Since both lane boundaries are dashed, you may change lanes after signaling,
                        and all movements (straight, left, right, U-turn) are permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left', 'turn_left, turn_right, u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6662, out 878, 5.95 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides, and the road continues ahead
                        into a built-up area. My car is in the lane closest to the center of the visible
                        traffic flow. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a solid white line.
                        The line next to my car is dashed, and the line further ahead is solid. There is no
                        raised curb or barrier visible. The line next to my car is dashed, and the line
                        further ahead is solid.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it transitions to a solid white line.
                        There is no raised curb or barrier visible. The line next to my car is dashed, and the
                        line further ahead is solid.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed/solid) of
                        both boundaries fit the role of lane_line. | markings: no markings were reported, so
                        there is no agreement to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): allowed: No markings prohibit going straight, and the
                        boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight, change left, or change right,
                        provided you signal. Since the lane lines are dashed, you may change lanes after
                        signaling. No specific stopping or turning instructions are visible in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6662, out 906, 6.28 s
```
