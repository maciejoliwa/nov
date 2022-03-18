from dataclasses import dataclass
from typing import List, NoReturn, Any
from enum import IntEnum, auto
from tokens import TokenType, Token 

class LexerParsingState(IntEnum):

    EOF = 0,
    CONTINUE = auto()


@dataclass
class Lexer:
    
    _characters: List[str]
    _current: int

    def get_current_character(self) -> str:
        return self._characters[self._current]

    def is_whitespace(self) -> bool:
        is_space = self.get_current_character().isspace()
        return is_space

    def next_character(self) -> LexerParsingState:
        if (self._current + 1) < len(self._characters):
            self._current += 1
            return LexerParsingState.CONTINUE
        else:
            return LexerParsingState.EOF

    def peek(self) -> str:
        if self._current + 1 < len(self._characters):
            return self._characters[self._current + 1]

    def skip_whitespace(self) -> NoReturn:
        while self.is_whitespace():
            self.next_character()

    def parse_identifer(self, _literal: str) -> Token:
        next_character = self.peek()

        if next_character is None:
            return Token(TokenType.IDENTIFIER, _literal)

        if next_character.isalpha() or next_character == '_':
            _literal += next_character
            self.next_character()
            return self.parse_identifer(_literal)

        return Token(TokenType.IDENTIFIER, _literal)

    def parse_number(self, _literal: str) -> Token:
        next_character = self.peek()

        if next_character is None:
            return Token(TokenType.NUMBER, _literal)

        if next_character.isdigit():
            _literal += next_character
            self.next_character()
            return self.parse_number(_literal)

        return Token(TokenType.NUMBER, _literal)

    def parse_string(self, string: str) -> Token:
        next_character = self.peek()

        if next_character is None:
            return Token(TokenType.STRING, string)

        if next_character != '\"':
            string += next_character
            self.next_character()
            return self.parse_string(string)

        self.next_character()
        return Token(TokenType.STRING, string + '"')

    def tokenize(self) -> List[Token]:
        tokens = []

        while True:
            # self.skip_whitespace()
            character = self.get_current_character()

            if character == '<' and self.peek() == '-':
                tokens.append(Token(TokenType.ASSIGN, '<-'))
                self.next_character()
            
            elif character == '<' and self.peek() == '=':
                tokens.append(Token(TokenType.LESS_EQ, '<='))
                self.next_character()

            elif character == '<' and self.peek() == '!':
                tokens.append(Token(TokenType.ASSIGN_NEW, '<!'))
                self.next_character()

            elif character == '<':
                tokens.append(Token(TokenType.LESS, '<'))

            elif character == '>' and self.peek() == '=':
                tokens.append(Token(TokenType.GREATER_EQ, '>='))
                self.next_character()

            elif character == '>':
                tokens.append(Token(TokenType.GREATER, '>'))
            
            elif character == ';':
                tokens.append(Token(TokenType.SEMICOLON, ';'))

            elif character == '(':
                tokens.append(Token(TokenType.LEFT_PAREN, '('))

            elif character == ')':
                tokens.append(Token(TokenType.RIGHT_PAREN, ')'))

            elif character == '+':
                tokens.append(Token(TokenType.PLUS, '+'))

            elif character == '-':
                tokens.append(Token(TokenType.MINUS, '-'))

            elif character == '*':
                tokens.append(Token(TokenType.MULTIPLY, '*'))

            elif character == '/':
                tokens.append(Token(TokenType.DIVIDE, '/'))

            elif character == '\n':
                tokens.append(Token(TokenType.NEWLINE, '\n'))

            elif character == '_':
                tokens.append(Token(TokenType.UNDERSCORE, '_'))
            
            elif character == '{':
                tokens.append(Token(TokenType.LEFT_BRACE, '{'))

            elif character == '}':
                tokens.append(Token(TokenType.RIGHT_BRACE, '}'))

            elif character == '=' and self.peek() == '=':
                tokens.append(Token(TokenType.EQUAL, '==='))

            # PARSE IDENTIFIER
            elif character.isalpha():
                tokens.append(self.parse_identifer(character))

            elif character == '"':
                tokens.append(self.parse_string(character))
            
            # PARSE NUMBER
            elif character.isdigit():
                tokens.append(self.parse_number(character))

            state = self.next_character()

            if state == LexerParsingState.EOF:
                break

        return tokens