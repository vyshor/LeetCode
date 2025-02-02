func isArraySpecial(nums []int) bool {
    n := len(nums)
    parity := nums[0] & 1;
    for i := 1; i < n; i++ {
        new_parity := nums[i] & 1
        if parity == new_parity {
            return false
        }
        parity = new_parity
    }
    return true
}
