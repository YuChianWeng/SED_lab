<!--
Sync Impact Report
- Version change: N/A → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Safety (No Unsafe Eval)
  - [PRINCIPLE_2_NAME] → II. Clean Code & Modular Design
  - [PRINCIPLE_3_NAME] → III. Readability & Documentation
  - [PRINCIPLE_4_NAME] → IV. Test-First Discipline
  - [PRINCIPLE_5_NAME] → V. Robust Error Handling
- Added sections:
  - Additional Constraints (Section 2)
  - Quality Gates (Section 3)
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ updated)
- Follow-up TODOs: None
-->

# Python CLI Calculator Constitution

## Core Principles

### I. Safety (No Unsafe Eval)
The application MUST NOT use `eval()`, `exec()`, or any other mechanism that executes arbitrary strings as code. Mathematical expression parsing must be handled by a secure, dedicated parser or a white-listed tokenization strategy.
**Rationale**: Preventing arbitrary code execution is the highest priority for a CLI tool handling user-provided input.

### II. Clean Code & Modular Design
Logic must be separated into discrete, single-purpose modules. The calculator engine (math logic), the CLI parser, and the formatting/output layer must remain decoupled.
**Rationale**: Modular design ensures maintainability and allows for independent testing of the core logic without CLI overhead.

### III. Readability & Documentation
Code must follow PEP 8 standards. Every public function and class must have a Google-style docstring explaining its purpose, parameters, and return values. Variable names must be descriptive.
**Rationale**: As a tool intended for utility and potential extension, the codebase must be immediately understandable by new contributors.

### IV. Test-First Discipline
Every new mathematical operation or feature must have corresponding unit tests that cover both happy paths and edge cases (e.g., division by zero, overflow). Testing must be performed using `pytest`.
**Rationale**: Automated verification is the only way to ensure the mathematical correctness and reliability of the calculator.

### V. Robust Error Handling
The application MUST NOT crash or show raw stack traces to the user. All errors (invalid input, math errors, system errors) must be caught and reported via a user-friendly error message on `stderr`.
**Rationale**: A professional CLI tool provides clear feedback and fails gracefully.

## Technical Constraints

- **Language**: Python 3.10+
- **Standard Library**: Prefer standard library modules (e.g., `math`, `argparse`) unless a specialized library is justified for security or complexity.
- **Dependencies**: Any external dependency must be audited for security and justified in the implementation plan.

## Quality Gates

1. **Linting**: All code must pass `flake8` or `ruff` checks.
2. **Typing**: Use `mypy` for static type checking; public APIs must be fully typed.
3. **Coverage**: Minimum 90% code coverage for the core calculator engine.

## Governance

This constitution supersedes all other development practices within this project. Amendments to these principles require a MINOR version bump. Removal of a safety constraint requires a MAJOR version bump.

All Pull Requests must be reviewed against these principles. If a "Constitution Check" in a plan fails, the violation must be explicitly justified and approved.

**Version**: 1.0.0 | **Ratified**: 2026-03-25 | **Last Amended**: 2026-03-25
