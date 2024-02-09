class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n
        free = [0] * n
        cooldown = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            cooldown[i] = hold[i-1] + prices[i]
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            free[i] = max(free[i-1], cooldown[i-1])

        return max(free[-1], cooldown[-1])
