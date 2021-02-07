from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxx_len = 0
        for num in c:
            for i in [1, -1]:
                if num+i in c.keys():
                    maxx_len = max(maxx_len, c[num] + c[num+i])
        return maxx_len

# Runtime: 320 ms, faster than 48.59% of Python3 online submissions for Longest Harmonious Subsequence.
# Memory Usage: 16 MB, less than 66.31% of Python3 online submissions for Longest Harmonious Subsequence.
# Time: O(n)
# Space: O(n)