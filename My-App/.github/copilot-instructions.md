# Copilot Instructions for AI Coding Agents

## Project Overview
This codebase is a simple Python application with two main files:
- `App.py`: Main application logic
- `Tests.py`: Contains test cases for the application

## Architecture & Data Flow
- The project is monolithic and script-based, with all logic in top-level Python files.
- There are no submodules, packages, or external service integrations.
- Data flow is direct between functions/classes in `App.py` and their corresponding tests in `Tests.py`.

## Developer Workflows
- **Run the application:**
  ```zsh
  python App.py
  ```
- **Run tests:**
  ```zsh
  python Tests.py
  ```
- No build step is required; scripts can be executed directly.
- No external dependencies are required unless specified in the code (check for `import` statements).

## Project-Specific Conventions
- All code is in the workspace root; no folders or packages are used.
- Tests are in a separate file (`Tests.py`), not using a framework like `pytest` or `unittest` unless explicitly imported.
- If adding new features, place main logic in `App.py` and corresponding tests in `Tests.py`.
- Use clear function and variable names; follow existing naming patterns.

## Integration Points
- No external APIs, databases, or cloud services are integrated by default.
- If you add dependencies, document them in a `requirements.txt` file and update this instruction file.

## Examples
- To add a new function, define it in `App.py` and write a test for it in `Tests.py`.
- To debug, insert print statements or use Python's built-in `pdb` module.

## Key Files
- `App.py`: Main logic
- `Tests.py`: Test cases

---

If any conventions or workflows are unclear, please ask for clarification or provide suggestions for improvement.
