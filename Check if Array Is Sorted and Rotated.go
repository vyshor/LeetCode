func check(nums []int) bool {
    n := len(nums)
    use_rotates := nums[n-1] > nums[0]
    for i := 1; i < n; i++ {
        if nums[i-1] > nums[i] {
            if use_rotates {
                return false
            }
            use_rotates = true
        }
    }
    return true
}
