class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        dp = {}
        count = 0

        for i in range(n):
            if prefix not in dp:
                dp[prefix] = 1
            else:
                dp[prefix] += 1

            prefix += nums[i]

            if prefix - k in dp:
                count += dp[prefix - k]
        return count
