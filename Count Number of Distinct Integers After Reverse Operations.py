class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        dp = set()
        for i in range(n):
            dp.add(nums[i])
            dp.add(int(str(nums[i])[::-1]))

        return len(dp)
