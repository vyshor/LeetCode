class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if n-i < nums[i] and (nums[i-1] < n-i or i == 0):
                return n-i
            if nums[i] == n-i:
                return n-i
        return -1
    