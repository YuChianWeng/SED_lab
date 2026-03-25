import pytest
from src.evaluator import evaluate_op
from src.utils.errors import MathError

def test_evaluate_addition():
    assert evaluate_op(1.0, '+', 2.0) == 3.0
    assert evaluate_op(-1.0, '+', 5.0) == 4.0

def test_evaluate_subtraction():
    assert evaluate_op(10.0, '-', 4.0) == 6.0
    assert evaluate_op(2.0, '-', 5.0) == -3.0

def test_evaluate_multiplication():
    assert evaluate_op(3.0, '*', 4.0) == 12.0
    assert evaluate_op(-2.0, '*', 3.0) == -6.0

def test_evaluate_division():
    assert evaluate_op(8.0, '/', 2.0) == 4.0
    assert evaluate_op(5.0, '/', 2.0) == 2.5

def test_evaluate_division_by_zero():
    with pytest.raises(MathError, match="Error: Division by zero"):
        evaluate_op(5.0, '/', 0.0)

def test_evaluate_unknown_operator():
    with pytest.raises(MathError, match="Error: Unknown operator '%'"):
        evaluate_op(5.0, '%', 2.0)
