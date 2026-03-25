# Research: Python CLI Calculator

## Design Decisions

### 1. Parsing Strategy: Recursive Descent Parser
- **Decision**: Implement a hand-written Recursive Descent Parser instead of using `eval()`, `ast.literal_eval()`, or external libraries.
- **Rationale**: 
    - **Security**: Provides complete control over which operations are allowed, preventing any code execution vulnerabilities.
    - **Precision**: Allows for specific error messages like "Missing closing parenthesis at position X" or "Expected operator, found Y".
    - **Simplicity**: For the scope of basic arithmetic and parentheses, a recursive descent parser is lightweight and easy to maintain.
- **Alternatives considered**: 
    - `eval()`: Rejected due to severe security risks (Constitution violation).
    - `ast.literal_eval()`: Rejected as it doesn't support complex expressions like `(1+2)*3`.
    - `shunting-yard algorithm`: Good for infix to postfix conversion, but recursive descent is more idiomatic for building an AST or direct evaluation in Python.

### 2. Testing Framework: pytest
- **Decision**: Use `pytest` for all testing.
- **Rationale**: 
    - **Ecosystem**: Standard testing tool for Python.
    - **Features**: Supports parameterized tests which are ideal for evaluating hundreds of different mathematical expressions.
- **Alternatives considered**: 
    - `unittest`: Standard library, but requires more boilerplate and is less flexible for parameterization.

### 3. Error Handling
- **Decision**: Custom Exception hierarchy in `utils/errors.py`.
- **Rationale**:
    - **Granularity**: Allows the REPL to distinguish between "User interrupted session" (exit), "Lexing error" (invalid characters), and "Parsing error" (bad syntax).
    - **Consistency**: Centralized location for all error reporting logic ensures a uniform user experience on `stderr`.
