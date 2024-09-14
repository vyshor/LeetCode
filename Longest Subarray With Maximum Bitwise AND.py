class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        maxx = 0
        k = 0
        for num in nums:
            if num > k:
                k = num
                count = 1
                maxx = 1
            elif num == k:
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0
        return maxx
