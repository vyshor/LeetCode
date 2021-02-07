class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# O(n)
# Runtime: 144 ms, faster than 57.96% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19 MB, less than 33.96% of Python3 online submissions for Contains Duplicate.