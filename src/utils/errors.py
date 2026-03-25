class CalculatorError(Exception):
    """Base class for all calculator exceptions."""
    pass

class LexerError(CalculatorError):
    """Exception raised for errors during lexical analysis."""
    def __init__(self, message, position):
        super().__init__(f"Error: {message} at position {position}")
        self.position = position

class ParserError(CalculatorError):
    """Exception raised for errors during parsing."""
    def __init__(self, message, position):
        super().__init__(f"Error: {message} at position {position}")
        self.position = position

class MathError(CalculatorError):
    """Exception raised for errors during evaluation (e.g., division by zero)."""
    pass
