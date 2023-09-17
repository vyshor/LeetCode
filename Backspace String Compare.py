class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        stack2 = []
        for c in t:
            if c == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(c)

        return stack == stack2
