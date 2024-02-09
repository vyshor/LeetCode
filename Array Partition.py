class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        n = len(nums)

        for i in range(0, n, 2):
            summ += nums[i]

        return summ
