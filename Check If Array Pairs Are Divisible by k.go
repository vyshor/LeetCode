func canArrange(arr []int, k int) bool {
    dp := make([]int, k)
    for _, num := range arr {
        if num < 0 {
            num += ((-num/k)+1)*k
        }
        dp[num % k]++
    }

    if dp[0] % 2 == 1 {
        return false
    }

    i := 1
    j := len(dp)-1
    for i < j {
        if dp[i] != dp[j] {
            return false
        }
        i++
        j--
    }

    if i == j {
        return dp[i] % 2 == 0
    }
    return true
}
