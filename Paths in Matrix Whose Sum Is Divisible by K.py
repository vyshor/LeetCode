class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = {}
        dp[(0, 0, grid[0][0] % k)] = 1

        for i in range(n):
            for j in range(m):
                for h in range(k):
                    if (i, j, h) not in dp:
                        dp[(i, j, h)] = 0

                    h2 = (h + grid[i][j]) % k

                    if (i, j, h2) not in dp:
                        dp[(i, j, h2)] = 0

                    if i - 1 >= 0:
                        dp[(i, j, h2)] += dp[(i - 1, j, h)]

                    if j - 1 >= 0:
                        dp[(i, j, h2)] += dp[(i, j - 1, h)]

                    dp[(i, j, h2)] %= MOD

        return dp[(n - 1, m - 1, 0)]
