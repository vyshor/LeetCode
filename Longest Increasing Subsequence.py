class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for idx, num in enumerate(nums):
            seq = [x for i, x in enumerate(dp[:idx]) if nums[i] < num]
            if seq:
                dp[idx] = max(seq) + 1
        return max(dp) if dp else 0

# Runtime: 872 ms, faster than 65.69% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.

# Time Comlexity: n^2
# Space Complexity: n