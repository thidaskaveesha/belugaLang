import re
class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = {'function', 'if', 'return', 'int', 'float', 'bool', 'string'}
        self.token_spec = [
            ('NUMBER',   r'\d+(\.\d+)?'),   
            ('STRING',   r'".*?"'),          
            ('IDENT',    r'[a-zA-Z_][a-zA-Z_0-9]*'),  
            ('SYMBOL',   r'[{}();=+\-*/<>]'), 
            ('WHITESPACE', r'\s+'),          
            ('COMMENT',  r'//.*'),        
        ]
        self.regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_spec)

    def tokenize(self):
        for match in re.finditer(self.regex, self.code):
            kind = match.lastgroup
            value = match.group()

            if kind == 'WHITESPACE':
                continue  
            elif kind == 'COMMENT':
                continue 
            elif kind == 'IDENT' and value in self.keywords:
                kind = 'KEYWORD'  

            self.tokens.append((kind, value))

        return self.tokens