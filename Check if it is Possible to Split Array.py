class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True

        for i in range(1, n):
            if nums[i] + nums[i-1] >= m:
                return True
        return False
