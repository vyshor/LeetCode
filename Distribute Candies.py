from collections import Counter

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        return min(n, len(Counter(candyType).keys()))

# Time: O(n)
# Space: O(n)

# Runtime: 796 ms, faster than 66.84% of Python3 online submissions for Distribute Candies.
# Memory Usage: 16.1 MB, less than 81.71% of Python3 online submissions for Distribute Candies.