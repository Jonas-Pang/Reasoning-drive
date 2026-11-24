# Lane prompt lane_v4

lane_v3 with the owner's perception changes of 2026-11-17 (no country-specific description of what lines look like):

1. **Close-up image** ('zoom.json'): every request carries two images in one user message: Photo 1, the photo as in
   lane_v3, and Photo 2, the road just ahead of my car cut from it at its own resolution (box per dataset). One request.
2. **Procedure** ('procedure.txt'): look at Photo 1 first, then Photo 2, then compare. For each boundary, describe the line
   next to my car and further ahead separately, count the lines, count dashes and gaps, compare left and right. Look in
   Photo 2 for words, turn arrows and waiting areas. New cross-check question 'close_up': where the two photos differ,
   next to my car Photo 2 decides, changes further ahead and far markings are read from Photo 1. The reflection step checks
   the decision against the close_up result before the final actions.
3. 'fields.txt': the boundary and marking observations mention both photos; cross_check has the new key close_up.

Everything else (rules, rule passages, fields, scoring) is lane_v3's. The test split stays frozen on lane_v3; lane_v4 is
compared with lane_v3 on the development images.
