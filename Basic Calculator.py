class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        op = {"+": operator.add, "-": operator.sub}

        def evaluate(operate):
            # print(operate)
            size = len(operate)
            j = size - 1
            currentNum = ""
            summ = 0
            while j >= 0:
                if operate[j] in op:
                    num = int(currentNum)
                    summ = op[operate[j]](summ, num)
                    currentNum = ""
                else:
                    currentNum = operate[j] + currentNum
                j -= 1

            if currentNum != "":
                num = int(currentNum)
                summ += num

            return summ

        n = len(s)
        i = 0
        stack = []

        while i < n:
            if s[i] == ")":
                isolated = ""
                while True:
                    prev = stack.pop()
                    if prev == "(":
                        bracket_eval = evaluate(isolated)
                        if bracket_eval < 0 and stack:
                            if stack[-1] == "+":
                                stack[-1] = "-"
                            else:
                                stack[-1] = "+"
                            bracket_eval *= -1
                        for c in str(bracket_eval):
                            stack.append(c)
                        break
                    else:
                        isolated = prev + isolated
            else:
                stack.append(s[i])

            i += 1
        return evaluate(''.join(stack))
