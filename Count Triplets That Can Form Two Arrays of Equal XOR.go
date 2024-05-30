func countTriplets(arr []int) int {
    n := len(arr)
    dp := make(map[int64]int)
    count := 0
    for i := 0; i < n; i++ {
        current_xor := int64(0)
        for j := i; j < n; j++ {
            current_xor ^= int64(arr[j])
            if val, ok := dp[int64((i-1) << 32) | current_xor]; ok {
                count += val
            }

            key := int64(j << 32) | current_xor
            if _, ok := dp[key]; !ok {
                dp[key] = 1
            } else {
                dp[key]++
            }
        }
    }
    return count
}
