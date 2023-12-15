class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            a1, a2 = a
            b1, b2 = b
            return max(abs(a1 - b1), abs(a2 - b2))

        n = len(points)
        d = 0
        for i in range(1, n):
            d += dist(points[i - 1], points[i])
        return d
