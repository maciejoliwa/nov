import pathlib
import typing
import sys
import argparse

from lexer import Lexer
from nparser import Parser

import subprocess

def get_file_path(user_given_path: str) -> typing.Optional[pathlib.Path]:
    path = pathlib.Path(user_given_path)
    
    if path.exists() and path.is_file():
        return path

    return None

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(prog='nov', description="nov transpiler")
    argparser.add_argument('Novfile',
                            metavar='novfile',
                            type=str,
                            help='Path to the nov file'
    )
    argparser.add_argument('Outfile',
                            metavar='outfile',
                            type=str,
                            help='Path to the output file'
    )
    argparser.add_argument('-n', '--no-run',
                            action='store_true',
                            help='Your .js file won\'t be run after transpilation'
    )

    args = argparser.parse_args()
    args_dict = args.__dict__
    
    path = get_file_path(args_dict["Novfile"])
    

    with open(path, 'r') as _INPUT_NOV_FILE:
        contents = _INPUT_NOV_FILE.read()

        tokens = Lexer(list(contents), 0).tokenize()
        output = Parser(tokens).parse()

        print(output) 