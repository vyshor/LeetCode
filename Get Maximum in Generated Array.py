class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = {0:0, 1:1}
        h = 0
        if n:
            h = 1
        for i in range(2, n+1):
            if (i % 2):
                dp[i] = dp[i // 2] + dp[i // 2 + 1]
            else:
                dp[i] = dp[i // 2]
            h = max(h, dp[i])
        return h

# Runtime: 28 ms, faster than 87.00% of Python3 online submissions for Get Maximum in Generated Array.
# Memory Usage: 14.3 MB, less than 39.73% of Python3 online submissions for Get Maximum in Generated Array.

# Time: O(n)
# Space: O(n)