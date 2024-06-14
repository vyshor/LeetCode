func minIncrementForUnique(nums []int) int {
    sort.Ints(nums)
    minn := nums[0]
    count := 0
    for _, num := range nums {
        minn = max(minn, num)
        if num < minn {
            count += minn - num
        }
        minn++
    }
    return count
}
