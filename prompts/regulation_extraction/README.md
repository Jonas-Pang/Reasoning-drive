Prompt of the regulation extractor (`python main.py regulations extract`): it reads a new country's marking standard
(PDF), a few pages per request, and writes the passages in the template of `regulations/_template/`. The fixed parts
are `role.txt` and `instructions.txt`; `user.txt` is filled in for every group of pages. The answer follows the JSON
schema in `reasoning_drive/regulations/extract.py`.
