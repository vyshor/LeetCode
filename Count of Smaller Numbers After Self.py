class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        q = []

        for i in range(n - 1, -1, -1):
            dp[i] = bisect.bisect_left(q, nums[i])
            q.insert(dp[i], nums[i])

        return dp
