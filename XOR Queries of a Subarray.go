func xorQueries(arr []int, queries [][]int) []int {
    xorr := 0
    dp := []int{0}
    n := len(arr)
    for i := 0; i < n; i++ {
        xorr ^= arr[i]
        dp = append(dp, xorr)
    }

    ans := make([]int, 0)
    for _, query := range queries {
        ans = append(ans, dp[query[1]+1] ^ dp[query[0]])
    }
    return ans
}
