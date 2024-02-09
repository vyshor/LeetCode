class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dp = [0] * 26

        for i, c in enumerate(s):
            v = ord(c) - 97
            dp[v] = i

        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < dp[ord(stack[-1]) - 97]:
                    seen.remove(stack.pop())

                seen.add(c)
                stack.append(c)

        return "".join(stack)
