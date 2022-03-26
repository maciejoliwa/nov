import pathlib
from re import sub
import sys
from lexer import Lexer
from nparser import Parser

import subprocess

if __name__ == '__main__':
    file = sys.argv[1]
    file_path = pathlib.Path(file)

    if not file_path.is_file():
        print("Passed path is not a file!!")

    try:
        with open(file_path, 'r') as INPUT_FILE:
            content = INPUT_FILE.read()
            lexer = Lexer(list(content), 0)
            tokens = lexer.tokenize()
            parser = Parser(tokens)

            output = parser.parse()

            output_splitted_fname = file_path.name.split('.')[0:-1]
            output_splitted_fname.append('.js')

            final_output_fname = "".join(output_splitted_fname)

            with open(final_output_fname, 'w') as OUTPUT_FILE:
                OUTPUT_FILE.write(output)

            subprocess.run(["node", final_output_fname])
    except:
        print("There was an issue opening the file!!")
