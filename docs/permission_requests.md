# Permission to send dataset images to an external API

The BDD100K and CULane licences allow non-commercial research use but do not say whether images may be sent to an external service such as the OpenAI API. These images are therefore sent only after the dataset owners confirm it in writing. `data.send_to_api` in `config/experiment.yaml` lists the collections that may be sent.

| Dataset | Licence (short) | Permission requested | Answer | In `send_to_api` |
|---|---|---|---|---|
| Own dash-cam video | own recording | not needed | not needed | yes |
| BDD100K (US) | educational, research and non-profit use; keep the copyright notice | not yet | none | no |
| CULane (China) | non-commercial research and teaching; no redistribution | not yet | none | no |

Requests go to the contact on each dataset's official page (BDD100K: bdd100k.com; CULane: the project page of Xingang Pan et al.).

Each request sends one JPEG copy of the image with the target box, the instructions and, in Test B, the rule passages over HTTPS to OpenAI, with `store: false`.
