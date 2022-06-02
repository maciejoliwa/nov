import pathlib
import sys
import argparse

from lexer import Lexer
from nparser import Parser

import subprocess


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
    print(args)
