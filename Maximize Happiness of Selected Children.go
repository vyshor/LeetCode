func maximumHappinessSum(happiness []int, k int) int64 {
    sort.Ints(happiness)
    n := len(happiness)
    var count int64
    for i := 0; i < k; i++ {
        count += int64(max(0, happiness[n-i-1]-i))
    }
    return count
}
