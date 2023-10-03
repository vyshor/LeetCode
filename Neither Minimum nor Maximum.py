class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(set(nums))
        if n <= 2:
            return -1

        maxx, minn = max(nums), min(nums)
        for num in nums:
            if num != maxx and num != minn:
                return num
        return -1
