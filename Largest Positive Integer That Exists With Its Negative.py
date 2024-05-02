class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        maxx = -1
        for num in nums:
            if -num in seen:
                maxx = max(maxx, abs(num))
            seen.add(num)
        return maxx
