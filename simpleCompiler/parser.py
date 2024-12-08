"""
Input: It will recieve a list from the lexer.

Output: It will generate a tree representation called abstract syntax tree (AST)

Adding support for basic things

program = Program(function_definition)
function_definition = Function(identifier name, statement body)
statement = Return(exp)
exp = Constant(int)

"""

class Program:
    def __init__(self, function_definition):
        self.function_definition = function_definition

class Function:
    def __init__(self,identifier_name, statement_body):
        self.identifier_name = identifier_name
        self.statement_body = statement_body

class Return:
    def __init__(self,exp):
        self.exp = exp

class Constant:
    def __init__(self,integer):
        self.integer = integer
    




