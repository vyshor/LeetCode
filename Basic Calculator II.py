class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currentNum = ""
        op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

        for c in s:
            if c in op:
                if currentNum:
                    stack.append(int(currentNum))
                    currentNum = ""
                stack.append(c)
            else:
                currentNum += c

        if currentNum:
            stack.append(int(currentNum))

        stack2 = []
        i = 0
        n = len(stack)
        while i < n:
            if stack[i] == "*" or stack[i] == "/":
                stack2.append(op[stack[i]](stack2.pop(), stack[i + 1]))
                i += 1
            else:
                stack2.append(stack[i])
            i += 1

        stack = []
        n = len(stack2)
        i = 0
        while i < n:
            if stack2[i] in op:
                stack.append(op[stack2[i]](stack.pop(), stack2[i + 1]))
                i += 1
            else:
                stack.append(stack2[i])
            i += 1

        return stack[0]

