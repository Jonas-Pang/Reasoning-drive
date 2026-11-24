# Dataset images and the model API

Each request sends one JPEG copy of an image with the target box, the instructions and, in Test B, the rule passages over HTTPS to the OpenAI API, with `store: false`. `data.send_to_api` in `configs/experiment.yaml` lists the collections whose images may be sent.

| Dataset | What the licence allows | What it does not allow | In `send_to_api` |
|---|---|---|---|
| Own dash-cam video | own recording | | yes |
| BDD100K (US) | use, copy, modify and distribute for educational, research and not-for-profit purposes, without fee and without a signed licensing agreement, keeping the copyright notice | commercial use outside BDD and BAIR Commons members | yes |
| CULane (China) | free non-commercial use such as research, teaching and publication; must be cited | redistribution of the dataset or modified versions; commercial use | yes |

Sending an image to the model for inference is use of the dataset for research. No dataset image is published or redistributed: the repository holds only image IDs, labels and the model's text answers, CULane frames stay out of notebook outputs, reports may show a few frames with the citation, and labeling packages for helpers carry a no-sharing, delete-afterwards notice. Anyone reproducing the work downloads the datasets from their official pages. This is the project's reading of the licence terms; no separate permission was requested.
