# Implementation Plan: Python CLI Calculator

**Branch**: `001-cli-calculator` | **Date**: 2026-03-25 | **Spec**: specs/001-cli-calculator/spec.md
**Input**: Feature specification from `/specs/001-cli-calculator/spec.md`

## Summary

The goal is to build a secure, interactive CLI calculator in Python 3.11. The implementation will focus on a custom parser (avoiding `eval()`) to handle basic arithmetic and parentheses, ensuring safety and robust error handling.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: None (Standard Library only for core logic); pytest (dev)
**Storage**: N/A
**Testing**: pytest
**Target Platform**: Linux/Universal
**Project Type**: CLI Application (REPL)
**Performance Goals**: Response for valid expressions under 100ms
**Constraints**: Absolute ban on `eval()` and `exec()`. Must use safe parsing (AST or Recursive Descent).
**Scale/Scope**: Basic arithmetic (+, -, *, /) and parentheses `()`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Safety**: Verify no usage of `eval()`, `exec()`, or unsafe input parsing. (Plan: Use hand-written recursive descent parser).
- [x] **II. Clean Code**: Logic separated from CLI parser and formatting layers. (Plan: Decoupled parser and evaluator).
- [x] **III. Readability**: PEP 8 compliance and Google-style docstrings planned.
- [x] **IV. Test-First**: Unit tests for all mathematical operations and edge cases. (Using pytest).
- [x] **V. Error Handling**: User-friendly error messages on `stderr`, no raw stack traces.
- [x] **Quality Gates**: Typing (mypy), Linting (ruff), Coverage (pytest-cov 90%+).

## Project Structure

```text
src/
├── main.py              # Entry point & REPL loop
├── parser.py            # Tokenizer and Recursive Descent Parser
├── evaluator.py         # Mathematical evaluation logic
└── utils/
    └── errors.py        # Custom exceptions and error reporting
tests/
├── unit/
│   ├── test_parser.py   # Parser & Tokenizer tests
│   └── test_evaluator.py # Calculation logic tests
└── integration/
    └── test_repl.py     # REPL interaction tests
```

**Structure Decision**: Single project structure is chosen as this is a standalone CLI tool without a backend/frontend split.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Custom Parser | Security (No Eval) | `eval()` is unsafe for user input. |
