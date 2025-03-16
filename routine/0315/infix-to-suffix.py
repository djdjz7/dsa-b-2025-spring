# http://cs101.openjudge.cn/practice/24591/

from enum import Enum
from typing import List


class TokenType(Enum):
    operator = 1
    number = 2
    left_bracket = 3
    right_bracket = 4


class Token:
    __slots__ = ["type", "data"]

    def __init__(self, token_type: TokenType, data):
        self.type = token_type
        self.data = data


def parse(infix):
    num_ch = "1234567890."
    tokens = []
    num = ""
    for ch in infix:
        if ch in num_ch:
            num += ch
        else:
            if num:
                tokens.append(Token(TokenType.number, num))
                num = ""
            if ch in "+-*/":
                tokens.append(Token(TokenType.operator, ch))
            elif ch == "(":
                tokens.append(Token(TokenType.left_bracket, None))
            else:
                tokens.append(Token(TokenType.right_bracket, None))
    if num:
        tokens.append(Token(TokenType.number, num))
    return tokens


def transform(infix: List[Token]):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    operators = []
    for token in infix:
        if token.type == TokenType.number:
            output.append(token)
            continue
        if token.type == TokenType.left_bracket:
            operators.append(token)
            continue
        if token.type == TokenType.right_bracket:
            while operators[-1].type != TokenType.left_bracket:
                output.append(operators.pop())
            operators.pop()
            continue
        while (
            operators
            and operators[-1].type != TokenType.left_bracket
            and precedence[operators[-1].data] >= precedence[token.data]
        ):
            output.append(operators.pop())
        operators.append(token)
    while operators:
        output.append(operators.pop())
    return output


n = int(input())
for i in range(n):
    infix = parse(input().strip())
    suffix = transform(infix)
    print(*map(lambda x: x.data, suffix))
