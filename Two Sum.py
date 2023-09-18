class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, num in enumerate(nums):
            if target - num in dp:
                return [i, dp[target-num]]
            dp[num] = i
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i1, x in enumerate(nums):
#             for i2, y in enumerate(nums[i1+1:]):
#                 if x + y == target:
#                     return [i1, i2+1+i1]
#
#
# # O(n^2)
# # Runtime: 5296 ms
# # Memory: 14.6 MB
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums2 = set([target - x for x in nums])
#         nums2 = list(nums2.union(set(nums)))
#         x1 = nums.index(nums2[0])
#         l = len(nums2)
#         if l == 2:
#             x2 = nums.index(nums2[1])
#         elif l == 1:
#             x2 = len(nums) - nums[::-1].index(nums2[0])
#         else:
#             return self.twoSum([-1 * x for x in nums], (-1 * target))
#         return [x1, x2]
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dp = {}
#         for i, num in enumerate(nums):
#             try:
#                 idx = dp[target - num]
#                 return [idx, i]
#             except KeyError:
#                 dp[num] = i
#
# # O(n)
# # Runtime: 68 ms
# # Memory: 15 MB