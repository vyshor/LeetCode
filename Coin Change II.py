class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[-1] = 1

        coins.sort(reverse=True)
        for coin in coins:
            for i in range(amount, -1, -1):
                if dp[i] > 0 and i - coin >= 0:
                    dp[i - coin] += dp[i]
        return dp[0]

