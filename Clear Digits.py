class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        stack = []
        mask = [1] * n
        for i in range(n):
            if s[i].isdigit() and stack:
                mask[stack.pop()] = 0
                mask[i] = 0
            elif not s[i].isdigit():
                stack.append(i)
        ans = ''
        for i in range(n):
            if mask[i] == 1:
                ans += s[i]
        return ans