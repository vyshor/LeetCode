class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        n = len(nums)
        total = 0
        for i in range(k - 1):
            total += nums[i]
        i = 0
        j = k - 1
        maxx = 0
        while i < n:
            total += nums[j]
            j += 1
            j %= n
            maxx = max(maxx, total)
            total -= nums[i]
            i += 1
        return k - maxx
