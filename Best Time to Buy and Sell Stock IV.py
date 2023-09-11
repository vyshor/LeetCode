class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        hold = [[0] * (k + 1) for _ in range(n)]
        free = [[0] * (k + 1) for _ in range(n)]

        for j in range(k):
            hold[0][j] = -prices[0]
        hold[0][-1] = float('-inf')

        for i in range(1, n):
            for j in range(k + 1):
                hold[i][j] = hold[i - 1][j]
                if j < k:
                    hold[i][j] = max(hold[i][j], free[i - 1][j + 1] - prices[i])

                free[i][j] = max(free[i - 1][j], hold[i - 1][j] + prices[i])

        # print(hold)
        # print(free)

        return max(free[-1])
