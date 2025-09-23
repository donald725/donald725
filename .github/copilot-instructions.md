## Purpose

This file gives concise, actionable guidance for AI coding agents to be immediately productive in this repository.

## Big-picture overview

- Small personal repo with three focused areas:
  - `PyCode/` — utility scripts (e.g., `PyCode/LakeLevel_Temp2.py`) that perform web scraping and text extraction.
  - `My-App/` — intended application code (`App.py`) and tests (`Tests.py`) — currently empty placeholders.
  - `Jupyter/` — interactive experiments (`Notebook.ipynb`).

There is no package or build system present (no `requirements.txt`, `pyproject.toml`, or `Pipfile`).

## Key integration & dataflow patterns (examples from repo)

- `PyCode/LakeLevel_Temp2.py` fetches a public page using `requests`, parses HTML with `BeautifulSoup`, then applies regular expressions against `soup.get_text()` to extract fields like report date, lake level and surface temperature. Example patterns used:
  - Regex: `r"(Report.*)\n(\d\d.*)"` and `r"(Current.*)\n(\d\d.*)"` — expects a label line followed by a numeric/date line.
  - Output is printed to stdout via `print(...)` (no return/value abstraction).

## Developer workflows (how to run / debug right now)

- Run a script directly (macOS, zsh):

```bash
python3 PyCode/LakeLevel_Temp2.py
```

- Install the runtime dependencies the script uses (not provided):

```bash
python3 -m pip install requests beautifulsoup4
```

- There are no automated tests or CI configured. `My-App/Tests.py` exists but is empty.
- Tests are present under `My-App/` using `pytest` (e.g., `My-App/test_lakelevel.py`). Run tests using the Python module runner to avoid PATH issues:

```bash
python3 -m pytest -q
```

## Project-specific conventions

- Scripts are lightweight, script-first (top-level execution). When modifying or extending, prefer adding small functions and returning values instead of only printing, so tests and reuse are easier.
- Prefer using the existing scraping pattern in `PyCode/LakeLevel_Temp2.py`: fetch -> soup -> text -> regex. If you change the parsing, update the regexes and keep prints for quick CLI feedback.

## When modifying the repo, discoverable rules to follow

- If you add third-party dependencies, add a `requirements.txt` at the repo root with pinned names (example: `requests==...` and `beautifulsoup4==...`). No lockfile is present.
- If you add tests, place them under `My-App/` or a top-level `tests/` folder and use plain `unittest` or `pytest`; there is no existing test runner configuration.

## Useful files to inspect

- `PyCode/LakeLevel_Temp2.py` — primary working example for web scraping and text extraction.
- `Jupyter/Notebook.ipynb` — exploratory analysis (open in Jupyter for context).
- `My-App/App.py`, `My-App/Tests.py` — currently placeholders; check before adding similarly-named modules.

## Safety & expectations for AI edits

- Preserve existing top-level scripts' CLI behavior unless explicitly refactoring. For `LakeLevel_Temp2.py`, keep prints or provide a CLI switch so existing usage doesn't break.
- Avoid creating heavy infra changes (no CI, packaging or container files exist).

---

If anything here is unclear or you want the file to include more examples (for instance, a recommended `requirements.txt` or a suggested test for `LakeLevel_Temp2.py`), tell me what to add and I will update this file.
