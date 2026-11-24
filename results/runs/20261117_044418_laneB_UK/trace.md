# Reasoning of lane run 20261117_044418_laneB_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk and curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        dashed line on my left and a solid line on my right. | roles: The dashed line on the
                        left correctly identifies a lane divider, and the solid line on the right correctly
                        identifies an edge line. | markings: The straight arrow is consistent with the lane's
                        path and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe to do so. [UK-Rule127] "A broken white line. This marks the centre of the road.
                        When this line lengthens and the gaps shorten, it means that there is a hazard ahead.
                        Do not cross it un"
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line (UK-Rule127).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow (UK-TSRGD-Part6,item20).
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change to the left lane
                        if safe. Changing to the right is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13644, out 760, 7.6 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line is visible on the right side of the
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid lines
                        correctly function as a lane divider and an edge line. | markings: No specific arrows
                        or text are visible in my lane to contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        you should not change lanes to the left or right as the boundaries are solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 777, 15.27 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides and a bus stop on the left. The road ahead
                        appears to be a straight continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the road on my right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as the rightmost lane (2) are consistent
                        with a lane line on my left and an edge line on my right. | roles: The white solid
                        line on the left is a lane divider, and the white solid line on the right is an edge
                        line. | markings: No markings were observed in the lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but as this is solid,
                        it indicates a firmer division. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid white line on
                        the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white line and curb
                        on the right
Step 6  go_straight     allowed (contested, label not_determined): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may proceed straight ahead but should not change
                        lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 638, 7.26 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides. A bus is ahead in the distance, and there
                        is a box junction in the foreground. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is used for
                        parking.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A yellow criss-cross box junction is painted in the middle of the
                        road ahead of my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. I am in
                        the left lane of a two-lane road. | roles: The solid white lines correctly define the
                        boundaries of my lane. | markings: The box junction is correctly identified in the
                        lane ahead. | unseen: None | result: consistent
Step 5  Rule            left_boundary: I should keep between the broken white lines, but since this is solid,
                        it indicates a more fixed division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            right_boundary: I should keep between the white lines. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            area:grid: I must not cause my vehicle to enter the box junction so that it has to
                        stop within the box junction due to the presence of stationary vehicles. [UK-
                        TSRGD-11(1)] "Subject to sub-paragraphs (2), (3) and (4), the yellow criss-cross
                        marking conveys the prohibition that a person must not cause a vehicle to enter the
                        box junct"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight ahead. Do not enter the box junction unless your exit is clear, as
                        you must not stop within the yellow criss-cross markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 13644, out 673, 14.67 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus and parked cars. The road continues straight ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a cycle lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has parked cars.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol and a white line are painted in the lane to
                        my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly act as lane
                        dividers. | markings: The bike symbol is in the lane to the left, not in my lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 13644, out 602, 6.72 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates the lanes.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid lines
                        correctly function as a lane divider on the left and an edge line on the right. |
                        markings: No specific arrows or words are visible in my lane; the dashed lines are
                        lane dividers. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but since this is
                        solid, it generally prohibits lane changes unless safe and necessary. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 13644, out 657, 7.13 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction ahead. My car is in one of the lanes of the
                        main carriageway. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        cycle lane or a restricted lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        dashed line on the left and a solid line on the right. | roles: The white dashed line
                        on the left and solid line on the right are consistent with standard UK lane markings.
                        | markings: No markings were observed in my lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: I may cross the dashed line to overtake or turn off if it is safe to do
                        so. [UK-Rule127] "A broken white line. This marks the centre of the road. When this
                        line lengthens and the gaps shorten, it means that there is a hazard ahead. Do not
                        cross it un"
Step 5  Rule            right_boundary: I should keep between the lane dividers, and the solid line indicates
                        a firmer restriction against crossing. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 6  change_left     allowed (correct): Allowed by the dashed white line [UK-Rule127].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no u-turn arrow is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if it is safe to do so,
                        but you should not move into the lane on your right as it is separated by a solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13644, out 690, 6.37 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street or cul-de-sac with a wide paved area ahead. The road appears to
                        end or open into a shared space/parking area. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which is adjacent to a
                        sidewalk and a building.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly act as lane
                        dividers. | markings: The straight arrow is consistent with the lane's path. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken/solid white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to proceed straight ahead as indicated
                        by the arrow. Lane changes to the left or right are prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 661, 7.65 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A wide urban street with shops on both sides. The road ahead appears to be a multi-
                        lane thoroughfare with a central area and side lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is adjacent to a
                        sidewalk and shops.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk and trees.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane dividers between lanes of the same direction. | markings: The
                        straight arrow is consistent with the lane's position and the surrounding boundaries.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You should proceed straight ahead as
                        indicated by the road marking. Lane changes to the left or right are prohibited by the
                        solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 821, 15.31 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with trees and parked cars on both sides. The road ahead
                        appears to be a continuous stretch of road with a central dividing area. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid white line separates my lane from a cycle lane on the left.
                        white solid, curb yes, special_lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        the left boundary being a special lane line (cycle lane) and the right boundary being
                        a lane line. | roles: The white solid lines correctly identify the boundaries of a
                        standard lane next to a cycle lane and another traffic lane. | markings: The straight
                        arrow is consistent with the lane's purpose and the surrounding boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: I must not drive in the cycle lane marked by a solid white line. [UK-
                        Rule140] "You MUST NOT drive or park in a cycle lane marked by a solid white line
                        during its times of operation."
Step 5  Rule            right_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            arrow:straight: I must only proceed ahead. [UK-TSRGD-Part6,item20] "Vehicular traffic
                        must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line and the cycle lane
                        rule
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and the lane
                        divider rule
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       prohibited: prohibited by the straight arrow marking
Step 6  turn_right      prohibited: prohibited by the straight arrow marking
Step 6  u_turn          prohibited: prohibited by the straight arrow marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left into
                        the cycle lane or to the right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 687, 6.23 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and a parking/stopping area on
                        the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a cycle lane on the left.
                        yellow solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or another lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on the left and a white line on the right. | roles: The yellow solid line
                        correctly identifies a special lane (cycle lane) boundary, and the white line marks
                        the edge of the usable carriageway. | markings: The straight arrow is consistent with
                        the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow line indicates a bus or designated lane, which my car should
                        not enter unless permitted. [UK-Rule141] "Bus lanes. These are shown by road markings
                        and signs that indicate which (if any) other vehicles are permitted to use the bus
                        lane."
Step 5  Rule            right_boundary: The white line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line (UK-Rule141)
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white line (UK-
                        TSRGD-S11P4-item11)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Do not attempt to change lanes
                        to the left into the cycle lane or to the right onto the pavement/parking area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 721, 8.08 s
```
