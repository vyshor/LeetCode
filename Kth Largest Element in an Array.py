class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

# Runtime: 64 ms, faster than 74.00% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15 MB, less than 89.44% of Python3 online submissions for Kth Largest Element in an Array

# Time: O(nlgn)
# Space: O(1)