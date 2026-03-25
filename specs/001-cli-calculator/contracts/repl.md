# Interface Contract: CLI REPL

The application provides an interactive Read-Eval-Print Loop (REPL).

## Commands

| Command | Action | Description |
|---------|--------|-------------|
| `exit` | TERMINATE | Gracefully exit the application. |
| `quit` | TERMINATE | Alias for `exit`. |
| `<expression>` | EVALUATE | Calculate mathematical expressions (e.g., `1+2`). |

## Input/Output Behavior

### Successful Calculation
- **Input**: `1 + 2 * 3`
- **Output**: `7.0` (on `stdout`)
- **Next State**: Prompt for next input.

### Error Case
- **Input**: `1 / 0`
- **Output**: `Error: Division by zero` (on `stderr`)
- **Next State**: Prompt for next input.

### Invalid Syntax
- **Input**: `(1 + 2`
- **Output**: `Error: Unbalanced parentheses at position 6` (on `stderr`)
- **Next State**: Prompt for next input.

### Malicious Input
- **Input**: `__import__('os').system('ls')`
- **Output**: `Error: Invalid character '_' at position 0` (on `stderr`)
- **Next State**: Prompt for next input.
