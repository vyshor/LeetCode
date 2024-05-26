func checkRecord(n int) int {
    mod := func(num int) int {
        const MOD = 1000000007
        return num % MOD
    }

    dp := [][]int{
        {0, 1, 0, 1},
        {1, 0, 0, 0},
    }

    for i := 1; i < n; i++ {
        new_dp := [][]int{
            {0, dp[0][3], dp[0][1], mod(dp[0][1]+dp[0][2]+dp[0][3])},
            {mod(dp[0][1]+dp[0][2]+dp[0][3]), mod(dp[1][0]+dp[1][3]), dp[1][1], mod(dp[1][0]+dp[1][1]+dp[1][2]+dp[1][3])},
        }
        dp = new_dp
    }

    total := 0
    for i := 0; i < 2; i++ {
        for j := 0; j < 4; j++ {
            total += dp[i][j]
            total = mod(total)
        }
    }
    return total
}

