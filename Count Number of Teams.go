func countTriplets(arr []int) int {
    dp := make([][]int, 0)
    count := 0
    for _, num := range arr {
        k := sort.Search(len(dp), func(i int) bool { return dp[i][0] >= num })
        for j := 0; j < k; j++ {
            count += dp[j][1]

        }
        dp = slices.Insert(dp, k, []int{num, k})
    }
    return count
}

func numTeams(rating []int) int {
    count := countTriplets(rating)
    slices.Reverse(rating)
    return count + countTriplets(rating)
}


