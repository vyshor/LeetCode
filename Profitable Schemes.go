func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
    MOD := 1000000007
    dp := make([][]int, n+1)
    for i := 0; i < n+1; i++ {
        dp[i] = make([]int, minProfit+1)
    }
    dp[n][minProfit] = 1

    for k, ppl := range group {
        money := profit[k]
        for i := 0; i < n+1; i++ {
            for j := 0; j < minProfit+1; j++ {
                if i-ppl >= 0 && dp[i][j] > 0 {
                    new_money := max(j-money, 0)
                    dp[i-ppl][new_money] += dp[i][j]
                    dp[i-ppl][new_money] %= MOD
                }
            }
        }
    }

    var total_count int
    for i := 0; i< n+1; i++ {
        total_count += dp[i][0]
        total_count %= MOD
    }
    return total_count
}

