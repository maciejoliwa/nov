from re import sub
from lexer import Lexer
from nparser import Parser

import subprocess

with open("entry.nov", "r") as INPUT_FILE:
    content = INPUT_FILE.read()
    lexer = Lexer(list(content), 0)
    tokens = lexer.tokenize()
    parser = Parser(tokens)

    output = parser.parse()

    with open('nov.js', 'w') as OUTPUT_FILE:
        OUTPUT_FILE.write(output)

    subprocess.run(["node", "nov.js"])