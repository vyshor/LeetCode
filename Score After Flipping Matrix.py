class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if not grid[i][0]:
                for j in range(m):
                    grid[i][j] ^= 1

        count = n * (1 << (m - 1))
        for j in range(1, m):
            current_count = 0
            for i in range(n):
                current_count += grid[i][j]
            count += (1 << (m - 1 - j)) * max(current_count, n - current_count)
        return count
