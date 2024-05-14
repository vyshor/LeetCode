class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        gold_pos = {}
        dp = {}
        maxx = 0

        k = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    gold_pos[(i, j)] = (1 << k)
                    k += 1

        def explore(i, j, state):
            nonlocal m, n, grid, dp, gold_pos, maxx
            state |= gold_pos[(i, j)]

            if (i, j, state) in dp:
                return dp[(i, j, state)]

            val = grid[i][j]
            maxx_move = 0
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] and gold_pos[(x, y)] & state == 0:
                    maxx_move = max(maxx_move, explore(x, y, state))

            val += maxx_move
            dp[(i, j, state)] = val
            maxx = max(maxx, val)
            return val

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    explore(i, j, 0)
        # print(dp)
        return maxx
