from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f, l = bisect_left(nums, target), bisect_right(nums, target)-1
        return [f, l] if f < len(nums) and nums[f] == target else [-1, -1]

# Runtime: 84 ms, faster than 74.14% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 52.62% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

# Time: O(n)
# Space: O(1)