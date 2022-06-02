import pathlib
import sys
import argparse

from lexer import Lexer
from nparser import Parser

import subprocess


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description="nov transpiler")
    argparser.add_argument('Novfile',
                            metavar='novfile',
                            type=str,
                            help='Path to the nov file'
    )
