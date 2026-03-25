# Data Model: Python CLI Calculator

## Token Types
Represents the basic building blocks of a mathematical expression.

| Type | Examples | Description |
|------|----------|-------------|
| NUMBER | 1, 3.14, 42 | Numerical values (float/int) |
| OPERATOR | +, -, *, / | Basic arithmetic operators |
| PAREN_OPEN | ( | Opening grouping symbol |
| PAREN_CLOSE | ) | Closing grouping symbol |
| EOF | | End of expression marker |

## Entities

### 1. Token
```python
@dataclass
class Token:
    type: TokenType
    value: Union[float, str, None]
    position: int
```

### 2. Result
The outcome of an evaluation.

| Field | Type | Description |
|-------|------|-------------|
| value | Optional[float] | Calculated value if successful |
| error | Optional[str] | Error message if evaluation failed |
| position | int | Error position index for highlighting errors |

## Validation Rules
- **Numbers**: MUST be valid float representations.
- **Parentheses**: MUST be balanced.
- **Operators**: MUST NOT be consecutive (except unary +/- if supported).
- **Division**: Denominator MUST NOT be zero.
