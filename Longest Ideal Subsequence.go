func longestIdealString(s string, k int) int {
    dp := make([]int, 26)
    largest := 0
    for _, c := range s {
        pos := (int) (c - 'a')
        maxx := 1
        for i := max(0, pos-k); i < min(26, pos+k+1); i++ {
            maxx = max(maxx, dp[i]+1)
        }
        dp[pos] = maxx
        largest = max(largest, maxx)
    }

    return largest
}
