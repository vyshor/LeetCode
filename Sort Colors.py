class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pt1, pt0, pt2 = 0, 0, n - 1
        while pt2 >= 0 and nums[pt2] == 2:
            pt2 -= 1

        while pt0 < n and nums[pt0] == 0:
            pt0 += 1
            pt1 += 1

        while pt1 <= pt2:
            # print(pt0, pt1, pt2)
            if nums[pt1] == 2:
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt2 -= 1
            elif nums[pt1] == 0:
                if pt1 == pt0:
                    pt1 += 1
                    pt0 += 1
                else:
                    nums[pt1], nums[pt0] = nums[pt0], nums[pt1]
                    pt0 += 1
            else:
                pt1 += 1

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         pt_0, pt_1, pt_2 = 0, 0, 0
#         while pt_2 < n:
#             if nums[pt_2] == 0:
#                 nums[pt_1], nums[pt_2] = nums[pt_2], nums[pt_1]
#                 nums[pt_0], nums[pt_1] = nums[pt_1], nums[pt_0]
#                 pt_0 += 1
#                 pt_1 += 1
#                 pt_2 += 1
#             elif nums[pt_2] == 1:
#                 nums[pt_1], nums[pt_2] = nums[pt_2], nums[pt_1]
#                 pt_1 += 1
#                 pt_2 += 1
#             else:
#                 pt_2 pt_2+= 1
