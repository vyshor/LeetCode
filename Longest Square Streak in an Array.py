class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        maxx = -1
        for num in nums:
            sqrt = int(math.sqrt(num))
            root = sqrt ** 2
            if root == num and sqrt in dp:
                dp[num] = dp[sqrt] + 1
                maxx = max(maxx, dp[num])
            else:
                dp[num] = 1
        return maxx
