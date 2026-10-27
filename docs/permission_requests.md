# Permission to send dataset images to a third-party API

The licences of BDD100K and CULane allow non-commercial research use, but neither says whether images may be sent to an external service (here the OpenAI API) for processing. Silence is not permission, so these images are **not** sent until the owners confirm it in writing. `config/experiment.json` enforces this: `data_policy.send_to_api` lists the collections that may be sent (`own_video` only for now). Add a collection there only after a written reply, and record the reply below.

| Dataset | Licence (short) | Asked | Answer | Allowed in `send_to_api` |
|---|---|---|---|---|
| Own dash-cam video | the author's own footage | not needed | not needed | yes |
| BDD100K (US) | educational, research and non-profit use; keep the copyright notice | not yet | none | no |
| CULane (China) | non-commercial research and teaching; no redistribution | not yet | none | no |

Send each request to the contact given on the dataset's official page (BDD100K: bdd100k.com, licence page; CULane: the project page of Xingang Pan et al.). Keep the reply (e-mail as PDF) outside the repository and note its date here.

## Draft: BDD100K

> Subject: Permission request: BDD100K images and a third-party vision-language API (course research)
>
> Dear BDD100K team,
>
> I am a graduate student at the University of Florida. For the course EGN 6216 (AI Systems) I study whether giving a multimodal language model the text of the local traffic rules helps it interpret lane markings in images from different countries. I would like to use about 150 images from the BDD100K 100K validation split.
>
> Each image would be sent, one at a time, to the OpenAI API (model gpt-6.1-sol) together with a question about one marked lane marking. Under OpenAI's API terms the images are not used for training; requests are made with storage switched off, and OpenAI keeps abuse-monitoring logs for up to 30 days. No images are published or redistributed: the repository contains only image IDs, my labels and the model's text answers, and figures in reports would carry your copyright notice.
>
> Could you confirm whether this use is permitted under the BDD100K licence? I will follow any conditions you set.
>
> Thank you very much,
> Jiahao Pang, University of Florida

## Draft: CULane

> Subject: Permission request: CULane test images and a third-party vision-language API (course research)
>
> Dear Dr. Pan,
>
> I am a graduate student at the University of Florida. For the course EGN 6216 (AI Systems) I study whether giving a multimodal language model the text of the local traffic rules (GB 5768.3-2025) helps it interpret lane markings. I would like to use about 150 frames from the CULane test split, at most two per clip, for non-commercial course research only.
>
> Each frame would be sent, one at a time, to the OpenAI API (model gpt-6.1-sol) with a question about one marked lane marking. The images are not used for training under OpenAI's API terms; requests are made with storage switched off, and OpenAI keeps abuse-monitoring logs for up to 30 days. I would not publish or redistribute any frame: my public repository contains only frame IDs, my labels and the model's text answers, and no CULane image appears in any notebook or report.
>
> Does the CULane licence permit sending the frames to such an API in this way? If not, I will not use CULane images with the API.
>
> Thank you very much,
> Jiahao Pang, University of Florida

## What happens to an image that is sent

See the README, section *Data sent to the API*: one JPEG copy with the target box drawn on it, the instructions and (Test B) the rule passages, over HTTPS to OpenAI; `store: false`; not used for training by default; abuse-monitoring logs for up to 30 days; images are scanned for illegal content on upload.
