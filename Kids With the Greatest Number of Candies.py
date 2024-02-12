class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curMax = max(candies)
        a = []
        for c in candies:
            a.append(c + extraCandies >= curMax)
        return a
