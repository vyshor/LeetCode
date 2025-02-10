func countBadPairs(nums []int) int64 {
    n := len(nums)
    counter := make(map[int]int)
    for i := 0; i < n; i++ {
        offset := nums[i]-i
        counter[offset]++
    }

    total_count := (int64(n) * int64(n-1)) >> 1
    for _, v := range counter {
        total_count -= (int64(v) * int64(v-1)) >> 1
    }
    return total_count
}
