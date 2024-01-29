class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def exploreCell(i, j, moves):
            nonlocal dp
            if not (0 <= i < m and 0 <= j < n):
                return 1
            if moves == 0:
                return 0

            if (i, j, moves) in dp:
                return dp[(i, j, moves)]

            total = 0
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                total += exploreCell(x, y, moves - 1)

            dp[(i, j, moves)] = total % MOD
            return dp[(i, j, moves)]

        return exploreCell(startRow, startColumn, maxMove)
