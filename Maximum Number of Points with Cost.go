func maxPoints(points [][]int) int64 {
    n := len(points)
    m := len(points[0])
    for i := 0; i < n-1; i++ {
        maxx := 0
        dp := make([]int, m)
        for j := 0; j < m; j++ {
            maxx = max(maxx-1, points[i][j])
            dp[j] = maxx
        }
        maxx = 0
        for j := m-1; j > -1; j-- {
            maxx = max(maxx-1, points[i][j])
            points[i+1][j] += max(dp[j], maxx)
        }
    }
    var ans int64
    for _, val := range points[n-1] {
        ans = max(ans, int64(val))
    }
    return ans
}
