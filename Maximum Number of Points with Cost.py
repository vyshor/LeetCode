class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        for i in range(n-1):
            maxx = 0
            dp = [0] * m
            for j in range(m):
                maxx = max(maxx-1, points[i][j])
                dp[j] = max(dp[j], maxx)

            maxx = 0
            for j in range(m-1, -1, -1):
                maxx = max(maxx-1, points[i][j])
                dp[j] = max(dp[j], maxx)
                points[i+1][j] += dp[j]
        return max(points[-1])
