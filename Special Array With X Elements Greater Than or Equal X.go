func specialArray(nums []int) int {
    sort.Ints(nums)
    n := len(nums)

    for i := 0; i < n; i++ {
        if i != 0 && nums[i] == nums[i-1] {
            continue
        } else if (n-i < nums[i] && (i == 0 || nums[i-1] < n-i)) || nums[i] == n-i {
            return n-i
        }
    }
    return -1
}
