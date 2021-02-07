class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

# Time: O(n) # Probably wrong solution, but idk why this is faster than 90%
# Space: O(1)
# Runtime: 44 ms, faster than 91.86% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 6.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        if nums[e] > nums[s]:
            return nums[0]
        while e - s > 1:
            mid = (e - s) // 2 + s
            if nums[mid] > nums[s]:
                s = mid
            else:
                e = mid + 1

        return nums[s]

# Time: O(lgn)
# Space: O(1)
# Runtime: 48 ms, faster than 73.14% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 6.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        if nums[e] > nums[s]:
            return nums[0]
        while e - s> 1:
            mid = (e + s) // 2
            if nums[mid] > nums[s]:
                s = mid
            else:
                e = mid

        return nums[e]

# Runtime: 52 ms, faster than 39.09% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.9 MB, less than 6.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.