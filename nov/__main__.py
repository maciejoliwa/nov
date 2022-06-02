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
    path: pathlib.Path = get_file_path(args_dict["Novfile"])
    out_path: pathlib.Path = get_file_path(args_dict["Outfile"])

    if path is None:
        print("The given .nov file does not exist or the path is invalid!")
        sys.exit(1)

    if out_path is None:
        with open(args_dict["Outfile"], 'w') as _:
            pass

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

        with open(out_path, 'w+') as OUTPUT_FILE:
            OUTPUT_FILE.write(output)

        print("Successfully transpiled your nov file! 🚀")
        
        if args_dict["no_run"] == False:
            if 'prompt' in output:
                print('Couldn\'t run file with node, since it uses web browser API')
                sys.exit(0)

            subprocess.run(['node', out_path])
