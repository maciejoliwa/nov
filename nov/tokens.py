from enum import Enum
from dataclasses import dataclass
from typing import Union, Optional


class TokenType(Enum):

    IDENTIFIER = "<IDENTIFIER>"
    STRING = "<STRING>"
    NUMBER = "<NUMBER>"
    ASSIGN = "<-"
    ASSIGN_NEW = "<!"
    GREATER = ">"
    GREATER_EQ = ">="
    LESS = "<"
    LESS_EQ = "<="
    SEMICOLON = ";"
    EQUAL = "=="
    UNDERSCORE = "_"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    NEWLINE = "\n"
    TAB = "\t"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    MODULO = "%"
    COMMA = ","
    COLON = ":"
    DOT = "."
    LEFT_SQUARE_BRACKET = '['
    RIGHT_SQUARE_BRACKET = ']'

@dataclass
class Token:

    _type: TokenType
    _literal: str

