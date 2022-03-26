import pathlib
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
            p = file_path.parts[0:-1]

            content = INPUT_FILE.read()
            lexer = Lexer(list(content), 0)
            tokens = lexer.tokenize()
            parser = Parser(tokens)

            output = parser.parse()

            output_splitted_fname = file_path.name.split('.')[0:-1]
            output_splitted_fname[-1] += ".js"
            output_splitted_fname = list(p) + output_splitted_fname

            output_splitted_fname = pathlib.Path(*output_splitted_fname)

            with open(output_splitted_fname, 'w') as OUTPUT_FILE:
                OUTPUT_FILE.write(output)

            subprocess.run(["node", output_splitted_fname])
    except:
        print("There was an issue opening the file!!")
