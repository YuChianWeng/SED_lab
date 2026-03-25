from dataclasses import dataclass
from enum import Enum, auto
from typing import Union, Optional, List
from src.utils.errors import LexerError, ParserError, MathError
from src.evaluator import evaluate_op

class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    PAREN_OPEN = auto()
    PAREN_CLOSE = auto()
    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: Union[float, str, None]
    position: int

@dataclass
class Result:
    value: Optional[float] = None
    error: Optional[str] = None
    position: int = 0

class Tokenizer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def tokenize(self) -> List[Token]:
        tokens = []
        while self.pos < len(self.text):
            char = self.text[self.pos]
            if char.isspace():
                self.pos += 1
            elif char.isdigit() or char == '.':
                tokens.append(self._read_number())
            elif char in '+-*/':
                tokens.append(Token(TokenType.OPERATOR, char, self.pos))
                self.pos += 1
            elif char == '(':
                tokens.append(Token(TokenType.PAREN_OPEN, char, self.pos))
                self.pos += 1
            elif char == ')':
                tokens.append(Token(TokenType.PAREN_CLOSE, char, self.pos))
                self.pos += 1
            else:
                raise LexerError(f"Invalid character '{char}'", self.pos)
        
        tokens.append(Token(TokenType.EOF, None, self.pos))
        return tokens

    def _read_number(self) -> Token:
        start_pos = self.pos
        dot_count = 0
        while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
            if self.text[self.pos] == '.':
                dot_count += 1
                if dot_count > 1:
                    break
            self.pos += 1
        
        val_str = self.text[start_pos:self.pos]
        try:
            return Token(TokenType.NUMBER, float(val_str), start_pos)
        except ValueError:
            raise LexerError(f"Invalid number '{val_str}'", start_pos)

class Parser:
    """
    Recursive Descent Parser for mathematical expressions.
    Grammar:
    expr   : term ((PLUS | MINUS) term)*
    term   : factor ((MUL | DIV) factor)*
    factor : NUMBER | LPAREN expr RPAREN
    """
    def __init__(self, text: str):
        tokenizer = Tokenizer(text)
        self.tokens = tokenizer.tokenize()
        self.pos = 0

    def _current_token(self) -> Token:
        return self.tokens[self.pos]

    def _consume(self, token_type: Optional[TokenType] = None) -> Token:
        token = self._current_token()
        if token_type and token.type != token_type:
            raise ParserError(f"Expected {token_type.name}", token.position)
        self.pos += 1
        return token

    def parse(self) -> float:
        result = self._expr()
        if self._current_token().type != TokenType.EOF:
            raise ParserError("Unexpected token", self._current_token().position)
        return result

    def _expr(self) -> float:
        result = self._term()
        while self._current_token().type == TokenType.OPERATOR and self._current_token().value in '+-':
            op = self._consume().value
            right = self._term()
            result = evaluate_op(result, op, right)
        return result

    def _term(self) -> float:
        result = self._factor()
        while self._current_token().type == TokenType.OPERATOR and self._current_token().value in '*/':
            op = self._consume().value
            right = self._factor()
            result = evaluate_op(result, op, right)
        return result

    def _factor(self) -> float:
        token = self._current_token()
        if token.type == TokenType.NUMBER:
            self._consume()
            return token.value
        elif token.type == TokenType.PAREN_OPEN:
            self._consume()
            result = self._expr()
            self._consume(TokenType.PAREN_CLOSE)
            return result
        else:
            raise ParserError(f"Expected number at position {token.position}", token.position)
