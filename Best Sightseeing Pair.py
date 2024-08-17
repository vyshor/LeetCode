class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxx0, maxx1 = 0, 0
        for val in values:
            maxx0, maxx1 = max(maxx0-1, val), max(maxx1, val+maxx0-1)
        return maxx1
