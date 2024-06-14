class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        minn = nums[0]
        count = 0
        for num in nums:
            minn = max(minn, num)
            if num < minn:
                count += minn - num
            minn += 1
        return count
