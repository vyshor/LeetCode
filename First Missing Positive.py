class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num > n or num <= 0:
                nums[i] = n + 1

        for i, num in enumerate(nums):
            abs_num = abs(num)
            if abs_num <= n:
                if nums[abs_num - 1] > 0:
                    nums[abs_num - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             while i + 1 != nums[i] and 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#
#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1
#         return n + 1

