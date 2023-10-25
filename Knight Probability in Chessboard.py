class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {}

        # Probability that it is off the board
        def getProb(i, j, moves_left):
            if not (0 <= i < n and 0 <= j < n):
                return 1

            if moves_left == 0:
                return 0

            if (i, j, moves_left) in dp:
                return dp[(i, j, moves_left)]

            cum_prob = 0
            for (x, y) in [(i + 1, j + 2), (i + 2, j + 1), (i - 1, j + 2), (i - 2, j + 1), (i + 1, j - 2),
                           (i + 2, j - 1), (i - 1, j - 2), (i - 2, j - 1)]:
                cum_prob += getProb(x, y, moves_left - 1) / 8

            dp[(i, j, moves_left)] = cum_prob
            return dp[(i, j, moves_left)]

        offBoard = getProb(row, column, k)
        # print(offBoard)
        # print(dp)
        return 1 - offBoard
