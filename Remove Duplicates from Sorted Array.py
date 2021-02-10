class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_pt = 0
        checker = 1
        while checker < len(nums):
            if nums[checker] != nums[unique_pt]:
                nums[unique_pt+1], nums[checker] = nums[checker], nums[unique_pt+1]
                unique_pt += 1
            checker += 1
        return unique_pt+1

# Time: O(n)
# Space: O(1)

# Runtime: 80 ms, faster than 82.72% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 16.1 MB, less than 30.15% of Python3 online submissions for Remove Duplicates from Sorted Array.