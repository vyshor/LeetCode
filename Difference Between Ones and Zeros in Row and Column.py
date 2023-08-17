class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        nm = n + m

        rows = [0] * m
        cols = [0] * n
        for i in range(n):
            for j in range(m):
                v = 2 * grid[j][i]
                rows[j] += v
                cols[i] += v

        for i in range(n):
            for j in range(m):
                grid[j][i] = rows[j] + cols[i] - nm
        return grid


