class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        ny, nx = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * nx for _ in range(ny)]
        for x in range(nx - 1, -1, -1):
            for y in range(ny - 1, -1, -1):
                if obstacleGrid[y][x]:
                    continue

                if y + 1 < ny:
                    dp[y][x] += dp[y + 1][x]
                if x + 1 < nx:
                    dp[y][x] += dp[y][x + 1]

                if y == ny - 1 and x == nx - 1 and obstacleGrid[y][x] != 1:
                    dp[y][x] = 1

        return dp[0][0]


