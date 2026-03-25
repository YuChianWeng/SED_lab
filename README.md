# Python CLI Calculator

A secure, interactive command-line calculator written in Python. It evaluates mathematical expressions safely using a custom-built recursive descent parser, ensuring that no arbitrary or malicious code can be executed (strictly avoids `eval()`).

## Features (What It Can Do)

* **Basic Arithmetic**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Operator Precedence**: Correctly evaluates expressions following the standard mathematical order of operations (e.g., multiplication and division are performed before addition and subtraction).
* **Parentheses for Grouping**: Supports nested parentheses `()` to override default precedence and group complex expressions.
* **Decimal & Integer Support**: Handles both whole numbers and floating-point decimals accurately. Cleanly formats whole-number results as integers.
* **Interactive REPL Loop**: Provides a continuous prompt (`>>>`) for rapid, sequential calculations without needing to restart the tool.
* **Graceful Session Management**: Easily exit the calculator by typing `exit`, `quit`, or using standard keyboard interrupts (`Ctrl+C`, `Ctrl+D`).
* **Robust Error Handling**: Safely catches mistakes without crashing the application. It points out exactly what went wrong:
  * Catching division by zero.
  * Pointing out invalid characters (e.g., letters or unsupported symbols).
  * Catching syntax errors like missing numbers, consecutive operators, or unbalanced parentheses.

## Usage Guide

### Starting the Calculator
Ensure you have Python 3.11+ installed. Run the main script from your terminal:

```bash
python src/main.py
```

### Example Calculations
Once the `>>>` prompt appears, simply type your expression and press `Enter`:

```text
>>> 1 + 2
3
>>> 2.5 * 4
10
>>> 2 * (3 + 4)
14
>>> 10 - 2 * 3
4
>>> (10 - 2) * 3
24
```

### Error Handling Examples
If an invalid expression is entered, the calculator will provide a helpful error message on standard error (`stderr`) and let you try again:

```text
>>> 5 / 0
Error: Division by zero
>>> 1 + * 2
Error: Expected number at position 4
>>> 100 $ 50
Error: Invalid character '$' at position 4
>>> (1 + 2
Error: Unexpected token at position 6
```

### Exiting
To exit the application, type:
```text
>>> exit
```
*(Alternatively, type `quit` or press `Ctrl+C`)*

---

## Developer Quickstart

If you want to contribute to or test the code:

1. **Install Dev Dependencies:**
   ```bash
   pip install pytest pytest-cov ruff mypy
   ```
2. **Run Tests:**
   ```bash
   pytest
   ```
3. **Run Linting & Type Checking:**
   ```bash
   ruff check src/
   mypy src/
   ```
