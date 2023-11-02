class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = [[1] * m for _ in range(n)]
        arr = []

        for i in range(n):
            for j in range(m):
                arr.append((grid[i][j], i, j))

        arr.sort()
        h = len(arr)
        for k in range(h):
            num, i, j = arr[k]
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] > num:
                    dp[x][y] += dp[i][j]

        count = 0
        for i in range(n):
            for j in range(m):
                count += dp[i][j]

        return count % MOD
