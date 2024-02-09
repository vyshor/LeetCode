class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = bisect.bisect_left(nums, target)
        if i >= n or nums[i] != target:
            return [-1, -1]
        j = bisect.bisect_right(nums, target)
        return [i, j-1]

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         mmax, mmin = -1, 10**5 + 1
#         def processRange(f, l):
#             nonlocal mmax, mmin
#             if l < f:
#                 return
#             m = (f+l)//2
#             if target == nums[m]:
#                 mmax = max(mmax, m)
#                 mmin = min(mmin, m)
#                 if f != l:
#                     processRange(f,m-1)
#                     processRange(m+1,l)
#             elif target > nums[m] and f != l:
#                 processRange(m+1,l)
#             elif f != l:
#                 processRange(f,m-1)
#         processRange(0, len(nums)-1)
#         return [mmin, mmax] if mmax != -1 else [-1, -1]
#
# # Time: O(lgn)
# # Space: O(1)
#
# # Runtime: 92 ms, faster than 12.99% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# # Memory Usage: 15.3 MB, less than 79.86% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#
# from bisect import bisect_left, bisect_right
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         f, l = bisect_left(nums, target), bisect_right(nums, target)-1
#         return [f, l] if f < len(nums) and nums[f] == target else [-1, -1]
#
# # Runtime: 84 ms, faster than 74.14% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# # Memory Usage: 15.4 MB, less than 52.62% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#
# # Time: O(n)
# # Space: O(1)