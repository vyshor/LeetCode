class Solution:
    def firstUniqChar(self, s: str) -> int:
        dp = {}
        n = len(s)
        for i, c in enumerate(s):
            if c in dp:
                dp[c] = -1
            else:
                dp[c] = i
        minn = n
        for c, i in dp.items():
            if i != -1:
                minn = min(minn, i)
        return minn if minn != n else -1
