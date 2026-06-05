import re

def tokenize(expression):
    if expression == "":
        return []
    regex = re.compile(r"\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

class Interpreter:
    def __init__(self):
        self.vars = {}

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens:
            return ""
        
        self.tokens = tokens
        self.pos = 0
        
        result = self.parse_expression()
        
        if self.pos != len(self.tokens):
            raise Exception("Unexpected token: " + self.tokens[self.pos])
        
        return result

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse_expression(self):
        # Look ahead: identifier followed by '=' (but not '=>')
        if (self.pos < len(self.tokens)
                and re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', self.tokens[self.pos])
                and self.pos + 1 < len(self.tokens)
                and self.tokens[self.pos + 1] == '='):
            return self.parse_assignment()
        return self.parse_additive()

    def parse_assignment(self):
        name = self.consume()          # identifier
        self.consume()                 # '='
        value = self.parse_expression()
        self.vars[name] = value
        return value

    def parse_additive(self):
        left = self.parse_multiplicative()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_multiplicative()
            left = left + right if op == '+' else left - right
        return left

    def parse_multiplicative(self):
        left = self.parse_factor()
        while self.peek() in ('*', '/', '%'):
            op = self.consume()
            right = self.parse_factor()
            if op == '*':
                left = left * right
            elif op == '/':
                if right == 0:
                    raise Exception("Division by zero")
                left = left / right
            else:
                if right == 0:
                    raise Exception("Modulo by zero")
                left = left % right
        return left

    def parse_factor(self):
        tok = self.peek()

        if tok is None:
            raise Exception("Unexpected end of expression")

        if tok == '(':
            self.consume()
            value = self.parse_expression()
            if self.peek() != ')':
                raise Exception("Expected closing ')'")
            self.consume()
            return value

        if re.fullmatch(r'[0-9]*\.?[0-9]+', tok):
            self.consume()
            return float(tok) if '.' in tok else int(tok)

        if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', tok):
            self.consume()
            if tok not in self.vars:
                raise Exception(f"ERROR: Invalid identifier. No variable with name '{tok}' was found.")
            return self.vars[tok]

        raise Exception(f"Unexpected token: {tok}")

# original kata: https://www.codewars.com/kata/53005a7b26d12be55c000243
# my solution: https://www.codewars.com/kata/reviews/543c96b122e0f3ca8a0000bc/groups/6a2280bc732e825c7b7bbebd
