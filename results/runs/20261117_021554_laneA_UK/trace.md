# Reasoning of lane run 20261117_021554_laneA_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides. The road ahead appears to be a
                        continuous street with parked cars and some moving traffic. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line on the left, with a curb and sidewalk beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line on the right, separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (left
                        edge line, right lane line). | roles: The yellow solid line on the left correctly
                        identifies the edge of the roadway, and the white line on the right separates lanes. |
                        markings: No markings are present to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid yellow edge line prohibits crossing onto the sidewalk or the
                        area beyond.
Step 5  Rule            right_boundary: The solid white lane line prohibits changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, label not_determined): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the right are prohibited
                        by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2949, out 734, 45.57 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with an intersection ahead. My car is in a lane approaching a
                        junction with traffic lights. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line and a curb on the left side of my lane.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow edge line and curb prohibit moving to the left.
Step 5  Rule            right_boundary: The dashed white line allows changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): left_boundary: prohibited by solid yellow line and
                        curb
Step 6  change_right    allowed (contested, label prohibited): right_boundary: allowed by dashed white line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can proceed straight or change into the right lane. Changing to the left is
                        prohibited by the solid yellow line and curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2949, out 697, 44.27 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a bicycle lane and a parking area on the right.
                        Ahead is a junction with traffic lights. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bicycle lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A bicycle symbol is painted in the lane to my left.;
                        line:stop_line (full): A white stop line is painted across my lane at the junction.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        to the left, parking to the right). | roles: The white solid lines correctly define
                        the boundaries of my lane. | markings: The stop line is consistent with the junction
                        ahead. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bicycle lane on the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits moving into the parking area on the
                        right.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        the junction.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right_boundary
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the line:stop_line
Step 6  turn_left       stop_first: stop_first due to the line:stop_line
Step 6  turn_right      stop_first: stop_first due to the line:stop_line
Step 6  u_turn          stop_first: stop_first due to the line:stop_line
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before proceeding through the
                        junction. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 2949, out 870, 15.74 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a sidewalk and parked cars on the left. The
                        road continues straight ahead towards a distant intersection or junction. (lanes 3,
                        mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        to the left, lane to the right). | roles: The white dashed line on the left and solid
                        line on the right are consistent with lane-line roles. | markings: No markings are
                        present to contradict the boundaries. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for a lane change to the left.
Step 5  Rule            right_boundary: The solid line prohibits a lane change to the right.
Step 6  change_left     allowed (contested, label not_determined): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or change into the left lane. Changing into the right
                        lane is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2949, out 740, 45.31 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street in the UK with parked cars on the left. The road ahead is a
                        straight stretch of a two-way street. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which has parked cars.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the oncoming traffic lane.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        text:other (full): The word 'SLOW' is painted in large white letters across the lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white center line prohibits crossing into the opposite lane.
Step 5  Rule            text:other: The 'SLOW' marking advises the driver to reduce speed.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to change lanes as both
                        boundaries are solid lines. Be mindful of the 'SLOW' marking and reduce your speed as
                        appropriate for the residential area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 736, 15.58 s
```
