class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxx = nums[0]
        maxx_idx = 0
        for i, num in enumerate(nums):
            if num > maxx:
                maxx = num
                maxx_idx = i

        for num in nums:
            if num != maxx:
                if maxx < 2*num:
                    return -1

        return maxx_idx
