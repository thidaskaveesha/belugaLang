import sys
import os

from Lexer import Lexer
from Parser import Parser
from CodeGenerator import CodeGenerator

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python beluga.py <filename>.beluga")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".beluga"):
        print("Error: File extension must be .beluga")
        sys.exit(1)

    if not os.path.exists(filename):
        print("Error: File not found")
        sys.exit(1)

    with open(filename, "r") as file:
        code = file.read()

    try:
        # Lexing
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Code Generation
        generator = CodeGenerator(ast)
        python_code = generator.generate()

        # Write generated code to temp file
        with open("output.py", "w") as outfile:
            outfile.write(python_code)

        print("Compilation successful! Running output...")
        
        os.system(f"python output.py")

    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        sys.exit(1)
