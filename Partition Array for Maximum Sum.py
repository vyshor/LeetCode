class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = {}

        def getMax(i):
            nonlocal dp
            if i in dp:
                return dp[i]

            maxx = 0
            maxx_val = 0
            for i2 in range(min(n-i, k)):
                maxx_val = max(maxx_val, arr[i+i2])
                maxx = max(maxx, (i2+1)*maxx_val + getMax(i+i2+1))
            dp[i] = maxx
            return dp[i]

        ans = getMax(0)
        return ans
