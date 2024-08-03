func minSwaps(nums []int) int {
    k := 0
    for _, num := range nums {
        k += num
    }
    if k == 0 {
        return 0
    }

    n := len(nums)
    total := 0
    for i := 0; i < k-1; i++ {
        total += nums[i]
    }
    i := 0
    j := k-1
    maxx := 0
    for i < n {
        total += nums[j]
        j++
        j %= n
        maxx = max(maxx, total)
        total -= nums[i]
        i++
    }
    return k-maxx
}
