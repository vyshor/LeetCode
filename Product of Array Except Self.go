func productExceptSelf(nums []int) []int {
    n := len(nums)
    dp_left := make([]int, n)
    dp_right := make([]int, n)
    left := 1
    for i := 0; i < n; i++ {
        left *= nums[i]
        dp_left[i] = left
    }

    right := 1
    for i := n-1; i >= 0; i-- {
        right *= nums[i]
        dp_right[i] = right
    }

    ans := make([]int, n)
    for i := 0; i < n; i++ {
        val := 1
        if i+1 < n {
            val *= dp_right[i+1]
        }
        if i-1 >= 0 {
            val *= dp_left[i-1]
        }
        ans[i] = val
    }
    return ans
}
