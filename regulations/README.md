# Regulations

One folder per country, named by its code. The prompts, the labeling tool and the scoring read everything about a country's rules from here.

| Folder | Content |
|---|---|
| `US/`, `CN/` | `region.yaml` (name, driving side, standard, which files the tasks use), `passages_marking.json` and `passages_lane.yaml` (the passages put into the prompt), `action_rules.json` and `lane_action_rules.json` (rule tables that prefill labels; never used to score the model) |
| `_common/` | the shared parts of the rule tables and the Chinese labels of the values |
| `_template/` | blank files for a new country |
| `inbox/` | PDFs of new standards (not in Git) |

A new country: copy `_template/` to `<CODE>/` and fill it in, or read the standard's PDF with the model:

```bash
python main.py regulations extract --pdf regulations/inbox/<file>.pdf --code UK --name "the United Kingdom" --driving-side left --title "..." --real
python main.py regulations check UK
python main.py regulations accept UK
```

The extractor writes `passages_draft.yaml` (every quote checked against its page, `verified_quote`) and `extraction_log.json`; the draft is used only after `accept`.
