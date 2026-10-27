# Prompt version v1

The prompt has four parts (Milestone 3, section 6.1):

1. `instructions.txt`: the task, the three reasoning steps and what each answer field means. `{STEP2}` is filled from `step2_A.txt` or `step2_B.txt`, and `{CITATION}` from `citation_A.txt` or `citation_B.txt`. Nothing in these files describes a region's rules.
2. Rule block (Test B only): `rules_header.txt` followed by every passage of the image's region from `rules/rule_passages.json`, each with its ID, source, section and page.
3. Fixed examples from `examples.json` (text only, the same in Test A and Test B, written from development images only). Empty for now.
4. The user message: `user.txt` plus the image with the cyan box drawn on it.

Test A and Test B differ only in part 2 and in the two one-line slots. Change these files only before the criteria freeze; a changed file changes the prompt hash saved with every run.
