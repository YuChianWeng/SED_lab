import pytest
from src.parser import Tokenizer, Parser, TokenType
from src.utils.errors import LexerError, ParserError

def test_tokenizer_numbers():
    tokenizer = Tokenizer("123.45")
    tokens = tokenizer.tokenize()
    assert len(tokens) == 2  # NUMBER, EOF
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].value == 123.45
    assert tokens[0].position == 0

def test_tokenizer_operators():
    tokenizer = Tokenizer("1 + 2 * 3 / 4 - 5")
    tokens = tokenizer.tokenize()
    # 1, +, 2, *, 3, /, 4, -, 5, EOF
    assert len(tokens) == 10
    types = [t.type for t in tokens]
    assert types == [
        TokenType.NUMBER, TokenType.OPERATOR, TokenType.NUMBER, TokenType.OPERATOR,
        TokenType.NUMBER, TokenType.OPERATOR, TokenType.NUMBER, TokenType.OPERATOR,
        TokenType.NUMBER, TokenType.EOF
    ]

def test_tokenizer_invalid_char():
    tokenizer = Tokenizer("1 @ 2")
    with pytest.raises(LexerError, match="Error: Invalid character '@' at position 2"):
        tokenizer.tokenize()

def test_parser_simple_expression():
    parser = Parser("1 + 2")
    # This will use the evaluator internally once integrated or we can mock it
    # For now, let's assume Parser.parse() returns the result value
    assert parser.parse() == 3.0

def test_parser_precedence():
    parser = Parser("1 + 2 * 3")
    assert parser.parse() == 7.0

def test_parser_malformed():
    parser = Parser("1 + + 2")
    with pytest.raises(ParserError, match="Error: Expected number at position 4"):
        parser.parse()
