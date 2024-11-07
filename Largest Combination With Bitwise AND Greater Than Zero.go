func largestCombination(candidates []int) int {
    dp := make([]int, 0)
    countBits := func(num int) {
        i := 0
        for num > 0 {
            if i == len(dp) {
                dp = append(dp, 0)
            }
            dp[i] += num % 2
            i++
            num >>= 1
        }
    }

    for _, num := range candidates {
        countBits(num)
    }
    return slices.Max(dp)
}
