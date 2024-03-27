func numSubarrayProductLessThanK(nums []int, k int) int {
    if k == 0 {
        return 0
    }
    n := len(nums)
    k2 := math.Log(float64(k))
    arr := make([]float64, n)
    for i := 0; i < n; i++ {
        arr[i] = math.Log(float64(nums[i]))
    }

    dp := make([]float64, n+1)
    summ := 0.
    count := 0
    for i, num := range arr {
        summ += num
        dp[i+1] = summ
    }

    for i, _ := range arr {
        remainder := k2 + dp[i]
        j := sort.Search(len(dp), func(j2 int) bool { return dp[j2] >= remainder })
        if j < i+1 {
            continue
        }

        count += j-i-1
    }

    return count
}
