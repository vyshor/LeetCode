class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dp = {}
        max_sum = -1
        for num in nums:
            max_digit = max(list(str(num)))
            if max_digit not in dp:
                dp[max_digit] = num
            else:
                max_sum = max(max_sum, dp[max_digit]+num)
                dp[max_digit] = max(dp[max_digit], num)
        return max_sum
