# Quickstart: Python CLI Calculator

## Setup Environment
1. Ensure you have **Python 3.11** or higher.
2. (Optional) Create a virtual environment:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
3. Install development dependencies:
   ```bash
   pip install pytest pytest-cov mypy ruff
   ```

## Running the Calculator
Start the interactive REPL:
```bash
python src/main.py
```
Type expressions (e.g., `(1+2)*3`) or `exit` to quit.

## Running Tests
Execute the test suite:
```bash
pytest
```
To check coverage:
```bash
pytest --cov=src tests/
```

## Linting and Typing
Run code quality checks:
```bash
ruff check src/
mypy src/
```
