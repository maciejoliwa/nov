from enum import Enum
from dataclasses import dataclass
from typing import Union, Optional


class TokenType(Enum):

    IDENTIFIER = "<IDENTIFIER>"
    STRING = "<STRING>"
    NUMBER = "<NUMBER>"
    ASSIGN = "<-"
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

@dataclass
class Token:

    _type: TokenType
    _literal: str

