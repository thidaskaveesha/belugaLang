class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        return self.generate_program(self.ast)

    def generate_program(self, program):
        code = []
        for function in program["functions"]:
            code.append(self.generate_function(function))
        return '\n'.join(code)

    def generate_function(self, function):
        header = f"def {function['name']}({', '.join(param['name'] for param in function['parameters'])}):"
        body = '\n'.join(self.generate_statement(stmt) for stmt in function['body'])
        return f"{header}\n    {body}"

    def generate_statement(self, stmt):
        if stmt["type"] == "VariableDeclaration":
            return f"{stmt['varName']} = {stmt['value']}"
        elif stmt["type"] == "ReturnStatement":
            expr = stmt['expression']
            return f"return {expr['left']} {expr['operator']} {expr['right']}"
