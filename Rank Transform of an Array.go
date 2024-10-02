func arrayRankTransform(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }

    n := len(arr)
    dp := make([][]int, 0)
    for i, num := range arr {
        dp = append(dp, []int{num, i})
    }
    sort.Slice(dp, func(i, j int) bool {return dp[i][0] < dp[j][0]})

    ans := make([]int, n)
    rank := 1
    prev := dp[0][0]
    for _, p := range dp {
        num := p[0]
        i := p[1]
        if num != prev {
            rank++
        }

        ans[i] = rank
        prev = num
    }
    return ans
}
