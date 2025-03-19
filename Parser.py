class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else (None, None)

    def advance(self):
        token = self.peek()
        self.current += 1
        return token

    def expect(self, expected_type, expected_value=None):
        token = self.peek()
        if token[0] != expected_type or (expected_value and token[1] != expected_value):
            raise SyntaxError(f"Expected {expected_type} '{expected_value}', got {token}")
        return self.advance()

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        functions = []
        while self.peek()[0] is not None:
            functions.append(self.parse_function_declaration())
        return {"type": "Program", "functions": functions}

    def parse_function_declaration(self):
        return_type = self.expect("KEYWORD")[1]  # e.g., 'int'
        self.expect("KEYWORD", "function")
        name = self.expect("IDENT")[1]
        self.expect("SYMBOL", "(")
        parameters = self.parse_parameters()
        self.expect("SYMBOL", ")")
        self.expect("SYMBOL", "{")
        body = self.parse_block()
        self.expect("SYMBOL", "}")
        return {"type": "FunctionDeclaration", "returnType": return_type, "name": name, "parameters": parameters, "body": body}

    def parse_parameters(self):
        parameters = []
        while self.peek()[0] != "SYMBOL" or self.peek()[1] != ")":
            param_type = self.expect("KEYWORD")[1]
            param_name = self.expect("IDENT")[1]
            parameters.append({"type": param_type, "name": param_name})
            if self.peek()[1] == ",":
                self.advance()  # Skip comma
        return parameters

    def parse_block(self):
        statements = []
        while self.peek()[0] != "SYMBOL" or self.peek()[1] != "}":
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.peek()
        if token[0] == "KEYWORD" and token[1] in {"int", "float", "bool", "string"}:
            return self.parse_variable_declaration()
        elif token[0] == "KEYWORD" and token[1] == "return":
            return self.parse_return_statement()
        else:
            raise SyntaxError(f"Unexpected statement: {token}")

    def parse_variable_declaration(self):
        var_type = self.expect("KEYWORD")[1]  # e.g., 'int'
        var_name = self.expect("IDENT")[1]
        self.expect("SYMBOL", "=")
        value = self.expect("NUMBER")[1]  # Simplified to support only numbers for now
        self.expect("SYMBOL", ";")
        return {"type": "VariableDeclaration", "varType": var_type, "varName": var_name, "value": value}

    def parse_return_statement(self):
        self.expect("KEYWORD", "return")
        expression = self.parse_expression()
        self.expect("SYMBOL", ";")
        return {"type": "ReturnStatement", "expression": expression}

    def parse_expression(self):
        # Simplified: Only supports binary expressions with numbers for now
        left = self.expect("IDENT")[1]
        operator = self.expect("SYMBOL")[1]
        right = self.expect("IDENT")[1]
        return {"type": "BinaryExpression", "left": left, "operator": operator, "right": right}
