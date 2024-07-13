class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0

        def find_ab(s):
            nonlocal score
            n = len(s)
            if n == 0:
                return '', 0

            stack = []
            for i in range(n):
                if s[i] == 'b' and stack and stack[-1] == 'a':
                    score += x
                    stack.pop()
                else:
                    stack.append(s[i])

            return stack

        def find_ba(s):
            nonlocal score
            n = len(s)
            if n == 0:
                return '', 0

            stack = []
            for i in range(n):
                if s[i] == 'a' and stack and stack[-1] == 'b':
                    score += y
                    stack.pop()
                else:
                    stack.append(s[i])

            return stack

        stack = list(s)
        if x > y:
            find_ba(find_ab(stack))
        else:
            find_ab(find_ba(stack))
        return score
