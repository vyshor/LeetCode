class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            k ^= nums[i]
        count = 0
        while k:
            count += k%2
            k >>= 1
        return count