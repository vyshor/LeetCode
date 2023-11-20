class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxx = float('-inf')
        for i in range(n//2):
            maxx = max(maxx, nums[i]+nums[n-1-i])
        return maxx
