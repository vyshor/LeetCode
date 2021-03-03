class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append('X')
        for i in range(len(nums)):
            while nums[i] != 'X' and nums[i] != i:
                swap_idx = nums[i]
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
        return nums.index('X')

# Time: O(n)
# Space: O(1)

# Runtime: 148 ms, faster than 33.50% of Python3 online submissions for Missing Number.
# Memory Usage: 15.5 MB, less than 18.93% of Python3 online submissions for Missing Number.
