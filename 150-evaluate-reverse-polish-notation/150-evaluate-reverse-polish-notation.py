import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or token.strip('-').isnumeric():
                stack.append(int(token))
            else:
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    c = a + b
                    stack.append(c)
                elif token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    c = b - a
                    stack.append(c)
                elif token == '*':
                    a = stack.pop()
                    b = stack.pop()
                    c = a * b
                    stack.append(c)
                elif token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    c = b / a
                    stack.append(math.trunc(c))
        return stack[-1]
