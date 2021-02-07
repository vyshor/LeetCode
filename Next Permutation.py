class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            prev_num = nums[-1]
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] < prev_num:
                current_idx = idx
                change_num = nums[idx]
                next_larger_num = idx+1
                while idx+1 < len(nums) and nums[idx+1] > change_num:
                    idx += 1
                nums[current_idx], nums[idx] = nums[idx], nums[current_idx]
                nums[current_idx+1:] = nums[-1: current_idx - len(nums):-1]
                return
            prev_num = nums[idx]
        nums[:] = nums[::-1]

# Runtime: 52 ms, faster than 14.29% of Python3 online submissions for Next Permutation.
# Memory Usage: 14.3 MB, less than 23.40% of Python3 online submissions for Next Permutation.

# Time: O(n)
# Space: O(1)