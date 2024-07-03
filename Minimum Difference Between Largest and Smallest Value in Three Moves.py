class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        left, right = 0, n-1
        return min(nums[right-3]-nums[left], nums[right-2]-nums[left+1], nums[right-1]-nums[left+2], nums[right]-nums[left+3])
