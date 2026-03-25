from src.utils.errors import MathError

def evaluate_op(left: float, operator: str, right: float) -> float:
    """Evaluates a single binary operation."""
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        if right == 0:
            raise MathError("Error: Division by zero")
        return left / right
    else:
        raise MathError(f"Error: Unknown operator '{operator}'")
