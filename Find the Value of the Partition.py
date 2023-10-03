class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        minn = nums[1] - nums[0]
        for i in range(1, n):
            minn = min(minn, nums[i] - nums[i - 1])
        return minn
