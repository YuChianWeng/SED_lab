---

description: "Task list for Python CLI Calculator implementation"
---

# Tasks: Python CLI Calculator

**Input**: Design documents from `/specs/001-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/repl.md

**Tests**: Tests are requested in the feature specification and constitution. TDD approach is mandated by Phase 3+.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths assume single project structure at repository root (`src/`, `tests/`)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/`, `tests/unit/`, `tests/integration/`, `src/utils/`
- [X] T002 Initialize Python environment and install dev dependencies: `pytest`, `pytest-cov`, `ruff`, `mypy`
- [X] T003 [P] Configure `ruff.toml` and `mypy.ini` for the project

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Define custom exceptions (LexerError, ParserError, MathError) in `src/utils/errors.py`
- [X] T005 [P] Define Token and Result data models in `src/parser.py` (referencing data-model.md)
- [X] T006 [P] Implement base REPL loop structure in `src/main.py` with basic I/O and error catching

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Perform basic arithmetic (+, -, *, /) within an interactive session.

**Independent Test**: Launch `src/main.py`, enter `1+2`, get `3.0`.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T007 [P] [US1] Unit tests for basic arithmetic (+, -, *, /) in `tests/unit/test_evaluator.py`
- [ ] T008 [P] [US1] Unit tests for tokenizer/parser (numbers and basic ops) in `tests/unit/test_parser.py`

### Implementation for User Story 1

- [ ] T009 [US1] Implement tokenizer for numbers and basic operators in `src/parser.py`
- [ ] T010 [US1] Implement initial Recursive Descent Parser for flat expressions in `src/parser.py`
- [X] T011 [US1] Implement evaluation logic for basic operators in `src/evaluator.py`
- [ ] T012 [US1] Integrate parser and evaluator into REPL loop in `src/main.py`
- [X] T013 [US1] Add error handling for division by zero in `src/evaluator.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Complex Expressions (Priority: P2)

**Goal**: Support parentheses `()` and operator precedence in a single expression.

**Independent Test**: Launch `src/main.py`, enter `(2+3)*4`, get `20.0`.

### Tests for User Story 2

- [ ] T014 [P] [US2] Unit tests for parentheses and operator precedence in `tests/unit/test_evaluator.py`
- [ ] T015 [P] [US2] Unit tests for nested expression parsing in `tests/unit/test_parser.py`

### Implementation for User Story 2

- [ ] T016 [US2] Update tokenizer to handle `(` and `)` symbols in `src/parser.py`
- [ ] T017 [US2] Update Recursive Descent Parser to support parentheses and precedence levels in `src/parser.py`
- [ ] T018 [US2] Update evaluator to handle nested expression results in `src/evaluator.py`
- [ ] T019 [US2] Add error handling for unbalanced parentheses in `src/parser.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Session Management (Priority: P3)

**Goal**: Manage interactive session (exiting the tool via `exit` or `quit`).

**Independent Test**: Launch `src/main.py`, type `exit`, verify tool terminates gracefully.

### Tests for User Story 3

- [ ] T020 [P] [US3] Integration tests for REPL session control in `tests/integration/test_repl.py`

### Implementation for User Story 3

- [ ] T021 [US3] Finalize command handling for `exit` and `quit` in `src/main.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T022 [P] Finalize documentation in `README.md` (derived from `quickstart.md`)
- [ ] T023 [P] Final type checking with `mypy` and linting with `ruff`
- [ ] T024 Run full test suite with `pytest-cov` and ensure 90%+ coverage

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup (Phase 1).
- **User Stories (Phase 3+)**: All depend on Foundational (Phase 2).
  - P1 → P2 → P3 recommended, though P1 and P3 are mostly independent.
- **Polish (Final Phase)**: Depends on all user stories.

### Parallel Opportunities

- T003 (Config) can run in parallel with Setup.
- T005 and T006 can run in parallel within Phase 2.
- Tests (T007, T008) can run in parallel.
- Documentation (T022) can be worked on alongside implementation.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Implement User Story 1 (Basic Arithmetic).
3. **VALIDATE**: Ensure REPL works for simple expressions.

### Incremental Delivery

1. Add User Story 2 for complex math.
2. Add User Story 3 for polished session management.
3. Each story is verified with tests before implementation (TDD).
