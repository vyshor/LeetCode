class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        max_val = num = nums.pop()
        while nums:
            if num >= nums[-1]:
                num += nums.pop()
            else:
                num = nums.pop()
            max_val = max(max_val, num)
        return max_val

