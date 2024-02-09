class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        dp = [0] * n
        for num in nums:
            if num <= 0 or num > n:
                return False
            dp[num - 1] += 1
            if dp[num - 1] > 1 and num != n:
                return False

        for i in range(n):
            if dp[i] == 0:
                return False
        return dp[-1] == 2