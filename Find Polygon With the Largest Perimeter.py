class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        summ = sum(nums) - nums[-1]
        for i in range(n-1, 1, -1):
            if summ > nums[i]:
                return summ + nums[i]
            else:
                summ -= nums[i-1]
        return -1
