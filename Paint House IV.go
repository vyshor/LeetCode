func min2(a, b, c int64) int64 {
    if a <= b && a <= c {
        return a
    } else if (b <= a && b <= c) {
        return b
    }
    return c
}

func minCost(n int, cost [][]int) int64 {
    dp := make([]int64, 6)
    left := n / 2 - 1
    right := n /2
    for left >= 0 {
            dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] =
            min2(dp[1], dp[2], dp[5]) + int64(cost[left][1] + cost[right][2]),
            min2(dp[0], dp[3], dp[4]) + int64(cost[right][1] + cost[left][2]),
            min2(dp[0], dp[3], dp[5]) + int64(cost[left][0] + cost[right][1]),
            min2(dp[1], dp[2], dp[4])  + int64(cost[right][0] + cost[left][1]),
            min2(dp[1], dp[3], dp[5])  + int64(cost[left][0] + cost[right][2]),
            min2(dp[0], dp[2], dp[4]) + int64(cost[right][0] + cost[left][2])

            left--
            right++
    }
    return min(min2(dp[0], dp[1], dp[2]), min2(dp[3], dp[4], dp[5]))
}
