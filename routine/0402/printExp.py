# http://cs101.openjudge.cn/2025sp_routine/20576/


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


OPERATORS = set(["not", "and", "or"])
PRECEDENCE = {"not": 3, "and": 2, "or": 1}


def infix_to_suffix(infix):
    suffix = []
    operators = []
    for token in infix:
        if token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                suffix.append(operators.pop())
            operators.pop()
        elif token in OPERATORS:
            while (
                operators
                and operators[-1] != "("
                and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]
            ):
                suffix.append(operators.pop())
            operators.append(token)
        else:
            suffix.append(token)
    while operators:
        suffix.append(operators.pop())
    return suffix


def suffix_to_ast(suffix):
    stack = []
    for token in suffix:
        if token not in OPERATORS:
            stack.append(token)
            continue
        if token == "not":
            stack.append(Node("not", right=stack.pop()))
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(Node(token, lhs, rhs))
    return stack[0]


def ast_to_infix(ast: Node):
    arr = []
    if ast.left:
        if isinstance(ast.left, str):
            arr.append(ast.left)
        else:
            if PRECEDENCE[ast.left.val] < PRECEDENCE[ast.val]:
                arr += ["(", *ast_to_infix(ast.left), ")"]
            else:
                arr += ast_to_infix(ast.left)
    arr.append(ast.val)
    if ast.right:
        if isinstance(ast.right, str):
            arr.append(ast.right)
        else:
            if PRECEDENCE[ast.right.val] <= PRECEDENCE[ast.val]:
                arr += ["(", *ast_to_infix(ast.right), ")"]
            else:
                arr += ast_to_infix(ast.right)
    return arr


infix = input().split()
suffix = infix_to_suffix(infix)
ast = suffix_to_ast(suffix)
if isinstance(ast, str):
    print(ast)
else:
    print(*ast_to_infix(ast))
