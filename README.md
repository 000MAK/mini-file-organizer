# Mini File Organizer

A Python command-line utility that previews a file-move plan based on file extensions. It is **dry-run by default**; files move only when the explicit `--apply` flag is supplied.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Lists files in the selected folder and proposes destination subfolders based on extension.
- Uses lowercase extension names as folder names; extensionless files are grouped under `no-extension`.
- Shows the plan without moving files by default.
- When applying a plan, chooses an alternate filename if the destination name already exists.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Preview the plan (no files are moved):

```bash
python main.py ./sample-folder
```

Apply the move plan only after reviewing the printed destinations:

```bash
python main.py ./sample-folder --apply
```

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests cover previewing without moving files and applying a simple move plan.

## Safety notes and limitations

- Start with a disposable sample folder or backup.
- The `--apply` option performs actual moves; review the dry-run output first.
- The tool organizes files from the selected folder's top level; it is not a general-purpose backup or synchronization utility.
- Check the destination structure and file names before relying on the result.

## Related Quantix projects

- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Quantix 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)
- [All public repositories](https://github.com/000MAK?tab=repositories)

## License

MIT. See [LICENSE](LICENSE).
