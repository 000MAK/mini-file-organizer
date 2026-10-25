# Mini File Organizer

Creates a proposed file-move plan by extension. It is dry-run by default; use --apply to move files.

## Requirements

- Python 3.10+
- Standard library only; no `pip install` step required.

## Run

```bash
python main.py --help
```

## Example

`python main.py ./sample-folder` previews moves; add `--apply` only after reviewing the plan.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety notes

Use copies of important files. Review output before using it in production. Do not add credentials, private data, or real customer files to Git.

## License

MIT. See [LICENSE](LICENSE).
