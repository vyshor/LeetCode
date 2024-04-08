class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        dp[n][minProfit] = 1
        m = len(group)
        for k in range(m):
            ppl = group[k]
            money = profit[k]
            for i in range(n+1):
                for j in range(minProfit+1):
                    if i-ppl >= 0 and dp[i][j] > 0:
                        new_money = max(j-money, 0)
                        dp[i-ppl][new_money] += dp[i][j]
                        dp[i-ppl][new_money] %= MOD
        # print(dp)
        total_count = 0
        for i in range(n+1):
            total_count += dp[i][0]
        return total_count % MOD
