class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i]+1, dp[stack.pop()])
            stack.append(i)

        # print(dp)
        return max(dp)
