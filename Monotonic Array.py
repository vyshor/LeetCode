class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        asc, dsc = True, True
        for i in range(1, n):
            asc = asc and nums[i] >= nums[i - 1]
            dsc = dsc and nums[i] <= nums[i - 1]

        return asc or dsc
