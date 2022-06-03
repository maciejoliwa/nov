from dataclasses import dataclass
from typing import List, NoReturn
from tokens import Token, TokenType


_BUILTIN_FUNCTION_DEFINITIONS = {
    "to_string": "function __nov_t_str(v) { if (v) { return v.toString() } }",
    "on_click": "function __nov_on_click(e, f) { e.addEventListener('click', f); }",
    "foreach": "function __nov_for_each(arr, f) { arr.forEach(f); }",
}

_TRANSLATIONS = {
    "log": "console.log",
    "func": "function ",
    "forever": "while(true)",
    "elif": " else if",
    "and": "&&",
    "or": "||",
    "to_string": "__nov_t_str",
    "is": "===",
    "isNot": "!==",
    "else": "else ",
    "to_int": "Number.parseInt",
    "element": "document.querySelector",
    "return": "return ",
    "to_float": "Number.parseFloat",
    "new_element": "document.createElement",
    "on_click": "__nov_on_click",
    "foreach": "__nov_for_each",
}

@dataclass
class Parser:

    _tokens: List[Token]
    _current: int = 0

    def next_token(self) -> NoReturn:
        self._current += 1

    def replace_nov_identifier(self, literal: str) -> str:
        if literal in list(_TRANSLATIONS.keys()):
            return _TRANSLATIONS[literal]

        return literal

    def peek(self) -> Token:
        if self._current + 1 < len(self._tokens):
            return self._tokens[self._current + 1]

    def get_current_token(self) -> Token:
        return self._tokens[self._current]

    def parse(self) -> str:
        output = ""

        while True:
            token = self.get_current_token()

            if token is None:
                break

            if token._type == TokenType.IDENTIFIER:
                token._literal = self.replace_nov_identifier(token._literal)

                if self.peek()._type == TokenType.ASSIGN:
                    output += f"let {token._literal} = "
                    self.next_token()
                elif self.peek()._type == TokenType.ASSIGN_NEW:
                    output += f"{token._literal} = "
                    self.next_token()
                else:
                    output += token._literal

            else:
                output += token._literal

            self.next_token()

            if self._current >= len(self._tokens):
                break

        if "__nov_t_str" in output:
            output = _BUILTIN_FUNCTION_DEFINITIONS["to_string"] + "\n" + output

        if "__nov_on_click" in output:
            output = _BUILTIN_FUNCTION_DEFINITIONS["on_click"] + "\n" + output

        if "__nov_for_each" in output:
            output = _BUILTIN_FUNCTION_DEFINITIONS["foreach"] + "\n" + output

        return output
            
                