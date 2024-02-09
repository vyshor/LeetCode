class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pt_0, pt_1, pt_2 = 0, 0, 0
        while pt_2 < n:
            if nums[pt_2] == 0:
                nums[pt_1], nums[pt_2] = nums[pt_2], nums[pt_1]
                nums[pt_0], nums[pt_1] = nums[pt_1], nums[pt_0]
                pt_0 += 1
                pt_1 += 1
                pt_2 += 1
            elif nums[pt_2] == 1:
                nums[pt_1], nums[pt_2] = nums[pt_2], nums[pt_1]
                pt_1 += 1
                pt_2 += 1
            else:
                pt_2 += 1
