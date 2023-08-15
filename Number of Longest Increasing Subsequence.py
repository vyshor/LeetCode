class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1]] * n
        maxLen = 1
        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    if dp[j][0] == dp[i][0] + 1:
                        dp[j][1] += dp[i][1]
                    elif dp[j][0] < dp[i][0] + 1:
                        dp[j] = [dp[i][0] + 1, dp[i][1]]

                    if dp[j][0] > maxLen:
                        maxLen = dp[j][0]

        count = 0
        for d in dp:
            if d[0] == maxLen:
                count += d[1]

        return count
