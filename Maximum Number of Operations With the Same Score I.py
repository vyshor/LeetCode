class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        i = 2
        n = len(nums)
        summ = nums[0] + nums[1]
        count = 1
        while i+1 < n:
            if nums[i] + nums[i+1] == summ:
                count += 1
                i += 2
            else:
                break
        return count
