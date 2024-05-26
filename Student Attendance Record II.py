class Solution:
    def checkRecord(self, n: int) -> int:
        # 1st Index is A0 and A1
        # 2nd Index is LastA, LastL1, LastL2, LastP
        MOD = 10 ** 9 + 7

        def mod(num):
            return num % MOD

        dp = [
            [0, 1, 0, 1],
            [1, 0, 0, 0]
        ]

        for i in range(1, n):
            common_upper_half = mod(dp[0][1] + dp[0][2] + dp[0][3])
            dp = [
                [0, dp[0][3], dp[0][1], common_upper_half],
                [common_upper_half, mod(dp[1][0] + dp[1][3]), dp[1][1], mod(dp[1][0] + dp[1][1] + dp[1][2] + dp[1][3])]
            ]

        total = 0
        for i in range(2):
            for j in range(4):
                total += dp[i][j]
                total %= MOD
        return total

