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
