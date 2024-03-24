func maximumGap(nums []int) int {
    slices.Sort(nums)
    n := len(nums)
    if n < 2 {
        return 0
    }
    maxx := -1
    for i := 1; i < n; i++ {
        maxx = max(maxx, nums[i]-nums[i-1])
    }
    return maxx
}

