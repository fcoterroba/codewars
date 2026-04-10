import re

def calc(expression):
    tokens = re.findall(r'\d+\.?\d*|\.\d+|[+\-*/()]', expression)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def consume():
        nonlocal pos
        tok = tokens[pos]
        pos += 1
        return tok

    def parse_expression():
        left = parse_term()
        while peek() in ('+', '-'):
            op = consume()
            left = left + parse_term() if op == '+' else left - parse_term()
        return left

    def parse_term():
        left = parse_factor()
        while peek() in ('*', '/'):
            op = consume()
            left = left * parse_factor() if op == '*' else left / parse_factor()
        return left

    def parse_factor():
        token = peek()
        if token == '-':
            consume()
            return -parse_factor()
        if token == '(':
            consume()
            result = parse_expression()
            consume()
            return result
        s = consume()
        return float(s) if '.' in s else int(s)

    return parse_expression()

# original kata: https://www.codewars.com/kata/52a78825cdfc2cfc87000005
# my solution: https://www.codewars.com/kata/reviews/5ad0d4dd6165e69a5f00141d/groups/69d8d495584b4eb7368b922f
