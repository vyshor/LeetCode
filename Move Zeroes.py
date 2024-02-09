class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j, num in enumerate(nums):
            if num != 0:
                if i != j:
                    nums[i], nums[j] = num, 0
                i += 1


