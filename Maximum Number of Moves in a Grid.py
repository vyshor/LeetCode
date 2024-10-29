class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = {}
        n = len(grid)
        m = len(grid[0])

        def recur(i, j):
            nonlocal grid, dp, m, n
            if (i, j) in dp:
                return dp[(i, j)]

            if j == m:
                return 0

            if j + 1 == m:
                return 1

            moves = 0
            val = grid[i][j]
            if grid[i][j + 1] > val:
                moves = max(moves, recur(i, j + 1))
            if i - 1 >= 0 and grid[i - 1][j + 1] > val:
                moves = max(moves, recur(i - 1, j + 1))
            if i + 1 < n and grid[i + 1][j + 1] > val:
                moves = max(moves, recur(i + 1, j + 1))
            dp[(i, j)] = moves + 1
            return moves + 1

        maxx = 0
        for i in range(n):
            maxx = max(maxx, recur(i, 0))
        return maxx - 1

