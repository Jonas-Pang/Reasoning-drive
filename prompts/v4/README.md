# Prompt version v4

v3 with two targeted changes, made after the v3 runs (5 and 6). Files, order of the answer fields and the rule block are the same as in v3 (`../v3/README.md`), and Test A and Test B still differ only in the two slots and the rule block.

| File | Change | Why |
|---|---|---|
| `procedure.txt`, step 2 | If a rule written for this kind of marking and a general rule about all solid or broken lines both apply, the rule for this kind of marking decides. | In v3 the model answered that crossing a single solid yellow left edge line is allowed on 3 images (Test A) and 2 images (Test B). Test B cited the general passage 3A.04-01 ("a solid line discourages or prohibits crossing") instead of 3B.09-03 (left edge line). |
| `fields.txt`, definition of the action values | "allowed" and "prohibited" refer to the rule for this kind of marking; a restriction counts as prohibited; a general "discourages or prohibits" statement does not decide an action by itself. | v3 said "an action that is only discouraged counts as allowed". The model applied this to the general passage and concluded "discouraged, so allowed". |

Both changes are in the shared text, so Test A gets them too. Neither names a region, a passage or a marking's answer.

These changes were made by looking at errors on the 40 development images, and v4 is tested on the same images. A gain there is expected and does not show that v4 is better on new images; the held-out test set decides that.
