class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dp = {}
        dp2 = set()
        for i in range(n):
            if s[i] not in dp:
                dp[s[i]] = t[i]

                if t[i] in dp2:
                    return False
                dp2.add(t[i])
            else:
                if dp[s[i]] != t[i]:
                    return False
        return True
