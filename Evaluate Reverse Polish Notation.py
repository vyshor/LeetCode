class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/":lambda x, y: int(operator.truediv(x, y))}
        for token in tokens:
            if token in op:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(op[token](num1, num2))
            else:
                stack.append(int(token))
        return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                right, left = int(stack.pop()), int(stack.pop())
                stack.append(str(left + right))
            elif token == "-":
                right, left = int(stack.pop()), int(stack.pop())
                stack.append(str(left - right))
            elif token == "*":
                right, left = int(stack.pop()), int(stack.pop())
                stack.append(str(left * right))
            elif token == "/":
                right, left = int(stack.pop()), int(stack.pop())
                stack.append(str(int(left / right)))
            else:
                stack.append(token)

        return int(stack[0])
