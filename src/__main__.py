import pathlib
import typing
import sys
import argparse

from lexer import Lexer
from nparser import Parser

import subprocess

_COL_END = '\033[0m'
_COL_BLUE = '\033[94m'
_COL_GREEN = '\033[92m'

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
    argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = argparser.parse_args()
    args_dict = args.__dict__
    
    verbose = args_dict["verbose"]
    print("🦊 The Nov Programming Language 🦊")
    
    if verbose:
        print(f"{_COL_BLUE}Parsing the path...{_COL_END} 🦊")
    path = get_file_path(args_dict["Novfile"])
    if verbose:
        print(f"{_COL_GREEN}Done!\n{_COL_END}")

    with open(path, 'r') as _INPUT_NOV_FILE:
        contents = _INPUT_NOV_FILE.read()

        if verbose:
            print(f"{_COL_BLUE}Tokenizing...{_COL_END} 🦊")
        tokens = Lexer(list(contents), 0).tokenize()
        if verbose:
            print(f"{_COL_GREEN}Done!\n{_COL_END}")
        
        if verbose:
            print(f"{_COL_BLUE}Parsing and transpiling the file...{_COL_END} 🦊")
        output = Parser(tokens).parse()
        if verbose:    
            print(f"{_COL_GREEN}Done!\n{_COL_END}")

    print("Successfully transpiled your nov file! 🚀")