class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        a, b = s[0], s[1]
        ans = [a, b]
        n = len(s)
        for i in range(2, n):
            c = s[i]
            if a == b == c:
                continue
            else:
                ans.append(c)
                a, b = b, c
        return ''.join(ans)
