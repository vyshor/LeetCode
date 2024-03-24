class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 2:
            return 0
        maxx = -1
        for i in range(1, n):
            maxx = max(maxx, nums[i] - nums[i - 1])
        return maxx

