# Datasets

One folder per country, with the same code as `regulations/<CODE>/`. Images stay outside the repository (`DATASETS_ROOT` in `.env`); only labels, splits and hashes are here.

| Folder or file | Content |
|---|---|
| `US/`, `CN/` | `dataset.yaml` (collections, sources, licences, split rule) and one folder per label collection: the final labels of one labeling workspace (`python main.py label`) |
| `_template/` | `dataset.yaml` and the label header for a new country |
| `splits/` | the combined split of all countries (`split_v*.csv`), separation checks, coverage per marking type, candidate supply, moved clips |
| `sources.json`, `data_manifest.csv`, `data_hashes.csv` | where every download comes from, its licence and hashes |

The split rule is the same for every country: a clip goes to development if `sha1("6216:" + clip) mod 10 = 0`, otherwise to the test pool; 6 development and 30 test images per marking type, plus 30 degraded test images. `python main.py label combine <workspaces>` writes the next split version.
