func numSquares(n int) int {
    arr := make([]int, 0)
    for i := 1; i<n+1; i++ {
        sq := i*i
        if sq == n {
            return 1
        }
        if sq > n {
            break
        }
        arr = append(arr, sq)
    }

    dp := make([]int, n+1)
    for i := 0; i<n; i++ {
        dp[i] = n;
    }

    for _, num := range arr {
        for i := n; i > 0; i-- {
            if (i - num < 0) {
                break
            }
            dp[i-num] = min(dp[i-num], dp[i]+1)
        }
    }
    return dp[0]
}
