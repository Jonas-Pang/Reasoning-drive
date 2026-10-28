# Prompt version v2

Same four parts, same schema, same user message and the same rule block as v1 (`../v1/README.md`). Test A and Test B still differ only in the rule block and the two one-line slots. v2 changes the shared instructions, for every image and both tests, to reduce answers that are not supported by the image or by the rules. Each change answers an error seen on the development images with v1:

| Change | Why (v1 development run) |
|---|---|
| Step 1 "Look" describes only visible features and forbids inferring colour or arrow direction from position; hidden features lower the evidence level | keeps perception separate from rule knowledge; the place where guessing starts |
| The movements are defined for the lane the marking belongs to, including turning left out of a two-way left-turn lane between intersections | v1 defined movements "at the next intersection from the lane the arrow is in"; with the rule text the model called turn_left in a two-way left-turn lane not applicable |
| Which actions each marking class governs is stated (line: cross_line; arrow: movements; two-way left-turn lane: entering and turning left; other: none) | v1 answers set movements for a two-way left-turn lane and actions for lines that the marking does not govern |
| not_determined only with partial or insufficient evidence; with full evidence every governed action is allowed or prohibited | v1 answered not_determined for a U-turn from a fully visible left-turn arrow |
| Step 4 "Check" before answering, and reasoning must name the visible feature and the rule | an in-prompt self-check of the answer against these constraints |
| Test B: use the passages, not memory; cite only IDs in the list | grounding of the decision in the given text |

What v2 deliberately does not do: it contains no region's rules (Test A must still rely on the model's own knowledge), and no examples (examples written from the same development images that are scored would inflate the scores; they need a separate pool of development images first).

`lane_reasoner.scoring.consistency_issues` checks every answer against the same constraints without the API, so the effect of v2 on unsupported or contradictory answers can be measured.
